
import time
print("This is a birthday finder, based on an algorithm")  
time.sleep(1.5)         
print("Remember to press the equal to button after each operation.")
time.sleep(1.5)
print("Take your Birth Month")
time.sleep(1.0)
print("Multiply by 2")
time.sleep(1.0)
print("Add 5")
time.sleep(1.0)
print("Multiply by 5")
time.sleep(1.5)
print("Multiply by 10")
time.sleep(1.0)
print("Add your Birth Date")
time.sleep(1.0)
condition=True
BMD=int(input("Enter the Number:"))
print("Using advanced algorithm...")
time.sleep(3.0)
changed=BMD-250
BM=int((changed-(changed%100))/100)
BD=changed%100
MN={
    1:"January",
    2:"February",
    3:"March",
    4:"April",
    5:"May",
    6:"June",
    7:"July",
    8:"August",
    9:"September",
    10:"October",
    11:"November",
    12:"December"
}
MD={
    1:31,
    2:29,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31
}
if BM in MN and BD<=MD.get(BM) and BD!=0:
    BMN=MN.get(BM)
else:
    condition=False
if condition==True:
    print("\nYou were born on "+str(BD)+" "+str(BMN))
else:
    print("\nInvalid Number")
