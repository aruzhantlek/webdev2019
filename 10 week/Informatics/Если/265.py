k = int(input())
m = int(input())
n = int(input())

if n == 0 or k==0:
	print(0)
elif n % k == 0:
	print(2*m*int(n/k))
else:
	print(2*m*int(n/k) + 2*m)


if n <= k:
	print(2*m)
else:
	if (2*n) % k == 0:
		print(int(2*n/k)*m)
	else:
		print((int(2*n/k)+1)*m)