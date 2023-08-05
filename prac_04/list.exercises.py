def main():
    number = get_number()
    if number is not None:
       print(f"The minimum number is {min(number)}")
       print(f"The maximum number is {max(number)}")
       print(f"The sum is {sum(number)}")
       print(f"The length of number is {len(number)}")


def get_number():
    numbers = []
    for i in range(5):
        try:
            num = float(input("Enter numbers : "))
            numbers.append(num)
        except ValueError:
            print("Value error")
    return numbers

main()
