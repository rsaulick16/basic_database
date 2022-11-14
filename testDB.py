import dbStubExample

def main():
    usr = "Bob"
    pwd = "Pass1234"
    dbStubExample.AddUser(usr, pwd)
    dataRows = dbStubExample.getUser(usr)
    for row in dataRows:
        print(row)



# driver code
if __name__ == "__main__":
    main()
