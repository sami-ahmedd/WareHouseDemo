import mysql.connector

def connect_db():
    return mysql.connector.connect(host="localhost", user="root", password="root", database="amazon_warehouse")

def create_signup_table():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS signup (
            username VARCHAR(20),
            user_emailid VARCHAR(30),
            password VARCHAR(20)
        )
    """)
    db.commit()
    cursor.close()
    db.close()

def signup():
    db = connect_db()
    cursor = db.cursor()
    username = input("USERNAME: ")
    pw = input("PASSWORD: ")
    email = input("Enter email: ")
    try:
        cursor.execute("INSERT INTO signup (username, user_emailid, password) VALUES (%s, %s, %s)", (username, email, pw))
        db.commit()
        print("Signup successful!")
    except Exception as e:
        print("Error during signup:", e)
    cursor.close()
    db.close()

def login():
    db = connect_db()
    cursor = db.cursor()
    username = input("USERNAME: ")
    pw = input("PASSWORD: ")
    cursor.execute("SELECT * FROM signup WHERE username=%s AND password=%s", (username, pw))
    user = cursor.fetchone()
    if user:
        print("+++ LOGIN SUCCESSFUL +++")
        admin_menu()
    else:
        print("Invalid username or password.")
    cursor.close()
    db.close()

def admin_menu():
    while True:
        print("""
        \n\n\t\t\t STOCK MANAGEMENT FOR ADMIN
        \t\t\t **************************
        \t\t 1. USER DETAILS
        \t\t 2. PRODUCT MANAGEMENT
        \t\t 3. ORDER MANAGEMENT
        \t\t 4. PURCHASE MANAGEMENT
        \t\t 5. STAFF DETAILS
        \t\t 6. DATABASE SETUP
        \t\t 7. EXIT
        """)
        try:
            n = int(input("Enter your choice: "))
            if n == 1:
                print("Show Registered Users")  # Call function here
            elif n == 2:
                print("Manage Items")  # Call function here
            elif n == 3:
                print("Order Management")  # Call function here
            elif n == 4:
                print("Purchase Management")  # Call function here
            elif n == 5:
                print("Staff Details")  # Call function here
            elif n == 6:
                create_tables()
            elif n == 7:
                print("Exiting admin panel...")
                break
            else:
                print("Invalid Choice")
        except ValueError:
            print("Please enter a valid number.")

def create_tables():
    db = connect_db()
    cursor = db.cursor()
    print("Creating ITEMS table")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS items (
            item_code INT PRIMARY KEY,
            item_name CHAR(30) NOT NULL,
            price FLOAT(8,2),
            item_qty INT,
            item_cat CHAR(30)
        )
    """)
    print("Creating ORDERS table")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS warehouse_orders (
            item_pcode CHAR(30) NOT NULL,
            price FLOAT(8,2),
            item_qty INT,
            supplier CHAR(50),
            item_cat CHAR(30)
        )
    """)
    print("Creating SALES table")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customer_purchases (
            purchase_id INT PRIMARY KEY AUTO_INCREMENT,
            icode CHAR(30),
            iprice FLOAT(8,2),
            iqty INT,
            total DOUBLE(8,2)
        )
    """)
    print("Creating STAFF table")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS staff_details (
            name VARCHAR(30),
            gender VARCHAR(10),
            age INT,
            phoneNumber CHAR(10) UNIQUE,
            address VARCHAR(40)
        )
    """)
    db.commit()
    cursor.close()
    db.close()
    print("All tables created successfully.")

# Main driver
create_signup_table()
while True:
    print("1: Signup\n2: Login\n3: Exit")
    choice = input("Enter choice: ")
    if choice == '1':
        signup()
    elif choice == '2':
        login()
    elif choice == '3':
        print("Exiting program...")
        break
    else:
        print("Invalid choice.")
