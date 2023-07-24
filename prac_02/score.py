"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

score = float(input("Enter score: "))
if score < 0:
    print("Invalid score")
elif score < 50:
    print("Bad")
else:
    if score > 100:
        print("Invalid score")
    elif score > 90:
        print("Excellent")
    elif score > 50:
        print("Passable")
        





def main():
    score = get_score("Score: " ,0,100)
    grade = get_grade(score)
    print(f"your score is {score},and your grade is {grade}")


def get_score(prompt,low,high):
    number = int(input(prompt))
    while number < low or number > high:
        print("invalid score")
        number = input(prompt)
    return (number)


def get_grade(score):
    if score >= 90:
        return("Excellent")
    elif score >= 50:
        return("Passable")
    else:
        return("bad")

main()






import random


def main():
    score = random.randint(0,101)
    grade = get_grade(score)
    print(f"your score is {score},and your grade is {grade}")


def get_grade(score):
    if score >= 90:
        return("Excellent")
    elif score >= 50:
        return("Passable")
    else:
        return("bad")

main()