# instance variables change
class Car:
    WHEELS = 4 #CLASS VARIBLE IT NEVER CHANGES FOR ALL ITEMS IN CLASS
     def __int__(self,model,colour,year,make):
         self.model = model#INSTANCE VARIABLE
         self.colour= colour#INSTANCE VARIABLE
         self.year= year#INSTANCE VARIABLE
         self.make =make#INSTANCE VARIABLE
     def drive(self):
         print('the "self.model" has drove off')