#method chaining use return self

class Car:
    def turn_on(self):
        print("you start the car")
        return self
    def drive(self):
        print("you drive the car")
        return self
    def brake(self):
        print("you step on the brakes")
        return self
    def stop(self):
        print("you stop the car")
        return self
car = Car()

car.turn_on().stop()
