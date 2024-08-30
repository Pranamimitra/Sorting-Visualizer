import time

def bubble_sort(data, drawData, speed, order):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if (order == 'Ascending' and data[j] > data[j+1]) or (order == 'Descending' and data[j] < data[j+1]):
                data[j], data[j+1] = data[j+1], data[j]
                drawData(data, ['#FF5722' if x == j or x == j+1 else '#4CAF50' for x in range(len(data))])
                time.sleep(speed)
