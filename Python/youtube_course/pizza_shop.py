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
print("Sounds good " + name + ", we will make it in a few minutes your order is " + order + " thank you for choosing us.")
