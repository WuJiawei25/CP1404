"""
Wimbledon
Estimate: 60 minutes
Actual:   60 minutes
"""
import csv

FILENAME = "wimbledon.csv"

def read_data(filename):
    """Read and return Wimbledon data from a CSV file."""
    with open(filename, "r", encoding="utf-8-sig") as file:
        reader = csv.reader(file)
        next(reader)
        return list(reader)

def count_champions(data):
    """Count how many times each champion has won."""
    champion_to_count = {}
    for row in data:
        winner = row[2]
        if winner in champion_to_count:
            champion_to_count[winner] += 1
        else:
            champion_to_count[winner] = 1
    return champion_to_count

def get_countries(data):
    """Get a sorted list of unique winner countries."""
    countries = set()
    for row in data:
        countries.add(row[1])
    return sorted(countries)

def main():
    data = read_data(FILENAME)
    champion_to_count = count_champions(data)
    countries = get_countries(data)

    print("Wimbledon Champions: ")
    for champion, count in sorted(champion_to_count.items()):
        print(f"{champion} {count}")

    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(", ".join(countries))

main()
