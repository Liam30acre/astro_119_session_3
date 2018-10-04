#string

s = "I am a string."
print(type(s))	#says str

#Boolean

yes = True	#bolean true
print(type(yes))

no = False	#B False
print(type(no))

# List -- ordered and changeable 

alpha_list = ["a", "b", "c"]	#list initialzation 
print(type(alpha_list))
print(type(alpha_list[0]))	#says string
alpha_list.append("d")	#adds d to list end
print(alpha_list)

#Tuple -- ordered and unchangeable 

alpha_tuple = ("a", "b", "c")	#initialize tupele
print(type(alpha_tuple))

try:
	alpha_tuple[2] = "d"	#wont work raise error 
except TypeError:
	print("We cant add elements to tuples!")
print(alpha_tuple)