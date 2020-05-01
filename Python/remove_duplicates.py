inp = input('Enter The String : ')
rc=[]
for i in inp:
  if i not in rc:
    rc.append(i)
rc = "".join(rc)
print(rc)
