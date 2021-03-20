import csv
import pandas as pd
import sys

#Path to collect data
election_df = pd.read_csv("Resources/election_data1.csv")
election_df = pd.DataFrame(election_df)

print("Election Results")
print("------------------------")

#Find total number of votes
total_count = len(election_df)

#Percent per Candidate
percent_per_candidate = election_df["Candidate"].value_counts(normalize = True)
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
max_vote = max(percent_per_candidate)

print(max_vote)
#print("Winner: " + str(max_vote))
