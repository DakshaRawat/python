import csv 
filename = 'data.csv' 
with open(filename, mode='r') as file: 

    csv_reader = csv.reader(file) 