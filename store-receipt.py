print("=======================================================================")
print(" Publix")
print("=======================================================================")

finished = False

TAX_RATE = 0.070
item_no = 0
subtotal = 0.0
tax = 0.0
total = 0.0

a=input("enter the items and costs ( diffrent item to be seperated by ',' ")
a=a.split(",")



while (not finished):
    for i in a:
        print(i)
        prompt = "Enter amount for item #" + str(item_no + 1) + "(Type -1 to done or type any number to enter): $"
        price = float(input(prompt))
    if (price == -1):
        finished = True
    else:
        subtotal += price
        item_no += 1
        print("\tprice entered: ${:.2f}".format(price))

tax = subtotal * TAX_RATE
total = subtotal + tax
print("=======================================================================")
print("TOTAL ITEMS purchased: {:d}".format(item_no))
print("ITEMS purchased list: ")
print("SUBTOTAL: ${:.2f}".format(subtotal))
print("TAX: ${:.2f}".format(tax))
print("TOTAL: ${:.2f}".format(total))

print("=======================================================================")

print (" Publix Receipt")
print("=======================================================================")

print(" Thank you for your business!")