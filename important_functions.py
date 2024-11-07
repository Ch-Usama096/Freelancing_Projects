# Import the Modules
import csv
import os
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

# Create the Function to load the Data from the CSV File
def load_csv_file(csv_path):
    # Open the CSV File
    with open(csv_path , encoding = "utf-8-sig") as file_data:
        # Define the List for Save the Data
        csv_data = []
        # Read the Data from the CSV File 
        object = csv.DictReader(file_data)
        # Read the Data Line By Line
        for row_data in object:
            # Get the All Keys from the Dictionary
            keys = list(row_data.keys())
            # Save the Data in the List
            id = row_data["id"]
            dic_data = {}
            dic_data[id] = {}
            for index in range(0, len(row_data)):
                # Now Add the Full Records in the Dictionary according to the ID
                if keys[index] != "id":
                    dic_data[id][keys[index]] = row_data[keys[index]]
            csv_data.append(dic_data)
    return csv_data

# Create the Function to save the Data into the CSV File
def save_data_csv(data , filename):
    
    # Ope the CSV File
    file_path = f"updated_csv_files\\{filename}"
    with open(file_path , mode = "w" , newline = "") as file:
        write_data = csv.writer(file)
        # Add the Header Row in the CSV File
        keys = list(list(data[0].values())[0].keys())
        keys.insert(0 , "id")
        write_data.writerow(keys)
        # Now ADD the Data in the CSV File
        for index in range(0,len(data)):
            new_list = []
            for id , dic in data[index].items():
                new_list.append(id)
                for _ , values in dic.items():
                    new_list.append(values)
            write_data.writerow(new_list)

# Create the to load the Data from the User CSV File
def load_user_csv(csv_path):
    # Define the List for Save the Data
    csv_data = []
    # Open the CSV File
    with open(csv_path , encoding = "utf-8-sig") as file_data:
        # Read the Data from the CSV File
        object = csv.DictReader(file_data)
        # Read the Data Line By Line
        for row_data in object:
            # Save the Data in the List
            keys = list(row_data.keys())
            min_list = []
            for key in keys:
                min_list.append(row_data[key])
            csv_data.append(min_list)
    return csv_data



# Create the Function for Getting the Password and UserName For the Define the Type
def login():
    # Load the User CSV File
    user_file_path = r"CSV_Files\\users.csv"
    user_file_data = load_user_csv(user_file_path)

    # Get the Information from the User
    username = input("Enter your username==>")
    password = input("Enter your password==>")

    # Check the UserName and Paaword in the USER CSV File
    for index in range(0,len(user_file_data)):
        # Check the Username and Password
        if username == user_file_data[index][0] and password == user_file_data[index][1]:
            os.system("cls")
            print(f"Welcome {user_file_data[index][2]} : {username}")
            return user_file_data[index][2] , username
    return 0 , 0


# Create the Function for the Manager & Cashier MAIN MANU
def main_manu():
    # Define the Main Manu
    print("\nMain Manu\n")
    print("Press 1 : Sales Transaction")
    print("Press 2 : Add New Grocery Product (Only For Manager)")
    print("Press 3 : Logout")
    print("Press 4 : Search Transaction by Date")
    print("Press 5 : Search Transaction by Product")
    print("Press 6 : Search Transaction by Date & Product")
    print("Press 7 : Update Grocery Info")
    print("Press 8 : Display Sales Monthly")
    print("Press 9 : Display Sales Monthly with Product Ids")
    print("Press 10 : Display Sales of Each Product")

    # Get the option form the User
    choice = int(input("Please Enter your Choice==>"))
    return choice



# Create the Function for the Searching of Transaction with Date
def transaction_by_date(transaction_data):
    # Getting the Searching Date from User
    os.system("cls")
    user_date = input("Enter the Date (Day/Month/Year) for the Searching Transaction==>")
    
    # Get the Transaction Data 
    search_transaction = []
    for index in range(0,len(transaction_data)):
        for _ , product_details in transaction_data[index].items():
            # Now Check the User Date with Transaction Date
            if user_date == product_details["date"]:
                search_transaction.append(transaction_data[index])
    # Return the Search Transaction Data
    return search_transaction



# Create the Function for the Searching Transaction with Product Name
def transaction_by_name(transaction_data , groceries_data):
    # Get the Name of the Product from the User
    os.system("cls")
    user_product_name = input("Enter the Product Name==>").lower()

    # Search the Transaction Data in the Transaction File
    search_transaction = []
    for index in range(0,len(groceries_data)):
        groceries_id = list(groceries_data[index].keys())[0]
        product_name = list(groceries_data[index][groceries_id].values())[0].lower()
        # Check the User Product Name with the File Data Product Name
        if user_product_name in product_name:
            # Now get the Trasaction from the Transaction Data File
            for index1 in range(0,len(transaction_data)):
                transaction_id = list(transaction_data[index1].keys())[0]
                # Now, Extract the Transaction Data from the Transaction File
                if groceries_id == transaction_id:
                    search_transaction.append(transaction_data[index1])
    # Return the Search Transaction 
    return search_transaction



# Create the Functions for the Searching Transaction using Date and Name
def transaction_by_name_date(transaction_data , groceries_data):
    # Get the Data from the User
    os.system("cls")
    start_date   = input("Enter the Starting Date (Day/Month/Year) for the Searching Transaction==>")
    end_date     = input("Enter the Ending   Date (Day/Month/Year) for the Searching Transaction==>")
    user_product_name = input("Enter the Product Name==>").lower()

    # Converting the Date into the Actuall Format
    start_date = datetime.strptime(start_date , "%d/%m/%Y")
    end_date   = datetime.strptime(end_date   , "%d/%m/%Y")

    # Search the Transaction Data in the Transaction File
    search_transaction = []
    for index in range(0,len(groceries_data)):
        groceries_id = list(groceries_data[index].keys())[0]
        product_name = list(groceries_data[index][groceries_id].values())[0].lower()
        # Check the User Product Name with the File Data Product Name
        if user_product_name in product_name:
            # Now get the Trasaction from the Transaction Data File
            for index1 in range(0,len(transaction_data)):
                transaction_id   = list(transaction_data[index1].keys())[0]
                transaction_date = list(transaction_data[index1][transaction_id].values())[0]
                transaction_date = datetime.strptime(transaction_date   , "%d/%m/%Y")
                # Now, Extract the Transaction Data from the Transaction File
                if (groceries_id == transaction_id) and (start_date <= transaction_date <= end_date): 
                    search_transaction.append(transaction_data[index1])
    # Return the Search Transaction
    return search_transaction



# Create the Functions for update the Details of the Product
def update_details(groceries_data):
    # Get the Data from the User
    os.system("cls")
    user_product_id = input("Enter the Product Id==>")
    new_price       = input("Enter the New Price of the Product==>")
    new_stock_level = input("Enter the New Stcok Level for the Product==>")

    #Now Check the Id with the Groceries Data File
    for index in range(0,len(groceries_data)):
        # Get the Groceries ID 
        groceries_id = list(groceries_data[index].keys())[0]
        # Noe Check the Id's
        if user_product_id == groceries_id:
            # Now Update the Values
            groceries_data[index][groceries_id]["price"] = new_price
            groceries_data[index][groceries_id]["stock"] = new_stock_level
    # Return the All Updated Details
    return groceries_data


# Create the Function for display the sales according to the Month
def display_sales_monthly(transaction_data):

    # Get the Data from the User
    start_date   = input("Enter the Starting Date (Month/Year) for the Searching Transaction==>")
    end_date     = input("Enter the Ending   Date (Month/Year) for the Searching Transaction==>")
    
    # Define the Dicionary for Storing the Data
    all_sales_monthly  ,  counts_sales_monthly = {} , {}

    # Now Iterate over Data
    for index in range(0,len(transaction_data)):
        # Now get the Items 
        for id , transa_info in transaction_data[index].items():
            # Get the Date Data from the Actual Data
            date = datetime.strptime(transa_info["date"] , "%d/%m/%Y")
            month_date = date.strftime("%m/%Y")
           
            # Now filter the data according to the start and end date
            if start_date <= month_date <= end_date:
                # Now Add the Key of the Date in the Dictionary
                if month_date not in all_sales_monthly:
                    # Now Initalization the Dictionary
                    all_sales_monthly[month_date] , counts_sales_monthly[month_date] = 0 , 0
                
                # Now add the Data in the Dictionary
                all_sales_monthly[month_date]    = all_sales_monthly[month_date] + float(transa_info["payment"])
                counts_sales_monthly[month_date] = counts_sales_monthly[month_date] + 1
        
    # Plotting the Data

    # Now Get the Values of each month for the plotting
    sales , count = [] , []
    for key in all_sales_monthly:
        # Get the Values and store 
        sales.append(all_sales_monthly[key])
    for key in counts_sales_monthly:
        count.append(counts_sales_monthly[key])
    date = all_sales_monthly.keys()
    
    # Define the Figure of Plot
    plt.figure(figsize = (12,6))
    plt.plot(date , sales , label = "Monthly Sales" , marker = "x")
    plt.plot(date , count , label = "Total No. of Sales" , marker = "o")
    plt.title("Monthly Sales with total Number of Sales")
    plt.xlabel("Month Sales")
    plt.xticks(rotation = 90)
    plt.ylabel("Total Sales")
    plt.legend()
    plt.show()
    

# Create the Function for display the sales according to the Month with Product Id
def display_sales_monthly_product_id(transaction_data , groceries_data):

    # Get the Data from the User
    start_date   = input("Enter the Starting Date (Month/Year) for the Searching Transaction==>")
    end_date     = input("Enter the Ending   Date (Month/Year) for the Searching Transaction==>")
    product_id   = input("Please the Product Id(1-16) for the Slaes Visualization==>")

    # Now Filter the Product Id with Name
    product_info = {}
    for index in range(0 , len(groceries_data)):
        for id , pro_info in groceries_data[index].items():
            product_info[id] = pro_info["name"]
    
    # Define the Dicionary for Storing the Data
    all_sales_monthly  ,  counts_sales_monthly = {} , {}

     # Now Iterate over Data
    for index in range(0,len(transaction_data)):
        # Now get the Items 
        for id , transa_info in transaction_data[index].items():
            if id == product_id:
                # Get the Date Data from the Actual Data
                date = datetime.strptime(transa_info["date"] , "%d/%m/%Y")
                month_date = date.strftime("%m/%Y")
            
                # Now filter the data according to the start and end date
                if start_date <= month_date <= end_date:
                    # Now Add the Key of the Date in the Dictionary
                    if month_date not in all_sales_monthly:
                        # Now Initalization the Dictionary
                        all_sales_monthly[month_date] , counts_sales_monthly[month_date] = 0 , 0
                    
                    # Now add the Data in the Dictionary
                    all_sales_monthly[month_date]    = all_sales_monthly[month_date] + float(transa_info["payment"])
                    counts_sales_monthly[month_date] = counts_sales_monthly[month_date] + 1
    
    # Plot the Data

    # Now Get the Values of each month for the plotting
    sales , count = [] , []
    for key in all_sales_monthly:
        # Get the Values and store 
        sales.append(all_sales_monthly[key])
    for key in counts_sales_monthly:
        count.append(counts_sales_monthly[key])
    date = all_sales_monthly.keys()
    
    # Define the Figure of Plot
    plt.figure(figsize = (12,6))
    plt.plot(date , sales , label = "Monthly Sales" , marker = "x")
    plt.plot(date , count , label = "Total No. of Sales" , marker = "o")
    plt.title(f"Monthly Sales with total Number of Sales for {product_info[product_id]} Product")
    plt.xlabel("Month Sales")
    plt.xticks(rotation = 90)
    plt.ylabel("Total Sales")
    plt.legend()
    plt.show()
    

# Create the Function for display the sales according to the Month with Product Id
def display_sales_each_product(transaction_data , groceries_data):
    
    # Get the Data from the User
    start_date   = input("Enter the Starting Date (Month/Year) for the Searching Transaction==>")
    end_date     = input("Enter the Ending   Date (Month/Year) for the Searching Transaction==>")

    # Now get the Product Info
    product_info = {}
    for index in range(0 , len(groceries_data)):
        for id , pro_info in groceries_data[index].items():
            product_info[id] = pro_info["name"]
    
    # Define the Dictionary for the Product Sales
    product_sales = {}
    # Now Iterate over Data
    for index in range(0,len(transaction_data)):
        # Now get the Items 
        for id , transa_info in transaction_data[index].items():
            # Get the Date Data from the Actual Data
            date = datetime.strptime(transa_info["date"] , "%d/%m/%Y")
            month_date = date.strftime("%m/%Y")
            # Now filter the data according to the start and end date
            if start_date <= month_date <= end_date:
                if id in product_sales:
                    product_sales[id] += float(transa_info["payment"])
                else:
                    product_sales[id] = float(transa_info["payment"])
    
    # Plot the Data
    product_ids = product_sales.keys()
    product_id_detail = []
    for num in product_ids:
        product_id_detail.append(product_info[num])
    
    # Add the Data in the List
    product_value = []
    for key in product_sales:
        # Get the Values and store 
        product_value.append(product_sales[key])
    
    # Define the Figure
    plt.figure(figsize = (12,6))
    plt.bar(product_id_detail , product_value , color = "black")
    plt.xlabel("Product Name")
    plt.ylabel("Toatl Sales of Each Product")
    plt.title("Slaes of Each Product")
    plt.xticks(rotation = 90)
    plt.show()



    

