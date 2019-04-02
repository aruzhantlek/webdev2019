n = int(input())

# s = raw_input()
# a = []
# for x in s.split():
# 	a.append(int(x))

a = [int(x) for x in raw_input().split()]

for i in range(0, n):
	if a[i] % 2 == 0:
		print(a[i])
