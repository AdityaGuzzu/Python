import csv
with open('read/data.csv', 'r') as read_data:
    csv_reader = csv.reader(read_data)

    with open('data.csv', 'w') as write_data:
        csv_writer = csv.writer(write_data)

        for line in csv_reader:
            csv_writer.writerow(line)
