#create dependencies
import os
import csv

#Read csv file
csvpath = os.path.join("Resources", "election_data.csv")
votes = []
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    # The total number of votes cast
    vote_total = 0
    data = list(csvreader)
    vote_total = len(data)

    # A complete list of candidates who received votes
    khan = 0
    correy = 0
    li = 0
    otooley = 0
    
    # The total number of votes each candidate won
    for row in data:
        votes.append(row[2])
    for count in votes:
        if count == 'Khan':
            khan += 1
        elif count == 'Correy':
            correy += 1
        elif count == 'Li':
            li += 1
        elif count == "O'Tooley":
            otooley += 1

    # The percentage of votes each candidate won
    khan_pct = round((khan / vote_total) * 100)
    correy_pct = round((correy / vote_total) * 100)
    li_pct = round((li / vote_total) * 100)
    otooley_pct = round((otooley / vote_total) * 100)

    # The winner of the election based on popular vote.
    winner = []
    vote_list = [khan, correy, li, otooley]
    popular_vote = max(vote_list)
    if popular_vote == khan:
        winner.append('Khan')
    elif popular_vote == correy:
        winner.append("Correy")
    elif popular_vote == li:
        winner.append("Li")
    elif popular_vote == otooley:
        winner.append("O'Tooley")

    #Print Results
    print('Election Results\n------------------------')
    print(f'Total Votes: {vote_total}\n------------------------')
    print(f'Khan: {khan_pct}% ({khan})')
    print(f'Correy: {correy_pct}% ({khan})')
    print(f'Li: {li_pct}% ({khan})')
    print(f"O'Tooley: {otooley_pct}% ({khan})\n------------------------")
    print(f'Winner: {winner}\n------------------------')

# Create text file with results
f = open('Analysis/PyPoll_Analysis.txt', 'w')
f.write('Election Results\n------------------------\n')
f.write(f'Total Votes: {vote_total}\n------------------------\n')
f.write(f'Khan: {khan_pct}% ({khan})\n')
f.write(f'Correy: {correy_pct}% ({khan})\n')
f.write(f'Li: {li_pct}% ({khan})\n')
f.write(f"O'Tooley: {otooley_pct}% ({khan})\n------------------------\n")
f.write(f'Winner: {winner}\n------------------------')
f.close()
