import csv

with open ("budget_data.csv", "r") as file:
    budget_reader = csv.reader(file) # class = csv.reader
    header = next(budget_reader)
    #data = list(budget_reader)       # class = list
    value = 0 # must be defined out of loop
    change = []
    for row in budget_reader:
        change = row.append (row[0])

        average = change/len(change)