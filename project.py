#Define the menu of the restaurant
menu = {
    'Pizza':150,
    'Pasta':120,
    'Burger':80,
    'Coffee':60,
    'Tea':50,
}
 
print("Welcome To Our Restaurant")

#Display the menu of the resturant to the customer
 
print("Pizza: Rs150\nPasta: Rs120\nBurger: Rs80\nCoffee: Rs60\nTea: Rs50")

order_total = 0
item_1 = input("Enter the name of the item you want to order = ") 

if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Ordered item {item_1} is not available yet!")


while True:    

    another_order = input("Do you want to add another item? (Yes/No) ")

#Ask the customer if they want something else to order

    if another_order == "Yes":
        item_2 = input("Enter the name of the second  item = ")

#Check whether the item_2 is present in the menu of the restaurant
    
        if item_2 in menu:
            order_total += menu[item_2]
            print(f"Item {item_2} has been added to order")
        else:
            print("Ordered item {item_2} is not available!")
    else:
        break    
    
            
        
#Display The Total Amount To Pay By The Customer


print(f"The toatl amount of items to pay is {order_total}")

print(f"Thank You For Visiting To Our Resturant")
