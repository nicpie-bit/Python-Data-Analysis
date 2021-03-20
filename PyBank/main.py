import csv
import os
import pandas as pd
import sys

#Path to collect data
budget_df = pd.read_csv("Resources/budget_data.csv")
sys.stdout = open('Analysis/analysis.txt', 'w')

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

#Adding a row
first = [0]
change_amt = first + list_change
budget_df["Amount Changed"] = change_amt

#Find Greatest increase/decrease in profits
max_increase = max(list_change)
min_decrease = min(list_change)

#Find corresponding row
max_row = budget_df[budget_df["Amount Changed"]==max_increase]
min_row = budget_df[budget_df["Amount Changed"]==min_decrease]

#Find Date 
max_month_inc = max_row.iloc[0,0]
min_month_dec = min_row.iloc[0,0]

print('Greatest Increase in Profits: ' + max_month_inc + ' $' + str(max_increase))
print('Greatest Decrease in Losses: ' + min_month_dec + ' $' + str(min_decrease))

#Create txt file
sys.stdout.close()

os.chdir('../PyBank/Analysis')

#Print in Terminal
with open('analysis.txt', 'r') as f:
    text = f.read()
    print(text)
    f.close()
    #readAll = fileOpened.read()
#print(fileOpened.closed)




