import csv

# Read CSV file
with open('budget_data.csv', 'r') as file:
 reader = csv.reader(file)
next(reader)  # Skip the header row
data = list(reader)

# Count total number of months
total_months = len(data)

# Create variables for total amount and changes in profit/losses
net_total = 0
previous_profit_loss = 0
total_changes = 0
greatest_increase = 0
greatest_decrease = 0

# loop through the data and calculate net total, changes, and find greatest increase/decrease
for row in data:
 date = row[0]
profit_loss = int(row[1])
net_total += profit_loss
if previous_profit_loss != 0:
 change = profit_loss - previous_profit_loss
total_changes += change
if change > greatest_increase:
 greatest_increase = change
greatest_increase_date = date
if change < greatest_decrease:
 greatest_decrease = change
greatest_decrease_date = date
previous_profit_loss = profit_loss

# Calculate average change
average_change = total_changes / (total_months - 1)

# Print the analysis results
print("Financial Analysis")
print("--------")
print(f"Total Months: {total_months}")
print(f"Net Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")
