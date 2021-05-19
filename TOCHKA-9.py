n = input().split()
x1 = float(n[0])
y1 = float(n[1])
if (x1**2 + y1**2 <= 1) or ((x1**2 + y1**2 >= 1) and y1 <= 1 and x1 <= 1):
    print('YES')
else:
    print('NO')
