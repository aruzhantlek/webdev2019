from __future__ import print_function

a = []
n, m = [int(x) for x in input().split()]
for i in range(0, n):
	b = []
	for j in input().split():
		b.append(int(j))
	a.append(b)
maxn = a[0][0]
numr = 0
numc = 0
for i in range(0, n):
	for j in range(0, m):
		if a[i][j] > maxn :
			maxn = a[i][j]
			numr = i
			numc = j
print(maxn)
print(numr, end=" ")
print(numc)





