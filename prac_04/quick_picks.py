import random
def get_random_numbers():
    random_numbers = set()
    while len(random_numbers) < 5:
        random_numbers.add(random.randint(1,45))
    random_numbers = sorted(random_numbers)
    return(random_numbers)
def main():
    picks = int(input("How many quick picks? "))
    for i in range(picks):
        random_number = get_random_numbers()
        print(" ".join(str(num) for num in random_number))
main()