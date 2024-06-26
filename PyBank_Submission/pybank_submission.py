# In this Challenge, you are tasked with creating a Python script to analyze the financial records of your company.
# Your task is to create a Python script that analyzes the records to produce the table below:
# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)


### STEP 1: Import
# Import module and set path
import csv
csvpath = 'PyBank_Submission/budget_data.csv'


# Variable Creation Section
month_count = 0
total_profit = 0
last_month_profit = None
changes = []
month_changes = []


### STEP 2: Read in our data set
# The with statement ensures that the file is properly closed after the block of code is executed.
with open(csvpath, encoding='UTF-8') as csvfile:
    # The csv.reader() function is used to create a reader object csvreader that will iterate over lines in the CSV file (which use ',' to separate values)
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read in our header
    csv_header = next(csvreader)

    
    ### STEP 3: Calculations using a for loop
    for row in csvreader:
        # For every row in the data set we will add 1 to our month_count variable, which will tally the total amount of months in our data set
        month_count = month_count + 1
        # For every row we will take the integer of the second cell and add it to our total_profit variable, giving us the sum of our profit/losses.
        total_profit = total_profit + int(row[1])
        # This condition checks if it is the first month in the dataset. If it is the first month (month_count == 1), the profit value of the current row is             assigned to last_month_profit.
        if month_count == 1:
            last_month_profit = int(row[1])
        # If it is not the first month, the code calculates the profit change between the current month and the previous month.
        # The profit change is computed by subtracting the profit value of the previous month (last_month_profit) from the profit value of the current month             (int(row[1])).
        else:
            change = int(row[1]) - last_month_profit
            # The calculated profit change is then appended to the changes list to store all the profit changes.
            changes.append(change)
            # The corresponding month value (row[0]) is also appended to the month_changes list to track which month each profit change corresponds to.
            month_changes.append(row[0])
            # This step ensures that the profit value of the current month becomes the "last month profit" for the next iteration, enabling the calculation of               the next month's profit change.
            last_month_profit = int(row[1])

    
    ### STEP 4: Calculations building off of our for loop
    # Calculate our average change
    avg_change = sum(changes) / len(changes)
    # Calculate our greatest increase
    max_change = max(changes)
    # This line finds the index of the maximum value (max_change) in the list changes and assigns it to the variable max_month_indx.
    max_month_indx = changes.index(max_change)
    # This line retrieves the corresponding month value from the list month_changes using the index max_month_indx and assigns it to the variable max_month.
    max_month = month_changes[max_month_indx]
    # Calculate our greatest decrease
    min_change = min(changes)
    min_month_indx = changes.index(min_change)
    min_month = month_changes[min_month_indx]

    
    ### STEP 5: Create the desired table & format for readability
    print('Financial Analysis')
    print('----------------------------')
    print(f'Total Months: {month_count}')
    print(f'Total: ${total_profit}')
    print(f'Average Change: ${avg_change:.2f}')
    print(f'Greatest Increase in Profits: {max_month} ${max_change}')
    print(f'Greatest Decrease in Profits: {min_month} ${min_change}')


### STEP 6: Write our table out to a new document
# This line opens a file named 'election_results' in write mode ('w') and assigns the file object to the variable file2.
file = open('financial_analysis.txt', 'w')
file.write('Financial Analysis\n')
file.write('----------------------------\n')
file.write(f'Total Months: {month_count}\n')
file.write(f'Total: ${total_profit}\n')
file.write(f'Average Change: ${avg_change:.2f}\n')
file.write(f'Greatest Increase in Profits: {max_month} ${max_change}\n')
file.write(f'Greatest Decrease in Profits: {min_month} ${min_change}\n')
file.close()