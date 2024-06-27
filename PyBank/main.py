# Hi, this is my project! I'm David Flores Benitez :)

# First, I will import the CSV file needed for this project
import csv

# Now, I will assign variables to store the necessary results
total_of_months = 0
Grand_total = 0
Average_Change = 0
previous_profit_losses = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 0]
dates = []
changes = []

# Open the CSV file
with open('budget_data.csv') as bank_data:
    Bank_data_read = csv.reader(bank_data, delimiter=',')
    Titles = next(Bank_data_read)  # Skip the header row
    
    # Process the first row to initialize variables
    first_row = next(Bank_data_read)
    total_of_months += 1
    Grand_total += int(first_row[1])
    previous_profit_losses = int(first_row[1])
    
    # Process the rest of the rows
    for rows in Bank_data_read:
        total_of_months += 1
        Grand_total += int(rows[1])
        
        # Calculate the change and add it to the list of changes
        change = int(rows[1]) - previous_profit_losses
        changes.append(change)
        dates.append(rows[0])
        previous_profit_losses = int(rows[1])
        
        # Check for the greatest increase in profits
        if change > greatest_increase[1]:
            greatest_increase[0] = rows[0]
            greatest_increase[1] = change
        
        # Check for the greatest decrease in profits
        if change < greatest_decrease[1]:
            greatest_decrease[0] = rows[0]
            greatest_decrease[1] = change

# Calculate the average change
average_change = sum(changes) / len(changes)

# Prepare the summary of financial analysis
data_analysis = (
    f'Financial Analysis\n'
    f'----------------------------\n'
    f'Total Months: {total_of_months}\n'
    f'Total: ${Grand_total}\n'
    f'Average Change: ${average_change:.2f}\n'
    f'Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n'
    f'Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n'
)

# Print the analysis to the terminal
print(data_analysis)

# Export the analysis to a text file
output_file = "financial_analysis.txt"
with open(output_file, "w") as txt_file:
    txt_file.write(data_analysis)