s0=str(input())
s = s0.translate ({ord(c): " " for c in "!@#$%^&*()'[]{};:,./<>?\|`~-=_+"})
s = ''.join(s.split())
s = s.lower()

d = {}
n=0

for i in s: 
    if i in d: 
        d[i]+=1
    else:
        d[i]=1
    n+=1

print("Sentence :",s0,"\n") 

for a in sorted(d):
    print(a,":",str(round(d[a]/n,3)*100),end="%\n")


