# Create an empty dictionary to store user information
users = {}

# Define a function to sign up a new user
def sign_up():
    print("Sign up")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    email = input("Enter your email: ")
    # Add the new user information to the dictionary
    users[username] = {"password": password, "email": email}
    print("User created successfully")

# Define a function to log in an existing user
def log_in():
    print("Log in")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    # Check if the username and password match a registered user
    if username in users and users[username]["password"] == password:
        print("Login successful")
    else:
        print("Login failed")

# Offer the user the choice to sign up or log in
while True:
    choice = input("Do you want to sign up (s) or log in (l)? ")
    if choice == "s":
        sign_up()
    elif choice == "l":
        log_in()
    else:
        break
