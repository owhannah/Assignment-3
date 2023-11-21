from datetime import datetime

def calculate_max_items(money, item_price):
    if money < 0 or item_price <= 0:
        raise ValueError("\033[1;31mInvalid input:\033[0m Money should be non-negative, and item price should be positive.")
    
    max_items = int(money // item_price)
    remaining_money = money % item_price
    return max_items, remaining_money

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

def generate_receipt(max_items, total_cost, discount, loyalty_points, customer_name, item_name, item_price):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    receipt = (
        f"\n\033[1;36;40m********** Receipt **********\033[0m\n"
        f"\033[1;33;40 \033[1;32;40mHannah's Fruit Shop!\033[0m\n"
        f"Date/Time: {current_time}\n"
        f"\033[4;35;40mItem: {item_name}\033[0m\n"
        f"Quantity: {max_items}\n"
        f"Price per {item_name}: \033[3;33;40m{item_price:.2f}\033[0m\n"
        f"-------------------------------------\n"
        f"Total Cost: \033[1;37;41m{total_cost:.2f}\033[0m\n"
        f"Discount Applied: \033[1;37;41m{discount:.2f}\033[0m\n"
        f"Final Amount: \033[1;37;41m{total_cost - discount:.2f}\033[0m\n"
        f"Loyalty Points Earned: \033[1;37;41m{loyalty_points}\033[0m\n"
        f"\033[1;36;40m***********************************\033[0m"
    )
    return receipt

def display_fruit_ascii(fruit_name):
    if fruit_name.lower() == "apple":
        ascii_art = (
            "    ,--./,-.\n"
            "   /        \\\n"
            "  |          |.---.\n"
            "   \\        /     |\n"
            "    `._,._,      /\n"
            "       |||      |\n"
            "       |||      |\n"
        )
        print("\033[1;35;47mThis is your Apple!\033[0m")
    else:
        ascii_art = "\033[1;35;47mAscii art for other fruits can go here.\033[0m"
        print(f"\033[1;35;47mThis is your {fruit_name.capitalize()}!\033[0m")

    print(ascii_art)

def main():
    try:
        # Input: Amount of money, item price, and customer name
        money = float(input("\033[1;32;40mEnter the amount of money you have: \033[0m"))
        item_name = input("\033[1;32;40mEnter the name of the fruit you want to buy (e.g., apple): \033[0m")
        item_price = float(input(f"\033[1;32;40mHow much is each {item_name}?: \033[0m"))
        customer_name = input("\033[1;32;40mEnter the customer's name: \033[0m")

        # Calculate the maximum number of items and remaining money
        max_items, remaining_money = calculate_max_items(money, item_price)

        # Display ASCII art for the chosen fruit
        display_fruit_ascii(item_name)

        # Calculate total cost
        total_cost = max_items * item_price

        # Apply discounts based on the total cost
        total_cost, discount = apply_discount(total_cost)

        # Calculate loyalty points
        loyalty_points = calculate_loyalty_points(total_cost)

        # Display how many items can be bought
        print(f"\033[1;32;40mWith {money:.2f} pesos, you can buy {max_items} {item_name}s.\033[0m")

        # Display receipt
        receipt = generate_receipt(max_items, total_cost, discount, loyalty_points, customer_name, item_name, item_price)
        print(receipt)
        
    except ValueError as e:
        print("\033[1;31mError:\033[0m", e)
    except Exception as e:
        print("\033[1;31mAn unexpected error occurred:\033[0m", e)

if __name__ == "__main__":
    main()
