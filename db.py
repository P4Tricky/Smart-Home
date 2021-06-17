import sqlite3
from sqlite3 import Error
import os
import sys
from datetime import datetime


class Sensor:

    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = self.create_conn()

    def create_conn(self):
        try:
            conn = sqlite3.connect(self.db_file)
        except Error as e:
            print(e)

        return conn


    def create(self):
        table = """CREATE TABLE IF NOT EXISTS Sensor (
                    id integer PRIMARY KEY,
                    controller_id integer NOT NULL,
                    value integer NOT NULL,
                    date_created TEXT NOT NULL
                );"""
        try:
            c = self.conn.cursor()
            c.execute(table_sensor)
            c.close()

        except Error as e:
            print(e)


    def insert(self, data):
        query = """INSERT INTO Sensor(
            controller_id, value, date_created)
            VALUES(?,?,?)"""

        data = list(data)
        dt = datetime.now().strftime("%Y/%m/%d %H:%M:%S.%f")
        data = (int(data[0]), int(data[1]), str(dt))

        c = self.conn.cursor()
        c.execute(query, data)
        self.conn.commit()

        c.close()

    
    def delete_all(self):
        query = """DELETE FROM Sensor"""
        c = self.conn.cursor()
        c.execute(query)
        conn.commit()

        c.close()

    
    def query_all(self):
        query = """SELECT * FROM Sensor"""

        c = self.conn.cursor()
        c.execute(query)
        data = c.fetchall()

        c.close()
        return data

    
    def query_by_id(self, record_id):
        query = """SELECT * FROM Sensor
                WHERE id=?"""
        
        c = self.conn.cursor()
        c.execute(query, (record_id,))
        data = c.fetchall()

        c.close()
        return data
    
    
    def close_conn(self):
        self.conn.close()



class Device:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = self.create_conn()

    def create_conn(self):
        try:
            conn = sqlite3.connect(self.db_file)
        except Error as e:
            print(e)

        return conn


    def create(self):
        table = """CREATE TABLE IF NOT EXISTS Device (
                    id INTEGER PRIMARY KEY,
                    device TEXT NOT NULL,
                    status INTEGER NOT NULL,
                    date_created TEXT NOT NULL
                );"""
        try:
            c = self.conn.cursor()
            c.execute(table)
            c.close()

        except Error as e:
            print(e)


    def insert(self, data):
        query = """INSERT INTO Device(
            device, status, date_created)
            VALUES(?,?,?)"""

        data = list(data)
        dt = datetime.now().strftime("%Y/%m/%d %H:%M:%S.%f")
        data = (str(data[0]), int(data[1]), str(dt))

        c = self.conn.cursor()
        c.execute(query, data)
        self.conn.commit()

        c.close()

    
    def delete_all(self):
        query = """DELETE FROM Device"""
        c = self.conn.cursor()
        c.execute(query)
        conn.commit()

        c.close()

    
    def query_all(self):
        query = """SELECT * FROM Device"""

        c = self.conn.cursor()
        c.execute(query)
        data = c.fetchall()

        c.close()
        return data

    
    def query_by_id(self, record_id):
        query = """SELECT * FROM Device
                WHERE id=?"""
        
        c = self.conn.cursor()
        c.execute(query, (record_id,))
        data = c.fetchall()

        c.close()
        return data
    
    
    def close_conn(self):
        self.conn.close()







