import re

m = re.finditer(r'[^AEIOUaeiou +\-]([AEIOUaeiou]{2,})(?=[^AEIOUaeiou +\-])', input().strip())

found = 0
for mm in m:
    print(mm.group(1))
    found = 1

if found == 0:
    print('-1')