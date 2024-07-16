a = [list(map(int, input().split())) for _ in range(10)]
x = 1
y = 1

while True :
    if a[x][y] == 2 :
        a[x][y] = 9
        break
    if a[x+1][y] == 1 and a[x][y+1] == 1 :
        a[x][y] = 9
        break
    if a[x][y+1] != 1 :
        a[x][y] = 9
        y += 1
    elif a[x][1+y] == 1 :
        a[x][y] = 9
        x += 1
    else : 
        break

for i in range(10) :
    for j in range(10) :
        print(a[i][j], end=' ')
    print('')
