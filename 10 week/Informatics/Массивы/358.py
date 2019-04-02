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
for i in range(0, n):
	for j in range(0, m):
		if a[i][j] > maxn:
			maxn = a[i][j]
			numr = i 

maxes = []
maxes.append(numr)
for i in range(0, n):
	for j in range(0, m):
		if a[i][j] == maxn and i != numr:
			maxes.append(i)

b = []
maxsum = 0
for i in range(0, len(maxes)):
	b.append(0)
	for j in range(0, m):
		b[i] = b[i] + a[i][j]
	if b[i] > maxsum:
		maxsum = b[i]
		numr = i

print(numr)




