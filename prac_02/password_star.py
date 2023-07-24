
def main():
    password = get_the_password("password:",0 )
    lenth = get_the_lenth(password)
    print(lenth * "*")


def get_the_password(prompt,low):
    number = input(prompt)
    while len(number) <= low:
        print("invalid password")
        number = input(prompt)
    return number


def get_the_lenth(password):
    return len(password)

main()