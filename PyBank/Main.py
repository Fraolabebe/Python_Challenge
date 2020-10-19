#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 11:28:46 2020

@author: fraolabebe
"""

data =open("/Users/fraolabebe/Python_Challenge/PyBank/Resources/budget_data.csv","r")
data = data.readlines()

#Variables
months = 0
total_revenue = 0
list1=[]
net_change_list = []
greatest_increase = 0
greatest_decrease = 0
total_net = 0
greatest_m=""
lowest_m=""



months=len(data)-1
  #Removed the header


for i in range(len(data)) :
        if i==0:
            continue
        x = data[i].split(",")
        total_revenue += int(x[1]) #total revenue 
        list1.append(int (x[1]))
        
avg_revenue = total_revenue//months

#Greatest Increase
greatest_increase = max(list1)

#Greatest Decrease
greatest_decrease = min(list1)


for j in range(len(data)):
    k = data[j].split(",")
    if j==0:
        continue
    if int(k[1])==greatest_increase:
        greatest_m=k[0]
    if int(k[1])==greatest_decrease:
        lowest_m=k[0]
        
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {months}\n"
    f"Total Revenue: ${total_revenue}\n"
    f"Average Revenue Chnage: ${avg_revenue}\n"
    f"Greatest Increase in Revenue: {greatest_m} (${greatest_increase})\n"
    f"Greatest Decrease in Revenue: {lowest_m} (${greatest_decrease})\n")


        
with open("file_to_output", "w") as txt_file:
    txt_file.write(output)        
        
        
        
        
        
        
        
        
        
        
        
        
        

