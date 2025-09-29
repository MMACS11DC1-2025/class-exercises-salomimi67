file = open("2.4/responses.csv")
myline = ""
for line in file:
    if "" in line.lower():
        myline = line