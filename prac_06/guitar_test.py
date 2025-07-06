from guitar import Guitar

def main():
    """Test get_age() and is_vintage() methods."""
    test_guitar_1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    test_guitar_2 = Guitar("Another Guitar", 2013, 500)

    print(f"{test_guitar_1.name} get_age() - Expected 102. Got {test_guitar_1.get_age()}")
    print(f"{test_guitar_2.name} get_age() - Expected 11. Got {test_guitar_2.get_age()}")
    print(f"{test_guitar_1.name} is_vintage() - Expected True. Got {test_guitar_1.is_vintage()}")
    print(f"{test_guitar_2.name} is_vintage() - Expected False. Got {test_guitar_2.is_vintage()}")


main()