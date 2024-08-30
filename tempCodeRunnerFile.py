from tkinter import *
from tkinter import ttk
import random
from bubblesort import bubble_sort

root = Tk()
root.title('Sorting Algorithm Visualiser')
root.geometry('900x600+200+80')
root.config(bg='#C8A2C8')
data = []
def drawData(data, colorArray):
    canvas.delete("all")
    canvas_height = 450
    canvas_width = 870
    x_width = canvas_width / (len(data) + 1)
    offset = 10
    spacing_bet_rect = 10
    normalised_data = [i / max(data) for i in data]

    for i, height in enumerate(normalised_data):
        x0 = i * x_width + offset + spacing_bet_rect
        y0 = canvas_height - height * 400

        x1 = (i * 1) * x_width
        y1 = canvas_height

        # Use colorArray[i] to get the color value
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0 + 2, y0, anchor=SW, text=str(data[i]), font=("new roman", 15, "italic bold"),
                           fill="white")

    root.update_idletasks()
def StartAlgorithm():
    global data
    bubble_sort(data, drawData, speedscale.get())

def Generate():
    global data
    print('Selected Algorithm:' + selected_algorithm.get())
    minimumvalue = int(minvalue.get())
    maximumvalue = int(maxvalue.get())
    sizeavalue = int(sizevalue.get())
    
    data = []
    for _ in range(sizeavalue):
        data.append(random.randrange(minimumvalue, maximumvalue + 1))

    # Pass a list of colors, for example, all red:
    drawData(data, ['#A90042' for x in range(len(data))])




mainlabel= Label(root, text= "Algorithm: ", font = ("new roman", 14, "bold"), bg="#05897A",
                 width=8, fg="black", relief= GROOVE, bd=5)
mainlabel.place(x=0,y=0)

selected_algorithm=StringVar()

algo_menu = ttk.Combobox(root, width=15, font=("new roman", 16, "bold"), textvariable= selected_algorithm,
                         values=['Bubble Sort', 'Quick Sort' , 'Merge Sort', 'Insertion Sort'])
algo_menu.place(x=145, y=0)
algo_menu.current(0) #by default it will show Merge Sort


random_generate = Button(root, text="Generate", bg="#2DAE9A", font=("arial",12,"bold"), relief= SUNKEN, activebackground= "#05945B", 
                         activeforeground="white", bd=5, width=10, command=Generate)
random_generate.place(x=750, y=60)

sizevaluelabel= Label(root, text="Size: ", font= ("new roman", 12, "italic bold"), bg= "#0E6DA5",
                      width=10, fg="black", height=2, relief=GROOVE, bd=5)
sizevaluelabel.place(x=0, y=60)

sizevalue = Scale(root, from_ =0, to = 30, resolution = 1, orient = HORIZONTAL, font = ("arial",14, "italic bold"), 
                  relief= GROOVE, bd=2, width=10)
sizevalue.place(x=120, y=60)

minvaluelabel= Label(root, text="Min value", font= ("new roman", 12, "italic bold"), bg= "#0E6DA5",
                      width=10, fg="black", height=2, relief=GROOVE, bd=5)
minvaluelabel.place(x=250, y=60)

minvalue = Scale(root, from_ =0, to = 10, resolution = 1, orient = HORIZONTAL, font = ("arial",14, "italic bold"), 
                  relief= GROOVE, bd=2, width=10)
minvalue.place(x=370, y=60)

maxvaluelabel= Label(root, text="Max value", font= ("new roman", 12, "italic bold"), bg= "#0E6DA5",
                      width=10, fg="black", height=2, relief=GROOVE, bd=5)
maxvaluelabel.place(x=500, y=60)

maxvalue = Scale(root, from_ =0, to = 100, resolution = 1, orient = HORIZONTAL, font = ("arial",14, "italic bold"), 
                  relief= GROOVE, bd=2, width=10)
maxvalue.place(x=620, y=60)

start = Button(root, text="START", bg="#C45B09", font=("arial",12,"bold"), relief= SUNKEN, activebackground= "#05945B", 
                         activeforeground="white", bd=5, width=10, command= StartAlgorithm)
start.place(x=750, y=0)

speedLabel = Label(root, text="SPEED", font= ("new roman", 12, "italic bold"), bg= "#0E6DA5",
                      width=10, fg="black", relief=GROOVE, bd=5)
speedLabel.place(x=400,y=0)

speedscale = Scale(root, from_ =0.1, to = 5.0, resolution = 0.2,length=200, digits=2,  orient = HORIZONTAL, font = ("arial",14, "italic bold"), 
                  relief= GROOVE, bd=2, width=10)
speedscale.place(x=520, y=0)

canvas = Canvas(root, width= 870, height = 450, bg= "blue")
canvas.place(x=10, y=130)


root.mainloop()
