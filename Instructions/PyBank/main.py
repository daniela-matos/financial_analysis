def show_line():
    print(f"-"*30)

print("Financial Analysis")
show_line()

import csv

with open("budget_data.csv", "r") as file:
    budget_reader = csv.reader(file)    # class = csv.reader
    header = next(budget_reader)
    count_line = 0 
    for row in file:
        count_line += 1                 # = count_line = count_line + 1
    print(f"Total months: {count_line}")
    data = list(budget_reader)          # class = list
    value = 0                           # must be defined out of loop
    for row in data:
        value += int(row[1])     # [1] means second column += means value +
print(f"Total Profit/Losses: ${value}")