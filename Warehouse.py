import mysql.connector


# ------------------ DATABASE CONNECTION ------------------
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="amazon_warehouse"
)
mycursor = mydb.cursor()


# ------------------ SIGNUP TABLE ------------------
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS signup(
        username VARCHAR(20),
        user_emailid VARCHAR(30),
        password VARCHAR(20)
    )
""")


# ------------------ DATABASE SETUP ------------------
def create_tables():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="amazon_warehouse"
    )
    mycursor = mydb.cursor()

    print("Creating ITEMS table...")
    sql = """CREATE TABLE IF NOT EXISTS items(
                item_code INT(4) PRIMARY KEY,
                item_name CHAR(30) NOT NULL,
                price FLOAT(8,2),
                item_qty INT(4),
                item_cat CHAR(30)
            )"""
    mycursor.execute(sql)

    print("Creating ORDERS table...")
    sql = """CREATE TABLE IF NOT EXISTS warehouse_orders(
                item_pcode CHAR(30) NOT NULL,
                price FLOAT(8,2),
                item_qty INT(4),
                supplier CHAR(50),
                item_cat CHAR(30)
            )"""
    mycursor.execute(sql)
    print("ORDER table created")

    print("Creating SALES table...")
    line = """CREATE TABLE IF NOT EXISTS customer_purchases(
                purchase_id INT(4) PRIMARY KEY AUTO_INCREMENT,
                icode CHAR(30),
                iprice FLOAT(8,2),
                iqty INT(4),
                Total DOUBLE(8,2)
            )"""
    mycursor.execute(line)
    print("SALES table created")

    print("Creating STAFF table...")
    mycursor.execute("""
        CREATE TABLE IF NOT EXISTS Staff_details(
            Name VARCHAR(30),
            Gender VARCHAR(10),
            Age INT(3),
            PhoneNumber CHAR(10) UNIQUE KEY,
            Address VARCHAR(40)
        )
    """)
    print("STAFF table created")


# ------------------ USER DETAILS ------------------
def registered_users():
    while True:
        print("\t\t\t 1. DISPLAY ALL USERS REGISTERED")
        print("\t\t\t 2. Back (Main Menu)")
        u = int(input("\t\t Enter Your Choice: "))

        if u == 1:
            display_users()
        if u == 2:
            break


def display_users():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="amazon_warehouse"
    )
    mycursor = mydb.cursor()

    sql = "SELECT username, user_emailid FROM signup"
    mycursor.execute(sql)

    print("\t\t\t\t USER DETAILS")
    print("\t\t", "-" * 30)
    print("\t\t email and names stored on system are ")
    print("\t\t", "-" * 27)

    for i in mycursor:
        print("\t\t", i[0], "\t", i[1])

    print("\t\t", "-" * 30)


# ------------------ ITEM MANAGEMENT ------------------
def item_details():
    while True:
        print("\t\t\t 1. Add New Product")
        print("\t\t\t 2. Display all products")
        print("\t\t\t 3. Search product")
        print("\t\t\t 4. Update product quantity")
        print("\t\t\t 5. Delete product")
        print("\t\t\t 6. Back to menu")

        p = int(input("\t\t Enter Your Choice: "))

        if p == 1:
            add_item()
        elif p == 2:
            display_all()
        elif p == 3:
            search_item()
        elif p == 4:
            update_item()
        elif p == 5:
            delete_item()
        elif p == 6:
            break


def add_item():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="amazon_warehouse"
    )
    mycursor = mydb.cursor()

    code = int(input("\t\t Enter product code: "))
    name = input("\t\t Enter product name: ")
    qty = int(input("\t\t Enter product quantity: "))
    price = float(input("\t\t Enter product unit price: "))
    cat = input("\t\t Enter Product category: ")

    query = "INSERT INTO items VALUES(%s, %s, %s, %s, %s)"
    val = (code, name, price, qty, cat)
    mycursor.execute(query, val)
    mydb.commit()


def search_item():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="amazon_warehouse"
    )
    mycursor = mydb.cursor()

    inp = int(input(
        " ================================= \n"
        " [1] search by item code \n"
        " [2] search by item name \n"
        " [3] search by item price \n"
        " [4] search by item category \n"
        " [5] display all products \n"
        " =================================\n:"
    ))

    if inp == 1:
        search = input("Enter item code: ")
        mycursor.execute("SELECT * FROM items WHERE item_code=%s", (search,))
    elif inp == 2:
        search = input("Enter item name: ")
        mycursor.execute("SELECT * FROM items WHERE item_name=%s", (search,))
    elif inp == 3:
        search = input("Enter price: ")
        mycursor.execute("SELECT * FROM items WHERE price=%s", (search,))
    elif inp == 4:
        search = input("Enter category: ")
        mycursor.execute("SELECT * FROM items WHERE item_cat=%s", (search,))
    elif inp == 5:
        display_all()
        return

    result = mycursor.fetchall()
    print("|| code || item name || item price || item quantity || item category ||")
    print("=" * 60)
    for x in result:
        print(x)


def display_all():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="amazon_warehouse"
    )
    mycursor = mydb.cursor()

    print("==================== \n Displaying all items \n====================")
    mycursor.execute("SELECT * FROM items")
    result = mycursor.fetchall()

    print("|| code || item name || item price || item quantity || item category ||")
    print("=" * 60)
    for x in result:
        print(x)


def update_item():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="amazon_warehouse"
    )
    mycursor = mydb.cursor()

    code = int(input("Enter the product code: "))
    qty = int(input("Enter the quantity to add: "))

    sql = "UPDATE items SET item_qty=item_qty+%s WHERE item_code=%s"
    val = (qty, code)
    mycursor.execute(sql, val)
    mydb.commit()

    print("\t\t Item details updated")


def delete_item():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="amazon_warehouse"
    )
    mycursor = mydb.cursor()

    i_code = int(input("Enter code of the item you wish to delete: "))
    sql = "DELETE FROM items WHERE item_code=%s"
    val = (i_code,)
    mycursor.execute(sql, val)
    mydb.commit()

    print(mycursor.rowcount, "record(s) deleted")


# ------------------ ORDER MANAGEMENT ------------------
def order_details():
    while True:
        print("\t\t\t 1. Add Order")
        print("\t\t\t 2. Display Orders")
        print("\t\t\t 3. Back (Main Menu)")

        o = int(input("\t\t Enter Your Choice: "))

        if o == 1:
            add_order()
        elif o == 2:
            display_orders()
        elif o == 3:
            break


def add_order():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="amazon_warehouse"
    )
    mycursor = mydb.cursor()

    code = int(input("Enter product code: "))
    qty = int(input("Enter product quantity: "))
    price = float(input("Enter product unit price: "))
    cat = input("Enter product category: ")
    supplier = input("Enter Supplier details: ")

    query = "INSERT INTO warehouse_orders VALUES(%s, %s, %s, %s, %s)"
    val = (code, price, qty, supplier, cat)
    mycursor.execute(query, val)
    mydb.commit()


def display_orders():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="amazon_warehouse"
    )
    mycursor = mydb.cursor()

    sql = "SELECT * FROM warehouse_orders"
    mycursor.execute(sql)

    print("\t\t\t\t\t ORDER DETAILS")
    print("-" * 85)
    print("orderid || price || quantity || supplier || category")
    print("-" * 85)

    for i in mycursor:
        print(i[0], "\t", i[1], "\t", i[2], "\t", i[3], "\t", i[4])


# ------------------ PURCHASE MANAGEMENT ------------------
def customer_purchase():
    while True:
        print("\t\t\t 1. Add purchase")
        print("\t\t\t 2. Display User purchase transaction")
        print("\t\t\t 3. Cancel purchase")
        print("\t\t\t 4. Back (Main Menu)")

        s = int(input("\t\t Enter Your Choice: "))

        if s == 1:
            add_purchase()
        elif s == 2:
            display_purchase()
        elif s == 3:
            delete_purchase()
        elif s == 4:
            break


def add_purchase():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="amazon_warehouse"
    )
    mycursor = mydb.cursor()

    icode = input("Enter product code: ")
    sql = "SELECT count(*) FROM items WHERE item_code=%s"
    val = (icode,)
    mycursor.execute(sql, val)

    for x in mycursor:
        cnt = x[0]

    if cnt != 0:
        sql = "SELECT * FROM items WHERE item_code=%s"
        mycursor.execute(sql, val)

        for x in mycursor:
            print(x)
            price = int(x[2])
            iqty = int(x[3])

        qty = int(input("Enter no of quantity: "))

        if qty <= iqty:
            total = qty * price
            print("Total amount to pay: ", total)

            sql = "INSERT INTO customer_purchases (icode, iprice, iqty, total) VALUES(%s, %s, %s, %s)"
            val = (icode, price, qty, total)
            mycursor.execute(sql, val)

            sql = "UPDATE items SET item_qty=item_qty-%s WHERE item_code=%s"
            val = (qty, icode)
            mycursor.execute(sql, val)

            mydb.commit()
        else:
            print("Quantity not available")
    else:
        print("Product is not available")


def display_purchase():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="amazon_warehouse"
    )
    mycursor = mydb.cursor()

    sql = "SELECT * FROM customer_purchases"
    mycursor.execute(sql)

    print("\t\t\t\t USER PURCHASE DETAILS")
    print("-" * 80)
    print("|| purchaseid || item code || item price || item quantity || total purchase amount ||")
    print("=" * 70)

    for x in mycursor:
        print(x[0], "\t", x[1], "\t", x[2], "\t", x[3], "\t", x[4])


def delete_purchase():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="amazon_warehouse"
    )
    mycursor = mydb.cursor()

    id = int(input("Enter purchase id to be deleted: "))
    sql = "DELETE FROM customer_purchases WHERE purchase_id=%s"
    cap = (id,)
    mycursor.execute(sql, cap)
    mydb.commit()

    print(mycursor.rowcount, "record(s) deleted")


# ------------------ STAFF MANAGEMENT ------------------
def staff_details():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="amazon_warehouse"
    )
    mycursor = mydb.cursor()

    print("1: New staff entry")
    print("2: Remove staff")
    print("3: Existing staff details")

    ch = int(input("Enter your choice: "))

    # NEW STAFF ENTRY
    if ch == 1:
        fname = input("Enter name: ")
        gender = input("Gender(M/F/O): ")
        age = int(input("Enter your Age: "))
        phno = input("Staff phone no.: ")
        add = input("Address: ")

        mycursor.execute(
            "INSERT INTO Staff_details(Name, Gender, Age, PhoneNumber, Address) VALUES(%s, %s, %s, %s, %s)",
            (fname, gender, age, phno, add)
        )
        mydb.commit()

        print("""+++++++++++++++++++++++++++++
+ STAFF IS SUCCESSFULLY ADDED +
+++++++++++++++++++++++++++++""")

    # REMOVE STAFF
    elif ch == 2:
        nm = input("Enter staff name to remove: ")
        mycursor.execute("SELECT name FROM Staff_details WHERE name=%s", (nm,))
        pin = mycursor.fetchone()

        if pin is not None:
            mycursor.execute("DELETE FROM Staff_details WHERE name=%s", (nm,))
            mydb.commit()
            print("""+++++++++++++++++++++++++++++++++
++ STAFF IS SUCCESSFULLY REMOVED ++
+++++++++++++++++++++++++++++++++""")
        else:
            print("STAFF DOES NOT EXIST!!!!!!")

    # EXISTING STAFF DETAILS
    elif ch == 3:
        sql = "SELECT * FROM Staff_details"
        mycursor.execute(sql)

        print("\t\t\t\t STAFF DETAILS")
        print("\t\t", "-" * 50)
        print("|| employee name || gender || age || phone no. || Address ||")
        print("=" * 70)

        for i in mycursor:
            print("\t\t", i[0], "\t", i[1], "\t", i[2], "\t", i[3], "\t", i[4])

        print("\t\t", "-" * 50)

    else:
        print("NO STAFF EXISTS!!!!!!!")
    mydb.commit()


# ------------------ LOGIN SYSTEM ------------------
while True:
    print("""1: Signup
2: Login""")
    ch = int(input("SIGNUP/LOGIN (1,2): "))

    # SIGNUP
    if ch == 1:
        username = input("USERNAME: ")
        pw = input("PASSWORD: ")
        email = input("Enter email: ")

        mycursor.execute(
            "INSERT INTO signup VALUES(%s, %s, %s)",
            (username, email, pw)
        )
        mydb.commit()

    # LOGIN
    elif ch == 2:
        username = input("USERNAME: ")
        mycursor.execute("SELECT username FROM signup WHERE username=%s", (username,))
        pot = mycursor.fetchone()

        if pot is not None:
            print("VALID USERNAME!!!!!!")
            pw = input("PASSWORD: ")
            mycursor.execute("SELECT password FROM signup WHERE password=%s", (pw,))
            a = mycursor.fetchone()

            if a is not None:
                print("LOGIN SUCCESSFUL!!!")
                # Admin Menu again here
            else:
                print("INCORRECT PASSWORD")
        else:
            print("INVALID USERNAME")

    else:
        break
