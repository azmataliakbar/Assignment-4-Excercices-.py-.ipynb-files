# fruit_shop.py
# This program calculates the total cost of fruits a user wants to buy.
# It displays the quantity of each fruit purchased and the cost per fruit using dictionaries.

def main():
    fruits = {
        'apple': 1.5,
        'durian': 50,
        'jackfruit': 80,
        'kiwi': 1,
        'rambutan': 1.5,
        'mango': 5
    }

    quantity_dict = {}
    cost_dict = {}
    total_cost = 0

    for fruit_name in fruits:
        price = fruits[fruit_name]
        amount_bought = int(input(f"\nHow many ({fruit_name}) do you want?: "))
        quantity_dict[fruit_name] = amount_bought
        fruit_cost = price * amount_bought
        cost_dict[fruit_name] = fruit_cost
        total_cost += fruit_cost

    print("\nQuantity:", quantity_dict)
    print("\nCost:", cost_dict)
    print(f"\nYour total is ${total_cost}")

# Python boilerplate
if __name__ == '__main__':
    main()
