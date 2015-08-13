# Static Methods
class Car(object):

    wheels = 4

    #Static Methods
    @staticmethod
    def make_car_sound(): 
        print 'VRooooommmm!'

    # Class Methods
    @classmethod
    def is_motorcycle(cls):
        return cls.wheels == 2

    def __init__(self, make, model):
        self.make = make
        self.model = model


mustang = Car('Ford', 'Mustang')
print mustang.wheels
# 4
print Car.wheels 
# 4
mustang.make_car_sound()
Car.make_car_sound()

if mustang.is_motorcycle():
	print 'it is not a car'
else:
	print 'mustang is a car'