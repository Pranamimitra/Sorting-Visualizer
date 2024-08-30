from tkinter import *
from tkinter import ttk
import random
import time
from bubblesort import bubble_sort

def drawData(data, colorArray):
    canvas.delete("all")
    canvas_height = 450
    canvas_width = 870
    x_width = canvas_width / (len(data) + 1)
    offset = 10
    spacing_bet_rect = 10
    normalized_data = [i / max(data) for i in data]

    for i, height in enumerate(normalized_data):
        x0 = i * x_width + offset + spacing_bet_rect
        y0 = canvas_height - height * 400
        x1 = (i + 1) * x_width - spacing_bet_rect
        y1 = canvas_height

        # Draw the bars
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i], outline="")
        # Draw the numbers on the bars
        canvas.create_text(x0 + (x1 - x0) / 2, y0, anchor=S, text=str(data[i]), font=("Helvetica", 10, "bold"), fill="white")

    root.update_idletasks()

def StartAlgorithm():
    global data
    algorithm = selected_algorithm.get()
    order = order_selection.get()
    if algorithm == 'Bubble Sort':
        bubble_sort(data, drawData, speedscale.get(), order)

def Generate():
    global data
    minimumvalue = int(minvalue.get())
    maximumvalue = int(maxvalue.get())
    sizeavalue = int(sizevalue.get())
    
    data = [random.randrange(minimumvalue, maximumvalue + 1) for _ in range(sizeavalue)]

    drawData(data, ['#FFEB3B' for _ in range(len(data))])  # Bright yellow bars

root = Tk()
root.title('Sorting Algorithm Visualiser')
root.geometry('900x600+200+80')
root.config(bg='#212121')  # Dark background

# Style for ttk widgets
style = ttk.Style()
style.configure('TButton', font=('Helvetica', 12, 'bold'), padding=10)
style.configure('TCombobox', font=('Helvetica', 12), padding=5)

# Header
header_frame = Frame(root, bg='#424242', padx=20, pady=10)  # Dark gray header
header_frame.pack(fill=X)

mainlabel = Label(header_frame, text="Algorithm: ", font=("Helvetica", 12, "bold"), bg="#424242", fg="white")
mainlabel.pack(side=LEFT)

selected_algorithm = StringVar()
algo_menu = ttk.Combobox(header_frame, width=20, textvariable=selected_algorithm,
                         values=['Bubble Sort', 'Quick Sort', 'Merge Sort', 'Insertion Sort'])
algo_menu.pack(side=LEFT, padx=10)
algo_menu.current(0)

order_selection = StringVar()
order_menu = ttk.Combobox(header_frame, width=15, textvariable=order_selection,
                         values=['Ascending', 'Descending'])
order_menu.pack(side=LEFT, padx=10)
order_menu.current(0)

speedLabel = Label(header_frame, text="SPEED", font=("Helvetica", 12, "bold"), bg="#424242", fg="white")
speedLabel.pack(side=LEFT, padx=10)

speedscale = Scale(header_frame, from_=0.1, to=5.0, resolution=0.2, orient=HORIZONTAL, font=("Helvetica", 12),
                  length=200, bg='#424242', fg='white')
speedscale.pack(side=LEFT, padx=10)

# Controls Frame
controls_frame = Frame(root, bg='#333333', padx=20, pady=10)  # Darker gray for controls
controls_frame.pack(fill=X, pady=10)

sizevaluelabel = Label(controls_frame, text="Size:", font=("Helvetica", 12, "bold"), bg='#333333', fg='white')
sizevaluelabel.grid(row=0, column=0, padx=10)

sizevalue = Scale(controls_frame, from_=0, to=30, orient=HORIZONTAL, font=("Helvetica", 12), length=150, bg='#333333', fg='white')
sizevalue.grid(row=0, column=1, padx=10)

minvaluelabel = Label(controls_frame, text="Min Value:", font=("Helvetica", 12, "bold"), bg='#333333', fg='white')
minvaluelabel.grid(row=0, column=2, padx=10)

minvalue = Scale(controls_frame, from_=0, to=10, orient=HORIZONTAL, font=("Helvetica", 12), length=150, bg='#333333', fg='white')
minvalue.grid(row=0, column=3, padx=10)

maxvaluelabel = Label(controls_frame, text="Max Value:", font=("Helvetica", 12, "bold"), bg='#333333', fg='white')
maxvaluelabel.grid(row=0, column=4, padx=10)

maxvalue = Scale(controls_frame, from_=0, to=100, orient=HORIZONTAL, font=("Helvetica", 12), length=150, bg='#333333', fg='white')
maxvalue.grid(row=0, column=5, padx=10)

# Button Frame for "Generate" and "Start"
button_frame = Frame(root, bg='#333333', padx=20, pady=10)
button_frame.pack(fill=X)

# Generate button in green
random_generate = Button(button_frame, text="Generate", bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"), command=Generate)
random_generate.pack(side=LEFT, padx=20)

# START button in red
start = Button(button_frame, text="START", bg="#F44336", fg="white", font=("Helvetica", 12, "bold"), command=StartAlgorithm)
start.pack(side=RIGHT, padx=20)

# Canvas for drawing
canvas = Canvas(root, width=870, height=450, bg="#424242")  # Dark gray canvas
canvas.pack(pady=10)

root.mainloop()
