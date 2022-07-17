from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
        print("The key is now generated!")

def read():
    

def modify():
    pass 

def welcome_menu():
    # input validation menu
    while True:
        print("Welcome to the settings menu!")
        choice = input("Would you like to 1: READ or 2: MODIFY? (Enter 1, 2, or 3 to BREAK)\n")
        if choice == "1" or choice == "2" or choice == "3":
            break 
        else:
            continue
    if choice == "1":
        read()
    if choice == "2":
        modify()
    if choice == "3":
        print("Thanks for stopping by. See you soon!\n")
        quit()


def main():
    welcome_menu()


if __name__ == "__main__":
    main()