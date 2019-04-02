S=set([int(x) for x in raw_input().split()])
n=int(raw_input());stop=0
while n>0 and stop==0:
    n-=1
    B=set([int(x) for x in raw_input().split()])
    if not(S.issuperset(B) and len(S-B)>0): stop=1
if stop==1: print "False"
else: print "True"