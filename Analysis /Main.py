#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 15:12:28 2020

@author: fraolabebe
"""

# %%
import os
import csv 




Data_csv = os.path.join("/Users/fraolabebe/Python_Challenge/Resources", "budget_data.csv")




# Variables 

total_months = 0
total_revenue = 1
months_of_change = []
net_change_list = []
greates_increase = ["", 0]
greatest_decrease = ["", 9999999999999999]
total_net = 0


# %% Open and Read csv

with open(Data_csv) as csv_file:
    csv.reader(csv_file, delimiter=",")
    
    #Read the header row first 
    
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")
    
    for csv_file in csv_file:
        print(csv_file)
        


        
# %% The total number of months included in the dataset
total_months = len(row(0))





# %% The total Amount of "profit/Losses" over the entire Period



# %% The average of the changes in "Profit/losses"Over the entire period




# %% The greatest incease in profits (date and amount) over the entire period


# %% The greatest decrease in losses (date and amount) over the entire period

# %%