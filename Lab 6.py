# lab 6
# Collaborator: Mollie Brewer
# Author: Wesly Menard
def decode_password(stored_password):

    encoded_password_int_list = []
    for item in stored_password:
        item = int(item)
        if item == 7:
            item = 0
        if item == 8:
            item = 1
        if item == 9:
            item = 2
        else:
            item += 3
        encoded_password_int_list.append(str(item))
        encoded_password = "".join(encoded_password_int_list)
    return encoded_password

user_password_to_encode = None

while True:
    print("\nMenu")    #added an empty line
    print("-------------")
    print("1. Encode", "\n""2. Decode""\n""3. Quit")
    print(" ")

    user_choice = int(input("Please enter an option: "))
    if user_choice > 3 or user_choice < 1:
        print("Invalid Menu Option. Choose option between 1 and 3. Try again!")


    elif user_choice == 1:
        while True:
            user_password_to_encode = input("Please enter your password to encode: ")
            try:
                user_password_to_encode = int(user_password_to_encode)
                if len(str(user_password_to_encode)) != 8:
                    print("Password must be 8 digits")

                else:
                    print("Your password has been encoded and stored!")
                    break

            except ValueError:
                print("Password must be numbers. Try again")




    elif user_choice == 2:
        # The password encoder should take in an 8-digit password in string format containing only integers.
        # After passing the password into the encoder, the encoder stores the encoded password to a new
        # variable, with each digit being shifted up by 3 numbers.
        # Examples:
        # “12345555” will become “45678888” after encoding.
        # “00009962” will become “33332295” after encoding
        stored_password = str(user_password_to_encode)
        decoded_password = decode_password(stored_password)
        print(f'Your encoded password is {decoded_password}, and the original password is {user_password_to_encode}.')


    elif user_choice == 3:
        break






