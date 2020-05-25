month={1:"Jan",2:"Feb",3:"Mar",4:"Apr",5:"May",6:"Jun",7:"Jul",8:"Aug",9:"Sep",10:"Oct",11:"Nov",12:"Dec"}
n=input()
if("/" in n):
 date=n.split('/')
 (date[0],date[1])=(date[1],date[0])
 print(date[0]+'/'+date[1]+'/'+date[2])
else:
 for i in range(1,13):
  if(month[i] in n):
   date=n.split(' ')
   mon=date[1].split(',')
   print(mon[0]+'/'+str(i)+'/'+date[2])
