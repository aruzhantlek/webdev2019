x = int(input())
cnt = 1
k = 0
for i in range(x):
	print(cnt)
	k+=1
	if cnt == k:
		cnt+=1
		k=0

