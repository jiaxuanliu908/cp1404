"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""
numbers_input = True
while numbers_input:
   try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        fraction = numerator / denominator
        print(fraction)
   except ValueError:
        print("Numerator and denominator must be valid numbers!")
   except ZeroDivisionError:
        print("Cannot divide by zero!")
        numbers_input = False
print("Finished.")
# 1 It appears when you type symbols and letters
# 2 When the denominator is zero
