#USING WHILE LOOP IN A GUESSING GAME
#secret_word = "i miss you"
#i = 0
#guess_limit = 3
#while i < guess_limit:
 #   guess = input ("guess:")
  #  if guess == secret_word:
   #     print("you win")
#else:
    #print("do you really know me!?")
feeling = "" # you can use this when you're want to input a variable
while True:
    print ("GUESS THE FEELING")
    feeling = input (":").lower()
    if feeling == "happy":
        print("i can't stop smiling :)")
    elif feeling == "sad":
        print("i just wanna cry --")
    elif feeling == "grumpy":
        print("I miss you <>")
    elif feeling == "annoyed":
        print("it's not what you said it's how you said it :(")
    elif feeling == "idk":
        print("do you even knw me")
    else :
        print("achana tu nayo!")