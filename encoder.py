#Jonathan Maynard
def password_encoder(password):
    encoded_password = ""
    for digit in password:
        encoded_digit = (int(digit) + 3) % 10
        encoded_password += str(encoded_digit)
    return encoded_password

password = input("Enter the 8-digit password to encode (only integers): ")

if len(password) != 8 or not password.isdigit():
    print("Please enter a valid 8-digit password containing only integers.")
else:
    # Encode the password and print the result
    encoded_password = password_encoder(password)
    print("Encoded password:", encoded_password)
