# ## PyPoll

# * In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)

# * You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. 

# Import module to create file paths across operating systems:
import os as os

# Import module for reading CSV files:
import csv as csv

# Assign variable csvpath to file location:
csvpath = os.path.join("Resources", "election_data.csv")

# Open file at csvpath and read with comma delimiter:
with open(csvpath,'r', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Assign variable 'header' to first row of csvreader data:
    header = next(csvreader)

# Your task is to create a Python script that analyzes the votes and calculates each of the following:

#   * The total number of votes cast

    # Convert data to list:
    csvdata = list(csvreader)

votes = set([vote[0] for vote in csvdata])
total_votes = len(votes)
# print(total_votes)

#   * A complete list of candidates who received votes

candidates = set([(vote[2]) for vote in csvdata])
# print(candidates)  # <--results:  {"O'Tooley", 'Correy', 'Li', 'Khan'}

#   * The total number of votes each candidate won

# create an empty list for each candidate, then loop through data and add name to that list each time the candidate name matches to the voting record, ultimately counting the length of that list as the total number of votes:

Khan_votes = []
for vote in csvdata:
    if vote[2] == "Khan":
        Khan_votes.append(vote[2])
Khan_total = len(Khan_votes)
# print(Khan_total)

Correy_votes = []
for vote in csvdata:
    if vote[2] == "Correy":
        Correy_votes.append(vote[2])
Correy_total = len(Correy_votes)
# print(Correy_total)

Li_votes = []
for vote in csvdata:
    if vote[2] == "Li":
        Li_votes.append(vote[2])
Li_total = len(Li_votes)
# print(Li_total)

OTooley_votes = []
for vote in csvdata:
    if vote[2] == "O'Tooley":
        OTooley_votes.append(vote[2])
OTooley_total = len(OTooley_votes)
# print(OTooley_total)

#   * The percentage of votes each candidate won

Khan_pct = round((Khan_total / total_votes) * 100, ndigits=3)
Correy_pct = round((Correy_total / total_votes) * 100, ndigits=3)
Li_pct = round((Li_total / total_votes) * 100, ndigits=3)
OTooley_pct = round((OTooley_total / total_votes) * 100, ndigits=3)

#   * The winner of the election based on popular vote.

tally = {'Khan': Khan_total, 'Correy': Correy_total, 'Li': Li_total, "O'Tooley": OTooley_total}
# print(tally)
winner = max(tally, key=tally.get)
# print(winner)

# * As an example, your analysis should look similar to the one below:

#   ```text
#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------
#   ```

analysis = f"Election Results\n\
-------------------------\n\
Total Votes: {total_votes}\n\
-------------------------\n\
Khan: {Khan_pct}% ({Khan_total})\n\
Correy: {Correy_pct}% ({Correy_total})\n\
Li: {Li_pct}% ({Li_total})\n\
O'Tooley: {OTooley_pct}% ({OTooley_total})\n\
-------------------------\n\
Winner: {winner}\n\
-------------------------"

print(analysis)

# * In addition, your final script should both print the analysis to the terminal and export a text file with the results.

results_file = os.path.join("PyPollResults.txt")
with open(results_file, "w", newline="") as datafile:
    datafile.write(analysis)
