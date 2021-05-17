#Program to calculate 2 to the power of x, where x can be +ve, -ve or zero.

#Using Left Shift Operator


if __name__=="__main__":
  
  P,Res=int(input()),1
  
  if(P>=0):
      
    Res = Res << P
      
  if(P<0):
      
    Res = Res << abs(P)
      
    Res = 1 / Res


  print(f"2 ^ {P} =",Res)
