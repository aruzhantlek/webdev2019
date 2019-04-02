import re

S = input().strip()
k = input().strip()

m = re.finditer(r'(?='+k+')', S)

found = 0
if m:
    for mm in m:
        print('(%i, %i)' % (mm.start(), mm.start()+len(k)-1))
        found = 1
if found == 0:
    print('(-1, -1)')
