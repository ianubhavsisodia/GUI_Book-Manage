import sqlite3
book=sqlite3.connect("Bookstore.db")
curbook=book.cursor()

curbook.execute('''CREATE TABLE books(
BookID INTEGER PRIMARY KEY AUTOINCREMENT,
Title TEXT (20) NOT NULL,
Author TEXT (20),
Price REAL);''')

for x in range(5):
    ttl=input("Enter the title of the book: ")
    ath=input("Enter the Author of book: ")
    pr=float(input("Enter the price of book: "))
    sql= "INSERT INTO books (title, author, price) VALUES ('"+ttl+"','"+ath+"','"+str(pr)+"');"

    try:
        curbook=book.cursor()
        curbook.execute(sql)
        book.commit()
        print('Record added successfully.')
    except:
        print('Error while adding record!')
        book.rollback()

book.close()
