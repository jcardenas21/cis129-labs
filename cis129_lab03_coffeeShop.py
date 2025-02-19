#coffee_qty, muffin_qty, doughnut_qty, and cookie_qty are determined by the user
print("*" * 40)
print("My Coffee and Muffin Shop")
coffee_qty = int(input("Number of coffees bought?"))
muffin_qty = int(input("Number of muffins bought?"))
doughnut_qty = int(input("Number of doughnuts bought?"))
cookie_qty = int(input("Number of cookies bought?"))
    
coffee_price = 5
muffin_price = 4
doughnut_price = 3
cookie_price = 2

#The following is used to determine our coffee, muffin, doughnut, and cookie prices in addition to the tax

coffee_total = coffee_qty * coffee_price
muffin_total = muffin_qty * muffin_price
doughnut_total = doughnut_qty * doughnut_price
cookie_total = cookie_qty * cookie_price
subtotal = coffee_total + muffin_total + doughnut_total + cookie_total
tax = subtotal * 0.06
total = subtotal + tax
    
print("*" * 40)
print("My Coffee and Muffin Shop Receipt")
print(f"{coffee_qty} coffee(s) at $5 each: $ {coffee_total}")
print(f"{muffin_qty} muffin(s) at $4 each: $ {muffin_total}")
print(f"{doughnut_qty} doughnut(s) at $3 each: $ {doughnut_total}")
print(f"{cookie_qty} cookie(s) at $2 each: $ {cookie_total}")
print(f"6% tax: & {tax}")
print("-" * 10)
print(f"${total}")
print("*" * 40)
print("Thanks for shopping at our coffee shop!!!")
