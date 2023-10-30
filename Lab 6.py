# def decode_password(password):
#   decoded_password = []
#   for i in password:
#       if i == "0":
#           decoded_password.append("3")
#       elif i == "1":
#           decoded_password.append("4")
#       elif i == "2":
#           decoded_password.append("5")
#       elif i == "3":
#           decoded_password.append("6")
#       elif i == "4":
#           decoded_password.append("7")
#       elif i == "5":
#           decoded_password.append("8")
#       elif i == "6":
#           decoded_password.append("9")
#       elif i == "7":
#           decoded_password.append("0")
#       elif i == "8":
#           decoded_password.append("1")
#       elif i == "9":
#           decoded_password.append("2")
#       else:
#           decoded_password.append(i)
#   return ''.join(decoded_password)

# password = "123434224"
# decoded_password = decode_password(password)
# print(decoded_password)


user_password_to_encode = None

while True:
    print("Menu")
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
        pass


    elif user_choice == 3:
        break





