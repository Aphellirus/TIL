p = input()

sc=['!', '@', '#', '$', '%', '&', '*']
num=['1','2','3','4','5','6','7','8','9','0']
c=0
n=0
ls = []
ls= ls + list(p)

for i in range(len(p)):
    if ls[i] in sc:
        c=c+1
    if ls[i] in num:
        n=n+1

if len(p)<7:
    print("Weak")
elif len(p)>=7 and n>1 and c>1:
    print("Strong")
else:
    print("Weak")
