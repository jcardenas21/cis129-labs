#coffee_qty and muffin_qty are determined by the user
print("*" * 40)
print("My Coffee and Muffin Shop")
coffee_qty = int(input("Number of coffees bought?"))
muffin_qty = int(input("Number of muffins bought?"))
    
coffee_price = 5
muffin_price = 4

#The following is used to determine our coffee and muffin price in addition to the tax

coffee_total = coffee_qty * coffee_price
muffin_total = muffin_qty * muffin_price
subtotal = coffee_total + muffin_total
tax = subtotal * 0.06
total = subtotal + tax
    
print("*" * 40)
print("My Coffee and Muffin Shop Receipt")
print(f"{coffee_qty} coffee(s) at $5 each: $ {coffee_total}")
print(f"{muffin_qty} muffin(s) at $4 each: $ {muffin_total}")
print(f"6% tax: & {tax}")
print("-" * 10)
print(f"${total}")
print("*" * 40)
