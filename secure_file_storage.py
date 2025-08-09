import os
from cryptography.fernet import Fernet
import getpass

# Create a key and save it
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Load the key from file
def load_key():
    return open("secret.key", "rb").read()

# Encrypt the file
def encrypt_file(file_path, key):
    f = Fernet(key)
    with open(file_path, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(file_path + ".encrypted", "wb") as file:
        file.write(encrypted_data)
    os.remove(file_path)
    print("File encrypted and original removed.")

# Decrypt the file
def decrypt_file(file_path, key):
    f = Fernet(key)
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    original_path = file_path.replace(".encrypted", "")
    with open(original_path, "wb") as file:
        file.write(decrypted_data)
    print("File decrypted and saved as:", original_path)

# Menu
def main():
    if not os.path.exists("secret.key"):
        print("No key found. Generating new encryption key...")
        generate_key()

    key = load_key()

    while True:
        print("\n--- Secure File Storage System ---")
        print("1. Encrypt a file")
        print("2. Decrypt a file")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            file_path = input("Enter path to file to encrypt: ").strip()
            if os.path.exists(file_path):
                encrypt_file(file_path, key)
            else:
                print("File does not exist.")

        elif choice == '2':
            file_path = input("Enter path to encrypted file: ").strip()
            if os.path.exists(file_path):
                try:
                    decrypt_file(file_path, key)
                except Exception as e:
                    print("Decryption failed:", str(e))
            else:
                print("File does not exist.")

        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()