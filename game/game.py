import table
import player

if __name__=='__main__':

    players=[player.Player('Shayan'),player.Player('Rehan'),player.Player('Azaan')]
    for i in players:
        i.details() 
    table.Table(players)
    for i in players:
        i.details()
        i.printHand()
