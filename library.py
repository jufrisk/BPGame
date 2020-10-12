# Currently temporary automated list to ease debugging!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
import sqlite3

import bp_db as db
import random
def new_player(players):
    #if len(players < 10):
        #players = list(range(12))
        #players = [str(i) for i in players]

    #while True:


        #if player == "stop":
            #break
        #players.append(player)

    playersmixed = random.sample(players, len(players))

    groupa = []
    groupb = []
    groupc = []
    allgroups = [groupa, groupb, groupc]
    counter = 0
    groupdivider = 0
    # divide players into groups, after x % 4 == 0 new group starts filling
    for player in playersmixed:

        if counter == 4:
            groupdivider += 1

            counter = 0
        counter += 1

        # add player to group
        allgroups[groupdivider].append(player)

    return allgroups


def groupgames(players):

    groupgamess = [
        players[0], players[1],
        players[2], players[3],
        players[0], players[2],
        players[1], players[3],
        players[3], players[0],
        players[1], players[2]
        ]
    return groupgamess

def readyforgame():
    players = db.printplayers()
    playersingroups = new_player(players)
    db.createstats(playersingroups)
    groupagames = groupgames(playersingroups[0])
    groupbgames = groupgames(playersingroups[1])
    groupcgames = groupgames(playersingroups[2])
    db.fillgames(groupagames, groupbgames, groupcgames)