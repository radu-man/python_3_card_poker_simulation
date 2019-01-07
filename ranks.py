

def flu(a,b,c):
    if a[1] == b[1] == c[1]:
        return True
    else:
        return False

d = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')

strcombo = [['A', '2', '3'], ['A', '3', '2'], ['2', 'A', '3'], ('2', '3', 'A'), ('3', 'A', '2'), ('3', '2', 'A'),\
           ['2', '3', '4'], ['2', '4', '3'], ['3', '2', '4'], ('3', '4', '2'), ('4', '2', '3'), ('4', '3', '2'),\
           ['3', '4', '5'], ['3', '5', '4'], ['4', '3', '5'], ('4', '5', '3'), ('5', '3', '4'), ('5', '4', '3'),\
           ['4', '5', '6'], ['4', '6', '5'], ['5', '4', '6'], ('5', '6', '4'), ('6', '4', '5'), ('6', '5', '4'),\
           ['5', '6', '7'], ['5', '7', '6'], ['6', '5', '7'], ('6', '7', '5'), ('7', '5', '6'), ('7', '6', '5'),\
           ['6', '7', '8'], ['6', '8', '7'], ['7', '6', '8'], ('7', '8', '6'), ('8', '6', '7'), ('8', '7', '6'),\
           ['7', '8', '9'], ['7', '9', '8'], ['8', '7', '9'], ('8', '9', '7'), ('9', '7', '8'), ('9', '8', '7'),\
           ['8', '9', 'T'], ['8', 'T', '9'], ['9', '8', 'T'], ('9', 'T', '8'), ('T', '8', '9'), ('T', '9', '8'),\
           ['9', 'T', 'J'], ['9', 'J', 'T'], ['T', '9', 'J'], ('T', 'J', '9'), ('J', '9', 'T'), ('J', 'T', '9'),\
           ['T', 'J', 'Q'], ['T', 'Q', 'J'], ['J', 'T', 'Q'], ('J', 'Q', 'T'), ('Q', 'T', 'J'), ('Q', 'J', 'T'),\
           ['J', 'Q', 'K'], ['J', 'K', 'Q'], ['Q', 'J', 'K'], ('Q', 'K', 'J'), ('K', 'J', 'Q'), ('K', 'Q', 'J'),\
           ['Q', 'K', 'A'], ['Q', 'A', 'K'], ['K', 'Q', 'A'], ('K', 'A', 'Q'), ('A', 'Q', 'K'), ('A', 'K', 'Q')]



def str(a,b,c):

    combo = [a[0],b[0],c[0]]

    if combo in strcombo:
        return True
    else:
        return False

def check2(player):
    a = player.c1
    b = player.c2
    c = player.c3

    # Straight flush

    if str(a,b,c) and flu(a,b,c):
        player.bank += 40
        player.sf += 1
        return player.bank

    #3 of a kind
    elif a[0] == b[0] == c[0]:
        player.bank += 30
        player.three += 1
        return player.bank

    #pair
    elif a[0] == b[0]:
        player.bank += 1
        player.pair += 1
        return player.bank

    elif a[0] == c[0]:
        player.bank += 1
        player.pair += 1
        return player.bank

    elif b[0] == c[0]:
        player.bank += 1
        player.pair += 1
        return player.bank

    #straight
    elif str(a,b,c):
        player.bank += 5
        player.straight += 1
        return player.bank

    #flush
    elif flu(a,b,c):
        player.bank += 3
        player.flush += 1
        return player.bank

    else:
        player.bank -= 3
        return player.bank
