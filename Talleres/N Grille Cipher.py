import tkinter as tk
import numpy as np
from math import log
from math import ceil

grille = []


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


def initialize_grille(n):
    global grille
    grille = [[0 for i in range(n)] for j in range(n)]


def rotate_clockwise(matrix):
    return list(zip(*matrix[::-1]))


def rotate_anticlockwise(matrix):
    return list(reversed(list(zip(*matrix))))


def click(row, col, button):
    global grille

    grille[row][col] = 1
    print(np.matrix(grille))
    if button['bg'] == 'yellow':
        button.config(bg="white")
        grille[row][col] = 0
        print(np.matrix(grille))
    else:
        button.config(bg="yellow")


def initialize_interface(n):
    print("Wtf")
    initialize_grille(n)
    root = tk.Tk()
    for row in range(n):
        for col in range(n):
            button = tk.Button(
                root,
                text="%s,%s" % (row, col)
            )
            button.grid(row=row, column=col, sticky="nsew")
            button.configure(command=lambda row=row, col=col, button=button: click(row, col, button))

    init_grill_button = tk.Button(root, text="Reset Grille", command=lambda: cipher(n))
    init_grill_button.grid(row=0, column=n + 1)

    decipher_button = tk.Button(root, text="decipher", command=lambda: decipher(n))
    decipher_button.grid(row=1, column=n + 1)

    label = tk.Label(root, text="")
    label.grid(row=n, column=0, columnspan=n, sticky="new")

    root.grid_rowconfigure(n, weight=1)
    root.grid_columnconfigure(n, weight=1)

    root.mainloop()


def cipher(n):
    global grille

    # plain_text = "JIMATTACKSATDAWN"
    plain_text = "JKTDSAATWIAMCNAT"

    text = list(plain_text.replace(" ", ""))

    a = [text[i:i + n] for i in range(0, len(text), n)]

    print(np.matrix(a))

    matrix_encrypted = [[0 for i in range(n)] for j in range(n)]
    matrix = grille
    while text:
        print(np.matrix(matrix))
        for i in range(n):
            for j in range(n):
                if matrix[i][j] != 0:
                    matrix_encrypted[i][j] = text[0]
                    text = text[1:]
        matrix = rotate_anticlockwise(matrix)

    print("".join([j for sub in matrix_encrypted for j in sub]))


def decipher(n):
    global grille

    # plain_text = "JKTDSAATWIAMCNAT"
    plain_text = "TESHN INCIG LSRGY LRIUS PITSA TLILM REENS ATTOG SIAWG IPVER TOTEH HVAEA XITDT UAIME RANPM TLHIE I"
    text = list(plain_text.replace(" ", ""))

    a = [text[i:i + n] for i in range(0, len(text), n)]
    flag = False

    if n%2 != 0:
        flag = True

    middle = ceil(n//2)
    #print(np.matrix(a))

    text_decrypted = []
    matrix = grille
    counter = 0
    while text:
        print(np.matrix(a))
        for i in range(n):
            for j in range(n):
                if matrix[i][j] != 0:
                    if flag and i == j == middle:
                        matrix[i][j] = 0
                    text_decrypted.append(a[i][j])
                    text = text[1:]
        counter += 1
        print("Rotación:" + str(counter) + "\n")
        print(np.matrix(matrix))
        matrix = rotate_anticlockwise(matrix)

    print(infer_spaces(str.lower("".join(text_decrypted))))


n = int(input())

initialize_interface(n)

