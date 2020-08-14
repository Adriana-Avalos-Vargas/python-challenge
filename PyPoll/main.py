#Adriana Avalos Vargas

#Lets call de modules
#Module for paths
import os
# Module for reading CSV files
import csv

#- - - - - - - - - - - - - -- - - - - -- - - - - - - -
#Lets fix the path
csvpath = os.path.join('Resources', 'election_data.csv')

#- - - - - - - - - - - - - - - - - - - - - - - - - -- 
#A counter to count the number of votes
c_votes = 0

#An empty dictionary
candidates = dict()
list_keys = candidates.keys



#Open de csv path
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        #print(row)
        #Lets count the number of votes
        c_votes += 1
        #Extract the name of the candidate
        name_candidate = row[2]
        #Lets define the keys of the dictionary
        if name_candidate in candidates:
            candidates[name_candidate] += 1
        else:
            candidates.update({row[2] : 1})
        
#lets see the result
print(candidates)

#Extract the names
names = list(candidates.keys())
#Extract votes for each candidates
votes = list(candidates.values())

#Look for the winner
max_vote = 0
winner = "0"

for x in range(0,len(votes)):
    if votes[x] > max_vote:
        max_vote = votes[x]
        winner = names[x]


prueba = []
#Look for the percentage
index = 0
while index < len(votes):
    valor = votes[index]/c_votes*100
    prueba.append(valor)
    index = index + 1



#Print election results
print("Election Results")
print("- - - - - - - - - - - - - - - - - ")
print(f"Total Votes: {c_votes}")
print("- - - - - - - - - - - - - - - - - ")
for i in range(0,4):
    print(f"{names[i]}: {round(prueba[i],3)} % ({votes[i]})")
print("- - - - - - - - - - - - - - - - - ")
print(f"Winner: {winner}")

#Lets save in a text file
#Lets specify the output path
output_path = os.path.join("analysis", "Vote_results.txt")
f = open(output_path, "w")
f.write("Election Results" + '\n')
f.write("- - - - - - - - - - - - - - - - - " + '\n')
f.write(f"Total Votes: {c_votes}" + '\n')
f.write("- - - - - - - - - - - - - - - - - " + '\n')
for i in range(0,4):
    f.write(f"{names[i]}: {round(prueba[i],3)} % ({votes[i]})" + '\n')
f.write("- - - - - - - - - - - - - - - - - " + '\n')
f.write(f"Winner: {winner}" + '\n')
f.close()