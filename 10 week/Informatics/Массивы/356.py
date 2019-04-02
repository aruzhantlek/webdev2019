# n = int(input())
# m = int(input())
a = []
s = input().split()
n = int(s[0])
m = int(s[1])
for i in range(0, n):
    c = []
    for j in input().split():
        c.append(int(j))
    a.append(c)
b = []
for i in range(0, n):
    b.append(0)
    for j in range(0, m):
        b[i] = b[i] + a[i][j]
msum = int()
num = int()
msum = b[0]
num = 0
for i in range(1, n) :
     if msum < b[i] :
        msum = b[i]
        num = i
print(msum)
print(num)