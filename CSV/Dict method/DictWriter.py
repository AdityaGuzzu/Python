import csv
with open('data.csv','r') as inp_file:
    inp_buf = csv.DictReader(inp_file)
    # for line in inp_buf:
    #     print(line)
    with open('output.csv','w',newline='') as out_file:
        out_buf = csv.DictWriter(out_file,fieldnames =['Player Name',' Jersey Number'])
        out_buf.writeheader()
        for line in inp_buf:
            out_buf.writerow(line)

