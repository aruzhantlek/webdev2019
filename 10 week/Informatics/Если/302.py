a = int(input())
b = int(input())
c = int(input())
if a + b > c and b + c > a and a + c > b :
	if c**2 == a**2 + b**2 :
		print("right")
	elif c**2 < a**2 + b**2 :
		print("acute")
	else : 
		print("obtuse")
else :
	print("impossible")