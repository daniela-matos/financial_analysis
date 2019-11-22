def show_line():
    print(f"-"*30)

print("Financial Analysis")
show_line()

import csv

with open("budget_data.csv", "r") as file:
    budget_reader = csv.reader(file)
    header = next(budget_reader) 
    count_line = 0 
    profit_loss = []            
    value = 0 
    change = []
    #for row in file: 
    #show_line()
    for row in budget_reader:
        count_line += 1        # = count_line = count_line + 1
        profit_loss.append(row[1])
        value += int(row[1]) # [1] means second column += means value +
        average = value/len(profit_loss)/2
        change_ave = change/len(change)
    for i in range(len(profit_loss)-1):
        change.append(int(profit_loss[i+1]) - int(profit_loss[i]))   
    
    print(f"Total Months: {count_line}")
    print(f"Total Profit/Losses: $ {average}")
    print(f"Average Change: ${change_ave}")