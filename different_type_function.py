#1.  def my_function()://defined using the def keyword
#   print("Hello from a function")

# my_function() //To call a function, use the function name followed by parenthesis

#2. def my_function(fname):
#   print(fname + " Refsnes")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")

#3. def my_function(fname, lname):
#   print(fname + " " + lname)

# my_function("Emil", "Refsnes")

#4. def my_function(fname, lname):
#   print(fname + " " + lname)

# my_function("Emil")


# 5. def my_function(*kids):
  
#   print("The youngest child is " + kids[0])
#   for x in kids:

#    print(x)

# my_function("Emil", "Tobias", "Linus","peter")



#6. def my_function(child3, child2, child1):
#   print("The youngest child is " + child1)

# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#7. def my_function(**kid):
#   print("His last name is " + kid["lname"])

# my_function(fname = "Tobias", lname = "Refsnes")


#8. def my_function(country = "Norway"):
#   print("I am from " + country)

# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")


#9. def my_function(food):
#   for x in food:
#     print(x)

# fruits = ["apple", "banana", "cherry"]

# my_function(fruits)

#10. def myfunction():    //function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
#   pass
