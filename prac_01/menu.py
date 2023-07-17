get_the_name = input("Enter name: ")
menu = ("(H)ello\n(G)oodbye\n(Q)uit")
print(menu)
choice = input(">>>").upper()
while choice != "Q":
    if choice == "H":
        print(f"hello {get_the_name}")
    elif choice == "G":
        print(f"goodbye {get_the_name}")
    else:
        print("invalid message")
    print(menu)
    choice = input(">>>").upper()
    print("finished message")