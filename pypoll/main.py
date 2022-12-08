import os
import csv

os.chdir(os.path.dirname(__file__))
resource = os.path.join('Resources', 'election_data.csv')

# use set to create a list of unique candidates    
candidate_list = []
candidate_set = set(candidate_list)

with open(resource) as poll_data:
    poll_reader = csv.reader(poll_data, delimiter=',')    
    header = next(poll_data)
    for row in poll_reader:
        candidate = str(row[2])
        candidate_list.append(candidate)


# the len (count) of the candidate_list is the total number of votes cast
total_votes = (len(candidate_list))

# count the votes per candidate as per candidate_set
raymon_count = 0
diana_count = 0
charles_count = 0
for x in candidate_list:
    if x == "Raymon Anthony Doane":
        raymon_count = raymon_count+1
    elif x == "Diana DeGette":
        diana_count = diana_count+1
    elif x == "Charles Casper Stockham":
        charles_count = charles_count+1

# calculate the percentages of votes per candidate
raymon_perc = "{0:.3f}%".format(((raymon_count/total_votes)*100))
diana_perc = "{0:.3f}%".format(((diana_count/total_votes)*100))
charles_perc = "{0:.3f}%".format(((charles_count/total_votes)*100))

# determine the winner
first =  ""
if (raymon_count > diana_count) and (raymon_count > charles_count):
    print = "Raymon Anthony Doane: + rfaymon_perc + "
elif (diana_count > raymon_count) and (diana_count > charles_count):
    first = "Diana DeGette"
else: first = "Charles Casper Stockham"


#  print to screen
print ("Election Results")
print("")
print ("------------------------------------------")
print (f"Total votes: {total_votes}")
print("")
print (f"Charles Casper Stockham  {charles_perc} ({charles_count})")
print("")
print (f"Diana DeGette   {diana_perc} ({diana_count})")
print("")
print (f"Raymon Anthony Doane {raymon_perc} ({raymon_count}) ")
print("")
print(f"Winner: {first}")

# create an utput text file in the analysis folder
answers_output = os.path.join('..','pypoll', 'Analysis', 'outputfile.txt')
with open (answers_output, "w") as output:
    output.write ("Election Results\n")
    output.write("\n")
    output.write ("------------------------------------------\n")
    output.write("\n")
    output.write (f"Total votes: {total_votes}\n")
    output.write("\n")
    output.write ("------------------------------------------\n")
    output.write("\n")
    output.write (f"Charles Casper Stockham  {charles_perc} ({charles_count})\n")
    output.write("\n")
    output.write (f"Diana DeGette   {diana_perc} ({diana_count})\n")
    output.write("\n")
    output.write (f"Raymon Anthony Doane {raymon_perc} ({raymon_count})\n ")
    output.write("\n")
    output.write ("------------------------------------------\n")
    output.write("\n")
    output.write(f"Winner: {first}\n")


