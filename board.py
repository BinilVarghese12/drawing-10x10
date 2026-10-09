import tkinter as tk


window = tk.Tk()
window.geometry("400x400")


canvas = tk.Canvas(window, width=400, height=400)

canvas.pack()

for row in range(10):
    for column in range(10):
        x = column * 40
        y = row * 40
        canvas.create_rectangle(x, y, x + 40, y + 40, fill="grey", outline="black")













window.mainloop()