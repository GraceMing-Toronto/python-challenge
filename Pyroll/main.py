import os
import csv
file = os.path.join(r'C:\Users\THINKPAD X1\Documents\Github\python-challenge\Pyroll\election_data.csv')
total_votes = 0 
winner_votes = 0
winner=""
khan_votes = 0
khanpercent = 0.00
correy_votes = 0
correypercent = 0.00
li_votes = 0
lipercent = 0.00
otooley_votes = 0
otooleypercent = 0.00
with open(file,newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",") 
    header = next(csvreader)
    for row in csvreader:
        total_votes +=1
        if (row[2] == "Khan"):
            khan_votes += 1
        elif (row[2] == "Correy"):
            correy_votes += 1
        elif (row[2] == "Li"):
             li_votes += 1
        elif (row[2] == "O'Tooley"): 
            otooley_votes += 1
khanpercent = round(khan_votes / total_votes*100,3)
correypercent = round(correy_votes / total_votes * 100,3)
lipercent = round(li_votes / total_votes * 100,3)
otooleypercent = round(otooley_votes / total_votes* 100,3)
winner_votes = max(khan_votes, correy_votes, li_votes, otooley_votes)
if(winner_votes == khan_votes):
    winner = "Khan" 
elif(winner_votes == correy_votes):
    winner = "Correy"
elif(winner_votes == li_votes):
    winner = "Li"
else:
    winner = "O'Tooley"
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Khan: {khanpercent}% ({khan_votes})")
print(f"Correy: {correypercent}% ({correy_votes})")
print(f"Li: {lipercent}% ({li_votes})")
print(f"O'Tooley: {otooleypercent}% ({otooley_votes})")
print(f"----------------------------")
print(f"Winner: {winner}")
print(f"----------------------------")
output_file = os.path.join(r'C:\Users\THINKPAD X1\Documents\Github\python-challenge\Pyroll\Election_Results_Summary.txt')
with open(output_file,"w",newline="") as file:
    file.write("Election Results\n")
    file.write("----------------------------\n")
    file.write(f"Khan: {khanpercent}% ({khan_votes})\n")
    file.write(f"Total: ${total_votes}\n")
    file.write(f"Correy: {correypercent}% ({correy_votes})\n")
    file.write(f"Li: {lipercent}% ({li_votes})\n")
    file.write(f"O'Tooley: {otooleypercent}% ({otooley_votes})\n")
    file.write("----------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("----------------------------\n")