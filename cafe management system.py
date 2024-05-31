#cafe management system

menu = {
    'pasta':80,
    'maggi':70,
    'coffe':90,
    'burger':120,
    'pizza':180,
    'salad':50
}
print("Welcome to TECH Cafe")
print("pasta:80\nmaggi:70\ncoffe:90\nburger:120\npizza:180\nsalad:50")

order_total = 0

item_1=input("Enter the name of item you want to order= ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1} has been added to your order")

else:
    print(f"Ordered item {item_1} is not available yet")

another_order=input("Do you want to add another item? (yes/no) ")
if another_order == "yes":
    item_2  = input("Enter the name of second item =")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to your order")
    else:
        print(f"Ordered item{item_2} is not available")

input(f"you have ordered {item_1} and {item_2}.")

print(f"The total amount of item is {order_total} to pay")
        