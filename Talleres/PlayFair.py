import numpy as np
import functools as ft

menu_options = {
        1: 'Encrypt a message',
        2: 'Decrypt a message',
        3: 'Exit',
    }


# Removes the duplicates in a list of characters whilst maintaining insertion order
def remove_duplicates(sequence):
    # A set to extract all the unique characters in 'sequence'
    unique_letters = set()

    # List comprehension used to build the list of characters without duplicates maintaining insertion order.
    # Adds the element 'x' to the returning list if it is not in unique_letters (if it isn't a duplicate).
    # unique_letters.add(x) returns None when successfully adding an element. if not (None) -> True
    return [x for x in sequence if not (x in unique_letters or unique_letters.add(x))]


# Concatenates the unique letters in key word with the alphabets & constructs the string that is to become the key_table
def concat_key_w_alphabet(unique_words_key):
    alphabet = "abcdefghiklmnopqrstuvwxyz"
    sequence = unique_words_key + list(alphabet)
    temp = set()
    # Returns the sequence of letters in order given the keyword, list comprehension works the same as remove_duplicates
    return [x for x in sequence if not (x in temp or temp.add(x))]


# Builds the key table given the string modified by concat key w alphabet
def build_key_table(key):
    key_table = [[x for x in range(5)] for y in range(5)]
    treated_key = remove_duplicates(key)
    table_alphabet = concat_key_w_alphabet(treated_key)
    counter = 0
    for i in range(5):
        for j in range(5):
            key_table[i][j] = table_alphabet[counter]
            counter += 1
    return key_table


# Separates the received messaged in pairs, as the PlayFair Cipher suggests
def separate_message_in_pairs(message):
    i = 0
    while i < len(message):
        if i == len(message) - 1:
            message.append("x")
            i += 2
            continue
        if message[i] == message[i+1]:
            message.insert(i+1, "x")
        i += 2
    return message


# Searches the index of each letter within the key_table
def search_letter_index(pair, table):
    # Boring solution
    # return [pos for pos, x in np.ndenumerate(table) if x in pair]

    # lambda function so it repeats the extraction of the pair of index for each letter of the sequence (pair)
    # Cool solution
    return ft.reduce(
        lambda i, j: i+j, [[(i,j) for j in range(len(table)) if table[i][j] in pair] for i in range(len(table))]
    )


# Gets all the pair of indexes of all the letters, so they can be encrypted/decrypted using the playfair rules
def get_all_indexes(pair, table):
    temp = [search_letter_index(pair[x], table) for x in range(len(pair))]
    return [temp[i][0] for i in range(len(temp))]


def encrypt(message, key):
    encrypted_message = []
    key_table = build_key_table(key)
    pairs = separate_message_in_pairs(message)

    indexes = get_all_indexes(pairs, key_table)

    for i in range(0,len(indexes), 2):
        # If both letters are in same column
        if indexes[i][1] == indexes[i+1][1]:

            x1 = (indexes[i][0] + 1) % 5
            y1 = indexes[i][1]
            x2 = (indexes[i+1][0] + 1) % 5
            y2 = indexes[i+1][1]
            encrypted_message.append(key_table[x1][y1])
            encrypted_message.append(key_table[x2][y2])
        # If both letters are in same row
        elif indexes[i][0] == indexes[i + 1][0]:
            x1 = indexes[i][0]
            y1 = (indexes[i][1] + 1) % 5
            x2 = indexes[i + 1][0]
            y2 = (indexes[i + 1][1] + 1) % 5
            encrypted_message.append(key_table[x1][y1])
            encrypted_message.append(key_table[x2][y2])
        else:
            x1, y1 = indexes[i][0], indexes[i+1][1]
            x2, y2 = indexes[i+1][0], indexes[i][1]

            encrypted_message.append(key_table[x1][y1])
            encrypted_message.append(key_table[x2][y2])

    return encrypted_message


def decrypt(message, key):
    message = message.replace(" ", "").lower().replace("j", "i")
    decrypted_message = []
    key_table = build_key_table(key)
    pairs = separate_message_in_pairs(message)
    indexes = get_all_indexes(pairs, key_table)

    for i in range(0, len(indexes), 2):
        # If both letters are in same column
        if indexes[i][1] == indexes[i + 1][1]:

            x1 = (indexes[i][0] - 1) % 5
            y1 = indexes[i][1]
            x2 = (indexes[i + 1][0] - 1) % 5
            y2 = indexes[i + 1][1]
            decrypted_message.append(key_table[x1][y1])
            decrypted_message.append(key_table[x2][y2])
        # If both letters are in same row
        elif indexes[i][0] == indexes[i + 1][0]:
            x1 = indexes[i][0]
            y1 = (indexes[i][1] - 1) % 5
            x2 = indexes[i + 1][0]
            y2 = (indexes[i + 1][1] - 1) % 5
            decrypted_message.append(key_table[x1][y1])
            decrypted_message.append(key_table[x2][y2])
        else:
            x1, y1 = indexes[i][0], indexes[i + 1][1]
            x2, y2 = indexes[i + 1][0], indexes[i][1]

            decrypted_message.append(key_table[x1][y1])
            decrypted_message.append(key_table[x2][y2])


    for i in range(1, len(decrypted_message)-2):
        if decrypted_message[i] == "x":
            if decrypted_message[i-1] == decrypted_message[i+1]:
                decrypted_message.pop(i)

    return decrypted_message


def print_menu():
    print("Welcome to PlayFair Cipher, choose your option: ")
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


def print_message(message):
    for i in range(len(message)):
        print(message[i], end='')
        if (i+1) % 2 == 0:
            print(" ", end='')


def play_fair():
    while True:
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Not an option. Please enter a number ...')

        if option == 1:
            print(" Enter the Message to Encrypt")
            message = list(input().replace(" ", "").replace("j", "i"))
            # Receives a String, lower cases it and removes all blank (" ") spaces from it.
            print(" Enter the cipher's key")
            key = list(input().lower().replace(" ", "").replace("j", "i"))
            encrypted = encrypt(message, key)
            print("The encrypted message is: ")
            print_message(encrypted)
            print("\n")

        elif option == 2:
            print(" Enter the Message to Decrypt")
            message = input()
            print(" Enter the cipher's key")
            key = list(input().lower().replace(" ", "").replace("j", "i"))
            decrypted = decrypt(message, key)
            print("The decrypted message is: ")
            print("".join(decrypted))
            print("\n")

        elif option == 3:
            print('Thanks message before exiting')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 3.')


"""
Slides excercise: 
message = "ZO MH LC HY ZK MN SO NQ DL KT OQ CY KI EC LK SO YI EQ PQ RX EY KR WM NS DL GY LD GF AB YA QN YE AP GN IX PG HY YS NB HT EC TL KF VN RP YT PU PF CY EB YA WM KI MP LF UZ LH TC YH NP CK KL LY YT KI GB DH CY EC RD GN CL GO IH YE TY KI XO UY VN SC LX KF MX PW"
key = "yoan pinzon"
"""

play_fair()
