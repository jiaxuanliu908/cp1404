
for i in range(0, 101, 10):
    print(i, end=' ')
print()

for y in reversed(range(0, 21, 1)):
    print(y, end=' ')
print()

number = int(input("number: "))
for i in range(number):
    print("*",end='')

number = int(input("number:"))
for i in range(1,number+1):
    print(i * '*', sep=' ')
