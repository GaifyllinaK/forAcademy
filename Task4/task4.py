import pathlib

print("Введите путь к файлу 1")
file1 = pathlib.Path(input())
with open(file1) as f:
    data = f.read().split("\n")
nums = list(map(int, data))
median = sum(nums)/len(nums)
moves = sum(abs(num-median) for num in nums)
print(int(moves))

