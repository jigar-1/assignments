import pandas as pd

# Read the data
df = pd.read_csv('Salaries.csv')

# Part 1
total_2015 = df[df['Year'] == 2015]['TotalPayBenefits'].sum()
total_2018 = df[df['Year'] == 2018]['TotalPayBenefits'].sum()
cost_increase = total_2018 - total_2015
print(f"Total salary cost increased by: {cost_increase}")

# Part 2
highest_mean_job = df[df['Year'] == 2014].groupby('JobTitle')['BasePay'].mean().idxmax()
print(f"Job title with highest mean salary in 2014: {highest_mean_job}")

# Part 3
saved_2018 = df[df['Year'] == 2018]['OvertimePay'].sum()
print(f"Money saved in 2018 by stopping OvertimePay: {saved_2018}")

# Part 4
top_5_jobs = df[df['Year'] == 2018]['JobTitle'].value_counts().head(5)
cost_top_5 = df[df['Year'] == 2018].groupby('JobTitle')['TotalPayBenefits'].sum().loc[top_5_jobs.index].sum()
print(f"Top 5 common jobs in 2018 and their total cost: {cost_top_5}")

# Part 5
top_earner = df.loc[df['TotalPayBenefits'].idxmax()]
print(f"Top earning employee: {top_earner['EmployeeName']} with {top_earner['TotalPayBenefits']}")