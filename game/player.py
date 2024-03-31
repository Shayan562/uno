# import deck
from deck import Card

class Player:
    sid=0
    def __init__(self,name) -> None:
        Player.sid+=1 
        self.id=Player.sid
        self.name=name
        self.numCards=0
        self.hand=[]



    def details(self):
        print(f"{self.id} {self.name}: {self.numCards}")
    
    def printHand(self):
        for card in self.hand:
            card.details()

    def updateCards(self,cards) -> None:
        self.hand.extend(cards)
        self.numCards+=len(cards)

    def drawCard(self) -> None:
        pass

    def executeMove(self,currCard,drawCard):
        print(f"{self.name}'s move")
        self.printHand()
        # move=int(input("Enter your card(index): "))
        move=-1
        #add condition for uno
        while(True):
            while(move<0 and move>self.numCards-1):
                move=int(input("Enter your card(index) or -1 to draw another: "))
                if(move==-1):
                    # drawnCard=drawCard(self,1)
                    self.updateCards(drawCard(self,1))
                    #draw card
            
            #cant place only wild card. add condition
            #option to press uno(calls function)
            card=self.hand[move]
            if(currCard.isValid(card)):
                self.hand.pop(move)
                break
        return card 