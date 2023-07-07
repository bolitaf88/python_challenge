# Dependencies 

import csv

# Files to load output
csvfile_load = "C:/Users/bolit/OneDrive/Desktop/python_challenge/PyBank/resources/budget_data.csv"
csvfile_output = "C:/Users/bolit/OneDrive/Desktop/python_challenge/PyBank/analysis/financial_analysis2.txt"

# Track Various revenue parameters 
total_months = 0
prev_profit_loss = 0
month_of_change = []
Profit_loss_change_list = 0
greatest_increase =["", 0]
greatest_decrease =["", 9999999999999999999999999]
total_profit_loss = 0
# Read the csv and convert into list of dictionaries where; csvreader = csvr.
with open(csvfile_load, "r") as profit_loss_data:
    csvr = csv.DictReader(profit_loss_data)

# Skeeping the header row (row 1). Though we don't have to worry about this stage, I just include for safety purposes.
    header = next(csvr)
    firstrow = next(csvr)
    total_months = total_months + 1
    total_profit_loss = total_profit_loss + int(firstrow["Profit/Losses"])
    prev_profit_loss = int(firstrow["Profit/Losses"])
# Time to loop through row two and beyond 
    for row in csvr: 

# Counting the totals "total_months" and "total_profit/loss"
        total_months = total_months + 1
        total_profit_loss = total_profit_loss + int(row["Profit/Losses"])


# Counting the Profit/loss changes
        Profit_loss_change = int(row["Profit/Losses"]) - prev_profit_loss
        prev_profit_loss = int(row["Profit/Losses"])
        Profit_loss_change_list = Profit_loss_change_list + Profit_loss_change
        month_of_change = month_of_change + [row["Date"]]
# calculating the greatest increase 
        if (Profit_loss_change > greatest_increase[1]):
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = Profit_loss_change

# Calculating greatest decrease
        if (Profit_loss_change < greatest_decrease[1]):
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = Profit_loss_change

    
# Calc Avg Profit/loss change. N/B* Using "profit_loss_change_list" as a denominator generates the same results for the "Avg_change."
    Avg_profit_loss = (Profit_loss_change) / total_months - 1


# Generating the Results 
output = (
    f"\nFinancial Analysis\n"
    f"------------------------------\n"
    f"Total Months: {total_months}\n"
    f"total Profit: ${total_profit_loss}\n"
    f"Avg Change: ${Avg_profit_loss}\n"
    f"Grtest Inc in P: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Grtest dec in p: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

# Printing the output (print) and exporting the results to text file (with open "statement")
print(output)

with open(csvfile_output, "w") as txt_file:
    txt_file.write(output)





    









