import csv

def getCSV(file):
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter =',')
        for row in csv_reader:
            print(row)

getCSV('super.csv')
        