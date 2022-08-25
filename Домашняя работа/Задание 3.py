x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if x2-x1==2 and abs(y2-y1)==1:
    print('YES')
elif x1-x2==2 and abs(y2-y1)==1:
    print('YES')
elif y1-y2==2 and abs(x2-x1)==1:
    print('YES')
elif y2-y1==2 and abs(x2-x1)==1:
    print('YES')
else:
    print('NO')
