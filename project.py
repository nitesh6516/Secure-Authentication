import bcrypt
import json
import os
import random
import string
import getpass
import warnings
from getpass import GetPassWarning

DB_FILE = os.path.abspath("users.db")  # Absolute path for clarity
MAX_ATTEMPTS = 3
OTP_LENGTH = 6


def load_users():
    if not os.path.exists(DB_FILE):
        return {}
    with open(DB_FILE, "r") as f:
        return json.load(f)


def save_users(users):
    with open(DB_FILE, "w") as f:
        json.dump(users, f)


def generate_otp():
    return ''.join(random.choices(string.digits, k=OTP_LENGTH))


def simulate_otp_send(otp):
    print(f"[SIMULATED OTP SEND] Your OTP is: {otp}")


def register(username, password):
    users = load_users()
    if username in users:
        return "User already exists."
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    users[username] = {"password": hashed, "attempts": 0, "locked": False}
    save_users(users)
    return "User registered successfully."


def login(username, password):
    users = load_users()
    if username not in users:
        return "User not found."

    user = users[username]

    if user.get("locked"):
        return "Account is locked due to multiple failed attempts."

    if bcrypt.checkpw(password.encode(), user["password"].encode()):
        # Proceed with OTP
        otp = generate_otp()
        simulate_otp_send(otp)
        entered_otp = input("Enter the OTP sent to your device: ")
        if entered_otp == otp:
            user["attempts"] = 0
            save_users(users)
            return "Login successful with MFA."
        else:
            return "Invalid OTP. Login failed."
    else:
        user["attempts"] += 1
        if user["attempts"] >= MAX_ATTEMPTS:
            user["locked"] = True
        save_users(users)
        return f"Login failed. Attempts left: {MAX_ATTEMPTS - user['attempts']}"


def get_secure_password(prompt):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=GetPassWarning)
        try:
            return getpass.getpass(prompt)
        except GetPassWarning:
            return input(prompt + " (visible): ")


def main():
    while True:
        print("\n=== Secure Authentication Module ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter username: ")
            password = get_secure_password("Enter password: ")
            print(register(username, password))
            print(f"[INFO] User database stored at: {DB_FILE}")

        elif choice == '2':
            username = input("Enter username: ")
            password = get_secure_password("Enter password: ")
            print(login(username, password))

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
    
