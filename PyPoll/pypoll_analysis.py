import os
import csv

# Files to load & output
file_to_load = os.path.join("..", "Resources", "election_data.csv")
file_to_output = os.path.join("analysis", "election_analysis.txt")

# Parameters for election data
votes_total = 0
candidates_list = []
candidate_choice = []
candidates_votes = {}
candidates_winner = ""
count_winner = 0

# Open and read csv
with open(file_to_load) as election_data:
    reader = csv.DictReader(election_data)

    for row in reader:

        # Total number of votes cast
        votes_total = votes_total + 1

        # Names of candidates
        candidates_list = row["Candidate"]

        # Candidate not an option
        if candidates_list not in candidate_choice:

            # Name added to those in running
            candidate_choice.append(candidates_list)

            # Number of votes for candidates
            candidates_votes[candidates_list] = 0

        # Calculation  of votes for candidates
        candidates_votes[candidates_list] = candidates_votes[candidates_list] + 1

# Print results
output = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total votes: {votes_total}\n"
    f"-------------------------\n"
)
print(output)

# Winning candidate
for candidate in candidates_votes:

        # Total number of votes
        votes = candidates_votes.get(candidate)
        vote_perc = float(votes) / float(votes_total) * 100

        # Winning candidate and number of votes
        if (votes > count_winner):
            count_winner = votes
            candidates_winner = candidate

# Print results
vote_output = (f"{candidate}: {vote_perc:.3f}% ({votes})\n")
print(vote_output)

winner_output = (
    f"-------------------------\n",
    f"Winner: {candidates_winner}\n",
    f"-------------------------\n"
)
print(winner_output)




