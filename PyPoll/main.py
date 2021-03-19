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
vote_per_candidate = election_df["Candidate"].value_counts(normalize = True)

print("Total Votes: " + str(total_count))
print(vote_per_candidate)