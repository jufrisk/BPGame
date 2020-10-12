import bp_db as db
import sqlite3

conn = sqlite3.connect("bptournament.db")
c = conn.cursor()
getA = "SELECT * FROM player_stats WHERE groupchar = '{}'".format("A")
c.execute(getA)
agroup = c.fetchall()
agroup = sorted(agroup, key=lambda tup: tup[7])
for i in agroup:
    print(i)
aname, apoints, awins, alosses, acupdiff, acupsfor, acupsagainst, arank, groupchar = agroup[1]
print(aname)
getB = "SELECT * FROM player_stats WHERE groupchar = '{}'".format("B")
c.execute(getB)
bgroup = c.fetchall()
bgroup = sorted(bgroup, key=lambda tup: tup[7])
for i in bgroup:
    print(i)
bname, bpoints, bwins, blosses, bcupdiff, bcupsfor, bcupsagainst, brank, groupcharb = bgroup[1]
print(bname)

getC = "SELECT * FROM player_stats WHERE groupchar = '{}'".format("C")
c.execute(getC)
cgroup = c.fetchall()
for i in cgroup:
    print(i)
cgroup = sorted(cgroup, key=lambda tup: tup[7])
for i in cgroup:
    print(i)
cname, cpoints, cwins, closses, ccupdiff, ccupsfor, ccupsagainst, crank, groupcharc = cgroup[1]

    # ranks = [(aname,(arank)), (bname, int(brank)), (cname, int(crank))]
    # decide = -5555555
    # for name, rank in ranks:
    #     if decide < rank:
    #         decide = rank
    #         loser = name
    # print("luuseri", loser)
    # ranks.remove((loser,decide))
    # print("3 jatkoon:", ranks[0], ranks[1])
    # return ranks[0], ranks[1]