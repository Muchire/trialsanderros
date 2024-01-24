  #import time
#x=5.0
#x= str(x)
#x_str = str(x)
#print(x_str)
#print(str("x"))
# print(type(x_str))
#for i in "vivian":
   # print (i)
#for i in range(10+3,2):
        #print (i)
#for breathin in range (8,0,-1):
 #   print(breathin)
  #  time.sleep(1)
#print("hold it")
#for holdit in range (5,0,-1):
 #   print(holdit)
  #  time.sleep(1)
#print("breath out")
#for breathout in range (4,0,-1):
 #   print(breathout)
  #  time.sleep(1)
#print("now youre relaxed")

#rows = int (input("how many rows ?:"))
#columns = int(input("how many columns?"))
#hexagonal = int(input("how many hexagonal"))
#symbol = input("enter a symbol to use:")

#for i in range (rows):
 #   for j in range (columns):
  #      for l in range (hexagonal):
   #         print (symbol)
    #print()

#for i in range (1,20):
 #    if i ==13:
  #       pass
   #  else :
    #     print (i ,end="")
#lists
#dinner =["pizza","nyama choma" ]
#dessert = ["cake","ice cream"]

#food = [dinner, dessert]

#for x in dessert:
  #   print(x)

#utensils = {"forks","cups"}
#dishes = {"bowls","plate"}

#utensils.update(dishes)
#for x in utensils:
 #   print(x)
#dinner_table = utensils.union(dishes)

#for x in dinner_table:
 #    print(x)
#cities = {'kenya':'nairobi','nanyuki'
         #  'tanzania':'moshi','zanzibar'
          # 'uganda':'kampala'}
#for x in cities:
# print(x)
#functions
#name= input("what is his name?")
#def vivian(age):
  #  print("she's gorgeous")
  #  print("she likes her boyfriend but sometimes she just wants to kill him")
  #  print("she's on day three of learning python today")
  #  print("she wishes she started sooner though")
  #  print("her boyfriends name is  " + name +" he is " + age +"years old")

#vivian("24")
#return function
#def multiply (number1,number2):
 #   return number1*number2
#x= multiply (3,5)
#print(x)
#def add(*numbers):
 #   sum=0
  #  numbers = list(numbers)
   # numbers[-2]=0
    #for i in numbers:
     #   sum += i
    #return sum
#print(add(2,4,3,2))
#print(add(4,6,5,4))

#def hello(**name):
 #   for key,value in name.items():
  #      print(value,end="")
#print("Hello",end="")
#hello(whatyournameis="bro",somethingyoureon="thin",somethingIlike="ice-cream")
#feeling1="hate"
#feeling2="feel"
#print("I {} the way I {} right now".format( feeling1, feeling2))

#number=3003920

#print("pi can be displayed as {:.4f}".format(number))
#print("{:b}".format(number))
# import random
#cards = random.randrange(1,2,3)

#print(cards)
#mylist =  ['rock','paper','scissors','spock']
#z =random.choice(mylist)
#print(z)
#try:
 #   numerator=int(input("enter a number:"))
  #  denominator=int(input("enter a number"))
   # result=numerator/denominator
    #print(result)
#except NameError:
 #   print("try other values")
#except TypeError:
  #  print("bring it on")
#else:
 #   print(result)
#finally:
#try:
# with open('C:\\Users\\desktop\\environment')as file:
 #  print(file.read())
#except FileNotFoundError:
 #   print("doesn't exist")

#text="i guess we're all really just cut from the same cloth"
#with open('trialanderror1.txt') as file:
 #   print(file.read())
#import shutil
#shutil.copyfile('trialanderror1.txt''')

#import os
#source=" fffff"
#destination ="C:\\Users\\user\\Desktop\\fffff"
#try:
 #   if os.path.exists(destination):
  #      print("already exists")
   # else :os.replace(source,destination)
    #print("file was moved")

#except FileNotFoundError:
 #   print(source+"not found")

#os.remove("test.txt")
#import weeks
#weeks.week4()
#weeks.week8()
#rock paper scissors game
#import random
#while True:
 #   choices =["rock","paper","scissors"]

  #  computer = random.choice(choices)
   # player = None
#while player not in choices:
 #   player= input ("rock, paper or scissors?")
  #  if player==computer:
   #    print("computer:", computer)
    #  print("tie")
    #elif player == "rock":
     #   if computer=="paper":
      #   print("computer:", computer)
       #  print("player:", player)
        # print("you lose")
    #if computer == "scissors":
     #    print("computer:", computer)
      #   print("player:", player)
       #  print("you win")
    #elif player == "paper":
     #   if computer=="rock":
      #   print("computer:", computer)
       #  print("player:", player)
        # print("you win")
        #if computer == "scissors":
         #print("computer:", computer)
         #print("player:", player)
         #print("you lose")
    #elif player == "scissors":
     #   if computer=="paper":
      #   print("computer:", computer)
       #  print("player:", player)
        # print("you win")
    #if computer == "rock":
     #    print("computer:", computer)
      #   print("player:", player)
       #  print("you lose")
    #play_again=input("play again?(yes/no):").lower()

    #f play_again != "yes":
     #   break
#print("bye")


# numbers = [2,2,2,5]
# for x_count in numbers:
#     output='x_count'
#
#     print (output)

# squares = []                      #create an empty
# for i in range (1,11):              #FOR LOOP
#     squares. append(i*i)              #DEFINE WHAT EACH SHOULD DOX
# print (squares)
#
# square = [ i*i for i in range (1,11)]
# print (square)
# list comprehensionms and dictionary comprehensions


# def temp (value):
#     if value >=40:
#         return "hot"
#     elif value <=39:
#         return "cold"
#
#
# cities = {'newyork':32,'nairobi':44,'nakuru':45,'chicogo':30}
# city= {key: temp(value) for (key,value)in cities.items()}
# print(city)

# zip function
# food= ("fries","fish","samosa","smokie")
# prices =(100,250,20,40)
# method = ("fried","boiled","fried","boiled/fried")
#
# menu =zip (food,prices,method)

# for i in menu:
#     print(i)

# import weeks
#
# weeks
