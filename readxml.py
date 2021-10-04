loop = int(input('loop = '))
step = 0
b = 0
s = 0
while step < loop:

    num = int(input('num = '))
    if num > b:
        if b > s:
            print(b)
        else:
            print(s)
        print(num)
    step += 1
    if num < b:
        print(s)
        print(b)
        continue
    s = b
    b = num
