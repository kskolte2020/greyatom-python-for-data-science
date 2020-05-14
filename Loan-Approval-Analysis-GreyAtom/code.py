# --------------
import pandas as pd
import numpy as np

#STEP 1
#reading csv file
df = pd.read_csv(path)

#creating a dataframe
bank = pd.DataFrame(df)

#checking categorical data
categorical_var = df.select_dtypes(include = 'object')
#print('Categorical values Shape: ',categorical_var.shape)

#checking numerical data
numerical_var = df.select_dtypes(include = 'number')
#print('Numerical Data Shape: ', numerical_var.shape)

#STEP 2
#Dropping LOAD_ID to create new dataframe banks
bank.drop('Loan_ID',axis = 1,inplace= True)
banks = bank

#to display no. of null values
#print('No. of Null Values:\n ',bank.isnull().sum())

bank_mode = banks.mode().iloc[0]

#filling NaN values with bank_mode
banks.fillna(bank_mode,inplace=True)
#checking if there are any null values
#print(banks.isnull().sum().values.sum())

#STEP 3
avg_loan_amount = banks.pivot_table(index=['Gender', 'Married', 'Self_Employed'],values='LoanAmount',aggfunc=np.mean)

#print('Average Loan Amount',avg_loan_amount)

#STEP 4
loan_approved_se = len(banks[(banks.Self_Employed=='Yes') & (banks.Loan_Status=='Y')])

loan_approved_nse = len(banks[(banks.Self_Employed=='No') & (banks.Loan_Status=='Y')])

percentage_se = round((loan_approved_se*100)/614,2)
percentage_nse = round((loan_approved_nse*100)/614,2)

print('% loan approval for self employed: ',percentage_se)
print('% loan approval for non-self employed: ',percentage_nse)

#STEP 6

loan_term = banks['Loan_Amount_Term'].apply(lambda x: int(x)/12 )
big_loan_term = len(loan_term[loan_term>=25])
print('No. of applicants having loan amount term >=25yrs: ',big_loan_term)

#STEP 7
loan_groupby = banks.groupby('Loan_Status')

loan_groupby = loan_groupby['ApplicantIncome','Credit_History']
mean_values = loan_groupby.mean()

print(round((mean_values.iloc[1,0]),2))



