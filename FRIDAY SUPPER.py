import random

meals = ['fries','rice','samosa','fish','buns']
snacks = ['pineapples','milk','juice','ice cream']

meals.sort()
snacks.sort()

for i in meals:
    print(i)
for i in snacks :
    print(i)


meal= random.choice (meals)
snack=random.choice(snacks)

print("the meal is " +meal)
print("the snack is " +snack)