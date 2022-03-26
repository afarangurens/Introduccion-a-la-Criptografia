import numpy as np
import functools as ft


# Removes the duplicates in a list of characters whilst maintaining insertion order
def remove_duplicates(sequence):
    # A set to extract all the unique characters in 'sequence'
    unique_letters = set()

    # List comprehension used to build the list of characters without duplicates maintaining insertion order.
    # Adds the element 'x' to the returning list if it is not in unique_letters (if it isn't a duplicate).
    # unique_letters.add(x) returns None when successfully adding an element. if not (None) -> True
    return [x for x in sequence if not (x in unique_letters or unique_letters.add(x))]


def concat_key_w_alphabet(unique_words_key):
    alphabet = "abcdefghiklmnopqrstuvwxyz"
    sequence = unique_words_key + list(alphabet)
    temp = set()
    return [x for x in sequence if not (x in temp or temp.add(x))]


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


def search_letter_index(pair, table):
    # Boring solution
    # return [pos for pos, x in np.ndenumerate(table) if x in pair]

    # Cool solution
    return ft.reduce(
        lambda i, j: i+j, [[(i,j) for j in range(len(table)) if table[i][j] in pair] for i in range(len(table))]
    )


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
            print("1")
            print(encrypted_message)
        # If both letters are in same row
        elif indexes[i][0] == indexes[i + 1][0]:
            x1 = indexes[i][0]
            y1 = (indexes[i][1] + 1) % 5
            x2 = indexes[i + 1][0]
            y2 = (indexes[i + 1][1] + 1) % 5
            encrypted_message.append(key_table[x1][y1])
            encrypted_message.append(key_table[x2][y2])
            print("2")
            print(encrypted_message)
        else:
            pass

    return encrypted_message


# Input message
message = list(input().replace(" ", "").replace("j", "i"))
# Receives a String, lower cases it and removes all blank (" ") spaces from it.
key = list(input().lower().replace(" ", "").replace("j", "i"))

key_table = build_key_table(key)
pairs = separate_message_in_pairs(message)
print(np.matrix(key_table))

print(encrypt(message, key))

# print(pairs)

"""
print(search_letter_index(pairs[0:2], key_table))
index = search_letter_index(pairs[0:2], key_table)
print(key_table[index[0][0]][index[0][1]])
"""

