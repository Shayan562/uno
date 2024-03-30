import deck
import random

class Table:
    def __init__(self, players) -> None:
        self.players=players
        self.uno=dict
        self.deck=deck.Deck()
        self.deal()
        self.currentCard=[deck.Card('numbered',random.choice(['red','green','blue','yellow']),random.randint(0,9))]
        self.currentPlayer=0
        self.rev=False

    # def initPlayer(self, playerNames) -> list:
    #     players=[]
    #     for name in playerNames:
    #         cards=self.deck.draw(7)
    #         players.append(player.Player(name,cards))
    #     return players

    def deal(self) -> None:
        #will be done over the network for each player
        for player in self.players:
            cards=self.deck.draw(7)
            player.updateCards(cards)

    def draw(self,player,n)->None:
        cards=self.deck.draw(n)
        player.updateCards(cards)

    def nextPlayer(self)->None:
        if(self.rev):
            self.currentPlayer=(self.currentPlayer-1)%len(self.players)
        else:
            self.currentPlayer=(self.currentPlayer+1)%len(self.players)

    def nextMove(self)->None:
        #these are conditions for special cards
        if(self.currentCard[0].value=='skip'):
            self.nextPlayer()
        elif(self.currentCard[0].value=='rev'):
            self.rev=not(self.rev) 
        elif(self.currentCard[0].value=='draw' and self.currentCard[0].color!='black'):#Can place only a numbered card on top of wild cards not special cards
            self.draw(self.players[self.currentPlayer],2)
        #incase the second card is a wild draw 4
        elif(len(self.currentCard)>1 and self.currentCard[1].color=='black' and self.currentCard[1].value=='draw'):
            self.draw(self.players[self.currentPlayer],4)
        
        #we move onto the player move now
        #here we send the move to the correct player
        currTurn=self.players[self.currentPlayer]
        playersCard=currTurn.executeMove(self.currentCard[0],self.draw)

        # if():
            
            



# if __name__=='__main__':
#     game=Table()
#     print(game.currentCard.details())

