import random
import time

your_money=1000
enemy_money=1000
bankrupt=False

print("Welcome to Mobile Lucky 9!")
print()
time.sleep(1.6)
print("Who has the highest card will WIN!")
time.sleep(2)
print()
print("You only have $1000 to play")
time.sleep(.9)
print("if you lose all of it, GAME OVER!")
print()
time.sleep(1)
name=input("Enter your name gambler: ")
print()
print(name + ", are you 18+?")
warning=input("Yes or No: ").lower()
print()

if warning =="yes":
  print("Get Ready!")
  time.sleep(1.3)
elif warning=="no":
  print("Ask your parent before you play this game!")
  time.sleep(.9)
  print("By the way, enjoy the game!")
  time.sleep(1.3)
else:
  print("invalid answer, by the way enjoy the game!")
  time.sleep(1.3)
print() 
while your_money or enemy_money >= 0 and not(bankrupt):
  if your_money or enemy_money>0:
    print("wait for your card ...")
    print()
    time.sleep(1.2)
    bet=input("Enter your bet: ")
    time.sleep(1)
    print()
    bet=int(bet)
    cards=[1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9]
    hand1=random.sample(cards, k=1)
    hand2=random.sample(cards, k=1)
    total_cards=hand1+hand2
    time.sleep(1)
    print(total_cards)
    time.sleep(1.5)
    your_card=total_cards[0]
    your_card2=total_cards[1]
    your_hand=your_card + your_card2 
  
    if your_hand==10:
      your_hand=0
    elif your_hand>10:
      your_hand-=10
    print("Your card: " + str(your_hand))
    print()
    time.sleep(1.5)

    computer_deck=[1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9]
    hand3=random.sample(computer_deck, k=1)
    print()
    time.sleep(1.6)
    hand4=random.sample(computer_deck, k=1)
    computer_cards=hand3+hand4
    print(computer_cards)
    computer_card=computer_cards[0]
    computer_card2=computer_cards[1]
    computer_hand=computer_card + computer_card2
    if computer_hand==10:
       computer_hand=0
    elif computer_hand>10:
         computer_hand-=10
    print("computer card: " + str(computer_hand))

    if computer_hand>your_hand and not(bankrupt):
      time.sleep(2)
      print()
      print("Computer win!")
      your_money=your_money-int(bet)
      enemy_money=enemy_money+int(bet)
      time.sleep(2)
  
    elif computer_hand<your_hand and not(bankrupt):
      time.sleep(2)
      print()
      print("You win!")
      enemy_money=enemy_money-int(bet)
      your_money+=int(bet)
      time.sleep(2)
      print()
    
    elif computer_hand==your_hand and not (bankrupt):
      time.sleep(2)
      print()
      print("It is draw!")
      time.sleep(2)
  
    print()
    print("Your remaining money: $" + str(your_money))
    print("Enemy remaining money: $" + str(enemy_money))
    print()
    time.sleep(1.5)
    print("Next Round!")
    time.sleep(2.5)
    
  else:
    bankrupt=True
    
if bankrupt:
  if your_money>enemy_money:
    print("You win!")
elif bankrupt:
  if your_money<enemy_money:
    print("You Lose!")
    
    
    
