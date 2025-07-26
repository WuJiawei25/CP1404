from unreliable_car import UnreliableCar

def test_unreliable_car():
    """Test driving behavior of UnreliableCar with different reliability levels."""
    low_reliability_car = UnreliableCar("LowReliability", 100, 10)
    high_reliability_car = UnreliableCar("HighReliability", 100, 90)

    low_drive_count = 0
    high_drive_count = 0
    test_attempts = 100

    for i in range(test_attempts):
        if low_reliability_car.drive(1) > 0:
            low_drive_count += 1
        if high_reliability_car.drive(1) > 0:
            high_drive_count += 1

    print(f"Low reliability car drove {low_drive_count} times out of {test_attempts}")
    print(f"High reliability car drove {high_drive_count} times out of {test_attempts}")

    if low_drive_count < high_drive_count:
        print("Test passed: Low reliability car drove less than high reliability car.")
    else:
        print("Test failed: Unexpected drive behavior. (Try increasing number of attempts or checking logic.)")

test_unreliable_car()