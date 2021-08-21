import os
import csv
import operator


csvpath = r"C:\Users\stagecustomnc\OneDrive\MU_DataAnalyticsBC\MonashUniversityBootcamp\python-challenge\PyPoll\Resources\election_data.csv"

with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile)
    csvheader = next(csvreader)
    
    
    counter = 0

    #A complete list of candidates who received votes
    candidate_list = []
    candidate_set = set()
    
    for row in csvreader:
        counter += 1
        candidate_list.append(row[2])
      
    #to get a set of unique Candidates (i.e. no duplicates)
    for candidates in candidate_list:
        candidate_set.add(candidates)
    formattedCounter = "{:,.0f}".format(counter)
    
    #The total number of votes cast
    print(counter)
    
    #convert the set to a list
    uniqueCandidate_List = list(candidate_set)
        
    #The total number of votes each candidate won
    vote_count = {}.fromkeys(candidate_set,0)
    for i in candidate_list:
        for j in uniqueCandidate_List:
            if str(i) == j:
                vote_count[j] += 1 
    print(vote_count)
    
    #The percentage of votes each candidate won
    vote_count2 = {}
    for j in uniqueCandidate_List:
        vote_count2[j] = "{:.3%}".format((float(vote_count[j])/float(counter)))
    print(vote_count2)
    
    #sort Candidate List according to value of vote_count dictionary
    sortedCandidateList = sorted(uniqueCandidate_List, key=vote_count.get, reverse =True)
    
    #list comprehension of the required output by the homework
    vote_summary = [f"{j}: {vote_count2[j]} ({vote_count[j]:,d})" for j in sortedCandidateList]
    
    #The winner of the election based on popular vote.
    max_key = max(vote_count,key=vote_count.get)
    print(max_key)

#print the analysis to the terminal and export a text file with the results.
textpath2 = os.path.join("analysis","election_results.txt")

with open(textpath2, 'a') as summarisedtext:
    summarisedtext.truncate(0)
    summarisedtext.writelines("Election Results\n")
    summarisedtext.writelines("-"*30+"\n")
    summarisedtext.writelines(f"Total Votes: {formattedCounter}\n")
    summarisedtext.writelines("-"*30+"\n")
    for vote in vote_summary:
        summarisedtext.writelines(vote+"\n")
    summarisedtext.writelines("-"*30+"\n")
    summarisedtext.writelines(f"Winner: {max_key}\n")
    summarisedtext.writelines("-"*30+"\n")
    
                                
  


    


    