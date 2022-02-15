#multiline strings: option one
#print("""Hello I'm a multiline string.
#because I can make waffles.
#and my lines are seperated""")

#option2
#print("Hello I'm a multiline string. \n"+ "Because I want waffles. \n" + "and this way my lines seperated again.")



#making a little game a pizzashop practicing input function
print("Hello Welcome to Pizzaland!!")

#input
name = input("what is your name?\n")

print("hello! " + name +  ", Thank you for visiting us today.\n\n\n")
#menu

menu = "Cheese Pizza,"  "Pepperoni with Onion," "Pinnaple Chicken"


print(name + ", What can I get you? \n We just opened recently this is our menu so far.\n\n" 
+ menu)

#take the order
order = input()
price = 8.99

quantity = input("How many  pizza would you like?\n")

# str converted to int # int = whole numbers
total = price * int(quantity)

print("thank you! Your total is: $" + str(total))  #making int to str aka Text

print("Sounds good " + name + ", we will have your " + quantity +" " + order + ", thank you for\n choosing us.")
