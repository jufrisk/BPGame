import random
from PyQt5 import QtCore, QtGui, QtWidgets
from thisis2 import Ui_Dialog
from startgame import Ui_MainWindow
from library import new_player
import groups
from library import groupgames
from library import readyforgame
import games_olio as games
import Elimination as elim
import bp_db as db
import sys
#from startgame import frontti
from startgame import Ui_MainWindow


def main():


    db.createdb()

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()



    #groupgamesssss = [groupagames, groupbgames, groupcgames]
    #groupA = playersingroups[0]
    #groupaplayers = {name: games.playerStats(name=name) for name in groupA}
    #groupB = playersingroups[1]
    #groupbplayers = {name: games.playerStats(name=name) for name in groupB}
    #groupC = playersingroups[2]
    #groupcplayers = {name: games.playerStats(name=name) for name in groupC}




    #db.createstats(groupA, groupB, groupC)



         #   for i in resultofgame:
           #     name, cupdiff = i
          #      groupaplayers[name].updateStats(cupdiff)

            # update group standings
          #  groupA = games.sortgroup(groupA, groupaplayers)
           # for name in groupA:
           #    groupaplayers[name].getGroup()





   # toElims = elim.best23rd(groupA[2], groupB[2], groupC[2], groupaplayers, groupbplayers, groupcplayers)
   # elim.whoisatelim(groupA[0], groupB[0], groupC[0], groupA[1], groupB[1], groupC[1], toElims[0], toElims[1])

main()

















