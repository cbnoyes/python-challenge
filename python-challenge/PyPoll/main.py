import os
import csv

poll_csv = os.path.join("resources", "election_data.csv")
os.chdir(os.path.dirname(os.path.realpath(__file__)))

#The percentage of votes each candidate won
def dict_pct(original):
    total = sum(original.values())

    new = {}
    for key in original:
        value = original[key]
        pct = round(100 * (value/total), 3) 
        new[key] = pct
    return new

        
#Variables
total_votes = 0
candidates = []
candidate_votes = {}
winner = ""

with open(poll_csv) as input:
    csv_reader = csv.DictReader(input, delimiter=',')
    #first_row = next(csv_reader)
    
    for row in csv_reader:  

#The total number of votes cast
        total_votes = total_votes + 1

#A complete list of candidates who received votes
        name = row["Candidate"]
        if name not in candidates:
            candidates.append(name)
            candidate_votes[name] = 0

#The total number of votes each candidate won
        candidate_votes[name] = candidate_votes[name] + 1

#The winner of the election based on popular vote
winner = max(candidate_votes, key=candidate_votes.get)

results = (
    f'\nElection Results\n'
    f'-------------------------\n'
    f'Total Votes: {total_votes}\n'
    f'-------------------------\n'
    f'{candidate_votes}\n'
    f'{dict_pct(candidate_votes)}\n'
    f'-------------------------\n'
    f'Winner: {winner}\n'
    f'-------------------------\n'
)

with open("analysis/election_analysis.txt", "w") as txt_file:
    txt_file.write(results)
