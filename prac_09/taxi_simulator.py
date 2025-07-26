from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

def show_taxis(taxis):
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

def choose_taxi(taxis):
    try:
        choice = int(input("Choose taxi: "))
        if 0 <= choice < len(taxis):
            return taxis[choice]
        else:
            print("Invalid taxi choice")
    except ValueError:
        print("Invalid input; enter a number")
    return None

def main():
    taxis = [
        Taxi("Prius", 100, 1.23),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    current_taxi = None
    total_bill = 0.0

    print("Let's drive!")
    print("q)uit, c)hoose taxi, d)rive")
    choice = input(">>> ").lower()

    while choice != 'q':
        if choice == 'c':
            show_taxis(taxis)
            selected_taxi = choose_taxi(taxis)
            if selected_taxi:
                current_taxi = selected_taxi
        elif choice == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                try:
                    distance = float(input("Drive how far? "))
                    if distance >= 0:
                        current_taxi.start_fare()
                        current_taxi.drive(distance)
                        trip_cost = current_taxi.get_fare()
                        print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                        total_bill += trip_cost
                    else:
                        print("Distance must be >= 0")
                except ValueError:
                    print("Invalid distance")
        else:
            print("Invalid option")

        print(f"Bill to date: ${total_bill:.2f}")
        print("q)uit, c)hoose taxi, d)rive")
        choice = input(">>> ").lower()

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    show_taxis(taxis)


main()