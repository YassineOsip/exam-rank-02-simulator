#!/usr/bin/python3

import sqlite3

import logging
logging.basicConfig(filename="story.log", filemode="w", level=logging.DEBUG)

try:
    conn = sqlite3.connect("ErsDb.db")
except Exception as ex:
    logging.error("can't connect to the database, got this message: %s" % ex)

def register(login, password):
    try:
        conn.execute("INSERT INTO USER (LOGIN, PASSWORD)\
                        VALUES ('%s', '%s')" % (login, password))
        conn.commit()
    except Exception as ex:
        logging.error("registration failed,got this message : %s" % ex)

def selectByLogin(login):
    try:
        cursor = conn.execute("SELECT LOGIN, PASSWORD FROM USER")
        user = cursor.fetchone()
        if user == None:
            logging.warning("selectionByLogin failed,can't find this login %s" % login)
        else:
            return user
    except Exception as ex:
        logging.error("selectionByLogin failed,got this message : %s" % ex)

register("ayidbelh", "pass2")
#print(selectByLogin("ylafkih"))
