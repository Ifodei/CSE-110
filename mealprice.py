#Any other side order on top of the main meal costs $0.5 irregardles which type.
child_price= float(input ("What is the price of a child's meal?"))
adult_price= float(input ("What is the price of an adult's meal?"))
child_no= int(input ("How many children are there?"))
adult_no= int(input ("How many adults are there?"))
side_order_no= int(input ("How many sideorders will you have?"))
side_order= 0.5 * side_order_no
print ()
subtotal= (child_no * child_price) + (adult_no * adult_price) + side_order
print (f"Subtotal: ${subtotal}")
print ()
tax_rate= float(input ("What is the sales tax rate?"))
sales_tax= (subtotal * tax_rate)/100
print (f"Sales Tax: ${sales_tax}")
total_price= subtotal + sales_tax
print (f"Total: ${total_price}")
print ()
payment_amount= float(input("What is the payment amount?"))
change= payment_amount - total_price
print (f"Change: ${change:.2f}")