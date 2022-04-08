import tkinter as tk
import numpy as np

grille = []

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

    print(np.matrix(a))

    text_decrypted = []
    matrix = grille
    while text:
        print(np.matrix(matrix))
        for i in range(n):
            for j in range(n):
                if matrix[i][j] != 0:
                    print(a[i][j])
                    text_decrypted.append(a[i][j])
                    text = text[1:]
        matrix = rotate_anticlockwise(matrix)

    print(text_decrypted)


n = int(input())

initialize_interface(n)

