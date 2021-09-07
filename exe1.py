#this is my first code.
print("Franklyn's dog")
#jason is teaching me code 
print("This is my second line in code")

#Start MAth 
print("Math Calc", 5*3)
#trial Math
print("Is 5 greater than 2", 5>=2)

#First Variable problem 

apples=10
bananas=5
customers=2

print("Customer wants 8 apples how many are left? There are", apples-8, "left")
print("Customer 2 wants 2 bananas how many are left? There are", bananas-2, "left")


#Trying out string formatters

my_name= 'Franklyn'
my_age= 26
my_star_sign= 'Aquarius'
my_height= 188.235

print("My name is %s ." % my_name)
print("I am %d years old." % my_age)
print("I am an %s by birth." % my_star_sign)
print("My height is %d cms" % (my_height))

# Important lesson to remember. The book does not close all comands with parenthesis . You have to open and close all parenthesis to execute without errors.

#Trying to use more formatted strings

#The following text will make no sense at all

a = 'Thanks to Jason I have written %d lines of code.' %25
b = 'A lot of this still doesnt make too much sense its like a toy'

print (a+b) 
print ("Coders find this interesting but %s ." % b)

#More typing code 

curry = "%s %s %s %s" # Switching between %r and %s makes change the output 
print (curry % (1,2,3,4))
print (curry % ("red","green","blue","yellow"))


#More typing exercises

colours = "red green blue black"
shapes = "\nSquare \nCircle \nRectangle \nTriangle"

print("The colours are",colours)
print("These are the shape of my heart", shapes)
