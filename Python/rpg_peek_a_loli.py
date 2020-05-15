def hm():
 home = input ('''
    Peek a loli 
    1.Play
    2.About
    ''')

 if home == '1':
    print ("")
    print ("the game starts now!")    
    print ("")
    
 elif home == '2':
    print ("you have all the reasons to believe that")
    print ("your friend hides a folder with anime girls inside,")
    print ("and you gonna check this.")
    back = input ('''
      press any key to menu
       ''')
    
    if back == '1':
        hm()
        
    else:
        hm()
hm()

print ("you are in front of your friend's computer.")
print ("the computer is on a desk.")
    
def desk():
  look = input ('''
   look: 
   1.computer
   2.desk
   ''')
    
  if look == '2': 
    print ("there's only a flyer about Pablo Picasso:")
    print ("")
    print ("'Did you know that Picasso has a really large name?")
    print ("'let's see:'")
    print ("")
    print ("'P.ablo D.iego J.osé F.rancisco de P.aula J.uan'")
    print ("'N.epumoceno M.aria de los R.emédios C.ipriano de la'")
    print ("'S.anta T.rindade C.líto R.uis e P.icasso.'")
    print ("")
    desk()
    
  elif look == '1':
    print ("you turn on the computer. it needs a password:")
    
    def loop():
     pw = input ('''
      password:
          
      (press 1 to go back)
      ''')
      
     if pw == '1':
      desk()
  
     elif pw == 'pdjfpjnmrcstcrp':
      print ("correct password. welcome, senpai")
      print ("")
      
     elif pw == 'PDJFPJNMRCSTCRP':
      print ("correct password. welcome, senpai")
 
     else:
      print ("wrong password. try again")
      loop()
    loop()
   
  else:
   desk()
desk()

print ("")
print ("you access the computer")
print ("")
print ("SCANDALOUS")
print ("")
print ("⠄⠄⠄⢰⣧⣼⣯⠄⣸⣠⣶⣶⣦⣾⠄⠄⠄⠄⡀⠄⢀⣿⣿⠄⠄⠄⢸⡇⠄⠄")
print ("⠄⠄⠄⣾⣿⠿⠿⠶⠿⢿⣿⣿⣿⣿⣦⣤⣄⢀⡅⢠⣾⣛⡉⠄⠄⠄⠸⢀⣿⠄")
print ("⠄⠄⢀⡋⣡⣴⣶⣶⡀⠄⠄⠙⢿⣿⣿⣿⣿⣿⣴⣿⣿⣿⢃⣤⣄⣀⣥⣿⣿⠄")
print ("⠄⠄⢸⣇⠻⣿⣿⣿⣧⣀⢀⣠⡌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⣿⣿⣿⠄")
print ("⠄⢀⢸⣿⣷⣤⣤⣤⣬⣙⣛⢿⣿⣿⣿⣿⣿⣿⡿⣿⣿⡍⠄⠄⢀⣤⣄⠉⠋⣰")
print ("⠄⣼⣖⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⢇⣿⣿⡷⠶⠶⢿⣿⣿⠇⢀⣤")
print ("⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣷⣶⣥⣴⣿⡗")
print ("⢀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠄")
print ("⢸⣿⣦⣌⣛⣻⣿⣿⣧⠙⠛⠛⡭⠅⠒⠦⠭⣭⡻⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠄")
print ("⠘⣿⣿⣿⣿⣿⣿⣿⣿⡆⠄⠄⠄⠄⠄⠄⠄⠄⠹⠈⢋⣽⣿⣿⣿⣿⣵⣾⠃⠄")
print ("⠄⠘⣿⣿⣿⣿⣿⣿⣿⣿⠄⣴⣿⣶⣄⠄⣴⣶⠄⢀⣾⣿⣿⣿⣿⣿⣿⠃⠄⠄")
print ("⠄⠄⠈⠻⣿⣿⣿⣿⣿⣿⡄⢻⣿⣿⣿⠄⣿⣿⡀⣾⣿⣿⣿⣿⣛⠛⠁⠄⠄⠄")
print ("⠄⠄⠄⠄⠈⠛⢿⣿⣿⣿⠁⠞⢿⣿⣿⡄⢿⣿⡇⣸⣿⣿⠿⠛⠁⠄⠄⠄⠄⠄")
print ("⠄⠄⠄⠄⠄⠄⠄⠉⠻⣿⣿⣾⣦⡙⠻⣷⣾⣿⠃⠿⠋⠁⠄⠄⠄⠄⠄⢀⣠⣴")
print ("⣿⣿⣿⣶⣶⣮⣥⣒⠲⢮⣝⡿⣿⣿⡆⣿⡿⠃⠄⠄⠄⠄⠄⠄⠄⣠⣴⣿⣿⣿")
print ("")
print ("that's the end")
