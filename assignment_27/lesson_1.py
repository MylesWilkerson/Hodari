'''
################################################
#  Program: Pod_leaders.py                     #
#  Author: Myles Wilkerson                     #
#  Date: 3/10/2021                             #
#  Description: Program to be used by the      #
#               POD Leaders in instructing     #
#               the POD members about Object   #
#               Oriented Programming concepts  #
#  The Hidden Genius Project                   #
#  OAK8 Cohort                                 #
################################################
'''

import sqlite3
from sqlite3 import Error

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

connection = create_connection("hgp2")
