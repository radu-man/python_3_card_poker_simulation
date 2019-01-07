from deck import card,getNames,workingDeck,newdeck
from ranks import check2

names = []
class NewPlayer:

    def __init__(self,name,card1,card2,card3,strfl = 0,three = 0,straight = 0,flush = 0,pair = 0,bankroll = 5000):
        self.name = name
        self.c1 = card1
        self.c2 = card2
        self.c3 = card3
        self.bank = bankroll
        self.sf = strfl
        self.three = three
        self.straight = straight
        self.flush = flush
        self.pair = pair
        names.append(self)

    def newcards(self):
        self.c1 = card()
        self.c2 = card()
        self.c3 = card()


howManyPlayers = int(input('How many players:'))
howManyHands = int(input('How many hands to play:'))



for x in range(howManyPlayers):
    x = NewPlayer(getNames(x),card(),card(),card())
    newdeck()

for h in range(howManyHands):

    howManyHands -= 1
    workingDeck.clear()
    newdeck()

    for i in names:
        i.newcards()

    for name in names:
        check2(name)


for i in names:
    print('{} has: {},{},{} and a bankroll of {}. He had {} Straight Flushes, {} Three of a Kind, {} Straights, {} Flushes and {} Pairs'.format(i.name,i.c1,i.c2,i.c3,i.bank,i.sf,i.three,i.straight,i.flush,i.pair))

