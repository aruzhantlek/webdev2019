a = int(input())
b = int(input())
if b == 0 :
	print("INF")
elif a == 0 :
	print("NO")
elif (b % a) == 0 :
	print(int(-b/a))
else:
	print("NO")