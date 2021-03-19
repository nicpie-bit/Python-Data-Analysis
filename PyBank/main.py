import csv
import pandas as pd

#Path to collect data
budget_df = pd.read_csv("Resources/budget_data.csv")

print("Financial Analysis")
print("---------------------------")

#Find number of months
numberMonths = len(budget_df)
print('Total Months: ' + str(numberMonths))

#Find Total Amounnt over whole period
Total = budget_df["Profit/Losses"].sum()
print('Total: ' + "$" + str(Total))

#Find the Average Change in Profit/Losses
list_change = []
i = 1
j = len(budget_df)
while i<j:
    change = budget_df["Profit/Losses"][i] - budget_df["Profit/Losses"][i-1]
    list_change.append(change)
    i += 1
avg_change = sum(list_change) / len(list_change)
print('Average Change: ' + "$" + str(round(avg_change, 2)))

#Find Greatest increase in profits
max_increase = max(list_change)
min_decrease = min(list_change)
i = 1
j = len(budget_df)
while i<j:
    max_month_inc = (budget_df["Date"][i] == max_increase)
    min_month_dec = (budget_df["Date"][i] == min_decrease)

print('Greatest Increase in Profits: ' + max_month_inc + ' $' + str(max_increase))

#Find Greatest decrease in losses

print('Greatest Decrease in Losses: ' + min_month_dec + ' $' + str(min_decrease))






