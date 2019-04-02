from __future__ import print_function

n = 4
a = []
for i in range(0, n):
    row = []
    for j in range(0, n):
        row.append(0)
    a.append(row)
for i in range(0, n):
    for j in range(0, n):
        if i + j == n-1:
            a[i][j] = 1
        if i + j > n-1:
            a[i][j] = 2
for i in range(0, n):
    for j in range(0, n):
        print(a[i][j], end =" ")
    print()