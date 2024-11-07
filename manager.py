# Import the Important Modules
import os

# Create the Function to Add the New Product
def add_new_product(groceries_data):
    
    while True:
        # Add the New Product in the Data Structure
        os.system("cls")
        new_id = str(len(groceries_data) + 1)
        product_name  = input("Enter the New Product Name==>")
        product_price = float(input("Enter the Price of Product==>"))
        product_stock = input("Enter the Stock of Product==>")

        # Crate the New Product Record
        new_product_record = {
            new_id : {
                "name"  : product_name,
                "price" : product_price,
                "stock" : product_stock
            }
        }
        # Add the New Record in the DS
        groceries_data.append(new_product_record)

        choice = input("Do you want to Add Another New Product (Y , N)==>")
        if (choice == "N"):
            break
        
    # Return the Data
    return groceries_data

