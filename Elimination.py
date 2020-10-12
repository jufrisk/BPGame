import games_olio as games

class Elim_game(object):
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def getResult(self):
        winner = input("Who won")
        if self.player1 == winner:
            return f'{self.player1}'
        elif self.player2 == winner:
            return f'{self.player2}'


def whoisatelim(awinner, bwinner, cwinner, arunnerup, brunnerup, crunnerup, firstthird, secondthird):
    quarter1 = Elim_game(awinner, secondthird)

    quarter2 = Elim_game(bwinner, firstthird)
    quarter3 = Elim_game(arunnerup, cwinner)
    quarter4 = Elim_game(brunnerup, crunnerup)

    print("Jatkopelit:")
    print(awinner, "vs", secondthird)
    print(bwinner, "vs", firstthird)
    print(arunnerup, "vs", cwinner)
    print(brunnerup, "vs", crunnerup)

    semi1 = Elim_game(quarter1.getResult(), quarter2.getResult())
    semi2 = Elim_game(quarter3.getResult(), quarter4.getResult())

    final = Elim_game(semi1.getResult(), semi2.getResult())

    print("WINNER: ", final.getResult())

def best23rd(athird, bthird, cthird, groupaplayers, groupbplayers, groupcplayers):
    arank = groupaplayers[athird].getRank()
    brank = groupbplayers[bthird].getRank()
    crank = groupcplayers[cthird].getRank()

    atuple = (arank, athird)
    btuple = (brank, bthird)
    ctuple = (crank, cthird)
    thirdlist = [atuple, btuple, ctuple]
    returnlist = [athird, bthird, cthird]
    iter = 0
    ranktobeat = 0
    for player in thirdlist:
        rank, name = player
        if iter == 0:
            worst_player = name
            ranktobeat = rank
            iter =+ 1
            continue
        if rank < ranktobeat:
            worst_player = name
            ranktobeat = rank


    print(worst_player, "didn't qualify")
    returnlist.remove(worst_player)
    return returnlist


