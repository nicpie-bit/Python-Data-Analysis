import csv
import pandas as pd

#Path to collect data
budget_df = pd.read_csv("Resources/budget_data.csv")

print("Financial Analysis")
print("---------------------------")

#Find number of months
numberMonths = len(budget_df)
print(numberMonths)

#Find Total Amounnt over whole period
Total = budget_df["Profit/Losses"].sum()
print(Total)

list_change = []
i = 1
j = len(budget_df)

while i<j:
    change = budget_df["Profit/Losses"][i] - budget_df["Profit/Losses"][i-1]
    



