import os

def mans_users():
    if os.path.exists("here.txt"):
        with open("here.txt", "r") as file:
            return dict(line.strip().split(',') for line in file)
    return {}

def save_users(users):
    with open("here.txt", "w") as file:
        file.writelines(f"{u},{p}\n" for u, p in users.items())

def register(users):
    username = input("Enter username: ")
    if username in users:
        print("Username already exists.")
    else:
        users[username] = input("Enter password: ")
        save_users(users)
        print("Successfully registered.")

def login(users):
    username = input("Enter username: ")
    if username in users and users[username] == input("Enter password: "):
        print("Login successful.")
    else:
        print("Invalid username or password.")

def change_password(users):
    username = input("Enter username: ")
    if username in users and users[username] == input("Enter old password: "):
        users[username] = input("Enter new password: ")
        save_users(users)
        print("Password successfully changed.")
    else:
        print("Invalid username or password.")

def main():
    users = mans_users()
    actions = {'1': register, '2': login, '3': change_password}

    while True:
        print("1. Register\n2. Log in\n3. Change password\n4. exit".)
        choice = input("Enter a number: ")
        if choice in actions:
            actions[choice](users)
        else:
            print("Invalid choice, please try again.")

main()
