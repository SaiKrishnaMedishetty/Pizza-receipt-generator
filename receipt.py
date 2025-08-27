from pizza import *

print("Helloo, welcome to Pizza Hut")
print("How can i help you")
cart = []

customer_name = input("May I know your name: ")
product = input("what do you want: ")
if product in pizza:
    cart.append(product)

else: 
    print("we dont have this product")
quantity = int(input("please enter the quantity: "))






if product == "veg" or "non-veg" or "vegan" in pizza:
    Total_amount = quantity * item_price[product]
    
print(f"the total amount is: {Total_amount}")






