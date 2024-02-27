import pathlib
import json
def Check_key(data,check_str):
    if check_str in data.keys():
        return True
    else:
        return False
def Get_value(id):
    for i in data1["values"]:
        if i["id"] == id:
            return i["value"]
def Get_structs(my_data):
    if "values" in my_data.keys():
        return my_data["values"]
def Handle_struct(my_struct):
    if Check_key(my_struct,"value") == True:
        my_struct["value"] = Get_value(my_struct["id"])
    if Get_structs(my_struct) != None:
        for mini_str in Get_structs(my_struct):
            Handle_struct(mini_str)
def write_json(new_data, filename):
    with open(filename,'r+') as file3:
        file3.truncate(0)
        json.dump(data2, file3, indent = 4)
print("Введите путь к файлу 1")
file1 = pathlib.Path(input())
f1 = open(file1)
data1 = json.load(f1)
print("Введите путь к файлу 2")
file2 = pathlib.Path(input())
f2 = open(file2)
print("Введите путь к файлу 3")
file3 = pathlib.Path(input())
data2 = json.load(f2)
for i in data2["tests"]:
    Handle_struct(i)
write_json(data2,file3)
f1.close()
f2.close()

