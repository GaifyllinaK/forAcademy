import math 
import pathlib
print("Введите путь к файлу 1")
file1 = pathlib.Path(input())
with open(file1, 'r', encoding='utf-8') as f:
    data = f.read().split()
print("Введите путь к файлу 2")
file2 = pathlib.Path(input())
with open(file2, 'r', encoding='utf-8') as f:
    data2 = f.readlines()    
x_cent = float(data[0])
y_cent = float(data[1])
r_circle = float(data[2])

for i in data2:
    i = i.split()
    x_point = float(i[0])
    y_point = float(i[1])
    hypotenuse = math.sqrt((x_point-x_cent) ** 2 + (y_point-y_cent) ** 2)
    if hypotenuse < r_circle:
        print("1")
    elif hypotenuse > r_circle:
        print("2")
    else: print("0")
 
