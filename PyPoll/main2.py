import os
import csv


csvpath = r"C:\Users\stagecustomnc\OneDrive\MU_DataAnalyticsBC\MonashUniversityBootcamp\python-challenge\PyPoll\Resources\election_data.csv"

with open(csvpath,'r') as csvfile:
    csvreader = csv.reader(csvfile)
    csvheader = next(csvreader)
    #The total number of votes cast
    counter = 0

    #A complete list of candidates who received votes
    candidate_list = []
    candidate_set = set()
    
    for row in csvreader:
        counter += 1
        candidate_list.append(row[2])
      

    for candidates in candidate_list:
        candidate_set.add(candidates)
    formattedCounter = "${:,.0f}".format(counter)
    print(counter)
    
    uniqueCandidate_List = list(candidate_set)
        
    #The total number of votes each candidate won
    vote_count = {}.fromkeys(candidate_set,0)
    for i in candidate_list:
        for j in uniqueCandidate_List:
            if str(i) == j:
                vote_count[j] += 1 
    print(vote_count)
    
    vote_count2 = {}
    
    #The percentage of votes each candidate won
    for j in uniqueCandidate_List:
        vote_count2[j] = "{:.3%}".format((float(vote_count[j])/float(counter)))
        #vote_count2 = sorted(vote_count2,key=vote_count2.get, reverse=True)
    print(vote_count2)
    
    #for j in uniqueCandidate_List:
    #    print(str(j))
    #    print(vote_count2[j])
     #   print(vote_count[j])

    vote_summary = [f"{j}: {vote_count2[j]} ({vote_count[j]})" for j in uniqueCandidate_List]
    #for vote in vote_summary:
     #   text = print(f"{vote}\n")
    
    #The winner of the election based on popular vote.
    max_key = max(vote_count,key=vote_count.get)
    print(max_key)

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
    
                                
    
    #for vote in vote_summary:
        #print(summarisedtext.writelines(vote))
   #vote_count2 = sorted(vote_count2,key=vote_count2.get, reverse=True)


    


    


    