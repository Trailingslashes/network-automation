import csv

with open('airtravel.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # escape first line
    year_1958 = dict()
    for row in reader:
        year_1958[row[0]] = row[1]

        max_1958 = max(year_1958.values())

        # print(max_1958)

    for k, v in year_1958.items():
        if max_1958 == v:
            print(f'Businest month in 1958:{k} | Flights:{v.strip()}')
