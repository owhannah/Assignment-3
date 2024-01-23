from datetime import datetime

def calculate_total_cost(apple_quantity, orange_quantity, apple_price=20, orange_price=25):
    total_cost = (apple_quantity * apple_price) + (orange_quantity * orange_price)
    return total_cost

def apply_discount(total_cost):
    # Apply a 10% discount if the total cost is greater than or equal to 100 pesos
    if total_cost >= 100:
        discount = 0.10 * total_cost
        total_cost -= discount
        return total_cost, discount
    return total_cost, 0

def calculate_loyalty_points(total_cost):
    # Give 1 loyalty point for every 5 pesos spent
    return int(total_cost / 5)

def generate_receipt(apple_quantity, orange_quantity, total_cost, discount, loyalty_points):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    receipt = (
        f"\n\033[1;35;47m********** Your Receipt **********\033[0m\n"
        f"\033[1;32;40mHannah's Fruit Shop\033[0m\n"
        f"Date/Time: {current_time}\n"
        f"\033[4;36;40mItem: Apple\033[0m\n"
        f"Quantity: {apple_quantity}\n"
        f"Price per Apple: \033[3;33;40m20.00\033[0m\n"
        f"-------------------------------------\n"
        f"\033[4;36;40mItem: Orange\033[0m\n"
        f"Quantity: {orange_quantity}\n"
        f"Price per Orange: \033[3;33;40m25.00\033[0m\n"
        f"-------------------------------------\n"
        f"Total Cost: \033[1;37;41m{total_cost:.2f}\033[0m\n"
        f"Discount Applied: \033[1;37;41m{discount:.2f}\033[0m\n"
        f"Final Amount: \033[1;37;41m{total_cost - discount:.2f}\033[0m\n"
        f"Loyalty Points Earned: \033[1;37;41m{loyalty_points}\033[0m\n"
        f"\033[1;35;47m***********************************\033[0m"
    )
    return receipt

def main():
    print("\033[1;32;40m")
    print("\033[1mWelcome to \033[0;35;47mHannah's Fruit Shop!\033[0m")
    print("\033[1;36mFresh fruits are here!\033[0m")

    try:
        # Asking the user for the quantity of apples and oranges
        apple_quantity = int(input("\033[0;33mHow many apples do you want to buy? \033[0m"))
        print("\033[1;37m")
        orange_quantity = int(input("\033[0;33mHow many oranges do you want to buy? \033[0m"))

        # Prices per fruit
        apple_price = 20
        orange_price = 25

        # Calculating the total amount to pay
        total_amount = calculate_total_cost(apple_quantity, orange_quantity, apple_price, orange_price)

        # Apply discounts based on the total cost
        total_amount, discount = apply_discount(total_amount)

        # Calculate loyalty points
        loyalty_points = calculate_loyalty_points(total_amount)

        # Displaying the output
        print("\033[1;33m")
        print(f"\nYou are buying {apple_quantity} apples and {orange_quantity} oranges.")
        print(f"The total amount to pay is \033[1m{total_amount - discount:.2f} pesos\033[0m.")

        # Display receipt
        receipt = generate_receipt(apple_quantity, orange_quantity, total_amount, discount, loyalty_points)
        print(receipt)

    except ValueError as e:
        print("\033[1;31m")
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

