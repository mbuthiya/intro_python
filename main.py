#python arithmetic operations
a = 5
print(type(a))
print(a)

b = a+1
print(b)

c = a - 1
print(c)

d = a * 2
print(d)

e = a / 2
print(e)

#python can also conduct exponential math
f = a**2
print(f)

#python shorthands
a+=1
print(a)

a-=2
print(a)
#booleans
im_true = True
im_false = False

print(im_true)
print(im_false)
print(type(im_false))

print(im_true and im_false)
print(im_false or im_true)

my_string = 'delta'
my_other_string = 'analytics'

print(my_string + " "+ my_other_string)

another_string = 'Hello, '+my_string+' '+my_other_string
print(another_string)
print(len(another_string))

#pythons list

my_list = ['a','b','c',1234]
print(my_list)

#picking items from list
print(my_list[2])
print(my_list[-1])

#picking a range of items from a list
list_two=my_list[2:]
print(list_two)

#adding items to a list 

list_two.append("Hello")
print(list_two)

#removing items from a list
list_two.pop()
print(list_two)

#dictionaries matches items called keys to other items called values
my_dict = {'someKey':'some value', 'Name':'James'}
print(my_dict['someKey']);
print(my_dict['Name'])

#looping through dictionaries
for key in my_dict:
    print("The key is "+key)

#items method returns the key value pair in a list
for key, value in my_dict.items():
    print("The key is "+key+". The value is "+value)
#sets are like lists but do not contain repeating values
valid_set = {1,3,4,"Hello"}
print(valid_set)

#when you present a value to a set that is repeated multiple times only one is added to a set
multiple_set = {1,2,3,4,3,2,2,2,2,2,2,"Hello world"}
print(multiple_set)

#functions
def am_i_happy(happinessLevel):
    if happinessLevel >= 10:
        return "You are very happy"
    elif happinessLevel >=5:
        return "You are happy"
    else:
        return "You are not happy"

print(am_i_happy(10))
print(am_i_happy(1))

#control flow
#If /elif/else

sleepy = True
hungry = False

if sleepy and hungry:
    print("Eat a snack and have a nap")
elif sleepy and not hungry:
    print("Take a Nap")
elif hungry and not sleepy:
    print("Eat a snack")
else:
    print("Go on with your day")

#Loops
##while loops
counter = 0
while (counter<10):
    print("You have counted to ",counter)
    counter+=1


print("You have finished counting")


#for loops
animals = ['cats','dogs','mice','hens']

for element in animals:
    print(element+" are cool")



        