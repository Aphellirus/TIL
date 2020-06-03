k=0
for i in range(8):
    for j in range(8):
        if k==0:
            print("⬜️",end="")
        if k==1:
            print("⬛️",end="")
        b=k
        k=0 if b==1 else 1   
    b=k
    k=0 if b==1 else 1
    print("",end="\n")
        
