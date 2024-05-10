# Election Results
# -------------------------
# Total Votes: 369711
# -------------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette
# -------------------------

# load in module and set path
import csv
csvpath = 'PyPoll/Resources/election_data.csv'


# variables
total_votes = 0
c1_amnt = 0
c2_amnt = 0
c3_amnt = 0


# read in our data set
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # read in our header
    csv_header = next(csvreader)
    # print(f'CSV Header: {csv_header}')
        
    # tally votes (amount of rows)
    for row in csvreader:
        
        # for every row, add 1 to our variable total_votes
        total_votes += 1

        # if the value in our 3rd column is equal to CCS, add 1 to our variable c1_amnt
        if row[2] == 'Charles Casper Stockham':
            c1_amnt += 1
        # if the value in our 3rd column is equal to DG, add 1 to c2_amnt
        elif row[2] == 'Diana DeGette':
            c2_amnt += 1
        # otherwise, add 1 to c3_amnt
        else:
            c3_amnt += 1

    # calculate percentages and assign them variables 
    prcnt_c1 = c1_amnt/(c1_amnt + c2_amnt + c3_amnt)
    prcnt_c2 = c2_amnt/(c1_amnt + c2_amnt + c3_amnt)
    prcnt_c3 = c3_amnt/(c1_amnt + c2_amnt + c3_amnt)

    # let's check and see if all that worked
    # print(total_votes)
    # print(c1_amnt)
    # print(c2_amnt)
    # print(c3_amnt)
    # print(prcnt_c1)
    # print(prcnt_c2)
    # print(prcnt_c3)

    # format our information to make it more readable
    print('Election Results')
    print('-----------------------')
    print(f'Total Votes: {total_votes}')
    print('-----------------------')
    print('Charles Casper Stockham: {:2.3%} ({})'.format(prcnt_c1, c1_amnt))
    print('Diana DeGette: {:2.3%} ({})'.format(prcnt_c2, c2_amnt))
    print('Raymon Anthony Doane: {:2.3%} ({})'.format(prcnt_c3, c3_amnt))
    print(f'----------------------')

    # find our winner
    # if c1 got the most votes, declare c1 winner
    if c1_amnt > (c2_amnt or c3_amnt):
        print('Winner: Charles Casper Stockham')
    # if c2 got the most votes, declare c2 winner
    elif c2_amnt > (c1_amnt or c3_amnt):
        print('Winner: Diana DeGette')
    # otherwise, declare c3 winner
    else:
        print('Winner: Raymon Anthony Doane')

file2 = open('election_results', 'w')
file2.write('Election Results\n')
file2.write('-----------------------\n')
file2.write(f'Total Votes: {total_votes}\n')
file2.write('-----------------------\n')
file2.write('Charles Casper Stockham: {:2.3%} ({})\n'.format(prcnt_c1, c1_amnt))
file2.write('Diana DeGette: {:2.3%} ({})\n'.format(prcnt_c2, c2_amnt))
file2.write('Raymon Anthony Doane: {:2.3%} ({})\n'.format(prcnt_c3, c3_amnt))
file2.write('-----------------------\n')
file2.write('Winner: Diana DeGette\n')
file2.write('-----------------------\n')