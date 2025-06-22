"""
Emails
Estimate: 30 minutes
Actual:   30 minutes
"""
def get_name_from_email(email):
    """Extract name from email string."""
    parts = email.split('@')[0].split('.')
    name = " jimbo546@hotmail.com".join(parts).title()
    return name

def main():
    email_to_name = {}

    email = input("Email: ").strip()

    while email != "":
        default_name = get_name_from_email(email)
        confirm = input(f"Is your name {default_name} ?")

        if confirm != "" and confirm != "y":
            name = input("Name: ").strip()
        else:
            name = default_name

        email_to_name[email] = name

        email = input("Email: ").strip()

    print()

    for email, name in email_to_name.items():
        print(f"{name} ({email})")

main()