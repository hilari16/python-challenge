import os
import csv

budget_csv = os.path.join('Resources','budget_data.csv')
output_file = os.path.join('analysis','budget_analysis.txt')

#lists to store data
date = []
net_profit = []
avg_profit = []

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader)

    for row in csvreader:
        # Add date
        date.append(row[0])

        # Add net_profit
        net_profit.append(row[1])
        
      
    # make net_profit an integer
    net_profit_int = [eval(i) for i in net_profit]

    # sum net_profit_int
    profit_sum = sum(net_profit_int)
   
    #solving for the average change in profit/losses
    # [(row2-row1)+(row3-row2)+...+(row87-row86)]/85
    for i in range(len(net_profit_int)-1):
        change_in_profit = (net_profit_int[i+1])-(net_profit_int[i])
        avg_profit.append(change_in_profit)
    
    change_in_profit_avg = sum(avg_profit)/len(avg_profit)
   
    #find the greatest increase in profit
    max_profit = max(avg_profit)
    date_max_profit = date[(avg_profit.index(max_profit))+1]
  
    #find the greatest decrease in profit
    min_profit = min(avg_profit)
    date_min_profit = date[(avg_profit.index(min_profit))+1]
    
output = (
    f"Financial Analysis\n"
    f"-------------------------------\n"
    f"Total Months: {len(date)}\n"
    f"-------------------------------\n"
    f"Total: ${profit_sum}\n"
    f"Average Change: ${round(change_in_profit_avg,2)}\n"
    f"Greatest Increase in Profits: {date_max_profit} (${max_profit})\n"
    f"Greatest Decrease in Profits: {date_min_profit} (${min_profit})\n"
)
   
with open(output_file,"w") as txtfile:
    txtfile.write(output)
    print(output)


    
        

        





    




