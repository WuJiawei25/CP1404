COLOUR_HEX_CODES = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aqua": "#00ffff",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "beige": "#f5f5dc",
    "bisque": "#ffe4c4",
    "black": "#000000",
    "blanchedalmond": "#ffebcd",
    "blue": "#0000ff"
}


print("Enter colour names to get hex code")
colour_name = input("Colour name: ").strip().lower()

while colour_name != "":
    hex_code = COLOUR_HEX_CODES.get(colour_name)
    try:
        print(f"The hex code for {colour_name} is {hex_code}")
    except:
        print("Invalid colour name")
    colour_name = input("Colour name: ").strip().lower()

