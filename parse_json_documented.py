# Python program
# to parse 'certain' json files
# from a folder

import json
import csv
import re
from collections import Iterable
from glob import glob
import os
             
# Function to deconstructed nested list into a 1 dimension list
def flatten_list(_2d_list):
    flat_list = []
    # Iterate through the outer list
    for element in _2d_list:
        if type(element) is list:
            # If the element is of type list, iterate through the sublist
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)
    return flat_list

# Grab the list of companies we are trying to look information for
sec_data = []
with open('comp_sec_id.csv', newline='') as f:
    for row in csv.reader(f):
    	sec_data.append(row[0])

# Get all files in the directory
# Base directory folder for search
base_dir = '/mnt/d/Documents/CIK/submissions'

# Declare empty string to temporary store path of the specific json files we want
check_sec = ""
# Declare empty list to store path of specific json files we want
data_list = []
# Declare variable of append function to make program faster
append = data_list.append


# Search through the list of conditions we want
for sec in sec_data:
    # Grab path for the files that match our conditions
	check_sec = glob(os.path.join(base_dir, f'*{sec}.json'))
	# Append the path into a list
	append(check_sec)

       
# Declare an empty list for loading each json files
data = []

# Convert data_list into 1 dimension list
data_list = flatten_list(data_list)


# Through the list of paths that we want to parse
for i in data_list:
	f = open(i)
    
    # Load the json file into empty list
	data = json.load(f)
    
    # Print key info that we want
    # Output to type of files you want
    # Example: python3 parse_json.py >parsed_sic.txt
	print(data["cik"], '\t', data["sic"], '\t', data["sicDescription"], '\t', data["name"])
	# Close the json file
	f.close()