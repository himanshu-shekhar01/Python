
menu = {
    'Pizza': 100,
    'Burger': 50,
    'Fries': 30,
    'Soda': 20,
    'Salad': 40,
    'Chicken Wings': 160,
    'Tea': 25,
    'Coffee': 30
}
print("welcome in Our Famous python Programming Restraunt")
print("Pizza: Rs.100\nBurger: Rs.50\nFries: Rs.30\nSoda: Rs.20\nSalad: Rs.40\nChicken Wings: Rs.160\nTea: Rs.25\nCoffee: Rs.30\n")

total_bill = 0

item = input("Enter the item you want: ").title()
if item in menu:
    quantity = int(input("Enter the quantity: "))
    total_bill  += menu[item]*quantity
    # print(total_bill)

else:
    print("Please order something from the menu which can we serve you")
    
another_order = input("Do you want something else:(yes/no)")
if another_order == "yes":
    item_2 = input("Enter the item you want: ").title()
    if item_2 in menu:
        quantity = int(input("Enter the quantity: "))
        total_bill  += menu[item_2]*quantity
        print(total_bill)
    else:
        print(f"Ordered item {item_2} is not available")
        
print("Thank You for coming here , its our pleasure.")
    


