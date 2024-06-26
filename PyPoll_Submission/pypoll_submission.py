# In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.
# Your task is to create a Python script that analyzes the votes and produces the following results:

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


### STEP 1: Import
# Load in module and set path
import csv
csvpath = 'PyPoll_Submission/election_data.csv'


# Floatin Variable Creation Section
total_votes = 0
c1_amnt = 0
c2_amnt = 0
c3_amnt = 0


### STEP 2: Read in our data set
# The with statement ensures that the file is properly closed after the block of code is executed.
with open(csvpath, encoding='UTF-8') as csvfile:
    # The csv.reader() function is used to create a reader object csvreader that will iterate over lines in the CSV file (which use ',' to separate values)
    csvreader = csv.reader(csvfile, delimiter=',')
    # The next() function is called to read the next row from the CSV file, which in this case is the header row. It is then stored as a variable csv_header
    csv_header = next(csvreader)

    
    ### STEP 3: Calculations using a for loop
    for row in csvreader:
        # For each row, the variable total_votes is incremented by 1, effectively tallying the total number of votes cast.
        total_votes += 1
        # If the value in the 3rd column of the current row is 'Charles Casper Stockham', the count of votes for this candidate (c1_amnt) is incremented by 1.
        if row[2] == 'Charles Casper Stockham':
            c1_amnt += 1
        # If the value in the 3rd column is 'Diana DeGette', the count of votes for this candidate (c2_amnt) is incremented by 1.
        elif row[2] == 'Diana DeGette':
            c2_amnt += 1
        # If the candidate is neither 'Charles Casper Stockham' nor 'Diana DeGette', the count of votes for the third candidate is incremented by 1 (c3_amnt).
        else:
            c3_amnt += 1

    
    ### STEP 4: Calculations building off of our for loop
    # This line calculates the percentage of votes received by candidate 1 ('Charles Casper Stockham').
    prcnt_c1 = c1_amnt/(c1_amnt + c2_amnt + c3_amnt)
    # This line calculates the percentage of votes received by candidate 2 ('Diana DeGette').
    prcnt_c2 = c2_amnt/(c1_amnt + c2_amnt + c3_amnt)
    # This line calculates the percentage of votes received by candidate 3 (the third candidate).
    prcnt_c3 = c3_amnt/(c1_amnt + c2_amnt + c3_amnt)
    
    
    ### STEP 5: Create the desired table &  format our information
    print('Election Results')
    print('-----------------------')
    # This line uses an f-string to dynamically insert the total number of votes (total_votes) into the output message "Total Votes: ".
    print(f'Total Votes: {total_votes}')
    print('-----------------------')
    # The percentage of votes received by candidate 1 (prcnt_c1) is formatted as a percentage with 3 decimal places.
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


### STEP 6: Write our table out to a new document
# This line opens a file named 'election_results' in write mode ('w') and assigns the file object to the variable file2.
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
file2.close()