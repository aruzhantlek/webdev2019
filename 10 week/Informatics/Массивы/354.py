from __future__ import print_function

n = int(input())

a = []
for i in range(0, n):
	a.append([])
	for j in range(0, n):
		if i+j == n - 1:
			a[i].append(1)
		elif i+j < n-1:
			a[i].append(0)
		else:
			a[i].append(2)


for i in range(0, n):
    for j in range(0, n):
        print(a[i][j], end =" ")
    print()