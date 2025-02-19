menu = {
    'Pizza': 40,
    'Burger': 30,
    'Hot Dog': 20,
    'Fries': 15,
    'Shake': 25,
    'Coffee': 10,
    'Pasta': 50,
    'Ice Cream': 15,
    'Donut': 10,
}

print("Welcome to Zapuk Zupuk Restaurant")
print("Pizza: Rs40\nBurger: Rs30\nHot Dog: Rs20\nFries: Rs15\nShake: Rs25\nCoffee: Rs10\nPasta: Rs50\nIce Cream: Rs15\nDonut: Rs10")

order_total = 0

item_1 = input("Enter the item = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item{item_1}has been added")

else:
    print("Sorry, we don't have this item") 

another_order = input("Do you want to add another order? (Yes/No): ")
if another_order ==  "Yes":
    item_2 = input("Enter the item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item {item_2} has been added")
    else:
        print("Sorry, we don't have this item")

print(f"Your total order amount to pay is {order_total}")
