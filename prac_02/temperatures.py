def main():


    celsius = float(input("Celsius: "))
    convert_celsius_to_fahrenheit(celsius)

    fahrenheit = float(input("Fahrenheit: "))
    convert_fahrenheit_to_celsius(fahrenheit)


def convert_fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    celsius = 5 / 9 * (fahrenheit - 32)
    print(f"Result: {celsius:.2f} C")


def convert_celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    fahrenheit = celsius * 9.0 / 5 + 32
    print(f"Result: {fahrenheit:.2f} F")


main()