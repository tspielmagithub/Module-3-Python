# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 17:40:22 2024

@author: Rom4i
"""

import os 


import csv

Candidates_count = {}


Ballot = []

Charles_Casper_Stockham = 0
Raymon_Anthony_Doane = 0
Diana_DeGette = 0


csvpath = os.path.join('C:/Users/Rom4i/OneDrive/Desktop/Boot camp/Homework 3 Python/PyPoll/resources/election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    

    for csvrow in csvreader:
            Ballot.append(csvrow[1])
            votes = len(Ballot)
   
            if csvrow[2] == "Charles Casper Stockham":
                Charles_Casper_Stockham += 1
  

            elif csvrow[2] == "Diana DeGette":
                Diana_DeGette +=1


            elif csvrow[2] == "Raymon Anthony Doane":
                Raymon_Anthony_Doane +=1
 

    Canidate1 = round((Charles_Casper_Stockham/votes)*100,3)
    Canidate2 = round((Diana_DeGette/votes)*100,3)
    Canidate3 = round((Raymon_Anthony_Doane/votes)*100,3)

  
    Candidates_count = {"Charles Casper Stockham": Charles_Casper_Stockham, "Diana DeGette": Diana_DeGette, "Raymon Anthony Doane": Raymon_Anthony_Doane }  

    Election_winner = max(Candidates_count, key=Candidates_count.get)



output_path = "election_result.txt"

file =  open(output_path, 'w') 


file.write("Election Results\n")
file.write("----------------------------\n")
file.write(f"Total votes: {votes}\n")
file.write("----------------------------\n")
file.write(f"Charles Casper Stockham: {Canidate1}% ({Charles_Casper_Stockham})\n")
file.write(f"Diana DeGette: {Canidate2}% ({Diana_DeGette})\n")
file.write(f"Raymon Anthony Doane: {Canidate3}% ({Raymon_Anthony_Doane}) \n")
file.write("----------------------------\n")
file.write(f"Winner: {Election_winner}\n")

file.close()


    
   



    
    