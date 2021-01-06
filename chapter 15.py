class Card():
    values=[None,None,"2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    suits=["spades","hearts","diamonds","clubs"]
#### tHIS iS a change
    def __init__(self,v,s):
        self.value=v
        self.suit=s

    def __lt__(self,c2):
        if self.value < c2.value:
            return True
        if self.value==c2.value:
            if self.suit < c2.suit:
                return True
        return False
    def __gt__(self,c2):
        if self.value> c2.value:
            return True
        if self.value==c2.value:
            if self.suit > c2.suit:
                return True
        return False
    def __repr__(self):
        v= self.values[self.value] + " of " + self.suits[self.suit]
        return v

Card1=Card(14,2)
Card2=Card(13,3)
print(Card1 > Card2)
print(Card1)   

from random import shuffle 
class Deck:
    def __init__(self):
        self.cards=[]
        for i in range (2,15):
            for j in range (4):
                self.cards.append(Card(i,j))
        shuffle(self.cards)
    def tirage(self):
        return self.cards.pop()

deck=Deck()
deck.cards[3]
for card in deck.cards:
    print (card)

class Player:
    def __init__(self,name):
        self.wins=0
        self.card=None
        self.name=name

class Game:
    def __init__(self):
        self.deck=Deck()
        n1=input('name p1: ')
        n2=input('name p2: ')
        self.p1=Player(n1)
        self.p2=Player(n2)

    def wins(self, winner):
        print("the winner of this round is {}".format(winner))
    
    def draw(self,p1n,p1c,p2n,p2c):
        print(" {} has card: {}, {} has card: {}".format(p1n,p1c,p2n,p2c))
    
    def winner(self,p1,p2):
        if p1.wins> p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        else:
            return " nobody ! it is a TIE !!!"

    def play_game(self):
        cards=self.deck.cards
        print("let's play war!")
        while len(cards)>1:
            resp=input(" wanna quit the game ? y/n")
            if resp=="y":
                break
            p1c=self.deck.tirage()
            p2c=self.deck.tirage()
            p1n=self.p1.name
            p2n=self.p2.name
            self.draw(p1n, p1c,p2n,p2c)
            if p1c>p2c:
                self.p1.wins +=1
                self.wins(self.p1.name)
            else:
                self.p2.wins +=1
                self.wins(self.p2.name)
        winnerrrrr=self.winner(self.p1,self.p2)
        print(" the winner is: {}".format(winnerrrrr))    


    
game=Game()
game.play_game()
