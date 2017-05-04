""" The Blueprints for Jeans """

class Jeans:
    def __init__(self, waist=0,length=0,color='blue'):
        self.waist = waist
        self.length = length
        self.color = color
        self.wearing = False

    def put_on(self):
        print ("Putting on {}x{} {} jeans".format(self.waist,self.length,self.color))
        self.wearing = True

    def take_off(self):
        print "Taking off {}x{} {} jeans".format(self.waist,self.length,self.color)
        self.wearing = False


myJeans = Jeans(30,30,"blue");
print dir(myJeans)
print type(myJeans)
myJeans.put_on()
myJeans.take_off()