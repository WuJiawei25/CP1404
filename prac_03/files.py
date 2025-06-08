name = input("Enter your name: ")
file = open("name.txt", "w")
file.write(name)
file.close()

file = open("name.txt", "r")
name_from_file = file.read()
file.close()
print(f"Hi {name_from_file}!")

with open("number.txt", "r") as file:
    first_number = int(file.readline())
    second_number = int(file.readline())
    print(first_number + second_number)

with open("number.txt", "r") as file:
    total = 0
    for line in file:
        total += int(line)
    print(total)