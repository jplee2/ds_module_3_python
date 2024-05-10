# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)



# import module and set path
import csv
csvpath = 'PyBank/Resources/budget_data.csv'


# variables
month_count = 0
total_profit = 0
last_month_profit = None

changes = []
month_changes = []

# read in our data set
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # read in our header
    csv_header = next(csvreader)
    # print(f'CSV Header: {csv_header}')

    # calcuations using a for loop
    for row in csvreader:

        # count months
        month_count = month_count + 1

        # add profit
        total_profit = total_profit + int(row[1])

        # this month profit - last month profit
        if month_count == 1:
            last_month_profit = int(row[1])
        else:
            change = int(row[1]) - last_month_profit
            changes.append(change)
            month_changes.append(row[0])

            # reset last month profit
            last_month_profit = int(row[1])
    
    # print(month_count)
    # print(total_profit)
    # print(len(changes))


    # calculate our average change
    avg_change = sum(changes) / len(changes)
    print(avg_change)


    # calculate our greatest increase
    max_change = max(changes)
    max_month_indx = changes.index(max_change)
    max_month = month_changes[max_month_indx]
    # print(max_change)
    # print(max_month)


    # calculate our greatest decrease
    min_change = min(changes)
    min_month_indx = changes.index(min_change)
    min_month = month_changes[min_month_indx]
    # print(min_change)
    # print(min_month)


    # format our information for readability
    print('Financial Analysis')
    print('----------------------------')
    print(f'Total Months: {month_count}')
    print(f'Total: ${total_profit}')
    print(f'Average Change: ${avg_change:.2f}')
    print(f'Greatest Increase in Profits: {max_month} ${max_change}')
    print(f'Greatest Decrease in Profits: {min_month} ${min_change}')

file = open('financial_analysis.txt', 'w')
file.write('Financial Analysis\n')
file.write('----------------------------\n')
file.write(f'Total Months: {month_count}\n')
file.write(f'Total: ${total_profit}\n')
file.write(f'Average Change: ${avg_change:.2f}\n')
file.write(f'Greatest Increase in Profits: {max_month} ${max_change}\n')
file.write(f'Greatest Decrease in Profits: {min_month} ${min_change}\n')
