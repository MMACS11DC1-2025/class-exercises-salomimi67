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
        #turns their intests line into a list
        person_intrests = line.strip().split(",")

most_common = ""
most_point = 0
other_intrests = ""

for line in file:
    point = 0
    other_fav = line.strip().split(",")
    other_person = other_intrests[1]

    for intrest in person_intrests:
        if intrest in person_intrests:
            point += 0
   # if person_intrests[2] == other_intrests[2]
      #  point +=1
   # if person_intrests[3] == other_intrests[3]
       # point +=1
   # if person_intrests[4] == other_intrests[4]
        #point +=1
   # if person_intrests[5] == other_intrests[5]
        #point +=1
   # if person_intrests[6] == other_intrests[6]
        #point +=1
    #if person_intrests[7] == other_intrests[7]
        #point +=1
   #if person_intrests[8] == other_intrests[8]
        #point +=1
    #if person_intrests[9] == other_intrests[9]
        #point +=1
   # other_person = other_intrests[1]

    if point > most_point:
        most_common = other_person
        most_point = point
print(most common " is the person with the most common similarities to you accordign to my data")
if most_point == 8:
    print("You guys have 8 similar intrests.")
elif most_point <= 7 or most_point >= 6:
    print("You guys have about 6-7 similar intrests.")
elif most_point == 5:
    print("You guys have 5 similar intrests.")
elif most_point == 4:
    print("You guys have 4 similar intrests.")
elif most_point == 3:
    print("You guys have 3 similar intrests.")
elif most_point == 2:
    print("You guys have 2 similar intrests.")
elif most_point == 1:
    print("You guys have 1 similar intrests.")   

#if person_intrests[2] == other_intrests[2]
    #print("You guys have the same favoutrite number!")
    #if
        #print("")
#if person_intrests[3] == other_intrests[3]
    #print("You guys have the same favoutrite pet!") 
    #if
        #print("")
#if person_intrests[4] == other_intrests[4]
    #print("You guys have the same favoutrite subject!") 
    #if
        #print("")
#if person_intrests[5] == other_intrests[5]
    #print("You guys have the same favoutrite sport (to play)!") 
    #if
        #print("")
#if person_intrests[6] == other_intrests[6]
    #print("You guys have the same favoutrite sport (to watch)!")
    #if
        #print("")
#if person_intrests[7] == other_intrests[7]
    #print("You guys have the same favoutrite genre of music!") 
    #if
        #print("")
#if person_intrests[8] == other_intrests[8]
    #print("You guys have the same favoutrite movie genre!") 
    #if
        #print("")
#if person_intrests[9] == other_intrests[9]
    #print("You guys have the same favoutrite fast food near by!") 
    #if
        #print("")
        