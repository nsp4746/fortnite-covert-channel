# Nikhil Patil
# Fortnite Covert Channel

import string, random
FILE_PATH = 'weapons.txt'

RARITIES = ["Common","Uncommon","Rare","Epic","Legendary","Mythic","Exotic"]

def extract_weapons_from_txt():
    weapon_list = list()
    current_weapon = None

    with open(FILE_PATH, 'r') as file:
        for line in file:
            line = line.strip()

            if line and not any(char.isdigit() for char in line) and line not in RARITIES:
                current_weapon = line

            elif line in RARITIES:
                if current_weapon:
                    weapon_entry = f"{line} {current_weapon}"
                    weapon_list.append(weapon_entry)

    return weapon_list

def create_dictionary():
    weapon_list = extract_weapons_from_txt()
    alphabet = string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
    alphabet = alphabet + " "
    num_letters = len(alphabet)

    weapon_dictionary = {}
    for i, weapon in enumerate(weapon_list):
        letter_index = i % num_letters
        letter = alphabet[letter_index]
        weapon_dictionary[weapon]  = letter

    return weapon_dictionary

def reverse_dictionary(dictionary):
    reversed_dictionary = dict()
    for key, value in dictionary.items():
        if value not in reversed_dictionary:
            reversed_dictionary[value]= [key]
        else:
            reversed_dictionary[value].append(key)

    return reversed_dictionary


def encode_string():
    encoded_output = []
    weapon_dictionary = create_dictionary()
    reversed_weapon_dictionary = reverse_dictionary(weapon_dictionary)
    input_string = input("Enter a string to be encoded: ")
    for letter in input_string:
        weapon = random.choice(reversed_weapon_dictionary[letter]) # Get the first weapon for the letter
        if weapon not in encoded_output:
            encoded_output.append(weapon)

    print("Encoded Output:", encoded_output)
    return encoded_output

def decode_string(encoded_string=None):
    decoded_output = []
    weapon_dictionary = create_dictionary()
    if encoded_string is None:
        encoded_string = input("Enter your encoded string:")
    else:
        for weapon in encoded_string:
            decoded_output.append(weapon_dictionary[weapon])

    print("Decoded Output:", decoded_output)
    return decoded_output

def main():
    encoded_string = encode_string()
    decode_string(encoded_string)

if __name__ == '__main__':
    main()