'''
INTRO:
In the DictReader, DictWriter methods, the data from the file will be extracted as a dict instead of a list
'''
import csv
with open('data.csv','r') as inp_file:
    inp_buf = csv.DictReader(inp_file)
    for line in inp_buf:
        print(line)