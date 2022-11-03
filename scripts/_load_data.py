import csv
periods = []
values  = []

with open('../data_samples/monthly_salary.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
        #print(row['period'], row['value'])
        if row['type'] == 'Neto':
            print(row)
            periods.append(row['period'])
            values.append(row['value'])