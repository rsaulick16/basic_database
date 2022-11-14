from datetime import datetime
import sqlite3
import hashlib
from random import choice

#Constants
DBFILEPATH = "testDB.sqlite3" # might need to add the full path to this file name
SECRET = "NoBugsAllowed"
ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def getDBConnection():
    '''This method will make a connection to 
    the database for the filename'''
    conn = sqlite3.connect(DBFILEPATH)
    # probably should put some error checking in here!
    return conn

def generateSalt():
    chars=[]
    for i in range(5):
        chars.append(choice(ALPHABET))
    return "".join(chars)


def AddUser(userName, password):
    salt = generateSalt()
    dbPwd = password + SECRET + salt
    encPwd = hashlib.md5(dbPwd.encode()).hexdigest()
    userDate = str(datetime.now())
    '''This method will add a user to the database
    and return True/False if the user was added successfully or not'''
    # Insert a row of data into stud table
    insertUserSQL = "INSERT INTO usertbl VALUES(?,?,?,?)"
    # substitution parameters - ? will be replaced by members of this tuple
    insertParams = (userName, encPwd, salt, userDate)
    conn = getDBConnection() # get connection
    cursor = conn.cursor() # create cursor on connection object
    cursor.execute(insertUserSQL, insertParams) #execute SQL insert using parameter substitution
    conn.commit() # Commit the changes
    conn.close() # close connection to db
    # TODO
    # check for errors
    # return True/False


def getUser(username):
    '''This method will return details of the user from the database
    for a given username'''
    if username == "" or username == None:
        return None
    else:
        selectSQL = "SELECT * FROM usertbl WHERE username = ?"
        selectParams = username
        conn = getDBConnection() # get connection
        cursor = conn.cursor() # create cursor on connection object
        cursor.execute(selectSQL, (selectParams,)) #execute SQL to get data using parameter substitution
        rows = cursor.fetchall() # fetch all rows from database
        conn.close() # close connection to db
        return rows

def validateUser(userName, hashedPwd):
    '''Given a username and hashedPwd, validate the user''' 
    if userName == "" or userName == None:
        return None
    else:
        SQL = "SELECT FROM usertbl WHERE username = ? \
               WHERE EXISTS (SELECT username FROM usertbl WHERE password = ?)"
        SQLParams = (userName, hashedPwd)
        conn = getDBConnection() # get connection
        cursor = conn.cursor() # create cursor on connection object
        cursor.execute(SQL, (SQLParams,)) #execute SQL to get data using parameter substitution
        rows = cursor.fetchall() # fetch all rows from database
        conn.close() # close connection to db
    pass

def delUser(username):
    '''This method will remove a user to the database and
    return True/False if the user was removed successfully or not'''
    if username == "" or username == None:
        return None
    else:
        SQL = "DELETE FROM usertbl WHERE username = ?"
        SQLParams = username
        conn = getDBConnection() # get connection
        cursor = conn.cursor() # create cursor on connection object
        cursor.execute(SQL, (SQLParams,)) #execute SQL to get data using parameter substitution
        rows = cursor.fetchall() # fetch all rows from database
        conn.close() # close connection to db
    pass

def updateUser(userName, data):
    '''This method will update a users data to the database
    and return True/False if the user was removed successfully or not'''
    if userName == "" or userName == None:
        return None
    else:
        SQL = "UPDATE userTbl \
               DELETE userName='?'\
               SELECT FROM usertbl WHERE EXISTS (SELECT FROM usertbl WHERE userName = ?)"
        SQLParams = userName
        conn = getDBConnection() # get connection
        cursor = conn.cursor() # create cursor on connection object
        cursor.execute(SQL, (SQLParams,)) #execute SQL to get data using parameter substitution
        rows = cursor.fetchall() # fetch all rows from database
        conn.close() # close connection to db
    pass
