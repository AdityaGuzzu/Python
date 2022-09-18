'''
At times, we forget the delimiter value. Sometimes it might have been moved from a comma to a '/t'
as in this case. So lets see how to change it
'''

import csv

#uncomment the following code to see what happens when we dont parse such data
'''
with open('input.csv','r') as inp_file:
    input_buf = csv.reader(inp_file)
    with open('output.csv','w') as out_file:
        output_buf = csv.writer(out_file)

        for line in input_buf:
            output_buf.writerow(line)
'''
with open('input.csv','r',newline='\n') as inp_file:
    input_buf = csv.reader(inp_file,delimiter = '\t')
    with open('output.csv','w') as out_file:
        output_buf = csv.writer(out_file)

        for line in input_buf:
            output_buf.writerow(line)


