import tkinter as tk
import time 

window = tk.Tk()
window.geometry("400x400")


canvas = tk.Canvas(window, width=400, height=400)

canvas.pack()
grid = [[0]*10 for _ in range(10)]

for row in range(10):
    for column in range(10):
        x = column * 40
        y = row * 40
        canvas.create_rectangle(
            x, y, x + 40, y + 40,
            fill="white",
            outline="black",
            tags=f"cell_{row}_{column}"
        )


def paint(event):
    column = event.x // 40
    row = event.y // 40

    if 0 <= row < 10 and 0 <= column < 10:
        canvas.itemconfig(
            f"cell_{row}_{column}",
            fill="black"
        )

        grid[row][column] = 1

def paint1(event):
    column = event.x // 40
    row = event.y // 40

    if 0 <= row < 10 and 0 <= column < 10:
        canvas.itemconfig(
            f"cell_{row}_{column}",
            fill="white"
        )

        grid[row][column] = 0

canvas.bind("<Button-1>", paint)
canvas.bind("<B1-Motion>", paint)
canvas.bind("<Button-2>", paint1)
canvas.bind("<B2-Motion>", paint1)



def output_grid():
    for row in grid:
        print(row)
    print()
    window.after(5000, output_grid)

window.after(5000, output_grid)




window.mainloop()