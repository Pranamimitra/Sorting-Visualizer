# Sorting-Visualizer
This is a project on different sorting techniques visualization using Python Tkinter.

# Sorting Algorithm Visualizer

## Overview
The Sorting Algorithm Visualizer is an interactive tool that helps users understand and visualize how various sorting algorithms work. This tool provides a graphical representation of sorting processes, making it easier to grasp the underlying concepts of each algorithm.

## Features
- **Multiple Sorting Algorithms**: Supports visualization of Bubble Sort, Quick Sort, Merge Sort, and Insertion Sort.
- **Customizable Data Set**: Users can generate random data sets of varying sizes and value ranges.
- **Adjustable Sorting Speed**: Control the speed of the sorting process to observe the algorithm at your preferred pace.
- **Ascending/Descending Order**: Choose whether to sort the data in ascending or descending order.
- **Real-time Visualization**: Watch as the sorting algorithm progresses, with the current state of the array displayed as bars of varying heights.

## Installation
1. **Clone the repository:**
    ```bash
    git clone https://github.com/pranamimitra/sorting-visualizer.git
    ```
2. **Navigate to the project directory:**
    ```bash
    cd sorting-visualizer
    ```
3. **Install the required dependencies:**
    - Ensure you have Python installed.
    - Install Tkinter, which is included in most Python distributions by default. If not, install it via:
    ```bash
    pip install python-tk
    ```

## Usage
1. **Run the application:**
    ```bash
    python visualizer.py
    ```
2. **Select the sorting algorithm** from the dropdown menu.
3. **Choose the order** (Ascending or Descending) for sorting.
4. **Generate a random data set** by adjusting the size, minimum value, and maximum value sliders, then clicking the "Generate" button.
5. **Start the sorting process** by clicking the "START" button.
6. **Observe the sorting process** in real-time on the graphical display.

## How It Works
- The visualization displays the array as vertical bars of varying heights, with each height representing the value of an element in the array.
- During the sorting process, the bars change color to indicate which elements are being compared, swapped, or currently sorted.

## Customization
- **Color Scheme**: The application's color scheme features a dark background with bright, contrasting colors for the bars and buttons.
- **Speed Control**: You can adjust the sorting speed using the provided slider, allowing you to either slow down or speed up the visualization.

## Acknowledgments
- **Tkinter**: For providing a straightforward way to create GUIs in Python.
- **Python**: For being a versatile and easy-to-use programming language.
