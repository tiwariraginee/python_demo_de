# #The try block will generate an error, because x is not defined:

# try:
#   print(x)
# except:
#   print("An exception occurred because x is not defined")



# #The try block will generate a NameError, because x is not defined:

# try:
#   print(x)
# except NameError:
#   print("Variable x is not defined")
# except:
#   print("Something else went wrong")

# #The try block does not raise any errors, so the else block is executed:

# try:
#   print("Hello")
#   y=200
#   print(y)
# except:
#   print("Something went wrong")
# else:
#   print("Nothing went wrong")  


# #The finally block gets executed no matter if the try block raises any errors or not:

# try:
#   print(x)
# except:
#   print("Something went wrong")
# finally:
#   print("The 'try except' is finished")


# #The try block will raise an error when trying to write to a read-only file:

# try:
#   f = open("demofile.txt")
#   try:
#     f.write("Lorum Ipsum")
#   except:
#     print("Something went wrong when writing to the file")
#   finally:
#     f.close()
# except:
#   print("Something went wrong when opening the file")  
# x = -1

# if x < 0:
#   raise Exception("Sorry, no numbers below zero")

strTest= "hello"

if not type(strTest) is int:
  raise TypeError("Only integers are allowed")

