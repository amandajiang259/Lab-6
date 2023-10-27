sent = 1


def encode(password):
    encoded_pass = ""
    for digit in password:
        enc_digit = int(digit) + 3
        if enc_digit > 9:
            str_enc = str(enc_digit)
            enc_digit = str_enc[-1]
        encoded_pass = encoded_pass + str(enc_digit)
    return encoded_pass


# Decode a password
# Anthony Thisse
def decode(password):
    decoded_pass = ""
    # For each digit in the encoded password
    for digit in password:
        # Shift up by 7 to get back to the base value, % by 10 to strip 10's digit and append to decoded_pass
        decoded_pass += str((int(digit) + 7) % 10)
    # Return the decoded password
    return decoded_pass


if __name__ == '__main__':
    while sent != 0:
        print("Menu Options:")
        print("1) Encode")
        print("2) Decode")
        print("3) Exit")
        option = int(input("Choice: "))

        if option == 1:
            password = input("Enter 8-digit password to encode: ")
            print(encode(password))
        elif option == 2:
            dec_password = input("Enter 8-digit password to decode: ")
            print(decode(dec_password))
        else:
            sent = 0
            break