import os

import csv

csvpath = os.path.join('..', 'main', 'accounting.csv')

with open(csvpath, newline='') as csvfile:

    #specifies the delimiter and sets variable for content
    csvreader = csv.reader(csvfile, delimiter=',')
    
    print(csvreader)

    #reads header row first 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        
