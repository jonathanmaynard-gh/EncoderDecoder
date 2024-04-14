#Jonathan Maynard

#Encoder function
def encoder(password):
    #Essentially takes in digits and adds 3 to them
    #And if it becomes greater than 9, go back down to 0 and wrap around
    encodedPassword = ""
    #Encoding logic
    for digit in password:
        encodedDigit = (int(digit) + 3) % 10
        encodedPassword += str(encodedDigit)
    return encodedPassword

#Decoder function
def decoder(encodedPassword):
    #Essentially goes in and subtracts 3 from digits
    #If it's a number that is 2 or less, it 'unwraps' back to 9
    decodedPassword = ""
    #Logic for decoder
    for digit in encodedPassword:
        decodedDigit = (int(digit) - 3) % 10
        decodedPassword += str(decodedDigit)
    return decodedPassword

#Main function
def main():
    #Password that's stored when there's an encoded password
    storedPassword = ''
    while True:
        #Menu options
        print("\nMenu\n-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = input("Please enter an option: ")

        #Logic with the menu options (if this numnber is pressed, do this...)
        if option == '1':
            password = input("Please enter your password to encode: ")
            if len(password) == 8 and password.isdigit():
                storedPassword = encoder(password)
                print("Your password has been encoded and stored!")
            else:
                print("Invalid password. Please ensure it is an 8-digit number.")

        elif option == '2':
            if storedPassword:
                original_password = decoder(storedPassword)
                print(f"The encoded password is {storedPassword}, and the original password is {original_password}.")
            else:
                print("No encoded password available. Please encode a password first.")

        #Quits the program
        elif option == '3':
            break
        #If a character other than 1-3 is inputted, output this:
        else:
            print("Invalid option. Please try again.")

#Initializing statement/line(s)
if __name__ == "__main__":
    main()