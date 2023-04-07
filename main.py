import sys

from Test import Application
import matplotlib.figure
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import *
from tkinter import ttk

def mainWidget():
    root1 = tk.Tk()
    root1.geometry("350x350")
    text = tk.Label(root1,
                    text="Номер таблицы",
                    font=("Helvetica 11")).place(x=65, y=150)
    NumTbl = tk.Entry(root1).place(x=95, y=150)
    text1 = tk.Label(root1,
                    text="Значение интерполяции",
                    font=("Helvetica 11")).place(x=65, y=170)
    NumInt = tk.Entry(root1).place(x=95, y=170)
    tk.Button(root1,
              text='N',
              command=root1.quit,
              font=("Helvetica 11")).place(x=170, y=180)

    tk.mainloop()
def tkek():
    root = tk.Toplevel()
    tk.Label(root,
             text="x").grid(row=0)
    tk.Label(root,
             text="y").grid(row=1)

    x1 = tk.Entry(root)
    x2 = tk.Entry(root)
    x3 = tk.Entry(root)
    x4 = tk.Entry(root)
    x5 = tk.Entry(root)
    x6 = tk.Entry(root)
    x7 = tk.Entry(root)
    x8 = tk.Entry(root)
    y1 = tk.Entry(root)
    y2 = tk.Entry(root)
    y3 = tk.Entry(root)
    y4 = tk.Entry(root)
    y5 = tk.Entry(root)
    y6 = tk.Entry(root)
    y7 = tk.Entry(root)
    y8 = tk.Entry(root)


    x1.grid(row=0, column=1)
    x2.grid(row=0, column=2)
    x3.grid(row=0, column=3)
    x4.grid(row=0, column=4)
    x5.grid(row=0, column=5)
    x6.grid(row=0, column=6)
    x7.grid(row=0, column=7)
    x8.grid(row=0, column=8)
    y1.grid(row=1, column=1)
    y2.grid(row=1, column=2)
    y3.grid(row=1, column=3)
    y4.grid(row=1, column=4)
    y5.grid(row=1, column=5)
    y6.grid(row=1, column=6)
    y7.grid(row=1, column=7)
    y8.grid(row=1, column=8)
    tk.Button(root,
              text='OK',
              command=root.quit).grid(row=3,
                                      column=4,
                                      sticky=tk.W,
                                      pady=4)
    lstX = [x1, x2, x3, x4, x5, x6, x7, x8]
    lstY = [y1, y2, y3, y4, y5, y6, y7, y8]

    global x, y, interpol

    for i in range(len(lstX)):
        lstX[i].insert(0, x[i])
        lstY[i].insert(0, y[i])

    tk.mainloop()


    if (len(x) == 0) and (len(y) == 0):
        tk.Label(root,
                 text="interpolation").grid(row=2)
        interpoll = tk.Entry(root)
        interpoll.grid(row=2, column=1)
        INTERPOL = float(interpoll.get())
        X = np.array(
            [float(x1.get()), float(x2.get()), float(x3.get()), float(x4.get()), float(x5.get()), float(x6.get()),
             float(x7.get()), float(x8.get())], dtype=float)
        Y = np.array(
            [float(y1.get()), float(y2.get()), float(y3.get()), float(y4.get()), float(y5.get()), float(y6.get()),
             float(y7.get()), float(y8.get())], dtype=float)
        return INTERPOL, X, Y
    else:
        X = [x1.get(), x2.get(), x3.get(), x4.get(), x5.get(), x6.get(),
             x7.get(), x8.get()]
        Y = [y1.get(), y2.get(), y3.get(), y4.get(), y5.get(), y6.get(),
             y7.get(), y8.get()]
        for i in range(len(X)):
            if X[i] != "":
                x[i] = float(X[i])
        for i in range(len(Y)):
            if Y[i] != "":
                y[i] = float(Y[i])

    grafik()


def grafik():
    global x, y
    b = lagranz(x, y, interpol)
    print(b)
    xnew = np.linspace(np.min(x), np.max(x), 100)
    ynew = [lagranz(x, y, i) for i in xnew]
    # c = lagranz(x, y, interpol)
    # x = np.append(x, interpol)
    # y = np.append(y, c)
    plt.plot(x, y, 'o', xnew, ynew)
    plt.plot(interpol, int(b), 'ro')
    plt.grid(True)
    # plt.title(r'$\Phi_k(x) = \prod_{{j=0, j\neq k}}^n \frac{x-x_j}{x_k-x_j}, k = 0, ..., n$')
    # plt.title(r'$P_n(x) = \sum_{j=0}^n y_j L_j(x)/L_j(x_j)$')
    plt.title(r'$P_n(x) = \sum_{j=0}^n \frac{'
              r'y_j (x-x_0)(x-x_1)...(x-x_{j-1})(x-x_{j+1})}'
              r'{(x_j-x_0)(x_j-x_1)...('
              r'x_j-x_{j-1})(x_j-x_{j+1})(x_j-x_n)}$')
    plt.show()

def formula():
    global x, y
    a = ''
    b = ''
    fin = []
    for i in range(8):
        for j in range(8):
            if (i != j):
                a += fr'({interpol}-({x[j]}))'
                b += fr'{x[i]}-({x[j]}))'
        if (i != 7):
            fin += [fr'${y[i]}' r'\frac{' fr'{a} 'r'}' r'{' fr'{b}' r'}+$']
        else:
            fin += [fr'${y[i]}' r'\frac{' fr'{a} 'r'}' r'{' fr'{b}' r'}$']

    root = tk.Toplevel()
    # root = tk.Tk()
    app = Application(fin, master=root)
    app.mainloop()

def HelloWidget(lstx, lsty):
    root1 = tk.Tk()
    root1.geometry("350x350")
    text = tk.Label(root1,
                    text="Вы хотите изменить данные?",
                    font=("Helvetica 11")).place(x=65, y=150)
    tk.Button(root1,
              text='Y',
              command=tkek,
              # command=root1.quit,
              font=("Helvetica 11")).place(x=95, y=180)
    tk.Button(root1,
              text='N',
              command=grafik,
              font=("Helvetica 11")).place(x=200, y=180)
    tk.Button(root1,
              text='Formula',
              command=formula,
              font=("Helvetica 11")).place(x=150, y=280)

    tk.mainloop()


    # mainframe = tk.Frame(root)
    # mainframe.pack()
    #
    # label = tk.Label(mainframe)
    # label.pack()
    #
    # fig = matplotlib.figure.Figure(figsize=(5, 4), dpi=1000)
    # ax = fig.add_subplot(111)
    # ax.text(0.2, 0.6, fin, fontsize=1)
    #
    # canvas = FigureCanvasTkAgg(fig, master=label)
    # canvas.get_tk_widget().pack(side="top", fill="both", expand=True)
    # canvas._tkcanvas.pack(side="top", fill="both", expand=True)
    #
    # hbar = Scrollbar(mainframe, orient=HORIZONTAL)
    # hbar.pack(side=BOTTOM, fill=X)
    # hbar.config(command=tk.Canvas.xview)
    #
    # ax.get_xaxis().set_visible(False)
    # ax.get_yaxis().set_visible(False)
    #
    # root.bind("<Return>", fin)
    # # scroll = tk.Scrollbar(mainframe, orient='horizontal', command=ax.hview)
    # # scroll.pack(side='bottom', fill='x')
    # # ax.config(xscroll)
    # root.mainloop()

def lagranz(x, y, interpol):
    z = 0
    for j in range(len(y)):
        p1 = 1
        p2 = 1
        for i in range(len(x)):
            if i == j:
                p1 = p1 * 1
                p2 = p2 * 1
            else:
                p1 = p1 * (interpol - x[i])
                p2 = p2 * (x[j] - x[i])
        z += y[j] * p1 / p2
    return z

# mainWidget()
print("Введите номер таблицы: ", end="")
table = int(input())
match table:
    case 0:
        x = ""
        y = ""
        interpol, x, y = tkek()
    case 1:
        x = np.array([-1, 0, 2, 4, 6, 10, 12, 13], dtype=float)
        y = np.array([2, 0, 5, 17, 27, 35, 35, 40], dtype=float)
        print("Введите значение интерполяции: ", end="")
        interpol = int(input())
        HelloWidget(x, y)
    case 2:
        print("Введите значение интерполяции: ", end="")
        interpol = int(input())
        x = np.array([-1, 1, 2, 4, 6, 7, 8, 11], dtype=float)
        y = np.array([2, 2, 5, 18, 25, 30, 29, 21], dtype=float)
        HelloWidget(x, y)
    case 3:
        print("Введите значение интерполяции: ", end="")
        interpol = int(input())
        x = np.array([-1, 0, 2, 5, 6, 9, 11, 15], dtype=float)
        y = np.array([0, -1, 3, 24, 30, 31, 32, 39], dtype=float)
        HelloWidget(x, y)

    case 4:
        print("Введите значение интерполяции: ", end="")
        interpol = int(input())
        x = np.array([-1, 1, 2, 4, 6, 7, 8, 11], dtype=float)
        y = np.array([2, 2, 5, 18, 25, 30, 29, 21], dtype=float)
        HelloWidget(x, y)
    case 5:
        print("Введите значение интерполяции: ", end="")
        interpol = int(input())
        x = np.array([-1, 0, 3, 4, 7, 9, 10, 17], dtype=float)
        y = np.array([0, 0, 12, 20, 25, 40, 42, 51], dtype=float)
        HelloWidget(x, y)
    case 6:
        print("Введите значение интерполяции: ", end="")
        interpol = int(input())
        x = np.array([-1, 1, 2, 3, 5, 7, 10, 13], dtype=float)
        y = np.array([3, 3, 6, 15, 20, 21, 18, 15], dtype=float)
        HelloWidget(x, y)
    case 7:
        print("Введите значение интерполяции: ", end="")
        interpol = int(input())
        x = np.array([-1, 1, 2, 5, 6, 7, 9, 12], dtype=float)
        y = np.array([0, 2, 5, 14, 6, 3, 2, 5], dtype=float)
        HelloWidget(x, y)
    case 8:
        print("Введите значение интерполяции: ", end="")
        interpol = int(input())
        x = np.array([-2, 0, 3, 5, 7, 11, 12, 15], dtype=float)
        y = np.array([5, 0, 9, 24, 30, 35, 33, 28], dtype=float)
        HelloWidget(x, y)
    case 9:
        print("Введите значение интерполяции: ", end="")
        interpol = int(input())
        x = np.array([-1, 1, 3, 5, 8, 11, 13, 17], dtype=float)
        y = np.array([1, 2, 3, 10, 8, 4, 4, 8], dtype=float)
        HelloWidget(x, y)

    case 10:
        print("Введите значение интерполяции: ", end="")
        interpol = int(input())
        x = np.array([-1, 0, 3, 6, 8, 9, 11, 13], dtype=float)
        y = np.array([0, 2, 4, 30, 31, 28, 25, 20], dtype=float)
        HelloWidget(x, y)

b = lagranz(x, y, interpol)
print(b)
xnew = np.linspace(np.min(x), np.max(x), 100)
ynew = [lagranz(x, y, i) for i in xnew]
# c = lagranz(x, y, interpol)
# x = np.append(x, interpol)
# y = np.append(y, c)
plt.plot(x, y, 'o', xnew, ynew)
plt.plot(interpol, int(b), 'ro')
plt.grid(True)
# plt.title(r'$\Phi_k(x) = \prod_{{j=0, j\neq k}}^n \frac{x-x_j}{x_k-x_j}, k = 0, ..., n$')
# plt.title(r'$P_n(x) = \sum_{j=0}^n y_j L_j(x)/L_j(x_j)$')
plt.title(r'$P_n(x) = \sum_{j=0}^n \frac{'
          r'y_j (x-x_0)(x-x_1)...(x-x_{j-1})(x-x_{j+1})}'
          r'{(x_j-x_0)(x_j-x_1)...('
          r'x_j-x_{j-1})(x_j-x_{j+1})(x_j-x_n)}$')
# plt.show()
# formula()
# a = ''
# b = ''
# fin = ''
# for i in range(8):
#     for j in range(8):
#         if (i != j):
#             a += fr'({interpol}-({x[j]}))'
#             b += fr'{x[i]}-({x[j]}))'
#     fin += fr'${y[i]}' r'\frac{' fr'{a} 'r'}' r'{' fr'{b}' r'}$'
# plt.title(f'{fin}', fontsize=2)

