import os
import csv

resource = os.path.join('pybank','Resources', 'budget_data.csv')

months = 0
# create space to store profits and months
profits = []
month = []
changes = []


# need to exclude first month when calculating changes and averages
# and set variables to zero
lastmonthprofit = 1088983
totalprofits = 0
totalchanges = 0
change = 0
highest = 0

with open(resource) as budgetfile:
    budgetreader = csv.reader(budgetfile, delimiter=',')
    # skip header row
    # define header
    header = next(budgetfile)

# calculate changes
    for row in budgetreader:
        months += 1
        profit = int(row[1])
        profits.append(profit)
        month.append(row[0])
        totalprofits = sum(profits)
        if profit != lastmonthprofit:
            change = profit - lastmonthprofit
            changes.append(change)
            lastmonthprofit = profit
            totalchanges = sum(changes)    

# calculate the average     
average_change =totalchanges/(months-1)

# find the higest and lowest values in the change array
highest = 0
lowest = 0
for x in changes:
    if x > int(highest):
        highest = x
for y in changes:
    if y < int(lowest):
        lowest = y

# find positions in arrays for higesht and lowest changes
# find the month according to index for higest and lowest and add 1 month as the first month change was skipped

high_index = changes.index(highest)
low_index = changes.index(lowest)
high_month = month[high_index+1]
low_month = month[low_index+1]
low_index = changes.index(lowest)


print ("Financial Analysis")
print ("-------------------------------------")
print (f"Total months:  {len(month)} \n")
print (f"Total:  $ {round(totalprofits, 2)}\n")
print (f"Average change:  $ {round(average_change,2)}\n")
print (f"Greatest increase in profits:  {high_month} (${highest})\n")
print (f"Greatest decrease in profits:  {low_month} (${lowest})\n")

# create an utput text file in the analysis folder
answers_output = os.path.join("pybank", "Analysis", 'outputfile.txt')
with open (answers_output, "w") as output:
    output.write ("Financial Analysis\n")
    output.write ("\n")
    output.write ("--------------------------------------\n")
    output.write ("\n")
    output.write (f"Total months:  {len(month)} \n")
    output.write ("\n")
    output.write (f"Total:  $ {round(totalprofits, 2)}\n")
    output.write ("\n")
    output.write (f"Average change:  $ {round(average_change,2)}\n")
    output.write ("\n")
    output.write (f"Greatest increase in profits:  {high_month} (${highest})\n")
    output.write ("\n")
    output.write (f"Greatest decrease in profits:  {low_month} (${lowest})\n")