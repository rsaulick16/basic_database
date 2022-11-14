import sqlite3
DBFilePath = "testDB.sqlite3"
connectionObject    = sqlite3.connect(DBFilePath)
cursorObject        = connectionObject.cursor()

dropTableSQL        = "DROP TABLE IF EXISTS usertbl"
cursorObject.execute(dropTableSQL)

# Create student table
createTableSQL      = "CREATE TABLE IF NOT EXISTS usertbl (userName text, userPWD text, PWDSalt text, dateAdded text)"
cursorObject.execute(createTableSQL)
connectionObject.close()
print("DONE")
