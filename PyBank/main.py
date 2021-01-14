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
    maximum = max(int(i) for i in difference)
    minimum = min(int(i) for i in difference)
    for (a,b) in zip(months[1:], difference):
        if float(b) == minimum:
            minmonth = (a)
        if float(b) == maximum:
            maxmonth = (a)
averagechange = round(sum(difference)/len(difference),2)

        
    #Print Statements
print('Financial Analaysis\n-------------')
print(f'Total Months: {month}')
print(f'Total: ${total}')
print(f'Average Change: ${averagechange}')
print(f'Greatest Increase in Profits: {maxmonth} (${maximum})')
print(f'Greatest Decrease in Profits: {minmonth} (${minimum})')

# Create text file with results
f = open('Analysis/PyBank_Analysis.txt', 'w')
f.write('Financial Analysis\n-------------\n')
f.write(f'Total Months: {month}\n')
f.write(f'Total: ${total}\n')
f.write(f'Average Change: ${averagechange}\n')
f.write(f'Greatest Increase in Profits: {maxmonth} (${maximum})\n')
f.write(f'Greatest Decrease in Profits: {minmonth} (${minimum})')
f.close()

