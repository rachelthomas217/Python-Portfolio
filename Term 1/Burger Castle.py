#Rachel Thomas
#10/19
#Code for a fast food place (for example, Burger Castle)
 
# set up tuples with valid orders and item descriptions
valid_orders = ("Burger","French Fries","Salad","Drink","Milkshake")
item_descriptions = ("Half-pound burger","Large fries","Side salad", "Diet root beer", "Chocolate shake")
 
# initialize empty order list
order = []
 
#print welcome message, menu and ordering instructions
print("Welcome to Burger Castle")
print("Menu: ",valid_orders)
print("Please enter each item in your order. Press 'Enter' or type 'Quit' on an empty line when finished.")
 
#use while loop to get all customer order items
while True:
#prompt for item
item = input("Enter Item: ")
 
#if item is empty line or "quit", exit loop
if ((item == "") or (item == "quit")):
break
 
#if item is a valid order, add it to the list, else print error message
if (item in valid_orders):
order.append(item)
else:
print("Sorry, we don't sell ",item)
 
#print empty line and order complete message
print("")
print("Order complete! You are having:")
 
#for each item in the order
for item in order:
#find the index of this item in the valid orders list
index = valid_orders.index(item)
 
#read the matching item description from the same index position
description = item_descriptions[index]
 
#print the description
print(description)
 
#print a thank you message
print("Thanks for visiting Burger Castle!")
 
