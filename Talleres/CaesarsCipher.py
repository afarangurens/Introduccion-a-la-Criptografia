from math import log

menu_options = {
        1: 'Encrypt a message',
        2: 'Decrypt a message',
        3: 'Exit'
}


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
            print_message(decrypt(message, k))
            print("\n")

        elif option == 3:
            print('So long!')
            exit()
        else:
            print('Please enter a number between 1 and 3.')


def bullshit_code(message):
    words = open("words-by-frequency.txt").read().split()

#caesars_cipher()

a = "itisclaimedtheearliestknownreferencetothistypeofcipherisinthekamasutrawhichsayswomenshouldlearntheartofsecretwritingtoconcealtheirliasons"

