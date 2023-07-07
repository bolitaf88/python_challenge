# Dependencies 
import csv

# Files to load and output
file_to_load = "C:/Users/bolit/OneDrive/Desktop/python_challenge/PyPoll/resources/election_data.csv"
file_to_output = "C:/Users/bolit/OneDrive/Desktop/python_challenge/PyPoll/analysis/election_analysis_1.txt"

# Total Vote Counter
total_votes = 0

# Candidate options and vote counters
candidate_options = []
candidate_votes = {}

# Winning candidate and winning count Tracker
winning_candidate = ""
winning_count = 0

# Read in the csv and convert it into a list of dictionaries 
with open(file_to_load) as election_data:
    reader = csv.DictReader(election_data)

    # for each row ...
    for row in reader:

        # Add to the total vote count 
        total_votes = total_votes + 1

        # Extract the candidate name from each row 
        candidate_name = row["Candidate"]

        # If the candidate does not match any existing candidate ...
        if candidate_name not in candidate_options:

            # add it to the list of candidates in the running 
            candidate_options.append(candidate_name)

            #And begin tracking the candidate's voter count
            candidate_votes[candidate_name] = 0

        # Then add a vote to that candidate's count 
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

# Print the Results and export
with open(file_to_output, "w") as txt_file:

    #Print the final vote count 
    election_results = (
        f"\n\nElection Results\n"
        f"----------------------------\n"
        f"Total votes: {total_votes}\n"
        f"----------------------------\n"
    )
#
    print(election_results)


    # save the final vote count to the text file
    txt_file.write(election_results)

    # Determine the winner by looping ...
    for candidate in candidate_votes:

        # Retrieve the vote count and percentage
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        #determine winning vote
        if (votes > winning_count):
            winning_count = votes 
            winning_candidate = candidate 
        # print each candidate's voter count and percentage 
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output)
        txt_file.write(voter_output)
  # save each candidates voter count 
    winninng_candidate_summary = (
    f"---------------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"--------------------------------\n"
     )
    print(winninng_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winninng_candidate_summary)

       
            
