# simple boolean operators, "and", "or"
name = "phillip"
age = 23
if name == "phillip" and age == 28:
    print("Your name is phillip, and you are also 28 years old.")

if name == "phillip" or name == "Rick":
    print("Your name is either phillip or Rick.")


# the "in" operator checks if a specified object exists within an
# iterable object container

animal = "cat"
if animal in ["cat", "dog"]:
    print("You are either a cat or dog.")

# the "is" operator checks for the instances themselves, not the values

x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)  # Prints out True
print(x is y)  # Prints out False
print(x is x)  # Prints out True

# the "not" operator can be used to inverse a booleans value

print(not False)  # prints True
print((not False) == (False))  # prints out false
