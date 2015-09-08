import sqlite3



def main():
    conn = sqlite3.connect("simpsons.db")

    getChoice(conn)                 
                       
    
def getChoice(conn):

    print "1: Create Table"
    print "2: Read Table"
    print "3: Add Record"
    print "4: Get Record by Search"
    print "5: Delete Records by Search"
    print "6: View/Delete Tables"
    print "q: Leave Program"
    print "" 
    choice = (raw_input("What would you like to do?: "))
    print ""
    print ""

    if (choice == '1'):
        createTable(conn)
    elif (choice == '2'):
        readTable(conn)
    elif (choice == '3'):
        addRecord(conn)
    elif (choice == '4'):
        searchRecord(conn)
    elif (choice == '5'):
        deleteRecord(conn)         
    elif (choice == 'q'):
        print "Quitter."
        conn.close()
    elif (choice == '6'):
        deleteTable(conn)       
    else:
        print "Please choose valid option."
        print ""
        print ""
        getChoice(conn)
    

    
def createTable(conn):

    tableName = raw_input("Name for table: ")

    conn.execute("CREATE TABLE if not exists "+tableName +"(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT,\
        NAME TEXT,\
        GENDER TEXT,\
        AGE INT,\
        OCCUPATION TEXT);")

    print tableName + " created!"
    print""
    print""

    getChoice(conn)


def readTable(conn):

    cursor = conn.execute("SELECT name FROM sqlite_master \
        WHERE type = 'table'\
        ORDER BY name;")
    
    tableList = cursor.fetchall()
    print "ALL TABLES IN DATABASE:"
    print "***********************"
    for t in range(0,len(tableList)):
        print str(t+1) + ": " + tableList[t][0]

    print ""
    print ""
    tableChoice = raw_input("To view a table, enter number. Any other key for main menu: ")

    #check if a number
    try:
        number = int(tableChoice)
    except ValueError:
        print ""
        print ""
        getChoice(conn)
    else:
        if (int(tableChoice) <= len(tableList)) and (int(tableChoice) > 0):
            cursor = conn.execute("SELECT * FROM " +tableList[int(tableChoice)-1][0])
            showRows = cursor.fetchall()
            for row in showRows:
                print row
            
            print ""
            print ""
            getChoice(conn)            
        else:
            print ""
            print ""
            getChoice(conn)             


def addRecord(conn):
    cursor = conn.execute("SELECT name FROM sqlite_master \
        WHERE type = 'table'\
        ORDER BY name;")
    
    tableList = cursor.fetchall()
    print "Which table to add a RECORD to? :"
    print "***********************"
    for t in range(0,len(tableList)):
        print str(t+1) + ": " + tableList[t][0]

    print ""
    print ""
    table = raw_input("To choose a table, enter number. Any other key for main menu: ")

    #check if a number
    try:
        number = int(table)
    except ValueError:
        print ""
        print ""
        getChoice(conn)

    table = tableList[int(table)-1][0]
    newValues = []
    cursor = conn.execute('SELECT * from '+table)
    headers = [description[0] for description in cursor.description]    
    for i in range(1,len(headers)):
        newValues.append(raw_input("Enter value for " + headers[i] +":  "))


    headerValues=""
    stringValues=""
    for s in range(0,len(newValues)):
        stringValues = stringValues + "'"+newValues[s] + "',"
        headerValues = headerValues + headers[s+1] + ","
    stringValues = stringValues[:-1]
    headerValues = headerValues[:-1]


    cursor.execute("INSERT INTO " +table+ "\
        ({})".format(headerValues)+" VALUES \
        ({})".format(stringValues))   


    conn.commit()

    newID = cursor.lastrowid
    print ""
    print "This was entered into table " + "'"+table+"'"
    print ""
    
    cursor = (conn.execute("SELECT * FROM " + table +" where " + headers[0] +" = " + str(newID)))

    newData = cursor.fetchall()    
 
    for i in range(0,len(headers)):
        print headers[i]+ ": " + str(newData[0][i])

    print ""
    redo = raw_input("If an error was made, type 'REDO' to delete record and try again. Any other key for main menu  :")

    if redo == 'REDO':
        cursor = conn.execute("DELETE FROM " + table +" where " + headers[0] +" = " + str(newID))
        print raw_input(" *** RECORD DELETED *** Press any key to confirm and re-enter data  :")


    print""
    print""

    getChoice(conn)

def searchRecord(conn):
    cursor = conn.execute("SELECT name FROM sqlite_master \
        WHERE type = 'table'\
        ORDER BY name;")
    
    tableList = cursor.fetchall()
    print "Which table to search through? :"
    print "***********************"
    for t in range(0,len(tableList)):
        print str(t+1) + ": " + tableList[t][0]

    print ""
    table = raw_input("To choose a table, enter number. Any other key for main menu: ")

    #check if a number
    try:
        number = int(table)
    except ValueError:
        print ""
        print ""
        getChoice(conn)

    table = tableList[int(table)-1][0]

    newValues = []
    print "Which FIELD to search through? :"
    print "***********************"
    cursor = conn.execute('SELECT * from '+table)
    headers = [description[0] for description in cursor.description]    
    for i in range(0,len(headers)):
        print str(i+1) + ":  " +headers[i]

    search = raw_input("To choose a FIELD, enter number. Any other key for main menu: ")

    #check if a number
    try:
        number = int(search)
    except ValueError:
        print ""
        print ""
        getChoice(conn)

    search = headers[int(search) - 1]
    print ""
    query = raw_input("Search table '"+table+"' where '" + search+  "' = ")
    print ""

    print " *** ALL MATCHING RECORDS *** "
       
    cursor = (conn.execute("SELECT * FROM " + table +" where " + search +" = '" + query+"'"))

    showRows = cursor.fetchall()
    print headers
    for row in showRows:
        print row

    print ""
    print raw_input("Any key to acknowledge: :")             

    print""
    print""

    getChoice(conn)

    
def deleteRecord(conn):
    cursor = conn.execute("SELECT name FROM sqlite_master \
        WHERE type = 'table'\
        ORDER BY name;")
    
    tableList = cursor.fetchall()
    print "Which table to DELETE records from :"
    print "***********************"
    for t in range(0,len(tableList)):
        print str(t+1) + ": " + tableList[t][0]

    print ""
    table = raw_input("To choose a table, enter number. Any other key for main menu: ")

    #check if a number
    try:
        number = int(table)
    except ValueError:
        print ""
        print ""
        getChoice(conn)

    table = tableList[int(table)-1][0]

    newValues = []
    print "Which FIELD to search for records? :"
    print "***********************"
    cursor = conn.execute('SELECT * from '+table)
    headers = [description[0] for description in cursor.description]    
    for i in range(0,len(headers)):
        print str(i+1) + ":  " +headers[i]

    search = raw_input("To choose a FIELD, enter number. Any other key for main menu: ")

    #check if a number
    try:
        number = int(search)
    except ValueError:
        print ""
        print ""
        getChoice(conn)

    search = headers[int(search) - 1]
    print ""
    query = raw_input("Search table '"+table+"' where '" + search+  "' = ")
    print ""
    
    cursor = (conn.execute("SELECT * FROM " + table +" where " + search +" = '" + query+"'"))

    showRows = cursor.fetchall()
    print headers
    for row in showRows:
        print row

    print ""
    print " *** THESE RECORDS WILL BE DELETED!!! *** "
    confirm = raw_input("Type 'YES' to confirm deletion, any other key to abort :")

    if confirm == 'YES':
        cursor = conn.execute("DELETE FROM " + table +" where " + search +" = '" + query+"'")
        print ""
        print raw_input(" *** RECORDS DELETED *** any key to continue")
        getChoice(conn)
    else:
        print""
        print""

        getChoice(conn)



def deleteTable(conn):

    cursor = conn.execute("SELECT name FROM sqlite_master \
        WHERE type = 'table'\
        ORDER BY name;")
    
    tableList = cursor.fetchall()
    print "ALL TABLES IN DATABASE:"
    print "***********************"
    for t in range(0,len(tableList)):
        print str(t+1) + ": " + tableList[t][0]

    print ""
    print ""
    tableChoice = raw_input("To delete a table, enter number. Any other key for main menu: ")

    #check if a number
    try:
        number = int(tableChoice)
    except ValueError:
        print ""
        print ""
        getChoice(conn)
    else:
        if (int(tableChoice) <= len(tableList)) and (int(tableChoice) > 0):
            confirm = raw_input("DELETE TABLE " + "'" +tableList[int(tableChoice)-1][0] + "? - TYPE 'YES' to confirm: ")
        else:
            print ""
            print ""
            getChoice(conn)             

        if (confirm == "YES"):
            try:
                conn.execute("DROP TABLE" + "'" +tableList[int(tableChoice)-1][0] +"'")
                print ""
                print "*** TABLE DELETED ***"
                print raw_input("Any key to acknowledge: :")                
            except sqlite3.Error:
                print ""
                print "*** ERROR: Table Delete not allowed. ***"
                print raw_input("Any key to acknowledge: :")
            else:
                print "TABLE DELTE ABORTED"
        else:
            print ""
            print "TABLE DELETE ABORTED"
            print raw_input("Any key to acknowledge: :")
        print ""
        print ""
        getChoice(conn)
        
        


main()
