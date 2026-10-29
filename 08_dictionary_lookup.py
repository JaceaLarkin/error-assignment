prices = {"pizza": 12, "burger": 8, "fries": 4, "soda": 2}


try:
    item = input("Enter a food item: ")
    print(prices[item])

except KeyError:
    print("Sorry, that item is not on the menu.")










