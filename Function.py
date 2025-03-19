import os
import sys
import sqlite3
from sqlite3 import Error
from PySide6.QtWidgets import QTableWidgetItem

class AppFunction():
    def __init__(self, arg):
        super(AppFunction, self).__init___()
        self.arg = arg

    def create_connection(db_file):
        # create a db connection to a sqlite database

        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)
        return conn
    
    def create_table(conn, creqate_table_sql):
        try:
            c = conn.cursor()
            c.execute(creqate_table_sql)
        except Error as e:
            print(e)
        
    def main(dbFolder):
        create_user_table = """ CREATE TABLE IF NOT EXISTS Users (
                                            USER_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                            USER_NAME TEXT,
                                            USER_EMAIL,
                                            USER_PHONE TEXT
                                        );
                                        """
        conn = AppFunction.create_connection(dbFolder)

        if conn is not None:
            AppFunction.create_table(conn, create_user_table)
        else:
            print("Error! can not create tteh db connection!")
    
    def getAllUsers(dbFolder):
        conn = AppFunction.create_connection(dbFolder)
        get_all_users = """
                            SELECT * FROM Users;
                        """
        try:
            c = conn.cursor()
            c.execute(get_all_users)
            return c
        except Error as e:
            print(e)

    def addUser(self, dbFolder):
        conn = AppFunction.create_connection(dbFolder)
        userName = self.ui.userName.text()
        email = self.ui.email.text()
        phoneNo = self.ui.phoneNo.text()

        insert_person_data_sql = f"""
        INSERT INTO USERS (USER_NAME, USER_EMAIL, USER_PHONE) VALUES ('{userName}', '{email}', '{phoneNo}');
        """

        if not conn.cursor().execute(insert_person_data_sql):
            print("Could not inser person data")
        else:
            conn.commit()
            #  clear form input
            self.ui.userName.setText("")
            self.ui.email.setText("")
            self.ui.phoneNo.setText("")

            # load new user from DB to table view
            AppFunction.displayUsers(self.AppFunction.getAllUsers(dbFolder))

    def displayUsers(self, rows):
        # create new row
        for row in rows:
            # get number of rows
            rowPosition = self.ui.tableWidget.rowCount()

            # skip rows that have alvready been loaded to table
            if rowPosition + 1 >row[0]:
                continue

            itemCount = 0
            self.ui.tableWidget.setRowCount(rowPosition+1)
            qtablewidgetitem = QTableWidgetItem()
            self.ui.tableWidget.setVerticalHeaderItem(rowPosition, qtablewidgetitem)

            # add items to row
            for item in row:
                self.qtablewidgetitem = QTableWidgetItem()
                self.ui.tableWidget.setItem(rowPosition, itemCount, self.qtablewidgetitem)

                self.qtablewidgetitem = self.ui.tableWidget.item(rowPosition)
                self.qtablewidgetitem.setText(str(item))


                itemCount = itemCount + 1

            rowPosition = rowPosition + 1
