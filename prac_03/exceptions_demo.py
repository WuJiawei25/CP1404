"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be zero.")
        denominator = int(input("Enter the denominator(no_zero): "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")

#Questions
#1.It will be triggered when a letter or decimal is entered.
#2.User enters 0 as the denominator
#3.Loop until the user enters a non-zero denominator