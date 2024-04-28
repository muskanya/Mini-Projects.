# Inventory Management System

inventory = {
        "A1": {"name": "Apples", "price": 16, "quantity": 10},
        "B2": {"name": "Bananas", "price": 8, "quantity": 20},
        "C3": {"name": "Milk", "price": 50, "quantity": 5},
    }

cart = {}
total_amount = 0

print("Welcome to the Supermarket!")

while True:
        print("\nAvailable Items:")

        for id, details in inventory.items():
            print(f"{id}: {details['name']} - ₹{details['price']} ({details['quantity']} in stock)")

        print("\n1. Add Item")
        print("2. View Cart")
        print("3. Remove Item")
        print("4. Checkout")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice in ['1', '3']:

            id = input("Enter the ID of the item: ")

            if id in inventory:

                if choice == '1':
                    quantity_available = inventory[id]["quantity"]
                    quantity = int(input(f"Enter quantity (available: {quantity_available}): "))

                    if quantity <= quantity_available:
                        inventory[id]["quantity"] -= quantity
                        cart[id] = cart.get(id, 0) + quantity
                        total_amount += quantity * inventory[id]["price"]
                        print(f"{quantity} {inventory[id]['name']} added to cart!")

                    else:
                        print(f"Insufficient quantity of {inventory[id]['name']} available.")

                else:

                    if id in cart:
                        quantity_in_cart = cart[id]
                        quantity = int(input(f"Enter quantity to remove (in your cart: {quantity_in_cart}): "))

                        if quantity <= quantity_in_cart:
                            inventory[id]["quantity"] += quantity
                            cart[id] -= quantity
                            total_amount -= quantity * inventory[id]["price"]
                            if cart[id] == 0:
                                del cart[id]
                            print(f"{quantity} {inventory[id]['name']} removed from cart.")

                        else:
                            print(f"Insufficient quantity of {inventory[id]['name']} in your cart.")

                    else:
                        print(f"Item with ID '{id}' not found in your cart.")

        elif choice == '2':

            if not cart:
                print("Your cart is empty.")

            else:
                print("\nYour Cart:")
                for id, quantity in cart.items():
                    details = inventory[id]
                    print(f"{quantity} {details['name']} - ₹{details['price']} each")
                print(f"\nTotal Amount: ₹{total_amount}")

        elif choice == '4':

            if not cart:
                print("Your cart is empty. Please add items before checkout.")

            else:
                print("\nYour Cart:")
                for id, quantity in cart.items():
                    details = inventory[id]
                    print(f"{quantity} {details['name']} - ₹{details['price']} each")
                print(f"\nTotal Amount: ₹{total_amount}")
                print("You only have to use cash any other method is not allowed")
                print("Thank you for shopping!")
                break

        elif choice == '5':
            print("Thank you for visiting!")
            break

        else:
            print("Invalid choice. Please try again.")