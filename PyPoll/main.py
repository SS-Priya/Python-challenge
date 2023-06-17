import os
import csv

# List declaration
country_list=[]
candidate_votes=[]
candidate_names=[]
vote_count=[]
vote_percent=[]
election_result=[]
analysis=[]

# Set path for .csv file
work_csv = os.path.join("Resources","election_data.csv")

# Open .csv file
with open(work_csv) as datafile:
    csvreader = csv.reader(datafile, delimiter=",")
   
    # Skipping the header to avoid counting it
    header = next(datafile)

    # Creating two list for country and cadidates votes
    for row in csvreader:
        country_list.append(row[1])
        candidate_votes.append(row[2])
      
    #Calculating Total Votes 
    tot_votes=len(candidate_votes) 
    
    
    # Next two "for" loops are for storing candidates names in a list
    for i in range(tot_votes-1):
        if country_list[i] != country_list[i+1]:
            index=int(i)
            break
    
    for j in range(index):
        if candidate_votes[j] != candidate_votes[j+1]:
            candidate_names.append(candidate_votes[j])
    candidate_names.append(candidate_votes[j])
    
    # Calculating number of votes for each candidates
    for i in candidate_names:
        count=0
        for j in candidate_votes:
            if j==i:
                count=count+1
    
    # Used a pre_defined round() function to round to 3 decimal places 
    
        vote_count.append(str(count))
        avg=round((count/tot_votes)*100,3)
        vote_percent.append(str(avg))
    
    # Finding maximum votes from a list
    winner=max(vote_count, key=lambda x:int(x)) 

    #Finding Winner Name
    count=len(vote_count)
    for i in range(count):
        if winner==vote_count[i]:
            winner_name= candidate_names[i]
 
    
# Stores results in a list, to print in terminal and write in a text file
analysis.append("\nElection Results\n")
analysis.append("\n-----------------------------")
analysis.append("\n\nTotal Votes: "+str(tot_votes))
for i in range(count):
    analysis.append("\n\n"+candidate_names[i]+": "+vote_percent[i]+"%  ("+vote_count[i]+")")
analysis.append("\n\n-----------------------------")
analysis.append("\n\nWinner: "+winner_name)
analysis.append("\n\n-----------------------------")

#Creates a text file under "analysis" folder and stores the path in output_file
output_file =os.path.join("analysis","Election_Results.txt")

# Opens the "Election_Results.txt" in write mode

with open(output_file,"w") as datafile: 
 
    # Loop to print the results in Terminal and Writes in file 
    
    for row in analysis:
          print(row)
          datafile.writelines(row)