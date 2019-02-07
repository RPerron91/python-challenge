import os
import csv

#lists to store info from csv
all_profits = []

#initializes counters
totalMonths = 0
profit = 0

#setup path to pull the csv file
csvpath = os.path.join('Resources', 'budget_data.csv')
print(csvpath)
with open(csvpath) as csvfile:

    #specifies the delimiter and sets variable for content
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #reads header row first 
    csv_header = next(csvreader)
   


    
    #loop through each row in csvreader
    for row in csvreader:
        #counts the number of rows in csvreader which equals the total number of months
        totalMonths += 1
        
        #appends row element to list for comparisons
        all_profits.append(row[1])

#using values from list to calculate each variable
greatest_decrease = min(float(num) for num in all_profits)
greatest_increase = max(float(num) for num in all_profits)
profit = sum(float(num) for num in all_profits)
average = profit/totalMonths

#printing all values to terminal
print("Financial Analysis")
print("------------------------")
print(f"Total Months: {totalMonths}")
print(f"Total Amount: ${profit}")
print("Average Change: $", round(average, 2))
print(f"Greatest Increase: ${greatest_increase}")
print(f"Greatest Decrease: ${greatest_decrease}")

#making path for new file
output_path = os.path.join('Resources', 'budget_summary.txt')

#outputs values to text document
with open(output_path, "w", newline='') as textfile:
    print("Financial Analysis", file=textfile)
    print("------------------------", file=textfile)
    print(f"Total Months: {totalMonths}", file=textfile)
    print(f"Total Amount: ${profit}", file=textfile)
    print("Average Change: $", round(average, 2), file=textfile)
    print(f"Greatest Increase: ${greatest_increase}", file=textfile)
    print(f"Greatest Decrease: ${greatest_decrease}", file=textfile)