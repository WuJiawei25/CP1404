import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBER_PRE_PICK = 6

def gennerate_quick_pick():
    numbers = []
    while len(numbers) < NUMBER_PRE_PICK:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in numbers:
            numbers.append(number)
    numbers.sort()
    return numbers

def main():
    try:
        number_of_picks = int(input("How many quick picks? "))
    except ValueError:
        print("Invalid input. Please enter an integer. ")
        return

    for i in range(number_of_picks):
        quick_pick = gennerate_quick_pick()
        print(" ".join(f"{number:2}" for number in quick_pick))

main()