import os
import csv
os.listdir()
file = os.path.join(r'C:\Users\THINKPAD X1\Documents\Github\python-challenge\Pybank\budget_data.csv')
total_months = []
total_pl = []
monthly_pl_change = []
with open(file,'r',newline="") as csvfile:
    csvreader =csv.reader(csvfile,delimiter =',')
    headers = next(csvreader, None)
    for row in csvreader: 
        total_months.append(row[0])
        total_pl.append(int(row[1]))
    for i in range(len(total_pl)-1):
        monthly_pl_change.append(total_pl[i+1]-total_pl[i])
        max_increase_value = max(monthly_pl_change)
        max_decrease_value = min(monthly_pl_change)
        max_increase_month = monthly_pl_change.index(max(monthly_pl_change)) + 1
        max_decrease_month = monthly_pl_change.index(min(monthly_pl_change)) + 1 
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_pl)}")
print(f"Average Change: {round(sum(monthly_pl_change)/len(monthly_pl_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")
output_file = os.path.join(r'C:\Users\THINKPAD X1\Documents\Github\python-challenge\Pybank\Financial_Analysis_Summary.txt')
with open(output_file,"w",newline="") as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {len(total_months)}\n")
    file.write(f"Total: ${sum(total_pl)}\n")
    file.write(f"Average Change: {round(sum(monthly_pl_change)/len(monthly_pl_change),2)}\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})\n")