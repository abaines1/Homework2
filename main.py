import database


def prompt_add_item():
    ItemName = input("What is the name of the item?: ")
    Category = input("What is the type of item?: ")
    Manufacture = input("What is the name of the manufacturer?: ")
    Cost = input("What is the cost of the item?: ")
    Quantity = input("How many would you like to add?: ")

    database.add_item(ItemName, Category, Manufacture, Cost, Quantity)

def prompt_delete_item():
    delete_id = input("What is the ID of the item you would like to delete?: ")
    print(database.delete_item(delete_id))


def prompt_for_search(prompt):
    if prompt == "Name":
        prompt2 = input("What is the item's name?: ")
        xList = database.search_by_name(prompt2)
        xName = xList[0][0]
        xQuantity = xList[0][1]
        if xQuantity == 0:
            print(f"Error! We are sold out of {xName}!\n")
        else:
            print(f"There are: {xQuantity} of them!\n")
    elif prompt == "Category":
        prompt3 = input("What is the category of item you're searching for?: ")
        yList = database.search_by_category(prompt3)
        print_inventory(yList)
    else:
        print("Error! Try again!")


def prompt_stock_update():
    stock_prompt = input("How many of the items are there?: ")
    name_prompt = input("What is the name of the item you are updating?: ")

    database.update_stock(stock_prompt, name_prompt)
    print("Success!\n")

def prompt_add_delivery_info():
    #EmployeeID, ItemID, DeliveryDay
    EmployeeID = input("What is the employee's ID?:" )
    ItemID = input("What is the ItemID of the object being delivered?: ")
    DeliveryDay = input("What day is the item delivered?: ")

    database.add_delivery_info(EmployeeID, ItemID, DeliveryDay)

def prompt_add_employee():
    FirstName = input("What is your first name?: ")
    LastName = input("What is your last name?: ")
    PhoneNumber = input("What is your phone number (numbers only)?: ")

    database.add_employee(FirstName, LastName, PhoneNumber)

def prompt_add_manufacture():
    Manufacture = input("What is the manufacture's name?: ")
    Address = input("What is the address of the manufacturer?: ")
    DeliveryDay = input("What is the delivery day?")

    database.add_manufacturer(Manufacture, Address, DeliveryDay)

def print_inventory(inventory_list):
    for ItemID, ItemName, Category, Manufacture, Cost, Quantity in inventory_list:
         print(f"ID: {ItemID} - Item Name: {ItemName} - Category: {Category} - Manufacture: {Manufacture} - Cost: ${Cost} - Quantity: {Quantity}")


def print_delivery_info(delivery_list):
    for EmployeeID, ItemID, DeliveryDay in delivery_list:
        print(f"EmployeeID: {EmployeeID} = ItemID: {ItemID} - DeliveryDay: {DeliveryDay}")


menu = '''Welcome to AB Hardware!

Please choose one of the following:
1. View Inventory
2. View Sold Out Inventory
3. Insert Item
4. Delete Item
5. Search
6. Update Stock
7. Add Delivery Information
8. View Delivery Information
9. Create employee
10. Create Manufacturer
11. Exit

Your Selection:
 
'''''

database.create_tables()

while (user_input := input(menu)) != '6':
    # 1 view inventory
    if user_input == '1':
        inventory_list = database.view_inventory()
        print_inventory(inventory_list)
    # 2 view sold out inventory
    elif user_input == '2':
        sold_out_list = database.view_sold_out_inventory()
        print_inventory(sold_out_list)
    # 3 Insert Item
    elif user_input == '3':
        prompt_add_item()
    # 4 Delete an item
    elif user_input == '4':
        prompt_delete_item()
    elif user_input == '5':
        prompt = input("Would you like to search by name or category?: ")
        prompt_for_search(prompt)
    elif user_input == '6':
        prompt_stock_update()
    elif user_input == '7':
        prompt_add_delivery_info()
    elif user_input == '8':
        delivery_list = database.view_delivery_info()
        print_delivery_info(delivery_list)
    elif user_input == '9':
        prompt_add_employee()
    elif user_input == '10':
        prompt_add_manufacture()
    else:
        pass
