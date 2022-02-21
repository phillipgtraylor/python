# prints string in reverse.
astring = "Hello world!"
print(astring[::-1])


# prints the string in upper or lower case respectively
bstring = "Hello world!"
print(bstring.upper())
print(bstring.lower())

# checking if the string starts with or ends with something
cstring = "Hello world!"
print(cstring.startswith("Hello"))
print(cstring.endswith("asdfasdfasdf"))

# split the string into many strings inside of a list
dstring = "Hello new world how are you!"
afewwords = dstring.split(" ")
print(afewwords)
