# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Books.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Book(object):
    def setupUi(self, Book):
        Book.setObjectName("Book")
        Book.resize(400, 317)
        self.verticalLayout = QtWidgets.QVBoxLayout(Book)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(14, 43, 14, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Book)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.t1 = QtWidgets.QLineEdit(Book)
        self.t1.setObjectName("t1")
        self.horizontalLayout.addWidget(self.t1)
        self.pushButton = QtWidgets.QPushButton(Book)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(45, 0, 45, 30)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Book)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.t2 = QtWidgets.QLineEdit(Book)
        self.t2.setObjectName("t2")
        self.horizontalLayout_2.addWidget(self.t2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(14, 11, 14, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(Book)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.t3 = QtWidgets.QLineEdit(Book)
        self.t3.setObjectName("t3")
        self.horizontalLayout_3.addWidget(self.t3)
        self.pushButton_2 = QtWidgets.QPushButton(Book)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(45, -1, 45, 49)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(Book)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.t4 = QtWidgets.QLineEdit(Book)
        self.t4.setObjectName("t4")
        self.horizontalLayout_4.addWidget(self.t4)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(120, -1, 120, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_3 = QtWidgets.QPushButton(Book)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_5.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.retranslateUi(Book)
        self.pushButton_3.clicked.connect(self.t4.clear) # type: ignore
        self.pushButton_3.clicked.connect(self.t3.clear) # type: ignore
        self.pushButton_3.clicked.connect(self.t2.clear) # type: ignore
        self.pushButton_3.clicked.connect(self.t1.clear) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Book)

        self.pushButton.clicked.connect(self.findprice)
        self.pushButton_2.clicked.connect(self.findtotal)

    def retranslateUi(self, Book):
        _translate = QtCore.QCoreApplication.translate
        Book.setWindowTitle(_translate("Book", "Form"))
        self.label.setText(_translate("Book", "Book Title:"))
        self.pushButton.setText(_translate("Book", "Find Price"))
        self.label_2.setText(_translate("Book", "Price:"))
        self.label_3.setText(_translate("Book", "Quantity:"))
        self.pushButton_2.setText(_translate("Book", "Find Total"))
        self.label_4.setText(_translate("Book", "Total:"))
        self.pushButton_3.setText(_translate("Book", "Reset"))

    def findprice(self):
        import sqlite3
        book=sqlite3.connect("Bookstore.db")
        curbook=book.cursor()
        ttl = self.t1.text()

        sql = "SELECT * FROM books WHERE Title = '"+ttl+"'"
        curbook=book.cursor()
        curbook.execute(sql)
        rec=curbook.fetchone()
        if rec!=None:
            print(rec)
            self.pr=rec[3]
            self.t2.setText('Rs. '+str(float(self.pr)))
        else:
            print("Book not available")
    
    def findtotal(self):
        self.qty=float(self.t3.text())
        total=(int)(self.qty)*((float)(self.pr))
        self.t4.setText('Rs. '+ str(total))
    
    
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Book = QtWidgets.QWidget()
    ui = Ui_Book()
    ui.setupUi(Book)
    Book.show()
    sys.exit(app.exec_())
