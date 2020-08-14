#Adriana Avalos Vargas

#Lets call de modules
#Module for paths
import os
# Module for reading CSV files
import csv

#- - - - - - - - - - - - - -- - - - - -- - - - - - - -
#Lets fix the path
csvpath = os.path.join('Resources', 'budget_data.csv')

#- - - - - - - - - - - - - - - - - - - - - - - - - -- 
#A counter to count the number of rows which is equivalent to the number
#of months
c_months = 0
#A variable to add the profit or losses in the entire period
c_pl = 0

#A variable that stores the previous profit/loss data
previous_data = 0
#A variable that stores the actual profit/loss data
actual_data = 0
# a list that will store the monthly change, for now is empty
changes = [] #money
months= [] # the month


#Open de csv path
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        #print(row)
        #Lets count the number of months
        c_months += 1
        #Lets investiagte what kind of data is stored in the second position of each row
        # extract the profit ir loss in each month (row)
        #pl = row[1]
        #print(type(pl))
        #Since it is a string it is necesary to convert it to a number
        pl = float(row[1])
        #Now we can add it in the "counter" for total profit losses
        c_pl +=  pl
        #Lets extrat the actual value
        actual_data = pl
        #Lets do the substraction to obtain the change (actual-previous)
        #and store it in a list
        difference = actual_data - previous_data
        changes.append(difference)
        months.append(row[0])
        #Rewrite previous data
        previous_data = float(row[1])



#Note: Since we define directly the difference or changes, there is a false difference 
# that comes from subtracting zero from the first observation so it must be removed.
#Lets remove it from changes and months
changes.pop(0)
months.pop(0)

#Up to here everything works, therefore we can try to finish the financial analysis

#Lets sum the changes in profit loss
#Define variable for total change
total_change = 0.0
#Cicle to add
for change in range(0, len(changes)):
    total_change  += changes[change]

    
#Get the number of obs
n = len(changes)

#Define average
pl_average = round(total_change/n,2)

#Lets look for the maximun change
greatest_increase = 0
position = 0

for change in range(0,len(changes)):
    if changes[change] > greatest_increase:
        greatest_increase = changes[change]
        position = change


#Lets look for the minimum change
greatest_decrease = 0
position_2 = 0

for change in range(0,len(changes)):
    if changes[change] < greatest_decrease:
        greatest_decrease = changes[change]
        position_2 = change


#Lets print the results.
print("Financial Analysis")
print("- - - - - - - - - - - - - - - - - ")
print(f"Total months : {c_months}")
print(f"Total : ${c_pl}" )
print(f"Average Change: ${pl_average}")
print(f"Greatest Increase in Profits: {months[position]} (${greatest_increase}) ")
print(f"Greatest Decrease in Profits; {months[position_2]} (${greatest_decrease}")

#Lets save the results in a text file
#Lets specify the output path
output_path = os.path.join("analysis", "Financial_analysis.txt")
f = open(output_path, "w")
f.write("Financial Analysis" + '\n')
f.write("- - - - - - - - - - - - - - - - - " + '\n')
f.write(f"Total months : {c_months}" + '\n')
f.write(f"Total : ${c_pl}" + '\n' )
f.write(f"Average Change: ${pl_average}" + '\n')
f.write(f"Greatest Increase in Profits: {months[position]} (${greatest_increase}) " + '\n')
f.write(f"Greatest Decrease in Profits; {months[position_2]} (${greatest_decrease})" + '\n')
f.close()