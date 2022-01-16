import os
import csv

file_to_load = os.path.join("Resources", "budget_data.csv")
file_to_output = os.path.join("analysis", "budget_analysis.txt")

#Parameters
total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_net = 0

# Open and read csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Read in header row first and skip first row
    header = next(reader)
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])

    for row in reader:

        # Add total months
        total_months += 1
        total_net += int(row[1])
        
        # Net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list += [net_change]
        month_of_change +=[row[0]]

        # Greatest profit increase
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
    
        #Greatest profit decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

# Average net change
net_monthly_avg = sum(net_change_list) / len(net_change_list)

# Print results
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
    )

#Print output and text file
print(output)
with open(file_to_output, "w") as txt_file:
    txt_file.write("output")
    txt_file.write(output)
    txt_file.close()
        
        