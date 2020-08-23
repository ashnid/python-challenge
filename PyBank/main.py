#Print top label
print("Financial Analysis")
print("----------------------------")

import os
import csv

#Set path for file
csvpath = os.path.join(".", "Resources", "budget_data.csv") 
pnl = 0.0
pnl_list = []
last_change = 0.0
i = 0

# Open CSV file
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile,delimiter=",")

    next(csvreader) #Skip the header row

    count = sum(1 for row in csvreader)

    #The total number of months included in the dataset
    print("Total Months: " + str(count)) # Row count minus header 

    csvfile.seek(0) # back to the begining of file
    next(csvreader) #Skip the header row

    for row in csvreader:
        #print(row[1])
        pnl = pnl + float(row[1])
        if i == 0:
            last_change = float(row[1])
        else:
            pnl_list.append(float(row[1]) - last_change)
            last_change = float(row[1])
        i += 1

    #The average of the changes in "Profit/Losses" over the entire period
    print("Total Profit and Losses: " + str(pnl))

    def Average(lst): 
        return sum(lst) / len(lst)

    print("Average Change in Profit and Losses: " + str(Average(pnl_list)))

   
    #The greatest increase in profits (date and amount) over the entire period

    # sorting the list 
    sorted(pnl_list)
    #print(sorted(pnl_list))

    #print(sorted(pnl_list)[-1])
    largest_number = sorted(pnl_list)[-1]
    #print(largest_number)

    #Find index of largest number in budget_data file
    largest_number_index = pnl_list.index(largest_number)
    #print("Largest Number Index:", largest_number_index)
    
    #Print date of largest increase in profits
    
    #sorting the list 
    sorted(pnl_list)
    #print(sorted(pnl_list))

    smallest_number = min(pnl_list)
    #print(smallest_number)

    smallest_number_index= pnl_list.index(smallest_number)
    #print("Smallest Number Index:", smallest_number_index)

    csvfile.seek(0) # back to the begining of file
    next(csvreader) #Skip the header row

    max_date = ""
    min_date = ""

    i = 0
    for row in csvreader:
        #print(row[1])
        if i == (largest_number_index + 1): # Index +1 since we are looking for the change from the previous year to the next year
            #print(row[0])
            max_date = row [0]
        elif i == (smallest_number_index + 1):
            #print(row[0])
            min_date = row [0]
        i += 1
        
    print("Greatest Increase in Profits:", sorted(pnl_list)[-1], max_date)
    print("Greatest Decrease in Profits:", min(pnl_list), min_date)

    #Export a text file with the results
    path = os.path.join('analysis', 'budget_results.txt')
    with open(path, 'w') as csvfileout:
        csvwriter = csv.writer(csvfileout)
        csvwriter.writerow(["Financial Analysis"])
        csvwriter.writerow(["----------------------------------------"])
        csvwriter.writerow(["Total Months:", count])
        csvwriter.writerow(["Total:", pnl])
        csvwriter.writerow(["Average Change:", Average(pnl_list)])
        csvwriter.writerow(["Greatest Increase in Profits:", max_date, largest_number])
        csvwriter.writerow(["Greatest Decrease in Profits:", min_date, smallest_number])
            
csvfile.close()
csvfileout.close()
