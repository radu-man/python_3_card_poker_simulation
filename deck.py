from random import randint

#deck with all 52 cards from where we will pick random cards to simulate the shuffle
deck = [
'Ah','2h','3h','4h','5h','6h','7h','8h','9h','Th','Jh','Qh','Kh',
'Ad','2d','3d','4d','5d','6d','7d','8d','9d','Td','Jd','Qd','Kd',
'Ac','2c','3c','4c','5c','6c','7c','8c','9c','Tc','Jc','Qc','Kc',
'As','2s','3s','4s','5s','6s','7s','8s','9s','Ts','Js','Qs','Ks']

#will pick a random card from the deck and return it
workingDeck = []

def newdeck():
    for i in deck:
        workingDeck.append(i)

newdeck()

def card():
    x = workingDeck[randint(0, len(workingDeck) - 1)]
    workingDeck.remove(x)
    return x

def cardsInDeck():
    return len(deck)

def getNames(n):
    names = ['Player1','Player2','Player3','Player4','Player5','Player6','Player7']
    name = names.pop(n)
    return name
