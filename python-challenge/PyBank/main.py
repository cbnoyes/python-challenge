import os
import csv

BUDGET_CSV = os.path.join("resources", "budget_data.csv")
#print("we start here:", os.getcwd())
os.chdir(os.path.dirname(os.path.realpath(__file__)))
#print("now we're here:", os.getcwd())

#Variables
last_month_profit = 0
profit_change_list = []
profit_change = 0

most_profit = [" ", 0]
least_profit = [" ", 0]

#open csv and convert to dictionary
with open(BUDGET_CSV) as input:
    csv_reader = csv.DictReader(input)

    first_row = next(csv_reader)
    last_month = first_row["Date"]
    last_month_profit = int(first_row["Profit/Losses"])
    total_months = 1
    net_profit = last_month_profit
    
    for row in csv_reader:
        total_months = total_months + 1
        current_profit = int(row["Profit/Losses"])
        net_profit = net_profit + current_profit

        #Average Change
        profit_change = current_profit - last_month_profit
        last_month_profit = current_profit
        profit_change_list.append(profit_change)
       

        #Greatest Increase in Profits
        if (profit_change > most_profit[1]):
            most_profit[0] = row["Date"]
            most_profit[1] = profit_change



        #Greatest Decrease in Profits
        if (profit_change < least_profit[1]):
            least_profit[0] = row["Date"]
            least_profit[1] = profit_change
        
average_profit_change = sum(profit_change_list) / len(profit_change_list)
average_profit_rounded = round(average_profit_change, 2)


#analysis

analysis = (
    f'\nFinancial Analysis\n'
    f'-------------------------\n'
    f'Total Months: {total_months}\n'
    f'Total: $ {net_profit}\n'
    f'Average Change: $ {average_profit_rounded}\n'
    f'Greatest Increase in Profits: {most_profit[0]} $({most_profit[1]})\n'
    f'Greatest Decrease in Profits: {least_profit[0]} $({least_profit[1]})\n'
)


with open("analysis/bank_analysis.txt", "w") as txt_file:
    txt_file.write(analysis)
