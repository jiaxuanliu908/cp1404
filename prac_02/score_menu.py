
def main():
    global score
    choice = input("Choice : ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_number("Score: ",0,100)
            print(f"OK! your score is {score}")
        elif choice == "P":
            grade = get_grade(score)
            print(f"your score is {score},and your grade is {grade}")
        elif choice =="S":
            star = get_the_stars(score)
            print(f"As many points as there are, there are just as many stars!!!\nyou have {score} stars\n{star}")
        else:
            print("Invalid choice !")
        choice = input("Choice : ").upper()
    print("OK SEE U !!!")

def get_valid_number(prompt,low,high):
    number = int(input(prompt))
    while number > high or number < low:
        print("Invalid number !")
        number = int(input(prompt))
    return (number)


def get_grade(score):
    if score >= 90:
        return("Excellent")
    elif score >= 50:
        return("Passable")
    else:
        return("bad")


def get_the_stars(score):
    i = score * "*"
    return(i)


main()