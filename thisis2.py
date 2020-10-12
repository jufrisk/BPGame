import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from games_olio import playerStats
import bp_db as db
from Elims import Ui_Dialog2

class Ui_Dialog(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1108, 775)
        self.centralwidget = QtWidgets.QWidget(Dialog)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(320, 240, 481, 201))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 4, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 3, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 1, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 2, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_15.setMaximumSize(QtCore.QSize(16770000, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 4, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 2, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 3, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.gridLayout_2.addWidget(self.label_18, 1, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_19.setObjectName("label_19")
        self.gridLayout_2.addWidget(self.label_19, 0, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_20.setObjectName("label_20")
        self.gridLayout_2.addWidget(self.label_20, 0, 1, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(50, 20, 261, 201))
        self.tableWidget.setMinimumSize(QtCore.QSize(261, 201))
        self.tableWidget.setMaximumSize(QtCore.QSize(500, 500))
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setRowCount(6)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(320, 20, 481, 201))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 4, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setMaximumSize(QtCore.QSize(16770000, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 0, 1, 1, 1)
        self.tableWidget_2 = QtWidgets.QTableWidget(Dialog)
        self.tableWidget_2.setGeometry(QtCore.QRect(50, 240, 261, 201))
        self.tableWidget_2.setMinimumSize(QtCore.QSize(261, 201))
        self.tableWidget_2.setMaximumSize(QtCore.QSize(500, 500))
        self.tableWidget_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget_2.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_2.setRowCount(6)
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.horizontalHeader().setVisible(False)
        self.tableWidget_2.horizontalHeader().setHighlightSections(False)
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget_2.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(320, 460, 481, 201))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_21 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.gridLayout_3.addWidget(self.label_21, 4, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.gridLayout_3.addWidget(self.label_22, 3, 0, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.gridLayout_3.addWidget(self.label_23, 1, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.gridLayout_3.addWidget(self.label_24, 2, 0, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_25.setMaximumSize(QtCore.QSize(16770000, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.gridLayout_3.addWidget(self.label_25, 4, 0, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.gridLayout_3.addWidget(self.label_26, 2, 1, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.gridLayout_3.addWidget(self.label_27, 3, 1, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.gridLayout_3.addWidget(self.label_28, 1, 0, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_29.setObjectName("label_29")
        self.gridLayout_3.addWidget(self.label_29, 0, 0, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_30.setObjectName("label_30")
        self.gridLayout_3.addWidget(self.label_30, 0, 1, 1, 1)
        self.tableWidget_3 = QtWidgets.QTableWidget(Dialog)
        self.tableWidget_3.setGeometry(QtCore.QRect(50, 460, 261, 201))
        self.tableWidget_3.setMinimumSize(QtCore.QSize(261, 201))
        self.tableWidget_3.setMaximumSize(QtCore.QSize(500, 500))
        self.tableWidget_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget_3.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_3.setRowCount(6)
        self.tableWidget_3.setColumnCount(2)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.horizontalHeader().setVisible(False)
        self.tableWidget_3.horizontalHeader().setHighlightSections(False)
        self.tableWidget_3.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget_3.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 670, 222, 48))
        self.pushButton_2.setObjectName("pushButton")
        self.pushButton_2.clicked.connect(self.bringgames)
        self.pushButton_2.clicked.connect(self.groups)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(850, 400, 222, 48))
        self.pushButton_3.setObjectName("pushButton")
        self.pushButton_3.clicked.connect(self.updateresult)
        self.pushButton_3.clicked.connect(self.viewupdate)

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(850, 600, 222, 48))
        self.pushButton_4.setObjectName("pushButton")
        self.pushButton_4.clicked.connect(self.endgroups)

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(850, 300, 113, 22))
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(850, 330, 113, 22))
        self.lineEdit_2.setObjectName("lineEdit")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(970, 300, 50, 22))
        self.lineEdit_3.setObjectName("lineEdit")

        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(970, 330, 50, 22))
        self.lineEdit_4.setObjectName("lineEdit")

        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(850, 270, 113, 22))
        self.lineEdit_5.setObjectName("lineEdit")

        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label")
        self.label_31.setGeometry(QtCore.QRect(880, 240, 71, 20))

        self.label_32 = QtWidgets.QLabel(self.centralwidget)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label")
        self.label_32.setGeometry(QtCore.QRect(830, 300, 71, 20))

        self.label_33 = QtWidgets.QLabel(self.centralwidget)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label")
        self.label_33.setGeometry(QtCore.QRect(830, 330, 71, 20))

        self.label_34 = QtWidgets.QLabel(self.centralwidget)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label")
        self.label_34.setGeometry(QtCore.QRect(970, 270, 71, 20))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_11.setText(_translate("Dialog", "0    0     0     0    0   0   0 "))
        self.label_12.setText(_translate("Dialog", "Player7"))
        self.label_13.setText(_translate("Dialog", "0    0     0     0    0   0   0 "))
        self.label_14.setText(_translate("Dialog", "Player6"))
        self.label_15.setText(_translate("Dialog", "Player8"))
        self.label_16.setText(_translate("Dialog", "0    0     0     0    0   0   0 "))
        self.label_17.setText(_translate("Dialog", "0    0     0     0    0   0   0 "))
        self.label_18.setText(_translate("Dialog", "Player5"))
        self.label_19.setText(_translate("Dialog", "Group"))
        self.label_20.setText(_translate("Dialog", "Stats"))
        self.label_8.setText(_translate("Dialog", "0    0     0     0    0   0   0 "))
        self.label_3.setText(_translate("Dialog", "Player3"))
        self.label_5.setText(_translate("Dialog", "0    0     0     0    0   0   0 "))
        self.label_2.setText(_translate("Dialog", "p1"))
        self.label_4.setText(_translate("Dialog", "Player4"))
        self.label_6.setText(_translate("Dialog", "0    0     0     0    0   0   0 "))
        self.label_7.setText(_translate("Dialog", "0    0     0     0    0   0   0 "))
        self.label.setText(_translate("Dialog", "p2"))
        self.label_9.setText(_translate("Dialog", "Group"))
        self.label_10.setText(_translate("Dialog", "Stats"))
        self.label_21.setText(_translate("Dialog", "0    0     0     0    0   0   0 "))
        self.label_22.setText(_translate("Dialog", "Player11"))
        self.label_23.setText(_translate("Dialog", "0    0     0     0    0   0   0 "))
        self.label_24.setText(_translate("Dialog", "Player10"))
        self.label_25.setText(_translate("Dialog", "Player12"))
        self.label_26.setText(_translate("Dialog", "0    0     0     0    0   0   0 "))
        self.label_27.setText(_translate("Dialog", "0    0     0     0    0   0   0 "))
        self.label_28.setText(_translate("Dialog", "Player9"))
        self.label_29.setText(_translate("Dialog", "Group"))
        self.label_30.setText(_translate("Dialog", "Stats"))
        self.label_31.setText(_translate("Dialog", "Group?"))
        self.label_32.setText(_translate("Dialog", "P1"))
        self.label_33.setText(_translate("Dialog", "P2"))
        self.label_34.setText(_translate("Dialog", "Scores"))
        self.pushButton_2.setText(_translate("Dialog", "Load data"))
        self.pushButton_3.setText(_translate("Dialog", "Update"))
        self.pushButton_4.setText(_translate("Dialog", "Advance"))

    def bringgames(self):
        conn = sqlite3.connect("bptournament.db")
        c = conn.cursor()
        query = c.execute("SELECT * FROM groupgames")
        a = c.fetchall()
        ro = 0
        col = 0
        for row in a[0]:
            if col == 2:
                ro = ro + 1
                col = 0
            self.tableWidget.setItem(ro, col, QtWidgets.QTableWidgetItem(str(row)))
            col = col + 1
        ro = 0
        col = 0
        for row in a[1]:
            if col == 2:
                ro = ro + 1
                col = 0
            self.tableWidget_2.setItem(ro, col, QtWidgets.QTableWidgetItem(str(row)))
            col = col + 1
        ro = 0
        col = 0
        for row in a[2]:
            if col == 2:
                ro = ro + 1
                col = 0
            self.tableWidget_3.setItem(ro, col, QtWidgets.QTableWidgetItem(str(row)))
            col = col + 1

    def groups(self):
        conn = sqlite3.connect("bptournament.db")
        c = conn.cursor()
        query2 = c.execute('''SELECT * FROM player_stats
                                   WHERE groupchar == 'A'; ''')

        agroup = c.fetchall()
        afirst = agroup[0]
        name, p, w, l, cd, cf, ca, rank, group = afirst
        name1 = '{}'.format(name)
        numbers = '{} {} {} {} {} {}'.format(w, l, cd, cf, ca, p)
        self.label.setText(name1)
        self.label_5.setText(numbers)

        asec = agroup[1]
        name, p, w, l, cd, cf, ca, rank, group = asec
        name2 = '{}'.format(name)
        numbers = '{} {} {} {} {} {}'.format(w, l, cd, cf, ca, p)
        self.label_2.setText(name2)
        self.label_6.setText(numbers)

        ath3 = agroup[2]
        name, p, w, l, cd, cf, ca, rank, group = ath3
        name3 = '{}'.format(name)
        numbers = '{} {} {} {} {} {}'.format(w, l, cd, cf, ca, p)
        self.label_3.setText(name3)
        self.label_7.setText(numbers)

        afour = agroup[3]
        name, p, w, l, cd, cf, ca, rank, group = afour
        name4 = '{}'.format(name)
        numbers = '{} {} {} {} {} {}'.format(w, l, cd, cf, ca, p)
        self.label_4.setText(name4)
        self.label_8.setText(numbers)

        query2 = c.execute('''SELECT * FROM player_stats
                                    WHERE groupchar == 'B'; ''')
        bgroup = c.fetchall()


        bfirst = bgroup[0]
        name, p, w, l, cd, cf, ca, rank, group = bfirst
        name1 = '{}'.format(name)
        numbers = '{} {} {} {} {} {}'.format(w, l, cd, cf, ca, p)
        self.label_18.setText(name1)
        self.label_13.setText(numbers)

        bsec = bgroup[1]
        name, p, w, l, cd, cf, ca, rank, group = bsec
        name2 = '{}'.format(name)
        numbers = '{} {} {} {} {} {}'.format(w, l, cd, cf, ca, p)
        self.label_14.setText(name2)
        self.label_16.setText(numbers)

        bth3 = bgroup[2]
        name, p, w, l, cd, cf, ca, rank, group = bth3
        name3 = '{}'.format(name)
        numbers = '{} {} {} {} {} {}'.format(w, l, cd, cf, ca, p)
        self.label_12.setText(name3)
        self.label_17.setText(numbers)

        bfour = bgroup[3]
        name, p, w, l, cd, cf, ca, rank, group = bfour
        name4 = '{}'.format(name)
        numbers = '{} {} {} {} {} {}'.format(w, l, cd, cf, ca, p)
        self.label_15.setText(name4)
        self.label_11.setText(numbers)

        query3 = c.execute('''SELECT * FROM player_stats
                                            WHERE groupchar == 'C'; ''')
        cgroup = c.fetchall()

        cfirst = cgroup[0]
        name, p, w, l, cd, cf, ca, rank, group = cfirst
        name1 = '{}'.format(name)
        numbers = '{} {} {} {} {} {}'.format(w, l, cd, cf, ca, p)
        self.label_28.setText(name1)
        self.label_23.setText(numbers)

        csec = cgroup[1]
        name, p, w, l, cd, cf, ca, rank, group = csec
        name2 = '{}'.format(name)
        numbers = '{} {} {} {} {} {}'.format(w, l, cd, cf, ca, p)
        self.label_24.setText(name2)
        self.label_26.setText(numbers)

        cth3 = cgroup[2]
        name, p, w, l, cd, cf, ca, rank, group = cth3
        name3 = '{}'.format(name)
        numbers = '{} {} {} {} {} {}'.format(w, l, cd, cf, ca, p)
        self.label_22.setText(name3)
        self.label_27.setText(numbers)

        cfour = cgroup[3]
        name, p, w, l, cd, cf, ca, rank, group = cfour
        name4 = '{}'.format(name)
        numbers = '{} {} {} {} {} {}'.format(w, l, cd, cf, ca, p)
        self.label_25.setText(name4)
        self.label_21.setText(numbers)

    def updateresult(self):
        firstplayer = self.lineEdit.text()
        secplayer = self.lineEdit_2.text()
        res1 = self.lineEdit_3.text()
        res2 = self.lineEdit_4.text()
        print("Tämä menee eteenpäin:", (firstplayer, res1), (secplayer, res2))
        db.updategroup((firstplayer, res1), (secplayer, res2))


    def viewupdate(self):
        group = self.lineEdit_5.text()
        getplayers = db.groupview(group)
        self.places = []
        if group == 'A':
            self.places = [self.label,
                      self.label_5,
                      self.label_2,
                      self.label_6,
                      self.label_3,
                      self.label_7,
                      self.label_4,
                      self.label_8
             ]

        elif group == 'B':
            self.places = [self.label_18,
                      self.label_13,
                      self.label_14,
                      self.label_16,
                      self.label_12,
                      self.label_17,
                      self.label_15,
                      self.label_11
                      ]
        elif group == 'C':
            self.places = [self.label_28,
                      self.label_23,
                      self.label_24,
                      self.label_26,
                      self.label_22,
                      self.label_27,
                      self.label_25,
                      self.label_21
                      ]
        rank = -99999999999999999
        print("**********************************************************************")
        for player in getplayers:
            pname1, p1, w1, l1, cd1, cf1, ca1, rank1, gr1 = player
            print(rank1)
            if rank < rank1:
                best = player
                rank = rank1
        print("Tää olis paras:", best)
        pname, p, w, l, cd, cf, ca, rankk, gr1 = best
        name1 = '{}'.format(pname)
        numbers = '{} {} {} {} {} {}'.format(w, l, cd, cf, ca, p)
        print("Paras:", name1)
        print("parhaanstatsit", numbers)
        self.places[0].setText(name1)
        self.places[1].setText(numbers)
        getplayers.remove(best)
        print("tässä on lista ekan jälkeen", getplayers)
        rank = -99999999999999999

        for player in getplayers:
            pname1, p1, w1, l1, cd1, cf1, ca1, rank1, gr1 = player
            if rank < rank1:
                pname, p, w, l, cd, cf, ca, r, gr = player
                best = player
                rank = rank1
        pname, p, w, l, cd, cf, ca, rankk, gr1 = best
        name1 = '{}'.format(pname)
        numbers = '{} {} {} {} {} {}'.format(w, l, cd, cf, ca, p)
        print("Toinen:", name1)
        print("2 numerot", numbers)
        self.places[2].setText(name1)
        self.places[3].setText(numbers)
        getplayers.remove(best)
        rank = -99999999999999999
        for player in getplayers:
            pname1, p1, w1, l1, cd1, cf1, ca1, rank1, gr1 = player
            if rank < rank1:
                pname, p, w, l, cd, cf, ca, r, gr = player
                best = player
                rank = rank1
        pname, p, w, l, cd, cf, ca, rankk, gr1 = best
        name1 = '{}'.format(pname)
        numbers = '{} {} {} {} {} {}'.format(w, l, cd, cf, ca, p)
        print("kolmas", name1)
        print("3numerot",numbers)
        self.places[4].setText(name1)
        self.places[5].setText(numbers)
        getplayers.remove(best)
        pname, p, w, l, cd, cf, ca, r, gr = getplayers[0]
        name1 = '{}'.format(pname)
        numbers = '{} {} {} {} {} {}'.format(w, l, cd, cf, ca, p)
        print("vika", name1)
        print("4numerot", numbers)
        self.places[6].setText(name1)
        self.places[7].setText(numbers)
        #games.game(firstplayer, secplayer, res1, res2)

#(playerName varchar2(15), player_points INT, player_wins INT, player_losses INT, player_cupdifference INT,
# player_cupsfor INT, player_cupsagainst INT, player_rank INT, groupchar CHAR(1),
    def endgroups(self):
        thirdone, thirdtwo = db.thirdplaces()
        thirdone, p = thirdone
        thirdtwo, p2 = thirdtwo
        awinner, arunnerup, bwinner, brunnerup, cwinner, crunnerup = db.getonetwo()
        print("moi")
        db.advance(awinner, arunnerup, bwinner, brunnerup, cwinner, crunnerup, thirdone, thirdtwo)
        print(awinner, arunnerup, bwinner, brunnerup, cwinner, crunnerup, thirdone, thirdtwo)
        Dialog = QtWidgets.QDialog()
        ui2 = Ui_Dialog2()
        ui2.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
