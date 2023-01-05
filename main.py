# Convert String to Morse Code

morse_code_dict = {
    "A": "· -",
    "B": "- · · ·",
    "C": "- · - ·",
    "D": "- · ·",
    "E": "·",
    "F": "· · - ·",
    "G": "- - ·",
    "H": "· · · ·",
    "I": "· ·",
    "J": "· - - -",
    "K": "- · -",
    "L": "· - · ·",
    "M": "- -",
    "N": "- ·",
    "O": "- - -",
    "P": "· - - ·",
    "Q": "- - · -",
    "R": "· - ·",
    "S": "· · ·",
    "T": "-",
    "U": "· · -",
    "V": "· · · -",
    "W": "· - -",
    "X": "- · · -",
    "Y": "- · - -",
    "Z": "- - · ·",
    "1": "· - - - -",
    "2": "· · - - -",
    "3": "· · · - -",
    "4": "· · · · -",
    "5": "· · · · ·",
    "6": "- · · · ·",
    "7": "- - · · ·",
    "8": "- - - · ·",
    "9": "- - - - ·",
    "0": "- - - - -",
    ".": "· - · - · -",
    ",": "- - · · - -",
    " ": "",
}


def string_to_morse_code():
    convert_again = True

    while convert_again:
        user_string = input(
            "What characters would you like converted to Morse Code (only alphanumeric, comma, period, and spaces are accepted)? ").upper()
        
        for x in user_string:
            try:
                morse_code_dict[x]
            except KeyError as error_character:
                print(f"{error_character} is not in Morse Code.")
            else:
                print(f"{x} = {morse_code_dict[x]}")
        
        convert_more = input("Type 'y' to convert more characters, or any other key to exit. ")

        if convert_more == "y":
            convert_again = True
        else:
            convert_again = False


string_to_morse_code()
