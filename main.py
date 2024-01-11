from morsa_code import MORSE_CODE_DICT

print("*"*10 + "  Welcome to Morse Convator  "+"*"*10)
print("*"*10 + "  Please enter what you would like to convert  "+"*"*10)

morse_code_keys = list(MORSE_CODE_DICT.keys())
game_on = True

def convert( ):
    converted_code = ""
    not_valid_input = ""
    user_input = input("\nWhat would you like to convert:   ")
    for letter in user_input:
        if letter.upper() not in morse_code_keys:
            not_valid_input += letter+", "
        # this will separate words
        elif letter == " ":
            converted_code += " "+"/"
        else:
            converted_code += (MORSE_CODE_DICT[letter.upper()])+"/"
    print(f'This is your input : {user_input}.')
    if not not_valid_input == "":
        print(f"These are not a valid inputs:  {not_valid_input} ")
    print( f'Converted Morse Code is: \n {converted_code}\n')


while game_on:
    convert()
    play_again = input("Do you like to play again(Y/N): ")
    if not play_again.upper() == "Y":
        print("*" * 10 + "  Thank you for.  " + "*" * 10)
        game_on =  False








