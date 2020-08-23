#Print top label
print("Election Results")
print("----------------------------")

import os
import csv
from collections import Counter

#Set path for file
csvpath = os.path.join(".", "Resources", "election_data.csv") 


# Open CSV file
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile,delimiter=",")

    next(csvreader) #Skip the header row

    count = sum(1 for row in csvreader)

    #The total number of months included in the dataset
    print("Total Votes: " + str(count)) # Row count minus header
    print("----------------------------")

    #complete list of candidates who received votes
    csvfile.seek(0) # back to the begining of file
    next(csvreader) #Skip the header row
    
    #Create blank list for candidate names
    candidates_list = []
    for row in csvreader:
        if row[2] not in candidates_list:
            candidates_list.append(row[2])
    print ("Candidates who recieved votes" ,candidates_list)
    print("----------------------------")

    #The total number of votes each candidate won
    csvfile.seek(0) #back to the begining of file
    next(csvreader) #Skip the header row

    #variables
    candidates_unique = []
    candidate_count = []

    for row in csvreader:
            #if candidate is alreaady in list then locate the candidate by index # and increment the vote count by 1
            if row[2] in candidates_unique:
                candidate_index = candidates_unique.index(row[2])
                candidate_count[candidate_index] = candidate_count[candidate_index] + 1
            else:
                #if candidate was not found in candidates_unique list then add to list and add 1 to vote count
                candidates_unique.append(row[2])
                candidate_count.append(1)
    print ("Number of votes for each candidate:", candidate_count)

    #The percentage of votes each candidate won
    Khan_count = (candidate_count [0] /count) *100
    Correy_count = (candidate_count [1]/count) *100
    Li_count = (candidate_count [2]/count) *100
    OTooley_count = (candidate_count [3]/count) *100
    print("Percentage for Khan:", Khan_count)
    print("Percentage for Correy:", Correy_count)
    print("Percentage for Li:" , Li_count)
    print("Percentage for O'Tooley:" , OTooley_count)

    #The winner of the election based on popular vote.
    pct = []
    max_votes = candidate_count[0]
    max_index = 0

    for x in range(len(candidates_unique)):
        vote_pct = round(candidate_count[x]/count*100, 2)
        pct.append(vote_pct)
        
        if candidate_count[x] > max_votes:
            max_votes = candidate_count[x]
            max_index = x
    winner = candidates_unique[max_index] 

    print("----------------------------")
    print ("Winner:" , winner)
    print("----------------------------")

# Export a text file with the results
output_path = os.path.join('analysis', 'election_results.txt')
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["----------------------------------------"])
    csvwriter.writerow(["Total Votes: " + str(count)])
    csvwriter.writerow(["----------------------------------------"])
    csvwriter.writerow(["Number of votes for each candidate:[Khan, Correy, Li', O'Tooley]", candidate_count])
    csvwriter.writerow(["----------------------------------------"])
    csvwriter.writerow(["Percentage for Khan:", Khan_count])
    csvwriter.writerow(["Percentage for Correy:", Correy_count]) 
    csvwriter.writerow(["Percentage for Li:" , Li_count])
    csvwriter.writerow(["Percentage for O'Tooley:" , OTooley_count])
    csvwriter.writerow(["----------------------------------------"])
    csvwriter.writerow(["Winner:" , winner])
    csvwriter.writerow(["----------------------------------------"])

    csvfile.close()

    