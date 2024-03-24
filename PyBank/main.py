# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 17:15:48 2024

@author: Rom4i
"""

import os 
import csv


sum_of_months = 0
total = 0
change = []
profit_loss=[]
months= []


csvpath = os.path.join ('C:/Users/Rom4i/OneDrive/Desktop/Boot camp/Homework 3 Python/PyBank/resources/budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    for csvrow in csvreader:
        sum_of_months+=1
      

  
        total+=int(csvrow[1])
      


        months.append(csvrow[0])

 
        profit_loss.append(int(csvrow[1])) 


        change.append(profit_loss[sum_of_months-1]-profit_loss[sum_of_months-2])

      
      
 
        
    totalchange = sum(change)
    averagechange = round(totalchange/(len(change)-1), 2)
    inc_profit = max(change)
    dec_profit = min(change)
    grt_decrease = change.index(dec_profit)
    grt_increase = change.index(inc_profit)
    
output_path = "budget_analysis.txt"
file =  open(output_path, 'w') 
file.write("Financial Analysis\n")
file.write("----------------------------\n")
file.write(f"Total Months: {sum_of_months}\n")
file.write(f"Total: ${total} \n")
file.write(f"Average Change: ${averagechange}\n")
file.write(f"Greatest Increase in Profits: {months[grt_increase]} (${inc_profit}) \n")
file.write(f"Dreatest Decrease in Profits: {months[grt_decrease]} (${ dec_profit})\n")

file.close()


    
   