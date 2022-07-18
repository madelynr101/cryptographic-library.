# Programmer: Madelyn Weathers 
# Purpose: To use symmetric key encryption to decrypt an encrypted message, to either read or write to the message, and then encrypt the message again. 

from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    return key

def read():
    file1 = open("myfile.txt","r") 
    while True:
        line = file1.readline()
        if line == '': break
        print(line)
    file1.close()   
    welcome_menu()

def modify():
    file1 = open("myfile.txt","w") 
    print("We are going to input into the text file step by step.")
    print("Continue entering until you are finished.")
    # User enters data until they are finished
    # Make sure to turn correct value back into string so text file can use the data
    while True:
        new = input("Is this a Float: F, String: S, or Integer: I? or Quit: Q \n")
        if new.upper() == "I":
            part = int(input(new))
            file1.write(str(part))
            file1.write("\n")
        if new.upper() == "S":
            part = input(new)
            file1.write(str(part))
            file1.write("\n")
        if new.upper() == "F":
            part = float(input(new))
            file1.write(str(part))
            file1.write("\n")
        if new.upper() == "Q":
            file1.close()
            welcome_menu()
        else:
            continue 

def encrypt(messages,fernet):
    encrypted_message = [fernet.encrypt(each_message.encode())
                        for each_message in messages]

def decrypt(messages, fernet):
    decrypted_message = [fernet.decrypt(each_message.decode())
                        for each_message in messages]

def welcome_menu():
    # input validation menu
    while True:
        print("Welcome to the settings menu!")
        choice1 = int(input("Would you like to 1: READ or 2: MODIFY? (Enter 1, 2, or 3 to EXIT)\n"))
        if choice1 == 1 or choice1 == 2 or choice1 == 3:
            break 
        else:
            continue
    if choice1 == 1:
        read()
    if choice1 == 2:
        while True:
            choice2 = int(input("WARNING! If you choose to modify the file, any original previous contents will be erased. Would you like to continue? 1 for yes, 2 for no\n"))
            if choice2 == 1 or choice2 == 2:
                break 
            else:
                continue
        if choice2 == 1:
            modify()
        if choice2 == 2:
            welcome_menu()
    if choice1 == 3:    
        print("Thanks for stopping by. See you soon!\n")
        quit()


def main():
    welcome_menu()
    key = generate_key()
    fernet = Fernet(key)

if __name__ == "__main__":
    main()