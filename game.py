#game rock paper scissors
from getpass import getpass 
import random
def game(player1,player2):

    if player1 == player2:
      return None
    elif player1== 'p':
        if player2 == 'r':
            return True
        elif player2 == 's':
                return False
    elif player1== 's':
        if player2 == 'p':
            return True
    
        elif player2 == 'r':
                return False                
    elif player1== 'r':
        if player2 == 'p':
            return True
        elif player2 == 'S':
                return False   
player1=getpass(str("player1 turn:rock(r) paper(p) or scissors(s):\n"))

player2=getpass(str("player2 turn: rock(r) paper(p) or scissors(s):\n"))
a=game(player1,player2)
if a== None:
    print("The game is tie!")
elif a:
     print("Player1 WIN!")
else:
    print("Player2 WIN!")   