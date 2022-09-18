'''
We will see how to use different delimitors instead of the default 'comma'
'''
import csv
with open('data.csv','r') as input_file:
    input_buf = csv.reader(input_file)
    with open('output.csv','w') as output_file:
        output_buf = csv.writer(output_file,delimiter='\t')

        for line in input_buf:
            output_buf.writerow(line)

