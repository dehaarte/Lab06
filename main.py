# Jahkiyah Dehaarte
def encode(password):
    encoded_password = ''
    for char in password:
        encoded_char = str((int(char) + 3) % 10)
        encoded_password += encoded_char
    return encoded_password


def main():

    def menu():
        print("\nMenu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        data = None

    while True:
        menu()
        menu_option = input("\nPlease enter an option: ")

        if menu_option == "1":
            encode_input = input("Please enter your password to encode: ")
            encode_data = encode(encode_input)
            print("Your password has been encoded and stored!")

        if menu_option == "2":
            decode_data = decode(encode_data)
            print(f"The encoded password is {encode_data}, and the original password is {decode_data}.")

        if menu_option == "3":
            break


if __name__ == '__main__':
    main()

