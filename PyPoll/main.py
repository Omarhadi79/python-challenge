import csv
# Create the path
file_path = "election_data.csv"

# Create variables to store data
total_votes = 0
candidates = []
votes_per_candidate = {}
winning_candidate = ""
winning_votes = 0

# Read csv file
with open(file_path, 'r') as csvfile:
 csvreader = csv.reader(csvfile, delimiter=",")
    
    # Skip header row
next(csvreader)

    # Loop through csv rows
for row in csvreader:
 # increase the total number of votes
 total_votes += 1
        
# Extract the candidate name
candidate = row[2]
             
# If the candidate is not already in the dictionary of votes per candidate, add them with 1 vote
if candidate not in votes_per_candidate:
 votes_per_candidate[candidate] = 1

# If the candidate is not in the list of candidates, add them
if candidate not in candidates:
 candidates.append(candidate)

else:
# Otherwise, increment the vote count for the candidate
 votes_per_candidate[candidate] += 1

# Calculate the percentage of votes and find the winning candidate
for candidate, votes in votes_per_candidate.items():
    percentage = (votes / total_votes) * 100
    if votes > winning_votes:
        winning_candidate = candidate
        winning_votes = votes
        
 # Print the candidate's name, percentage of votes, and total votes
print(f"{candidate}: {percentage:.2f}% ({votes})")

# Print the total number of votes
print(f"Total Votes: {total_votes}")

# Print the list of candidates who received votes
print("Candidates who received votes: " + ", ".join(candidates))

# Print the winner of the election based on popular vote
print(f"Winner: {winning_candidate}")
