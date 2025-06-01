import random


def main():

    score = float(input("Enter score: "))
    print(determine_score(score))

    score = random_score()
    print(determine_score(score))


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


main()


