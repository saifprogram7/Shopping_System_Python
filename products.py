#Welcome Message
print("Welcome to the Store")
print("We have a few products with limited quantity\n")

#Press Enter to view products
input("Please press Enter to view the products: ")

#Display products with price and quantity
print("\nProduct: Xbox, Price: £179, Quantity: 2")
print("Product: Playstation 4, Price: £259, Quantity: 3")
print("Product: Forza Horizon 5, Price: £15, Quantity: 4")
print("Product: Need For Speed Payback, Price: £15, Quantity: 5\n")

#Products stored in variable
product1 = "Xbox"
product2 = "Playstation 4"
product3 = "Forza Horizon 5"
product4 = "Need For Speed Payback"

prod={"xbox":179,"playstation":259,"forza horizon":15, "need for speed payback":15}
x= "xbox"
print("this is it ",prod[x])
#Prices stored in variable
price1 = 179
price2 = 259
price3 = 15
price4 = 15

#Quantity stored in variable
quantity1 = 2
quantity2 = 3
quantity3 = 4
quantity4 = 5

#Let the user know how to stop when they have finished adding products in the basket
print("Once you have finished please type Q or q")

#Ask user what product and quantity they want
alpha = 0
op = 0
while alpha == 0:
    productwanted = input("Please enter the product name you would like to buy: ")
    apple = productwanted.lower()
    if (productwanted == "q" or productwanted == "Q"):
        input("Your basket is ready to be processed ")
        alpha = 1
    else:
        quantitywanted = int(input("Please enter the product quantity you would like to buy: "))
        op = op+int(prod[apple])*quantitywanted
        print("item selected ", apple, prod[apple], " value ",quantitywanted, " op is ",op )

print(op)