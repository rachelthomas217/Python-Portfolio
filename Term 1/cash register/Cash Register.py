#Rachel Thomas
#9/9/19
#Cash Register Activity

#declare and initialize variables, calculate and store the sub-total and the amount of tax
#plus store the results, and finally calculate the total price and store the amount
items_num = 4
indv_item_cost = 10.00
sub_total = items_num * indv_item_cost
tax_rate = 0.008
tax_amnt = sub_total * tax_rate
total_cost = tax_amnt + sub_total

#printing out a receipt for a cash register now
#aka show the full receipt to the screen
#created seperators
sep1 = ": "
sep2 = ": $"
print("SALES RECEIPT")
print("_______________")
print("Number of Items" ,items_num,sep=sep1,end=" ")
print(" ")
print("Cost Per Item",indv_item_cost,sep=sep2)
print("Tax Rate",tax_rate, sep=sep1)
print("Tax Amount" ,tax_amnt,sep=sep2)
print(" ")
print("TOTAL SALE PRICE:" ,total_cost,sep=sep2)
print("_______________")

input()
