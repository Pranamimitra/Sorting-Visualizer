from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageDraw
import random
import time

# Global variables for statistics
comparisons_count = 0
swaps_count = 0
start_time = 0
paused = False
current_step = 0
steps = []

def update_stats():
    global comparisons_label, swaps_label, time_label
    global comparisons_count, swaps_count, start_time

    elapsed_time = round(time.time() - start_time, 2)
    
    comparisons_label.config(text=f"Comparisons: {comparisons_count}")
    swaps_label.config(text=f"Swaps: {swaps_count}")
    time_label.config(text=f"Time: {elapsed_time}s")

def colorArray(datalen, head, tail, border, currIdx, isSwapping=False):
    colors = []
    for i in range(datalen):
        if i >= head and i <= tail:
            colors.append("#2196F3")  # Bold Blue for sorting range
        else:
            colors.append("#FFFFFF")  # White for default

        if i == tail:
            colors[i] = '#FF5722'  # Bold Orange for pivot
        elif i == border:
            colors[i] = '#FF3D00'  # Darker Orange for border
        elif i == currIdx:
            colors[i] = '#FFEB3B'  # Bold Yellow for current index
        
        if isSwapping:
            if i == border or i == currIdx:
                colors[i] = '#4CAF50'  # Bold Green for swapping
    return colors

def bubble_sort(data, drawData, speed, order):
    global comparisons_count, swaps_count, start_time, paused, current_step, steps
    n = len(data)
    steps = []  # Clear previous steps
    for i in range(n):
        for j in range(0, n-i-1):
            comparisons_count += 1
            if (order == 'Ascending' and data[j] > data[j+1]) or (order == 'Descending' and data[j] < data[j+1]):
                swaps_count += 1
                data[j], data[j+1] = data[j+1], data[j]
                steps.append(data.copy())
                drawData(data, ['#FF3D00' if x == j or x == j+1 else '#4CAF50' for x in range(len(data))])
                if paused:
                    return
                time.sleep(speed)
            update_stats()

def quick_sort(data, head, tail, drawData, timeTick, order):
    global comparisons_count, swaps_count, start_time, paused, current_step, steps
    if head < tail:
        partitionIdx = partition(data, head, tail, drawData, timeTick, order)
        quick_sort(data, head, partitionIdx-1, drawData, timeTick, order)
        quick_sort(data, partitionIdx+1, tail, drawData, timeTick, order)
        if paused:
            return

def partition(data, head, tail, drawData, timeTick, order):
    global comparisons_count, swaps_count, start_time, paused, current_step, steps
    border = head
    pivot = data[tail]
    
    drawData(data, colorArray(len(data), head, tail, border, border))
    time.sleep(timeTick)

    for j in range(head, tail):
        comparisons_count += 1
        if (order == 'Ascending' and data[j] < pivot) or (order == 'Descending' and data[j] > pivot):
            drawData(data, colorArray(len(data), head, tail, border, j, True))
            time.sleep(timeTick)
            data[border], data[j] = data[j], data[border]
            swaps_count += 1
            border += 1
        drawData(data, colorArray(len(data), head, tail, border, j))
        time.sleep(timeTick)
        if paused:
            return

    drawData(data, colorArray(len(data), head, tail, border, True))
    time.sleep(timeTick)
    data[border], data[tail] = data[tail], data[border]
    swaps_count += 1
    steps.append(data.copy())
    return border

def merge_sort(data, left, right, drawData, timeTick, order):
    global comparisons_count, swaps_count, start_time, paused, current_step, steps
    if left < right:
        mid = (left + right) // 2
        merge_sort(data, left, mid, drawData, timeTick, order)
        merge_sort(data, mid + 1, right, drawData, timeTick, order)
        merge(data, left, mid, right, drawData, timeTick, order)
        if paused:
            return

def merge(data, left, mid, right, drawData, timeTick, order):
    global comparisons_count, swaps_count, start_time, paused, current_step, steps

    left_array = data[left:mid + 1]
    right_array = data[mid + 1:right + 1]

    i = 0
    j = 0
    k = left

    while i < len(left_array) and j < len(right_array):
        comparisons_count += 1
        if (order == 'Ascending' and left_array[i] <= right_array[j]) or (order == 'Descending' and left_array[i] >= right_array[j]):
            data[k] = left_array[i]
            i += 1
        else:
            data[k] = right_array[j]
            j += 1
        k += 1
        steps.append(data.copy())
        drawData(data, ['#FF5722' if x >= left and x <= right else '#4CAF50' for x in range(len(data))])
        time.sleep(timeTick)
        update_stats()  # Update statistics
        if paused:
            return

    while i < len(left_array):
        data[k] = left_array[i]
        i += 1
        k += 1
        swaps_count += 1
        steps.append(data.copy())
        drawData(data, ['#FF5722' if x >= left and x <= right else '#4CAF50' for x in range(len(data))])
        time.sleep(timeTick)
        update_stats()  # Update statistics
        if paused:
            return

    while j < len(right_array):
        data[k] = right_array[j]
        j += 1
        k += 1
        swaps_count += 1
        steps.append(data.copy())
        drawData(data, ['#FF5722' if x >= left and x <= right else '#4CAF50' for x in range(len(data))])
        time.sleep(timeTick)
        update_stats()  # Update statistics
        if paused:
            return

def insertion_sort(data, drawData, speed, order):
    global comparisons_count, swaps_count, start_time, paused, current_step, steps
    steps = []  # Clear previous steps
    for i in range(1, len(data)):
        key = data[i]
        j = i-1
        comparisons_count += 1
        while j >= 0 and ((order == 'Ascending' and data[j] > key) or (order == 'Descending' and data[j] < key)):
            data[j + 1] = data[j]
            j -= 1
            comparisons_count += 1
            swaps_count += 1
            drawData(data, ['#FF3D00' if x == j or x == j+1 else '#4CAF50' for x in range(len(data))])
            time.sleep(speed)
        data[j + 1] = key
        drawData(data, ['#FF3D00' if x == j + 1 else '#4CAF50' for x in range(len(data))])
        time.sleep(speed)
        steps.append(data.copy())
        update_stats()

def selection_sort(data, drawData, speed, order):
    global comparisons_count, swaps_count, start_time, paused, current_step, steps
    steps = []  # Clear previous steps
    for i in range(len(data)):
        min_idx = i
        for j in range(i + 1, len(data)):
            comparisons_count += 1
            if (order == 'Ascending' and data[j] < data[min_idx]) or (order == 'Descending' and data[j] > data[min_idx]):
                min_idx = j
            drawData(data, ['#FF3D00' if x == j or x == min_idx else '#4CAF50' for x in range(len(data))])
            time.sleep(speed)
        data[i], data[min_idx] = data[min_idx], data[i]
        swaps_count += 1
        drawData(data, ['#FF3D00' if x == i or x == min_idx else '#4CAF50' for x in range(len(data))])
        time.sleep(speed)
        steps.append(data.copy())
        update_stats()

def drawData(data, colorArray):
    canvas.delete("all")
    canvas_height = 450
    canvas_width = 700
    num_bars = len(data)
    
    # Adjust these values to control the breadth of the bars
    x_width = canvas_width / (num_bars + 2)  # Increase spacing to reduce bar width
    offset = 20
    spacing_bet_rect = 10  # Increase to add more space between bars

    # Normalize the data for height calculation
    max_data = max(data)
    normalized_data = [i / max_data for i in data]

    for i, height in enumerate(normalized_data):
        x0 = i * x_width + offset
        y0 = canvas_height - height * 400
        x1 = (i + 1) * x_width - spacing_bet_rect
        y1 = canvas_height

        # Draw the bars
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i], outline="")
        
        # Draw the numbers on the bars
        canvas.create_text(x0 + (x1 - x0) / 2, y0 - 15, anchor=S, text=str(data[i]), font=("Helvetica", 10, "bold"), fill="black")

    root.update_idletasks()

def startSorting():
    global paused
    paused = False
    global start_time
    start_time = time.time()  # Record the start time
    if algo.get() == 'Bubble Sort':
        bubble_sort(data, drawData, float(speedScale.get()), order.get())
    elif algo.get() == 'Quick Sort':
        quick_sort(data, 0, len(data) - 1, drawData, float(speedScale.get()), order.get())
    elif algo.get() == 'Merge Sort':
        merge_sort(data, 0, len(data) - 1, drawData, float(speedScale.get()), order.get())
    elif algo.get() == 'Insertion Sort':
        insertion_sort(data, drawData, float(speedScale.get()), order.get())
    elif algo.get() == 'Selection Sort':
        selection_sort(data, drawData, float(speedScale.get()), order.get())

def generateArray():
    global data
    data = [random.randint(1, 100) for _ in range(30)]
    drawData(data, ['#4CAF50' for _ in range(len(data))])

def loadArray():
    global data
    filename = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if filename:
        with open(filename, 'r') as file:
            data = list(map(int, file.read().split()))
        drawData(data, ['#4CAF50' for _ in range(len(data))])

def manualInput():
    global data
    input_str = manual_entry.get()
    if input_str:
        try:
            data = list(map(int, input_str.split(',')))
            drawData(data, ['#4CAF50' for _ in range(len(data))])
        except ValueError:
            print("Invalid input. Please enter integers separated by commas.")

# Main UI setup
root = Tk()
root.title("Sorting Algorithm Visualizer")

canvas = Canvas(root, width=700, height=450, bg='white')
canvas.grid(row=0, column=0, columnspan=4, padx=20, pady=20)

algo = StringVar(value='Bubble Sort')
order = StringVar(value='Ascending')
data = []

# UI Elements
Label(root, text="Select Algorithm:", font=("Helvetica", 12)).grid(row=1, column=0, padx=10, pady=10, sticky=W)
ttk.Combobox(root, textvariable=algo, values=['Bubble Sort', 'Quick Sort', 'Merge Sort', 'Insertion Sort', 'Selection Sort'], font=("Helvetica", 12)).grid(row=1, column=1, padx=10, pady=10)

Label(root, text="Order:", font=("Helvetica", 12)).grid(row=1, column=2, padx=10, pady=10, sticky=W)
ttk.Combobox(root, textvariable=order, values=['Ascending', 'Descending'], font=("Helvetica", 12)).grid(row=1, column=3, padx=10, pady=10)

Label(root, text="Speed:", font=("Helvetica", 12)).grid(row=2, column=0, padx=10, pady=10, sticky=W)
speedScale = Scale(root, from_=0.1, to_=2.0, orient=HORIZONTAL, resolution=0.1, length=200, font=("Helvetica", 12))
speedScale.set(1.0)
speedScale.grid(row=2, column=1, columnspan=2, padx=10, pady=10)

Button(root, text="Generate", bg='green', fg='white', font=("Helvetica", 12), command=generateArray).grid(row=3, column=0, padx=10, pady=10)
Button(root, text="Load from File", bg='lightblue', font=("Helvetica", 12), command=loadArray).grid(row=3, column=1, padx=10, pady=10)
Button(root, text="Start", bg='red', fg='white', font=("Helvetica", 12), command=startSorting).grid(row=3, column=2, padx=10, pady=10)
Button(root, text="Pause", bg='orange', fg='white', font=("Helvetica", 12), command=lambda: globals().update(paused=True)).grid(row=3, column=3, padx=10, pady=10)

# Manual input section
manual_frame = Frame(root)
manual_frame.grid(row=4, column=0, columnspan=4, pady=10)

Label(manual_frame, text="Enter Array (comma-separated):", font=("Helvetica", 12)).grid(row=0, column=0, padx=10)
manual_entry = Entry(manual_frame, font=("Helvetica", 12))
manual_entry.grid(row=0, column=1, padx=10)
Button(manual_frame, text="Submit", bg='lightgreen', font=("Helvetica", 12), command=manualInput).grid(row=0, column=2, padx=10)

# Statistics section
stats_frame = Frame(root, bg='lightgray')
stats_frame.grid(row=5, column=0, columnspan=4, pady=10)

comparisons_label = Label(stats_frame, text="Comparisons: 0", font=("Helvetica", 12), bg='lightgray')
comparisons_label.grid(row=0, column=0, padx=10)
swaps_label = Label(stats_frame, text="Swaps: 0", font=("Helvetica", 12), bg='lightgray')
swaps_label.grid(row=0, column=1, padx=10)
time_label = Label(stats_frame, text="Time: 0s", font=("Helvetica", 12), bg='lightgray')
time_label.grid(row=0, column=2, padx=10)

# Center the window
root.update_idletasks()
root_width = root.winfo_reqwidth()
root_height = root.winfo_reqheight()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width // 2) - (root_width // 2)
y = (screen_height // 2) - (root_height // 2)
root.geometry(f'{root_width}x{root_height}+{x}+{y}')

root.mainloop()
