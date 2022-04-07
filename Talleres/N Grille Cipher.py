import tkinter as tk
import numpy as np

grille = []


def initialize_grille(n):
    global grille
    grille = [[0 for i in range(n)] for j in range(n)]


def click(row, col):
    global grille

    grille[row][col] = 1
    print(np.matrix(grille))


def initialize_interface(n):
    initialize_grille(n)
    root = tk.Tk()
    for row in range(n):
        for col in range(n):
            button = tk.Button(root, text="%s,%s" % (row, col),
                               command=lambda row=row, col=col: click(row, col))
            button.grid(row=row, column=col, sticky="nsew")

    init_grill_button = tk.Button(root, text="Reset Grille", command=lambda: initialize_grille(n))
    init_grill_button.grid(row=0, column=n + 1)
    label = tk.Label(root, text="")
    label.grid(row=n, column=0, columnspan=n, sticky="new")

    root.grid_rowconfigure(n, weight=1)
    root.grid_columnconfigure(n, weight=1)

    root.mainloop()


n = int(input())

initialize_interface(n)

