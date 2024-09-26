product = dict()

def add_product():
    product_id = input("Please enter product ID (store_ID-productid): ")
    if product_id in product:
        print('product_id is duplicated, please input another one')
    else:
        price = float(input("please enter product price: "))
        product[product_id] = price
        print(f"Product {product_id} with price {price}")

def delete_product():
    product_id = input("Please enter product ID (store_ID-productid): ")
    if product_id in product:
        del product[product_id]
        print(f"Product {product_id} is deleted")
    else:
        print("Product ID is not found")

def total_price_by_store():
    store_id = input("Please input store ID")
    total = sum(price for pid, price in product.items() if pid.split('-')[0] == store_id)
    count_store = sum(1 for pid, price in product.items() if pid.split('-')[0] == store_id)
    print(f"Total price of products for store {store_id} is {total} and there are {count_store} products.")

def menu():
    while True:
        print("\nMenu:")
        print("1. Add product")
        print("2. Delete product")
        print("3. Get sum of product prices by store ID")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_product()
        elif choice == '2':
            delete_product()
        elif choice == '3':
            total_price_by_store()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

menu()
