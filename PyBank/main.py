import os
import csv

budget_csv = os.path.join('Resources','budget_data.csv')

#lists to store data
date = []
net_profit = []
avg_profit = []

print("Financial Analysis")
print()
print("-------------------------------")
print()

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader)

    for row in csvreader:
        # Add date
        date.append(row[0])

        # Add net_profit
        net_profit.append(row[1])
        
    
    print(f"Total Months: ", len(date))
    print()
    
    # make net_profit an integer
    net_profit_int = [eval(i) for i in net_profit]

    # sum net_profit_int
    profit_sum = sum(net_profit_int)
    print(f"Total: $", profit_sum)
    print()

    #solving for the average change in profit/losses
    # [(row2-row1)+(row3-row2)+...+(row87-row86)]/85
    for i in range(len(net_profit_int)-1):
        change_in_profit = (net_profit_int[i+1])-(net_profit_int[i])
        avg_profit.append(change_in_profit)
    
    change_in_profit_avg = sum(avg_profit)/len(avg_profit)
    print(f"Average Change: $", round(change_in_profit_avg,2))
    print()

    #find the greatest increase in profit
    max_profit = max(avg_profit)
    date_max_profit = date[(avg_profit.index(max_profit))+1]
    print(f"Greatest Increase in Profits:",date_max_profit,"($",max_profit,")")
    print()

    #find the greatest decrease in profit
    min_profit = min(avg_profit)
    date_min_profit = date[(avg_profit.index(min_profit))+1]
    print(f"Greatest Decrease in Profits: ", date_min_profit, "($",min_profit,")")


   



    
        

        





    




