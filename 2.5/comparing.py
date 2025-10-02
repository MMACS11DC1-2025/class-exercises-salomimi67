"""
Create a program that uses comparison operators (< > <= >=).
You must use the class' datafile, 'responses.csv' and analyze it
    to make at least 2 interesting observations.
You may use user input to add interactivity to the program.
You must design your algorithm in English first, then translate it to Python code.
Test as you go! Describe in your comments what steps you took to test your code.
"""
# opens file
file = open("2.4/responses.csv")

# deltes first line
garbage = file.readline()

# asks user for input(name to find their favoutie stuff to find someonen who has similarities)
print("Please put in your name in to help find someone with the same similarities as you.")
person = input()

# finds the person and their intrests
for line in file:
    if person in line:
        person_intrests = line.strip().split(",")

most_common = ""
most_point = 0

for line in file:
    if person in line:
        person_intrests = line.strip().split(",")