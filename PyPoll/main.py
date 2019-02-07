import csv
import os

#initializes array for all candidates, including duplicates
candidates = []


csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    #specifies the delimiter and sets variable for content
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #reads header row first 
    csv_header = next(csvreader)


    #looping through all of csv file
    for row in csvreader:
       #makes a list of all candidate votes, including duplicates
       candidates.append(row[2])

    #initializes array   
    num_cands = []
    #makes a set of unique values from candidates list
    candidates_short = list(set(candidates))
        
    #looping through elements in list candidates_short
    for x in candidates_short:
        #counts each instance of a new candidate and sorts them into a list
        num_cands.append(candidates.count(x))

#gets a total by adding the values of all the elements in array
total_votes = sum(float(num) for num in num_candidates)
#creating a dictionary of dictionaries to reference category value later
voter_dict = dict(zip('Name':candidates_short[], 'Votes':num_cands[])


most_votes = max(float(num) for num in num_cands)
#prints summary in command line
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
#loops each candidate in dictionary
for results in voter_dict:
    #calculate percentage of votes cast and print values for each candidate
    percent_votes = results['Name']/total_votes*100
    print(f" Candidate:{results['Name']} Votes:{results['Votes']} Percent Votes:{round(percent_votes, 2)}% ")
#print the winner using dictionary reference to the value of the name 
print(f"Winner is:{d['Name':most_votes]}")

#making path for new file
output_path = os.path.join('Resources', 'voter_summary.txt')

#outputs values to text document
with open(output_path, "w", newline='') as textfile:
    print("Election Results", file=textfile)
    print("------------------------", file=textfile)
    print(f"Total Votes: {total_votes}", file=textfile)
    print("-------------------------", file=textfile)
#loops each candidate in dictionary
    for results in voter_dict:
        #calculate percentage of votes cast and print values for each candidate
        percent_votes = results['Name']/total_votes*100
        print(f" Candidate:{results['Name']} Votes:{results['Votes']} Percent Votes:{round(percent_votes, 2)}% ", file=textfile)
    #print the winner using dictionary reference to the value of the name   
    print(f"Winner is:{d['Name':most_votes]}")