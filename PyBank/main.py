#create dependencies
import os
import csv

#Read csv file
csvpath = os.path.join("Resources", "budget_data.csv")
months = []
profits = []
difference = []

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    
    #Total number of months in dataset
    month = 0
    data = list(csvreader)
    month = len(data)

    #The net total amount of "Profit/Losses" over the entire period
    total = 0
    for row in data:
        months.append(row[0])
        profits.append(row[1])
    
    #Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
    for row in range(1,len(profits)):
        change = int(profits[row]) - int(profits[row - 1])
        difference.append(change)
    total = sum(float(row[1]) for row in data)
    maximum = max(float(row[1]) for row in data)
    minimum = min(float(row[1]) for row in data)
    for (a,b) in zip(months, profits):
        if float(b) == minimum:
            minmonth = (a)
            mindecrease = (b)
        if float (b) == maximum:
            maxmonth = (a)
            maxincrease = (b)
averagechange = round(sum(difference)/len(difference),2)

        
    #Print Statements
print('Financial Analaysis\n-------------')
print(f'Total Months: {month}')
print(f'Total: ${total}')
print(f'Average Change: ${averagechange}')
print('Greatest Increase in Profits: ' + str(maxmonth) + ' ($' + str(maxincrease) + ')')
print('Greatest Decrease in Profits: ' + str(minmonth) + ' ($' + str(mindecrease) + ')')
print(change)
