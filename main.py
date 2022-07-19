# Programmer: Madelyn Weathers 
# Purpose: To use symmetric key encryption to decrypt an encrypted message, to either read or write to the message, and then encrypt the message again. 

from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    return key

def read(fernet):
    print("Your encrypted text file is: \n")
    file1 = open("file1.csv","rb") 
    info = file1.read()
    print(info)
    file1.close()   
    print("Your decrypted file is: \n")
    dec_file = decrypts(fernet)
    print(dec_file)
    welcome_menu(fernet)

def modify(fernet):
    file1 = open("file1.csv","w") 
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
            encrypts(fernet)
            file1.close()
            welcome_menu(fernet)
        else:
            continue 

def beginning_textfile(fernet):
    file1 = open("file1.csv","w")
    file1.write("Please modify this file!\n")
    file1.close()
    encrypts(fernet)

def encrypts(fernet):
    with open("file1.csv", "rb") as file:
        original = file.read()
    encrypted = fernet.encrypt(original).encode()

    with open("file1.csv", "wb") as encrypted_file:
        encrypted_file.write(encrypted)

def decrypts(fernet):
    with open("file1.csv", "rb") as enc_file:
        encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted).decode()

    with open("file1.csv", "wb") as dec_file:
        dec_file.write(decrypted)
    return dec_file

def welcome_menu(fernet):
    # generate a text file so we don't run into an error 
    beginning_textfile(fernet)
    # input validation menu
    while True:
        print("Welcome to the settings menu!")
        choice1 = int(input("Would you like to 1: READ or 2: MODIFY? (Enter 1, 2, or 3 to EXIT)\n"))
        if choice1 == 1 or choice1 == 2 or choice1 == 3:
            break 
        else:
            continue
    if choice1 == 1:
        read(fernet)
    if choice1 == 2:
        while True:
            choice2 = int(input("WARNING! If you choose to modify the file, any original previous contents will be erased. Would you like to continue? 1 for yes, 2 for no\n"))
            if choice2 == 1 or choice2 == 2:
                break 
            else:
                continue
        if choice2 == 1:
            modify(fernet)
        if choice2 == 2:
            welcome_menu()
    if choice1 == 3:    
        print("Thanks for stopping by. See you soon!\n")
        quit()


def main():
    key = generate_key() 
    fernet = Fernet(key)
    welcome_menu(fernet)

if __name__ == "__main__":
    main()