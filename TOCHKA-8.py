n = input().split()
x1 = float(n[0])
y1 = float(n[1])
if (y1 <= 1 and y1 >= x1 - 1 and 1 >= x1**2 + y1**2) or (x1 >= 0 and 1 < x1**2 + y1**2):
    print('YES')
else:
    print('NO')
