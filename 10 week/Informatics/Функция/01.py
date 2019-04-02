importh math

def myabs(x):
	y = x
	if x < 0:
		y = x * -1
	return y

def circle_area(r)
	pi = 3.14
	y = pi * r * r
	return y

def distance(x1, y1, x2, y2):
	d = (x1-x2)**2 + (y1-y2)**2
	return math.sqrt(d)

d = distance(0, 0, 1, 1)
d = distance(x1=0, x2=1, y1=0, y2=0)
print(d)