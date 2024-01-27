items = ["smokies","samosa","chapo","kebab","smocha"]

prices= [30,30,30,40,60]



items.append(input("What can' you find:"))
prices.append (int(input("suggested prices:")))

# for i in items:
#     print(i)
#
# for i in prices :
#     print(i)

menu = zip(items,prices)

for i in menu :
    print(i)