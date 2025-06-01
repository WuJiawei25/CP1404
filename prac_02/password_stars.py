min_length = 8

def main():

    password = get_password()

    print("*" * len(password))


def get_password():
    """Get Password"""
    password = input("Enter your password: ")
    while len(password) < min_length:
        print(f"Password is Invalid, password must be at least {min_length} characters.")
        password = input("Enter your password: ")
    return password


main()