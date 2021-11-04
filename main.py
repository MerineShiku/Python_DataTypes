sentence = """Hey Boo
Want dinner tonight"""
print (sentence)
print(type(sentence))


#finding character by indexing
print (sentence[4])

#slicing 
sentence = "Merine"

print (sentence[1:5]) 

#immutable

name = "Merine"
# name(3) = "e" string is immutable but you can change the whole word
print (name)

#lists 
# x= []  list
x = [10, "merine", 2.55558907890]
print(x[2])
#slicing of lists
print(x[1:3])

#lists are mutable
x[1] = "Alannah"
print(x)

#Tuple # uses normal brackets and list use square brackets
# x= ()
#heterogenous 

x = ("hello", [1, 6, 8], (67, 89,20))
print(type(x))
#x[2] = "hey"
print(x) #immutable
y = "hello"
print(type(y)) # <class 'str'>
z = "hello",
print(type(z)) #<class 'tuple'># not the comma makes all the difference

k = ("hello")
print(type(k)) # <class 'str'> add comma to make it a Tuple


#Range
#a = range(20)
#for x in a:
# print(x)


 #mapping Type (Dictionary)

m = {"name" : "merine", "age": 30}
print(m["name"]) #dict is best for finding value when you dont know index
print(m.get("age")) #dict using  get method 

#dict is mutable 
 
m["age"] = 4
print (m) #results  {'name': 'merine', 'age': 4}


'''
Set types
'''
k = {2, 4, 6}
print(type(k))

# P = {}  # this is a dict

p =set() #this is a set 
print (type(set()))


# mixed data types ( all immutable )

set = {3.2, "hi", (1,2,3)}
print(type(set))
# TypeError: 'set' object is not subscriptable
#print(set[0])

# ====================
# no duplicates

set = {3.2, "hi", (1,2,3), "hi"}
print(set) # result will be   {3.2, "hi", (1,2,3)}

# ====================

# cannot have mutable (list) in a set
#set = {3.2, "hi", (1,2,3), [1,2,3]}
# unhashable type: 'list' (because  [1,2,3] is a list thus mutable)
#print(set)

'''
Boolean Type (True or False)
'''
#note capital T and F
print(type(True))

# boolean as numbers
print(True == 1)
print(False == 0)

# interesting logic
print(True + True)

# not boolean operator
print(not True)
print(not False)

# and boolean operator
print(True and False)
print(True and True)
print(False and False)

#or boolean operator
print(True or False)
print(True or True)
print(False or False)