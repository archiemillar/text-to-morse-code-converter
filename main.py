import pyfiglet
from morse_code import MORSE_CODE
import pandas as pd
import numpy as np
from tabulate import tabulate


while True:
    # Ascii art generator
    T = "Text to Morse Code Converter"
    ASCII_art_1 = pyfiglet.figlet_format(T)
    print(ASCII_art_1)

    # Display characters to use only #

    # Get MORSE_CODE dict keys and make " " appear as "SPACE"
    key_list = []

    for key in MORSE_CODE.keys():
        if key == " ":
            key = "SPACE"
        key_list.append(key)

    # Convert to dataframe
    letters = dict(enumerate(key_list[:26]))
    others = dict(enumerate(key_list[26:44]))
    digits = dict(enumerate(key_list[44:]))

    df_letters = pd.DataFrame.from_dict(letters, orient='index', columns=['Letters'])
    df_digits = pd.DataFrame.from_dict(digits, orient='index', columns=['Digits'])
    df_others = pd.DataFrame.from_dict(others, orient='index', columns=['Others'])

    # Merging dataframes
    df1 = df_letters.join(df_digits)
    final_df = df1.join(df_others).replace(np.nan, " ")

    # Show as table
    tabulated_df = tabulate(final_df, headers='keys', tablefmt='psql')

    print(f"You may only use the following characters.\n"
          f"{tabulated_df}\n"
          f"Feel free to use uppercase or lowercase letters or a mix of both.")

    # Ask user to type in message #
    message = input("Type your message: ").upper()

    # Check if all chars have morse code #
    converted_text = ""
    no_morse = ""

    for char in list(message):
        if char in MORSE_CODE:
            converted_text += f"{MORSE_CODE[char]} "
        else:
            no_morse += f"{char} "

    if no_morse:
        # If there are characters with no morse code
        print(f"The following characters you provided don't have Morse Code: {no_morse}\nPlease type in the characters "
              f"shown in the table only.")
    else:
        # If all valid characters
        print(f"Morse Code: {converted_text}")

    if input("Do you want to type a new message? Y/N: ") == "N":
        break

    print("\n" * 50)
