"""
Write an Olympic Judging program that outputs the average scores from 5 different judges. 

Each score is out of 10 points maximum. Half points are allowed (e.g. 7.5)

The program should take 5 inputs and output the final average score.

Example:

Judge 1: 5.5
Judge 2: 10
Judge 3: 7
Judge 4: 8.5
Judge 5: 9
Your Olympic score is 8.0
"""
print("What does judge 1 give out of 10?")
judge_1 = float(input())

print("What does judge 2 give out of 10?")
judge_2 = float(input())

print("What does judge 3 give out of 10?")
judge_3 = float(input())

print("What does judge 4 give out of 10?")
judge_4 = float(input())
      
print("What does judge 5 give out of 10?")
judge_5 = float(input())

average = 0
average = average + str(judge_1) + str(judge_2) + str(judge_3) + str(judge_4) + str(judge_5)
final = 0
final = final + average/5
print("Your olympic score is " + str(final))