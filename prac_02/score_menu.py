import random
def main():

    menu = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"

    print(menu)

    choice = input(">>>").upper()

    while choice != "Q":
        if choice == "G":
            score = random_score()
            print(score)
        elif choice == "P":
            print(determine_score(score))
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid choice")

        print(menu)
        choice = input(">>>").upper()

print("farewell")



def random_score():
    """Generate random scores"""
    score = random.randint(0, 100)
    return score

def determine_score(score):
    """Determine the score result"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def show_stars(score):
    """Print as many stars as the score"""
    print("*" * score)

main()