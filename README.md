# 🏬 Warehouse Stock Management System (Python + MySQL)

This is a command-line based Warehouse Stock Management System built using Python and MySQL. It supports user authentication, an admin panel, and database operations such as managing products, orders, staff, and purchases.

---

## ⚙️ Features

- User Signup and Login
- Admin Panel with menu-based navigation
- MySQL-based database setup and table creation
- Management for:
  - Registered Users
  - Products
  - Orders
  - Customer Purchases
  - Staff

---

## 🛠️ Setup Instructions

### 🔗 Prerequisites

- Python 3.x
- MySQL Server
- `mysql-connector-python` library

### 📦 Install Dependencies

Open your terminal and run:

```bash
pip install mysql-connector-python
```

### 🧩 MySQL Setup

1. Start your MySQL server.
2. Open MySQL Shell or Workbench and run:

```sql
CREATE DATABASE amazon_warehouse;
```

3. Update database credentials in the code if necessary:

```python
mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="amazon_warehouse"
)
```

---

## 🔐 Authentication Flow

1. **Signup**: Enter username, email, and password to register.
2. **Login**: Enter username and password to access the admin panel.

---

## 🖥️ Admin Menu Options

Once logged in as admin, the following options are available:

```
1. USER DETAILS         → View all registered users (to be implemented)
2. PRODUCT MANAGEMENT   → Add/View products (to be implemented)
3. ORDER MANAGEMENT     → Handle warehouse orders (to be implemented)
4. PURCHASE MANAGEMENT  → Track customer purchases (to be implemented)
5. STAFF DETAILS        → View staff records (to be implemented)
6. DATABASE SETUP       → Creates necessary tables in the database
7. EXIT                 → Exit the admin panel
```

---

## 📁 File Structure

This version uses a single Python file to manage all features and logic.

---

## 📝 Notes

- All database interactions are handled via MySQL Connector.
- Make sure MySQL Server is running before launching the script.
- Table creation will automatically run from the admin panel (Option 6).

---

## 📬 Contact

For questions or improvements, feel free to reach out:

**Name**: Sami Ahmed  
**Email**: [syedsami2005@gmail.com]
