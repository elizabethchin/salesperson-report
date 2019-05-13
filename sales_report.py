"""Generate sales report showing total melons each salesperson sold."""


salespeople = []
melons_sold = []

f = open('sales-report.txt')
#opens text file
#can improve code by making this into a function and refactor code
for line in f:
    #iterates the file line by line
    line = line.rstrip()
    #removes whitespaces to the right of the ine
    entries = line.split('|')
    #splits the line at | and makes it a string
    salesperson = entries[0]
    #sales person is index 0
    melons = int(entries[2])
    #number of melons sold is at index 2

    if salesperson in salespeople:
        #loop through salespeople list for sales person
        position = salespeople.index(salesperson)
        #get the index of the sales person in the list
        melons_sold[position] += melons
        #get the amount of melons sold and add to list

    else:
        salespeople.append(salesperson)
        #add salesperson
        melons_sold.append(melons)
        #add melons sold

for i in range(len(salespeople)):
    #prints all the sales person and number of melons sold
    print(f'{salespeople[i]} sold {melons_sold} melons')
