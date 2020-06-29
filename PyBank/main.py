# ## PyBank

# * In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. (Thankfully, your company has rather lax standards for accounting so the records are simple.)

# Import module to create file paths across operating systems:
import os as os

# Import module for reading CSV files:
import csv as csv

# Assign variable csvpath to file location:
csvpath = os.path.join("Resources", "budget_data.csv")

# Open file at csvpath and read with comma delimiter:
with open(csvpath,'r', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Assign variable 'header' to first row of csvreader data:
    header = next(csvreader)

# * Your task is to create a Python script that analyzes the records to calculate each of the following:

#   * The total number of months included in the dataset

    # Convert data to list:
    csvdata = list(csvreader)

months = [record[0] for record in csvdata]
# print(months)
total_months = len(months)
# print(total_months)

#   * The net total amount of "Profit/Losses" over the entire period

profit_losses = [int(record[1]) for record in csvdata]
# print(profit_losses)
total_profit_losses = sum(profit_losses)
# print(total_profit_losses)

#   * The average of the changes in "Profit/Losses" over the entire period

plchange = [int(csvdata[i+1][1]) - int(csvdata[i][1]) for i in range(0,len(csvdata)-1)] 
# print(plchange)
average_change = round(sum(plchange) / (total_months-1),2)
# print(average_change)

#   * The greatest increase in profits (date and amount) over the entire period

max_profit = max(plchange)
# print(max_profit)
max_profit_date = csvdata[plchange.index(max_profit)+1][0]
# print(max_profit_date)

#   * The greatest decrease in losses (date and amount) over the entire period

max_loss = min(plchange)
# print(max_loss)
max_loss_date = csvdata[plchange.index(max_loss)+1][0]
# print(max_loss_date)

# * As an example, your analysis should look similar to the one below:

#   ```text
#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)
#   ```

analysis = f"Financial Analysis\n\
----------------------------\n\
Total Months: {total_months}\n\
Total: ${total_profit_losses}\n\
Average Change: ${average_change}\n\
Greatest Increase in Profits: {max_profit_date} (${max_profit})\n\
Greatest Decrease in Profits: {max_loss_date} (${max_loss})"

print(analysis)

# * In addition, your final script should both print the analysis to the terminal and export a text file with the results.

results_file = os.path.join("PyBankResults.txt")
with open(results_file, "w", newline="") as datafile:
    datafile.write(analysis)
