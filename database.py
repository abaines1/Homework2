import sqlite3

'''
Database:

Delivery: EmployeeID, ItemID, Delivery_Day
ContactInfo: EmployeeID, FirstName, LastName, PhoneNumber
Manufacturer: ManufactureID, Manufacture, Address, DeliveryDay
Inventory: ItemID, ItemName, Manufacture, Category, Cost, Quantity

'''

CREATE_INVENTORY_TABLE = ''' CREATE TABLE IF NOT EXISTS Inventory (
    ItemID INTEGER PRIMARY KEY AUTOINCREMENT,
    ItemName TEXT,
    Category TEXT,
    Manufacture TEXT,
    Cost INTEGER,
    Quantity INTEGER,
    FOREIGN KEY(ItemID) REFERENCES Delivery(ItemID)
);'''

CREATE_MANUFACTURE_TABLE = ''' CREATE TABLE IF NOT EXISTS Manufacture (
    ManufactureID INTEGER PRIMARY KEY AUTOINCREMENT,
    Manufacture TEXT,
    Address TEXT,
    DeliveryDay TEXT,
    FOREIGN KEY(ManufactureID) REFERENCES Employee(ManufactureID)
);'''

CREATE_DELIVERY_TABLE = ''' CREATE TABLE IF NOT EXISTS Delivery (
    EmployeeID INTEGER PRIMARY KEY AUTOINCREMENT,
    ItemID INTEGER,
    DeliveryDay TEXT,
    FOREIGN KEY(ItemID) REFERENCES inventory(ItemID),
    FOREIGN KEY(EmployeeID) REFERENCES Employee(EmployeeID)
);'''

CREATE_EMPLOYEE_TABLE = ''' CREATE TABLE IF NOT EXISTS Employee (
    EmployeeID INTEGER PRIMARY KEY AUTOINCREMENT,
    ManufactureID INTEGER,
    FirstName TEXT,
    LastName TEXT,
    PhoneNumber TEXT,
    FOREIGN KEY(EmployeeID) REFERENCES Delivery(EmployeeID)
    FOREIGN KEY (ManufactureID) REFERENCES Manufacture(ManufactureID)
);'''

SELECT_INVENTORY = "SELECT * FROM inventory;"
SELECT_SOLD_OUT_INVENTORY = "SELECT * FROM inventory WHERE inventory.quantity = 0;"
SELECT_BY_NAME = "SELECT ItemName, Quantity FROM inventory WHERE ItemName = (?);"
SELECT_BY_CATEGORY = "SELECT * FROM inventory WHERE Category = (?);"
SELECT_DELIVERY_INFORMATION = "SELECT * FROM DELIVERY"

INSERT_ITEM = "INSERT INTO Inventory(ItemName, Category, Manufacture, Cost, Quantity) VALUES (?, ?, ?, ?, ?)"
INSERT_DELIVERY_INFO = "INSERT INTO Delivery(EmployeeID, ItemID, DeliveryDay) VALUES (?, ?, ?)"
INSERT_EMPLOYEE = "INSERT INTO Employee(FirstName, LastName, PhoneNumber) VALUES (?, ?, ?)"
INSERT_MANUFACTURER = "INSERT INTO Manufacture(Manufacture, Address, DeliveryDay) VALUES (?, ?, ?)"

DELETE_ITEM = "DELETE FROM inventory where ItemID = (?)"

UPDATE_STOCK = "UPDATE Inventory SET Quantity = (?) WHERE ItemName = (?)"


connection = sqlite3.connect("InventorySystem.db")


def create_tables():
    with connection:
        connection.execute(CREATE_INVENTORY_TABLE)
        connection.execute(CREATE_MANUFACTURE_TABLE)
        connection.execute(CREATE_DELIVERY_TABLE)
        connection.execute(CREATE_EMPLOYEE_TABLE)


def add_item(ItemName, Category, Manufacture, Cost, Quantity):
    with connection:
        connection.execute(INSERT_ITEM, (ItemName, Category, Manufacture, Cost, Quantity))

def delete_item(id):
    with connection:
        connection.execute((DELETE_ITEM), (id,))


def view_inventory():
    cursor = connection.cursor()

    cursor.execute(SELECT_INVENTORY)
    return cursor.fetchall()

def view_sold_out_inventory():
    cursor = connection.cursor()

    cursor.execute(SELECT_SOLD_OUT_INVENTORY)
    return cursor.fetchall()

def search_by_name(ItemName):
    cursor = connection.cursor()

    cursor.execute(SELECT_BY_NAME, (ItemName,))
    return cursor.fetchall()

def search_by_category(Category):
    cursor = connection.cursor()

    cursor.execute(SELECT_BY_CATEGORY, (Category,))
    return cursor.fetchall()

def update_stock(Quantity, ItemName):
    with connection:
        connection.execute(UPDATE_STOCK, (Quantity, ItemName))

def add_delivery_info(EmployeeID, ItemID, DeliveryDay):
    with connection:
        connection.execute(INSERT_DELIVERY_INFO, (EmployeeID, ItemID, DeliveryDay,))

def view_delivery_info():
    cursor = connection.cursor()

    cursor.execute(SELECT_DELIVERY_INFORMATION)
    return cursor.fetchall()

def add_employee(FirstName, LastName, PhoneNumber):
    with connection:
        connection.execute(INSERT_EMPLOYEE, (FirstName, LastName, PhoneNumber))

def add_manufacturer(Manufacture, Address, DeliveryDay):
    with connection:
        connection.execute(INSERT_MANUFACTURER, (Manufacture, Address, DeliveryDay))








