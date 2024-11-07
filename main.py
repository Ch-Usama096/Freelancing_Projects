# Import the Important Modules Here
import csv 
from datetime import datetime
import os 
from important_functions import load_csv_file , login , main_manu , save_data_csv , transaction_by_date
from important_functions import transaction_by_name , transaction_by_name_date , update_details
from important_functions import display_sales_monthly , display_sales_monthly_product_id , display_sales_each_product
from cashier import add_sale_transaction 
from manager import add_new_product


# Load the Groceries File Data
groceries_file_path = r"CSV_Files\\groceries.csv"
groceries_file_data = load_csv_file(groceries_file_path)
#print(f"Here is the Length of the Groceries File Data : {len(groceries_file_data)}")

# Load the Transaction File Data
transaction_file_path = r"CSV_Files\\transactions.csv"
transaction_file_data = load_csv_file(transaction_file_path)
#print(f"Here is the Length of the Transaction File Data : {len(transaction_file_data)}")

# Check the UserName and Password according to the User CSV File Data 
while True:
    role , username = login()

    if role == 0:
        print("Invalid UserName & Password, Please Feed the Accurate Information")
    else:
        while True:
            choice = main_manu()

            if choice == 1:
                # Call the add_sale_transaction (To add the New Transaction)
                transaction_file_data , groceries_file_data = add_sale_transaction(transaction_file_data , groceries_file_data)
            elif choice == 2 and role == "manager":
                # Call the add_new_product (to add the New Product Information)
                groceries_file_data = add_new_product(groceries_file_data)
            elif choice == 4:
                while True:
                    # Call the transaction_by_date for (Searching the Transaction with Date)
                    search_trnsaction_date = transaction_by_date(transaction_file_data)
                    # Dsiplay the All Searched Transaction Data
                    for index in range(0,len(search_trnsaction_date)):
                        for product_id , product_details in  search_trnsaction_date[index].items():
                            print(f"\nTransaction No. {index+1}")
                            print(f"Here is the ID of the Product : {product_id}")
                            print(f"Here is the Transaction Data : {product_details["date"]}")
                            print(f"Here is the Transaction Time : {product_details["time"]}")
                            print(f"Here is the Quantity of the Product : {product_details["quantity"]}")
                            print(f"Here is the Payment of the Product : {product_details["payment"]}")
                    choice = input("Do you want to Search Transaction with Other Date (Y , N)==>")
                    if (choice == "N"):
                        os.system("cls")
                        break
            elif choice == 5:
                while True:
                    # Call the transaction_by_name for (Searching the Transaction with name)
                    search_trnsaction_name = transaction_by_name(transaction_file_data , groceries_file_data)
                    # Dsiplay the All Searched Transaction Data
                    for index in range(0,len(search_trnsaction_name)):
                        for product_id , product_details in  search_trnsaction_name[index].items():
                            print(f"\nTransaction No. {index+1}")
                            print(f"Here is the ID of the Product : {product_id}")
                            print(f"Here is the Transaction Data : {product_details["date"]}")
                            print(f"Here is the Transaction Time : {product_details["time"]}")
                            print(f"Here is the Quantity of the Product : {product_details["quantity"]}")
                            print(f"Here is the Payment of the Product : {product_details["payment"]}")
                    choice = input("Do you want to Search Transaction with Other Name (Y , N)==>")
                    if (choice == "N"):
                        os.system("cls")
                        break
            elif choice == 6:
                while True:
                    # Call the transaction_by_name_date for (Searching the Transaction with Date & Name)
                    search_trnsaction_name_date = transaction_by_name_date(transaction_file_data , groceries_file_data)
                    # Dsiplay the All Searched Transaction Data
                    for index in range(0,len(search_trnsaction_name_date)):
                        for product_id , product_details in  search_trnsaction_name_date[index].items():
                            print(f"\nTransaction No. {index+1}")
                            print(f"Here is the ID of the Product : {product_id}")
                            print(f"Here is the Transaction Data : {product_details["date"]}")
                            print(f"Here is the Transaction Time : {product_details["time"]}")
                            print(f"Here is the Quantity of the Product : {product_details["quantity"]}")
                            print(f"Here is the Payment of the Product : {product_details["payment"]}")
                    choice = input("Do you want to Search Transaction with Other Name & Date(Y , N)==>")
                    if (choice == "N"):
                        os.system("cls")
                        break
            elif choice == 7:
                while True:
                    # Call update_detals for (Update the Details of the Product)
                    groceries_file_data = update_details(groceries_file_data)
                    # Update the CSV File too
                    save_data_csv(groceries_file_data , "updated_groceries.csv")
                    os.system("cls")
                    print("Successfull Groceries File Updated !")
                    choice = input("Do you want to Update Another Product Info(Y , N)==>")
                    if (choice == "N"):
                        os.system("cls")
                        break
            elif choice == 8:
                while True:
                    # Call display_sales_monthly function for ( the Display Sales )
                    display_sales_monthly(transaction_file_data)
                    choice = input("Do you want to again check the sales with different date(Y , N)==>")
                    if (choice == "N"):
                        os.system("cls")
                        break
            elif choice == 9:
                while True:
                    # Call display_sales_monthly_product_id function for ( the Display Sales )
                    display_sales_monthly_product_id(transaction_file_data , groceries_file_data)
                    choice = input("Do you want to again check the sales with different date(Y , N)==>")
                    if (choice == "N"):
                        os.system("cls")
                        break
            elif choice == 10:
                while True:
                    # Call display_sales_each_product function for ( the Display Sales )
                    display_sales_each_product(transaction_file_data , groceries_file_data)
                    choice = input("Do you want to again check the sales with different date(Y , N)==>")
                    if (choice == "N"):
                        os.system("cls")
                        break
            else:
                os.system("cls")
                save_data_csv(groceries_file_data , "updated_groceries.csv")
                save_data_csv(transaction_file_data , "updated_transaction.csv")
                os.system("cls")
                print("Successfull Files Updated !")
                break

            os.system("cls")
            print(f"Welcome {role} : {username}")
        # Only One User Work Currently, If you want to another user use it then the User will have to login
        exit()
            
            