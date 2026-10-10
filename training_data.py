import tkinter as tk
import time 
import csv  

window = tk.Tk()
window.geometry("1000x1000")

canvas = tk.Canvas(window, width=1000, height=1000)

canvas.pack()
grid = [[0]*20 for _ in range(20)]

for row in range(20):
    for column in range(20):
        x = column * 50
        y = row * 50
        canvas.create_rectangle(
            x, y, x + 50, y + 50,
            fill="white",
            outline="black",
            tags=f"cell_{row}_{column}"
        )


def paint(event):
    column = event.x // 50
    row = event.y // 50

    if 0 <= row < 20 and 0 <= column < 20:
        canvas.itemconfig(
            f"cell_{row}_{column}",
            fill="black"
        )

        grid[row][column] = 1

def paint1(event):
    column = event.x // 50
    row = event.y // 50

    if 0 <= row < 20 and 0 <= column < 20:
        canvas.itemconfig(
            f"cell_{row}_{column}",
            fill="white"
        )

        grid[row][column] = 0

canvas.bind("<Button-1>", paint)
canvas.bind("<B1-Motion>", paint)
canvas.bind("<Button-3>", paint1)
canvas.bind("<B3-Motion>", paint1)

def output_grid():
    for row in grid:
        print(row)
    print()
    window.after(5000, output_grid)
window.after(5000, output_grid)
def submit(event):
    global pixel_data
    pixel_data = "".join(str(value) for row in grid for value in row)

    print(pixel_data)
    window.destroy()

window.bind("<KeyRelease>", submit)
window.mainloop()

num1 = int(input("Enter the number you intended to draw: "))


with open('pixel_data.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(["Pixel Data", "Label"])
    writer.writerow([pixel_data, num1])





    
