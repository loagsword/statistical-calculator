import csv


def csv_reader2(filepath):
    rows = []

    with open(filepath, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        for row in csv_reader:
            rows.append(row)
    return rows
