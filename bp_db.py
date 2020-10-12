import library as lib
import groups
import sqlite3
conn = sqlite3.connect("bptournament.db")

c = conn.cursor()
def createdb():
    c.execute('''DROP TABLE groupgames''')
    c.execute('''DROP TABLE player_stats''')
    c.execute('''DROP TABLE tournament''')
    c.execute('''DROP TABLE advancers''')

    c.execute('''CREATE TABLE IF NOT EXISTS tournament
        (playerName TEXT)''')


    c.execute('''CREATE TABLE IF NOT EXISTS player_stats
        (playerName varchar2(15), player_points INT, player_wins INT, player_losses INT, player_cupdifference INT,
        player_cupsfor INT, player_cupsagainst INT, player_rank INT, groupchar CHAR(1),
        PRIMARY KEY (playerName),
        FOREIGN KEY (playerName) REFERENCES tournament(playerName));''')

    c.execute('''CREATE TABLE IF NOT EXISTS groupgames
        (g1h varchar(15), g1a varchar(15), g2h varchar(15), g2a varchar(15), g3h varchar(15), g3a varchar(15), 
        g4h varchar(15), g4a varchar(15), g5h varchar(15), g5a varchar(15), g6h varchar(15), g6a varchar(15));''')

    c.execute('''CREATE TABLE IF NOT EXISTS advancers
            (playerName TEXT)''')
    conn.commit()
    conn.close()

def createstats(groups):
    conn = sqlite3.connect("bptournament.db")
    c = conn.cursor()
    for player in groups[0]:

        newstats = "INSERT INTO player_stats VALUES('{}', {}, {}, {}, {}, {}, {}, {}, '{}')".format(player, 0, 0, 0, 0, 0, 0, 0, "A")

        c.execute(newstats)

    for player in groups[1]:
        newstats = "INSERT INTO player_stats VALUES('{}', {}, {}, {}, {}, {}, {}, {}, '{}')".format(player, 0, 0, 0, 0, 0, 0, 0, "B")
        c.execute(newstats)

    for player in groups[2]:
        newstats = "INSERT INTO player_stats VALUES('{}', {}, {}, {}, {}, {}, {}, {}, '{}')".format(player, 0, 0, 0, 0, 0, 0, 0, "C")
        c.execute(newstats)
    conn.commit()


def fillgames(groupagames, groupbgames, groupcgames):
    groupgames = groupagames
    conn = sqlite3.connect("bptournament.db")
    c = conn.cursor()
    groupfill = "INSERT INTO groupgames(g1h, g1a, g2h, g2a, g3h, g3a, g4h, g4a, g5h, g5a, g6h, g6a) VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')"\
        .format(groupgames[0], groupgames[1], groupgames[2],
                groupgames[3], groupgames[4], groupgames[5],
                groupgames[6], groupgames[7], groupgames[8],
                groupgames[9], groupgames[10], groupgames[11])
    c.execute(groupfill)
    groupgames = groupbgames
    groupfill = "INSERT INTO groupgames VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(groupgames[0], groupgames[1], groupgames[2],
                                                                                                                               groupgames[3], groupgames[4], groupgames[5],
                                                                                                                               groupgames[6], groupgames[7], groupgames[8],
                                                                                                                               groupgames[9], groupgames[10], groupgames[11])

    c.execute(groupfill)
    groupgames = groupcgames
    groupfill = "INSERT INTO groupgames VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')" \
        .format(groupgames[0], groupgames[1], groupgames[2],
                groupgames[3], groupgames[4], groupgames[5],
                groupgames[6], groupgames[7], groupgames[8],
                groupgames[9], groupgames[10], groupgames[11])

    c.execute(groupfill)
    conn.commit()
    conn.close()


def printplayers():
    playerlist = []
    conn = sqlite3.connect("bptournament.db")
    c = conn.cursor()
    query = c.execute("SELECT * FROM tournament")
    rows = c.fetchall()
    for row in rows:
        name, = row
        playerlist.append(name)
    return playerlist


def playerstodb(players):
    conn = sqlite3.connect("bptournament.db")
    c = conn.cursor()
    for player in players:
        row = "INSERT INTO tournament(playerName) VALUES('{}')".format(player)
        c.execute(row)

    conn.commit()

    c.close()


def updategroup(pandres1, pandres2):
    conn = sqlite3.connect("bptournament.db")
    c = conn.cursor()
    firstplayer , res1 = pandres1
    secplayer, res2 = pandres2
    if res1 > res2:
        results = (firstplayer, res1), (secplayer, -1*int(res1))
        print("tämä on kotivoitto:", results)

    else:

        results = (secplayer, res2), (firstplayer, -1 * int(res2))
        print("2Tämä on vierasvoitto", results)

    for i in results:
        name, cupdiff = i
        print("3Pelaajat:", name, cupdiff)
        getfrom = '''SELECT * FROM player_stats WHERE playerName == '{}';'''.format(name)
        print("4Tällä haetaan päivitystiedot", getfrom)
        c.execute(getfrom)
        query = c.fetchall()
        print("5Tämä saadaan", query)
        name, p, w, l, cd, cf, ca, rank, group = query[0]
        print("NAME:", name, "wins:", w, "losses:", l, "cupdiff:", cd, "cupsfor:", cf, "cupsagainst", ca, "points:", p, "rank:", rank)
        print()
        if int(cupdiff) > 0:
            neww = w +1
            newcd = cd + int(cupdiff)
            newcf = cf + int(cupdiff)
            newp = p + 3
            print("rankki", newcf, "cupdiff", newcd, "points:", newp)
            rank = newcf + newcd * 10000 + newp * 100000000
            sql_update_query = '''UPDATE player_stats 
                SET player_points = {}, player_wins = {}, 
                player_cupdifference = {}, player_cupsfor = {}, player_rank = {} WHERE playerName = '{}';'''\
                .format(newp, neww, newcd, newcf, rank, name)
            print("6 Päivitys", sql_update_query)
            c.execute(sql_update_query)
        else:
            print("ero;", int(cupdiff))
            newcd = cd + int(cupdiff)
            print("uus kuppiero", newcd)
            newl = l + 1
            newca = ca - int(cupdiff)
            print("rankki", cf, "cupdiff", newcd, "points:", p)
            rank = cf + newcd * 10000 + p * 100000000
            sql_update_query = '''UPDATE player_stats 
                            SET player_losses = {}, 
                            player_cupdifference = {}, player_cupsagainst = {}, player_rank = {} WHERE playerName = '{}';''' \
                .format(newl, newcd, newca, rank, name)
            print("7 häviäjän päivitys:", sql_update_query)
            c.execute(sql_update_query)
    conn.commit()
# playerName           player_points,            player_wins         player_losses ,           player_cupdifference
# player_cupsfor                player_cupsagainst ,             player_rank ,                groupchar


def groupview(group):
    conn = sqlite3.connect("bptournament.db")
    c = conn.cursor()

    get = "SELECT * FROM player_stats WHERE groupchar = '{}'".format(group)
    realget = c.execute(get)
    retget = c.fetchall()
    for i in retget:
        print("8 hae uudet tiedot", i)
    return retget

def thirdplaces():
    conn = sqlite3.connect("bptournament.db")
    c = conn.cursor()
    getA = "SELECT * FROM player_stats WHERE groupchar = '{}'".format("A")
    c.execute(getA)
    agroup = c.fetchall()
    agroup = sorted(agroup, key=lambda tup: tup[7])
    aname, apoints, awins, alosses, acupdiff, acupsfor, acupsagainst, arank, groupchar = agroup[1]

    getB = "SELECT * FROM player_stats WHERE groupchar = '{}'".format("B")
    c.execute(getB)
    bgroup = c.fetchall()
    bgroup = sorted(bgroup, key=lambda tup: tup[7])
    bname, bpoints, bwins, blosses, bcupdiff, bcupsfor, bcupsagainst, brank, groupcharb = bgroup[1]

    getC = "SELECT * FROM player_stats WHERE groupchar = '{}'".format("C")
    c.execute(getC)
    cgroup = c.fetchall()
    cgroup = sorted(cgroup, key=lambda tup: tup[7])
    cname, cpoints, cwins, closses, ccupdiff, ccupsfor, ccupsagainst, crank, groupcharc = cgroup[1]

    ranks = [(aname,(arank)), (bname, int(brank)), (cname, int(crank))]
    decide = -5555555
    for name, rank in ranks:
        if decide < rank:
            decide = rank
            loser = name
    print("luuseri", loser)
    ranks.remove((loser,decide))
    print("3 jatkoon:", ranks[0], ranks[1])
    return ranks[0], ranks[1]

def getonetwo():
    conn = sqlite3.connect("bptournament.db")
    c = conn.cursor()

    getA = "SELECT * FROM player_stats WHERE groupchar = '{}'".format("A")
    c.execute(getA)
    agroup = c.fetchall()
    agroup = sorted(agroup, key=lambda tup: tup[7])

    getB = "SELECT * FROM player_stats WHERE groupchar = '{}'".format("B")
    c.execute(getB)
    bgroup = c.fetchall()
    bgroup = sorted(bgroup, key=lambda tup: tup[7])


    getC = "SELECT * FROM player_stats WHERE groupchar = '{}'".format("C")
    c.execute(getC)
    cgroup = c.fetchall()
    cgroup = sorted(cgroup, key=lambda tup: tup[7])

    aname1, apoints, awins, alosses, acupdiff, acupsfor, acupsagainst, arank, groupchar = agroup[3]
    aname2, apoints, awins, alosses, acupdiff, acupsfor, acupsagainst, arank, groupchar = agroup[2]
    bname1, bpoints, bwins, blosses, bcupdiff, bcupsfor, bcupsagainst, brank, groupcharb = bgroup[3]
    bname2, bpoints, bwins, blosses, bcupdiff, bcupsfor, bcupsagainst, brank, groupcharb = bgroup[2]
    cname1, cpoints, cwins, closses, ccupdiff, ccupsfor, ccupsagainst, crank, groupcharc = cgroup[3]
    cname2, cpoints, cwins, closses, ccupdiff, ccupsfor, ccupsagainst, crank, groupcharc = cgroup[2]
    conn.commit()
    print("lohkijen 1 ja 2",aname1, aname2, bname1, bname2, cname1, cname2)
    return aname1, aname2, bname1, bname2, cname1, cname2

def advance(awinner, arunnerup, bwinner, brunnerup, cwinner, crunnerup, thirdone, thirdtwo):
    players = [awinner, arunnerup, bwinner, brunnerup, cwinner, crunnerup, thirdone, thirdtwo]
    conn = sqlite3.connect("bptournament.db")
    c = conn.cursor()
    for player in players:

        newstats = "INSERT INTO advancers VALUES('{}')".format(player)
        print(newstats)
        c.execute(newstats)
    conn.commit()
