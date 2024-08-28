import sqlite3
book=sqlite3.connect("Bookstore.db")
curbook=book.cursor()

total = 0
while True:
    curbook.execute("SELECT * FROM books")
    book_list=curbook.fetchall() 
    print(book_list,"\n")
    ttl=input("Enter Book's Title: ")
    sql = "SELECT * FROM books WHERE Title = '"+ttl+"'"
    curbook=book.cursor()
    curbook.execute(sql)
    rec=curbook.fetchone()
    if rec!=None:
        print(rec)
        price=rec[3]
        qty=int(input("Enter no. of books purchased: "))
        cost=price*qty
        total+=cost
    else:
        print("Book not available")
    choice=input("add more books[Y/N]?")
    if choice == "N": break
print("Total cost: ",total)

book.close()