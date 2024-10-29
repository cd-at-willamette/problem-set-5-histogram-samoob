from pgl import *

# 1a: create_histogram_array
def create_histogram_array(data: list[int]) -> list[int]:
    histogram = [0] * (max(data) + 1)  
    for value in data:
        histogram[value] += 1  
    return histogram

# 1b: print_histogram
def print_histogram(hist: list[int]) -> None:
    for index, value in enumerate(hist):
        print(f"{index}: {'*' * value}")  

# 1c: graph_histogram
def graph_histogram(hist: list[int], width: int, height: int) -> None:

    def my_rect(x, y, w, h, color):
        rect = GRect(x, y, w, h)
        rect.set_filled(True)
        rect.set_color(color)
        gw.add(rect)

    gw = GWindow(width, height)
    max_value = max(hist)  
    column_width = width / len(hist)  
    scale = height / max_value  

    for i, count in enumerate(hist):
        bar_height = count * scale  # Scale the height of the bar
        x = i * column_width
        y = height - bar_height  # Bars grow upwards from the bottom
        my_rect(x, y, column_width - 2, bar_height, 'red')  # Leave 2px gap between bars


PI_DIGITS = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 5, 8, 9, 7, 9]

# Call the functions
hist = create_histogram_array(PI_DIGITS)  
print(hist)  

print_histogram(hist)  

graph_histogram(hist, 400, 400)
