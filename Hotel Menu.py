#The Restaurant Menu.

menu = {
    "Pizza" : 400,
    "Pasta" : 200,
    "Burger" : 150,
    "Coffee" : 80,
    "Tea" : 50,
    "Fries" : 100

}


print("WELCOME TO OUR RESTAURANT!")

print("Pizza : Rs400\nPasta : Rs200\nBurger : Rs150\nCoffee : Rs80\nTea : Rs50\nFries : Rs100")

total_order = 0

item_1 = input("Enter your order please : ")
if item_1 in menu:
    total_order += menu[item_1]
    print(f"Your oder {item_1} has been added.")

else:
    print(f"The order {item_1} is not available please try something else : ")

another_order = input("Do want to order anything else? (Yes/No) ")

if another_order == "Yes":
    item_2 = input("Add another order please : ")
    if item_2 in menu:
        total_order += menu[item_2]
        print(f"The {item_2} has been added to you order")
    else:
        print(f" The {item_2} is not available.")

print(f"The total amount of you bill is {total_order}")
