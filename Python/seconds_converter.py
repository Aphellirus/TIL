a=int(input("Enter value in seconds : "))
mtemp=0
h=int (a/3600)
mtemp=a-(h*3600)
m=int(mtemp/60)
s=mtemp-(m*60)
d=int(h/24)
h=h-(d*24)
print(d,"Day's",h,"Hours",m,"Minuts",s,"Seconds")
