from silver_service_taxi import SilverServiceTaxi

def test_silver_service_taxi():
    taxi = SilverServiceTaxi("Hummer", 200, 2)  # fanciness 2倍

    print(taxi)

    taxi.drive(18)
    fare = taxi.get_fare()
    print(f"Fare for 18 km: ${fare:.2f}")

    expected_fare = taxi.price_per_km * 18 + taxi.flagfall
    assert abs(fare - expected_fare) < 0.01, f"Fare should be {expected_fare}, but got {fare}"

    assert round(fare, 2) == 48.78, f"Expected fare 48.78 but got {fare:.2f}"

test_silver_service_taxi()