names = [ "John", "Mark","Luke","Fridah","Garvin","Mathew","John","Mark","Joel"]

for i in names:
    print(i)

for i in range(0,len(names)):
    for u in range(i +1,len(names)):
        if (names[i]==names[u]):
         print ("the repeated names are:"  +names[u])

a = names[3]
print("the name is:" +a)

names.append( "Joel")

for i in names:
    print("NEW LIST:")
    print(i)

names.pop(3)

for i in names:
    print("updated list:")
    print(i)

names.sort()
print(names)

names.sort(key=len)
print(names)

total= len(names)
print(total)

scores= [45,30,33,24,33,44,56,76,89]

scores.sort()
print(scores)

scores.sort(reverse= True)
print(scores)

for i in range(0,len(scores)):
 for j in range (i +1,len(scores)):
    if (scores[i] == scores[j]):
        print(scores[j]);



