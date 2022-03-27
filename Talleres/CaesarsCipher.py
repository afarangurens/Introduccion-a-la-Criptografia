from math import log

menu_options = {
        1: 'Encrypt a message',
        2: 'Decrypt a message',
        3: 'Exit'
}

# Code to separate a string in separated english words
# Code accepted answer at: https://stackoverflow.com/questions/8870261/how-to-split-text-without-spaces-into-list-of-words
def infer_spaces(s):
    words = open("words-by-frequency.txt").read().split()
    wordcost = dict((k, log((i + 1) * log(len(words)))) for i, k in enumerate(words))
    maxword = max(len(x) for x in words)
    """Uses dynamic programming to infer the location of spaces in a string
    without spaces."""

    # Find the best match for the i first characters, assuming cost has
    # been built for the i-1 first characters.
    # Returns a pair (match_cost, match_length).
    def best_match(i):
        candidates = enumerate(reversed(cost[max(0, i-maxword):i]))
        return min((c + wordcost.get(s[i-k-1:i], 9e999), k+1) for k,c in candidates)

    # Build the cost array.
    cost = [0]
    for i in range(1,len(s)+1):
        c,k = best_match(i)
        cost.append(c)

    # Backtrack to recover the minimal-cost string.
    out = []
    i = len(s)
    while i>0:
        c,k = best_match(i)
        assert c == cost[i]
        out.append(s[i-k:i])
        i -= k

    return " ".join(reversed(out))


def print_menu():
    print("Welcome to Caesar's Cipher, choose your option: ")
    for key in menu_options.keys():
        print(key, '--', menu_options[key])


def encrypt(message, k):
    return [chr(((ord(i) - ord("a") + k) % 26) + ord("a")) for i in message]


def decrypt(message, k):
    return [chr(((ord(i) - ord("a") - k) % 26) + ord("a")) for i in message]


def print_message(message):
    print("".join(message))


def caesars_cipher():
    while True:
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Please enter a number ...')

        if option == 1:
            print(" Enter the Message to Encrypt")
            message = list(input().replace(" ", "").lower())
            print(" Enter the cipher's key")
            k = int(input())
            print("The encrypted message is: ")
            print_message(encrypt(message, k))
            print("\n")

        elif option == 2:
            print(" Enter the Message to Decrypt")
            message = list(input().replace(" ", "").lower())
            print(" Enter the cipher's key")
            k = int(input())
            print("The decrypted message is: ")
            print(infer_spaces("".join(decrypt(message, k))))
            print("\n")

        elif option == 3:
            print('So long!')
            exit()
        else:
            print('Please enter a number between 1 and 3.')


caesars_cipher()

