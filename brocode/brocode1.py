# variable 
first_name = "anni"
last_name = "gigauri"
full_name = first_name +" "+ last_name
print("Hello "+full_name)
#print(type(name))


age = 13
age += 1 
print("your age is: "+str(age))
#print(type(age))



height = 165.5
print("your height is: "+str(height)+"cm")
#print(type(height))



human = False
print("are you a human: "+str(human))
#print(type(human))




#multiple assignment

# name = "anni"
# age = 14
# attractive = True

#name, age, attractive = "anni", 14, True

#print(name)
#print(age)
#print(attractive)


#spongebob = 30
#patrick = 30
#sandy = 30
#squidward = 30

#spongebob = patrick = sandy = squidward = 30

#print(spongebob)
#print(patrick)
#print(sandy)
#print(squidwart)

name = "anni"

#print(len(name))
#print(name.find("o"))
#print(name.capitalize())
#print(name.upper())
#print(name.lower9())
#print(name.isdigit())
#print(name.isalpha())
#print(name.count("o"))
#print(name.replace9("o" , "a"))
#print(name*3)


#type casting = the data type of a value to another data type

#x = 1 #int
#y = 2.0 #float
#z = "3" #str

#x = str(x)
#y = str(y)
#z = str(z)

#print(x)
#print(y)
#print(z*3)





#name = input(" what is your name: ")
#age = input(" how old are you: ")
#height = float(input("how tall are you: "))

#age = age + 1 

#print("hello "+name)
#print("you are "+str(age)+" years old")
#print("you are "+str(height)+"cm tall ")



import math

pi = 3.14
x = 1
y = 2 
z = 3


#print(round(pi))
#print(math.ceil(pi))
#print(math.floor(pi))
#print(abs(pi))
#print(pow(pi,2))
#print(match.aqrt(420))
#print(max(x.y.z))
#print(min(x.u.z))


# slicing = create a subsrting by extracting elements from another string 
#     indexing[] or slice()
#     [start:stop:step]

name = "anni"

first_name = name[:4]         # [0:4]
last_name = name[4:]          # [4:end]
funky_name = name[::4]        # [0:end:4]
reversed_name = name[::-1]    # [0:end:-1]

print(first_name)


website = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,-4)

print(website1[slice])
print(website2[slice])



# if statement = a block of code that will execute if its condition is true

age = int(input("how old are you:  "))

if age >= 14:
    print("you are an adult!")
elif age == 100:
    print("you are a century old!")
elif age < 0:
    print("you havent been born yet!)
else:
    print("you are a child!")





























