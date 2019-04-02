n = int(input())
a = []
ok = True
for i in range(0, n):
	b = []
	for j in input().split() :
		b.append(int(j))
	a.append(b)
for i in range(0, n):
	for j in range(0, n):
		if a[i][j] != a[j][i]:
			ok = False
			break
		else :
			ok = True
if ok == True :
	print("yes")
else :
	print("no")