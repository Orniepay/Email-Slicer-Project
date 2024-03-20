def main():
    """
    Slices an email address into its constituent parts: username, domain, and extension.

    The function prompts the user to input an email address in the format <username@domain.extension>.
    It then splits the email address into the username, domain, and extension components and prints them.

    @param None

    @returns None
    """
    print("Welcome to the Email Slicer")
    print("")

    email_input = input("Input your email address: <username@domain.extension> ")

    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print("Username: ", username)
    print("Domain: ", domain)
    print("Extension: ", extension)

while True:
    main()