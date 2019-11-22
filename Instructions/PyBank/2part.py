import csv

with open ("budget_data.csv", "r") as file:
    budget_reader = csv.reader(file) # class = csv.reader
    header = next(budget_reader)
    profit_loss = []        #list(budget_reader)       # class = list
    value = 0 # must be defined out of loop

    for row in budget_reader:
        profit_loss.append(row[1])
        value += int(row[1]) # [1] means second column += means value +
    average = value/len(profit_loss)

    
    print(f"Total Profit/Losses: ${value}")
    print(f"Average change: {average}")

