import csv
import os
import pandas as pd

#Path to collect data
election_df = pd.read_csv("Resources/election_data1.csv")
election_df = pd.DataFrame(election_df)

file = os.path.join("Analysis", "poll_analysis.txt")

print("Election Results")
print("------------------------")

#Find total number of votes
total_count = len(election_df)

#Percent per Candidate
percent_per_candidate = election_df["Candidate"].value_counts(normalize = True)
votes_per_candidate = election_df["Candidate"].value_counts()
percent_per_candidate = [i*100 for i in percent_per_candidate]
khan_per = round(percent_per_candidate[0], 2)
correy_per = round(percent_per_candidate[1], 2)
li_per = round(percent_per_candidate[2], 2)
otooley_per = round(percent_per_candidate[3], 2)

#Votes per Candidate
khan_vote = (khan_per/100) * total_count
correy_vote = (correy_per/100) * total_count
li_vote = (li_per/100) * total_count
otooley_vote = (otooley_per/100) * total_count

print("Total Votes: " + str(total_count))
print("Khan: " + str(khan_per) + "%" + " (" + str(khan_vote) + ")")
print("Correy: " + str(correy_per) + "%" + " (" + str(correy_vote) + ")")
print("Li: " + str(li_per) + "%" + " (" + str(li_vote) + ")")
print("O'Tooley: " + str(otooley_per) + "%" + " (" + str(otooley_vote) + ")")

#Winner
votes = [khan_per, correy_per, li_per, otooley_per] #votes = [int(khan_vote), ....]  #winner = max(votes)
max_vote = votes[0]
for item in votes:
    if item > max_vote:
        max_vote = item
winners = votes_per_candidate.keys()
winner = winners[0]
print("Winner: " + str(winner))

output = (
    f"Election Results\n"
    f"---------------------\n"
    f"Total Votes: {total_count}\n"
    f"Khan: {khan_per}% ({khan_vote})\n"
    f"Correy: {correy_per}% ({correy_vote})\n"
    f"Li: {li_per}% ({li_vote})\n"
    f"O'Tooley: {otooley_per}% ({otooley_vote})\n"
    f"Winner: {winner}\n"
)

#Create txt file


os.chdir('../PyPoll/Analysis')

#Print in Terminal
with open('poll_analysis.txt', 'w') as f:
    f.write(output)