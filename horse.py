a = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}
res = input()
parse = [x for x in res]
# print(parse)
try:
    x1 = a.get(parse[0])
    y1 = int(parse[1])
    x2 = a.get(parse[3])
    y2 = int(parse[4])
    if (abs(x2 - x1) == 2 and abs(y2 - y1) == 1) or (abs(x2 - x1) == 1 and abs(y2 - y1) == 2):
        print('YES')
    else:
        print("NO")
except:
    print('ERROR')

    
