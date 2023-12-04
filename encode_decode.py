sent = 1


def encode(password):
    encoded_pass = ""
    # For each digit in the inputted password
    for digit in password:
        # Increment the number by 3
        enc_digit = int(digit) + 3
        if enc_digit > 9:
            # if the number is more than ten, then cut off the tens place, keeping value in ones place
            str_enc = str(enc_digit)
            enc_digit = str_enc[-1]
        encoded_pass = encoded_pass + str(enc_digit)
    # Return encoded password
    return encoded_pass


# Decode a password
# Anthony Thisse
def decode(password):
    decoded_pass = ""
    # For each digit in the encoded password
    for digit in password:
        # Shift up by 7 to get back to the base value, % by 10 to strip 10's digit and append to
        # decoded_pass
        decoded_pass += str((int(digit) + 7) % 10)
    # Return the decoded password
    return decoded_pass


if __name__ == '__main__':
    password = ""
    while sent != 0:
        #Menu added
        print("Menu")
        print("-" * 13)
        print("1. Encode")
        print("2. Decode")
        print("3. Exit\n")
        option = int(input("Please enter an option: "))

        if option == 1:
            password = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!\n")
        elif option == 2:
            print(f"The encoded password is {encode(password)}, and the original password is {decode(encode(password))}\n")
        else:
            sent = 0
            break