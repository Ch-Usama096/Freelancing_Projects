#  Import the Important Modules
import os 
from datetime import datetime

# Create the Function For add the Sale Transaction in the Data Structure
def add_sale_transaction(transaction_data , groceries_data):

    # Display All Groceries Data 
    while True:
        os.system("cls")
        print("Grocery List")
        for index in range(0 , len(groceries_data)):
            for id , dic in groceries_data[index].items():
                print(id , f"\t:\t{dic["name"]}")
        flag = True
        while flag:
            # Get the Product Information from the Client
            product_id       = int(input("Enter the Purchase Product ID==>"))
            product_quantity = int(input("Enter the Quantity of Purchased Product==>"))
            payment          = float(input("Enter the recieved payment==>"))

            # Now Check the Product Quantity Have or not
            for index in range(0 , len(groceries_data)):
                for id , dic in groceries_data[index].items():       
                    if product_id == int(id):
                        if int(dic["stock"]) < product_quantity: 
                            print("Insuffient Stock, Please Check your Product Quantity again add the Details")
                        else:
                            # Update the Groceries File Data
                            groceries_data[index][id]["stock"] = str(int(dic["stock"]) - product_quantity)
                            flag = False

        # Now Add the Transaction Data in the Transaction File
        new_transaction_reord = {product_id : {
            "date" : datetime.now().strftime("%d/%m/%Y"),
            "time" : datetime.now().strftime("%H:%M:%S %p"),
            "quantity" : product_quantity,
            "payment" : payment
        }}
        transaction_data.append(new_transaction_reord)

        choice = input("Do you want to Purchase Another Product (Y , N)==>")
        if (choice == "N"):
            break

    # Return the Results
    return transaction_data , groceries_data


                