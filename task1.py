data = input().split()
len = int(data[0])
step = int(data[1])
index = 0
while True:
    print(index+1)
    index = (index + step-1) % len
    if index == 0: break
   