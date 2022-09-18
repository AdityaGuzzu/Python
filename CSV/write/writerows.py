'''
Let's see the working of the writerows command
'''
import csv
with open('data.csv','r') as inp_file:
    inp_buf = csv.reader(inp_file)
    with open('output.csv','w') as out_file:
        out_buf = csv.writer(out_file)
        for line in inp_buf:
            out_buf.writerows(line)