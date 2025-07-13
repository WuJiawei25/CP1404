from guitar import Guitar

FILENAME = "guitars.csv"

def load_guitars(filename):
    """Load guitars from a CSV file."""
    guitars = []
    with open(filename, "r") as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitars.append(Guitar(name, year, cost))
    return guitars

def save_guitars(filename, guitars):
    """Save the list of guitars to a CSV file."""
    with open(filename, "w") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)

def display_guitars(guitars):
    """Display a list of guitars."""
    if not guitars:
        print("No guitars to display.")
        return

    print("Guitars:")
    index = 1
    for guitar in guitars:
        print(f"{index}. {guitar}")
        index += 1

def add_new_guitars():
    """Prompt user to enter new guitars and return a list of them."""
    new_guitars = []
    print("Add new guitars (leave name blank to finish):")
    name = input("Name: ").strip()
    while name:
        try:
            year = int(input("Year: "))
            cost = float(input("Cost: $"))
            new_guitar = Guitar(name, year, cost)
            new_guitars.append(new_guitar)
            print(f"{new_guitar} added.")
        except ValueError:
            print("Invalid input. Please enter valid year and cost.")
        name = input("Name: ").strip()
    return new_guitars

def main():
    """Main function."""
    guitars = load_guitars(FILENAME)
    print("These are the guitars loaded:")
    display_guitars(guitars)

    guitars.sort()
    print("\nGuitars sorted by year:")
    display_guitars(guitars)

    new_guitars = add_new_guitars()
    guitars.extend(new_guitars)

    guitars.sort()
    save_guitars(FILENAME, guitars)
    print(f"\n{len(new_guitars)} new guitars added and saved to {FILENAME}.")

main()