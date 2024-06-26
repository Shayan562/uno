import random


class Deck:
    def __init__(self)->None:
        self.cards=self.generateDeck()


    def generateDeck(self) -> list:
        deck=[]
        for i in ['red','green','blue','yellow']:
            for j in range(10):#append regular cards ->2 of each
                deck.append(Card('numbered',i,str(j)))
                deck.append(Card('numbered',i,str(j)))

            for j in ['skip','reverse','draw']:#special cards
                deck.append(Card('special',i,j))
                deck.append(Card('special',i,j))

        for i in range(4):#wild cards
            deck.append(Card('wild','black','wild'))
            deck.append(Card('wild','black','draw'))

        #no need to shuffle as we will draw randomly
        return deck
    

    def draw(self,n)->list:
        #get n random cards from the deck
        cards=[random.choice(self.cards) for i in range(n)]
        return cards


class Card:
    def __init__(self,cType,color,value)->None:
        self.cType=cType
        self.color=color
        self.value=value
    
    
    def details(self):
        print(f"{self.cType} {self.color} {self.value}")


    def isValid(self, card)->bool:
        ''' Following the classic rules; the colors match or the card is numbered and the numbers match.
            Can't put one skip over another different colored skip.
            Any card can be placed on top of the wild card except for another wild card'''
        if(self.color=='black' and card.color!='black'):
            return True
        if(card.color==self.color):#colors match
            return True
        if(card.cType=='numbered' and card.value==self.value):
            return True
        return False
    

#temporary driver code for testing
if __name__=='__main__':
    game=Deck()
    print(len(game.cards))

    temp=Card('special','green','skip')
    temp.details()
    print('-----------------')
    
    for card in game.cards:
        card.details()
        print(f"{card.isValid(temp)}")