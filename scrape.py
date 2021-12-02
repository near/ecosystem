import os
import re
import json
import csv


location = os.path.dirname(__file__)
#folder of NEAR ecosystem entities
directory = os.path.join(location, 'entities/')
#output json file
output_append = os.path.join(location, 'entities.json')

#open file, get md table, convert, store to json
def near_entitity_md_to_json(directory, filename, path):
        with open (path, "r") as myfile:
                data=myfile.read()
                #extract md table from file and store to variable
                try:
                    found = re.search('(?<=---)(.*)(?=---)', data, re.DOTALL).group()
                except AttributeError:
                # MD did not contain expected table
                    found = 'No Table Extracted' 
                d = {}
                strip = '"'
                for n, line in enumerate(found[1:-1].split('\n')):
                    #Not ideal split, potential to break
                    line_text = line.split(': ')
                    attr_name = line_text[0].strip(strip)
                    attr_value = line_text[1].strip(strip)
                    d[attr_name] = attr_value
                    out = {}
                    out = d
                    
                filename = output_append 
                listData = {}
                with open(filename) as fp:
                    listData = json.load(fp)
                    
                listData.append(out)
                
                with open(filename, 'w') as json_file:
                    json.dump(listData, json_file,  
                                    separators=(',',': '))

#clean out existing json
with open(output_append, mode='w', encoding='utf-8') as f:
    json.dump([], f)
    
#iterate over directory - all files    
for filename in os.listdir(directory):
    try:
        path = os.path.join(directory, filename)
        near_entitity_md_to_json(directory, filename, path)
    except:
        pass