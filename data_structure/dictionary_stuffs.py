# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(type(thisdict))
# print(thisdict["brand"])


thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(thisdict)
print(len(thisdict))

# thisdict = dict(name = "John", age = 36, country = "Norway")


# Access the Items:
'''x = thisdict["brand"]'''
x = thisdict.get("brand")
print(x)

getKeys = thisdict.keys()
print(getKeys);



car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change

getAllValues = car.values()
print(getAllValues);
print(car.items())