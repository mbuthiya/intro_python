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




        