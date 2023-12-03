import os
import csv
# import numpy to help get unique names for candidates
import numpy as np

election_csv = os.path.join('Resources','election_data.csv')

# lists to store data
ballot_id = []
county = []
candidate = []

print("Election Results")
print()
print("-----------------------")
print()

with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

    for row in csvreader:
        # Add ballot_id
        ballot_id.append(row[0])

        # Add county
        county.append(row[1])

        # Add candidate
        candidate.append(row[2])

    print(f"Total Votes: ", len(ballot_id))
    print()
    print("-----------------------")
    print()

    # find unique values to see all candidates
    cand_unq = list(np.unique([candidate]))

    # filter candidate list by name to get totals for all candidates
    charles = list(filter(lambda x: x == cand_unq[0], candidate))
    diana = list(filter(lambda x: x == cand_unq[1], candidate))
    raymon = list(filter(lambda x: x == cand_unq[2], candidate))

    # find percent vote for charles
    vote_count = (len(candidate))
    vote_count_ccs = (len(charles))
    ccs_percentage = (round((vote_count_ccs/vote_count*100),3))

    # find percent vote for diana
    vote_count_dd = (len(diana))
    dd_percentage = (round((vote_count_dd/vote_count*100),3))

    #find percent vote for raymon
    vote_count_rad = (len(raymon))
    rad_percentage = (round((vote_count_rad/vote_count*100),3))

    #print results
    print(cand_unq[0], f": ", ccs_percentage, "% ", "(", vote_count_ccs, ")", sep= "")
    print()
    print(cand_unq[1], f": ", dd_percentage, "% ", "(", vote_count_dd, ")", sep= "")
    print()
    print(cand_unq[2], f": ", rad_percentage, "% ", "(", vote_count_rad, ")", sep= "")
    print()
    print("-----------------------")
    print()

    #find candidate with most votes
    num_votes_per_cand = [vote_count_ccs, vote_count_dd, vote_count_rad]
                   
    #zip candidate with votes
    total_votes = list(zip(cand_unq, num_votes_per_cand))
  
    print(f"Winner: ", cand_unq[num_votes_per_cand.index(max(num_votes_per_cand))])
    
   