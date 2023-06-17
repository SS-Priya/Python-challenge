import os
import csv

# List declaration

prof_loss_list=[]
date_list=[]
monthly_changes=[]
monthly_name=[]
prof_loss_conv=[]
analysis=[]


# Set path for .csv file
work_csv = os.path.join("Resources","budget_data.csv")

# Open .csv file
with open(work_csv) as datafile:
    csvreader = csv.reader(datafile, delimiter=",")
   
    # Skipping the header to avoid counting it
    header = next(datafile)

    # Creating two list for date and profit&loss
    for row in csvreader:
        date_list.append(row[0])
        prof_loss_list.append(row[1])

    #Finding Total-Months 
    tot_months=len(date_list)

    # Converting the profit_loss list from string datatype to integer
    prof_loss_conv=[int(x)for x in prof_loss_list]

    # Calculating Net Amount by calling a user_define function called sum()
    net_amount=(sum(prof_loss_conv))

    # Finding changes in profit/loss and storing the changes and corrensponding 
    # dates in 2 new list
    for i in range(tot_months-1):
         
         monthly_changes.append(prof_loss_conv[i+1]-prof_loss_conv[i])      
         monthly_name.append(date_list[i+1])

    # Assigning first list value to variables to find increase and decrease in profit
    temp1=temp2=monthly_changes[0]

    # Stores list index value for greatest,lowest changes in 2 variables 
    # for printing results
    
    for i in range(tot_months-1):
        if monthly_changes[i]>temp1:
            temp1=monthly_changes[i]
            index1=i
        if monthly_changes[i]<temp2:
             temp2=monthly_changes[i]
             index2=i
   
    # Calculates Average in changes
    # Used pre_defined round() function to round to 2 decimal places

    average_pl=sum(monthly_changes)
    average_pl=round((average_pl/len(monthly_changes)),2)
    
    # User Define function definition to calculate sum of list values
    def sum(total):
        net_amount=0
        for x in total:
            net_amount= net_amount+total
        return net_amount
    
    # Stores results in a list, to print in terminal and write in a text file

    analysis.append("Financial Analysis\n")
    analysis.append("\n----------------------------------")
    analysis.append("\n\nTotal Months: "+str(tot_months))
    analysis.append("\n\nTotal: $"+str(net_amount))
    analysis.append("\n\nAverage Change: $"+str(average_pl))
    analysis.append("\n\nGreatest Increase in Profits: "+str(monthly_name[index1])+" ($"+str(monthly_changes[index1])+")")
    analysis.append("\n\nGreatest Decrease in Profits: "+str(monthly_name[index2])+" ($"+str(monthly_changes[index2])+")")
        
# Creates a text file under "analysis" folder and stores the path in output_file
output_file =os.path.join("analysis","Final_Analysis.txt")

# Opens the "Final_Analysis.txt" in write mode
with open(output_file,"w") as datafile: 
 
    # Loop to print the results in Terminal and Writes in file 
    for row in analysis:
        print(row)
        datafile.writelines(row)