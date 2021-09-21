import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="oscar_nominees"
)

print(mydb)
mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE oscar_nominees")

#mycursor.execute("SHOW DATABASES")
#for db in mycursor:
#print(db)

#mycursor.execute("CREATE TABLE Nominees (first_name VARCHAR(50), last_name VARCHAR(50), age int, movie VARCHAR(50), personID int PRIMARY KEY AUTO_INCREMENT )")
#mycursor.execute("SHOW TABLES")

#for tb in mycursor:
#print(tb)

def mainMenu():
    print("1. Make a new entry")
    print("2. Update an existing entry")
    print("3. Delete an entry")
    print("4. Display all entries")
    print("5. Quit")
    while True:
        try:
            choice = int(input("Enter your selection>> "))
            if choice == 1:
                insert()
                break
            elif choice == 2:
                update()
                break
            elif choice == 3:
                delete()
                break
            elif choice == 4:
                display()
                break
            elif choice == 5:
                break
            else:
                print("Invalid choice. Select 1-5")
        except ValueError:
            print("Invalid choice. Select 1-5")
    exit

def insert():
     fname = str(input("Enter the actor's first name >> "))
     lname = str(input("Enter the actor's last name >> "))
     a = int(input("Enter the actor's age>> "))
     film = str(input("Enter the movie>> "))

     mycursor.execute("INSERT INTO Nominees (first_name, last_name, age, movie) VALUES (%s, %s, %s, %s)", (fname, lname, a, film))
     mydb.commit()
     print("Successfully Inserted!")
     mycursor.execute("SELECT * FROM Nominees")
     for x in mycursor:
      print(x)
     home = input("Press any key to return to the main menu ")
     mainMenu()

def update():
    print("Which field would you like to update")
    print("1. First name")
    print("2. Last name")
    print("3. Age")
    print("4. Movie")
    print("5. Quit")
    while True:
        try:
            choice = int(input("Enter your selection>> "))
            if choice == 1:
                old_fname = int(input("Enter the person ID>> "))
                fname = str(input("Enter the new first name>> "))

                sql = "Update Nominees SET first_name = %s WHERE personID= %s"
                val = (fname, old_fname)

                mycursor.execute(sql, val)
                mydb.commit()
                break
            elif choice == 2:
                old_lname = int(input("Enter the person ID>> "))
                lname = str(input("Enter the new last name>> "))

                sql = "Update Nominees SET last_name = %s WHERE personID = %s"
                val = (lname, old_lname)

                mycursor.execute(sql, val)
                mydb.commit()
                break
            elif choice == 3:
                old_age = int(input("Enter the person ID>> "))
                age = int(input("Enter the new age>> "))

                sql = "Update Nominees SET age = %s WHERE personID = %s"
                val = (age, old_age)

                mycursor.execute(sql, val)
                mydb.commit()
                break
            elif choice == 4:
                old_movie = int(input("Enter the person ID>> "))
                movie = str(input("Enter the new movie>> "))

                sql = "Update Nominees SET movie = %s WHERE personID= %s"
                val = (movie, old_movie)

                mycursor.execute(sql, val)
                mydb.commit()
                break
            elif choice == 5:
                break
            else:
                print("Invalid choice. Select 1-5")
        except ValueError:
            print("Invalid choice. Select 1-5")
    exit
    print("Successfully Updated!")
    home = input("Press any key to return to the main menu ")
    mainMenu()

def delete():
    id = int(input("Enter the person ID>> "))
    sql = "DELETE FROM Nominees WHERE personID = %s"
    val = (id,)

    mycursor.execute(sql, val)
    mydb.commit()
    print("Successfully Deleted!")
    home = input("Press any key to return to the main menu ")
    mainMenu()

def display():
    print("Compiling Data...")
    mycursor.execute("SELECT * FROM Nominees")

    for x in mycursor:
     print(x)
    home = input("Press any key to return to the main menu ")
    mainMenu()


mainMenu()