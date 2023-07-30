
name = input("Enter name: ")
out_file = open("name.txt","a")
out_file.writelines(name)
out_file.close()

FILENAME = "name.txt"
in_file = open(FILENAME)
text = in_file.read()
in_file.close()
print(f"Your name is {text}")

with open("numbers.txt","r") as in_file:
   number1 = int(in_file.readline())
   number2 = int(in_file.readline())
   result = number1 + number2
   in_file.close()
print(result)


with open("numbers.txt","r") as in_file:
    for i in in_file:
        print(i)
in_file.close()

