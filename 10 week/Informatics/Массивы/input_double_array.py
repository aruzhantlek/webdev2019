from __future__ import print_function

n = int(input())
a = []

for i in range(0, n):
    c = []
    for j in range(0, m):
        k = int(input())
        c.append(k)
    a.append(c)

print()


for i in range(0, n):
    for j in range(0, n):
        print(a[i][j], end =" ")
    print()