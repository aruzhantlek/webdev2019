a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = c - a
f = d - b
if c >= a and d >= b :
	print(e)
	print(f)
elif d < b :
	print(c-a-1)
	print(100+d-b)
