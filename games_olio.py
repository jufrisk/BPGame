from bp_db import printplayers
from library import new_player

class playerStats(object):
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.cupsfor = 0
        self.cupsagainst = 0
        self.cupdifference = self.cupsfor - self.cupsagainst
        self.gamestotal = 0
        self.won = 0
        self.lost = 0
        self.rank = self.cupsfor + self.cupdifference * 10000 + self.points * 100000000

    def updateStats(self, resultofgame):
        if resultofgame > 0:
            self.points = self.points + 3
            self.won = self.won + 1
            self.cupsfor = self.cupsfor + resultofgame

        else:
            self.cupsagainst = self.cupsagainst - resultofgame
            self.lost = self.lost + 1

        self.gamestotal = self.gamestotal + 1


    def getGroup(self):
        print(self.name, self.won, self.lost, self.cupdifference, self.points)

    def getRank(self):
        return self.rank

def game(gameplayer1, gameplayer2, resplayer1, resplayer2):

    if resplayer1 > resplayer2:
        results = (gameplayer1, resplayer1), (gameplayer2, -1*resplayer1)
    else:
        results = (gameplayer2, resplayer2), (gameplayer1, -1 * resplayer2)

    for i in results:
        name, cupdiff = i
        playerStats[name].updateStats(cupdiff)


def sortgroup(playerslist, groupaplayers):
    bestrank = -999999
    sortedlist = []
    #bestrank
    for player in playerslist:

        if bestrank < groupaplayers[player].getRank():
            bestrank = groupaplayers[player].getRank()
            bestplyr = player

    sortedlist.append(bestplyr)
    playerslist.remove(bestplyr)

    bestrank = -999999

    # 2nd Best rank
    for player in playerslist:
        if bestrank < groupaplayers[player].getRank():
            bestrank = groupaplayers[player].getRank()
            bestplyr = player

    sortedlist.append(bestplyr)
    playerslist.remove(bestplyr)
    bestrank = -999999999999999
    for player in playerslist:
        if bestrank < groupaplayers[player].getRank():
            bestrank = groupaplayers[player].getRank()
            bestplyr = player

    sortedlist.append(bestplyr)
    playerslist.remove(bestplyr)
    sortedlist.append(playerslist[0])
    return sortedlist


def groupgames(players):
    groupagames = [
        players[0], players[1],
        players[2], players[3],
        players[0], players[2],
        players[1], players[3],
        players[3], players[0],
        players[1], players[2]
        ]

    return groupagames

def setti(players):
    groupaplayers = {name: games.playerStats(name=name) for name in players}
    return groupaplayers





# # 1-2 3-4 1-3 2-4 4-1 2-3

# def main():
#
#
#     player1temp = input("Insert player1 for the game: ")
#     player2temp = input("Insert player2 for the game: ")
#     resultofgame = game(player1temp, player2temp)
#
#     for i in resultofgame:
#         name, cupdiff = i
#         groupaplayers[name].updateStats(cupdiff)
#
#     #update group standings
#     updatedlist = sortgroup(groupA)
#
#     for name in updatedlist:
#         groupaplayers[name].getGroup()
#
# main()
