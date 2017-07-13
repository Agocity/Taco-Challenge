import time
class taco():
    def __init__(self, addTaco, meat, topping):
        self.add = addTaco
        self.meat = meat
        self.topping = topping

    def finished(self):
        print ("Your taco has " + self.meat + " with the topping of " + self.topping)


item = taco("add", "meat", "topping")

AddTaco =  "self.add"
meat = "self.meat"
topping = "self.topping"

print ("Hello, I will make a taco for you based on what you want!!!!")
time.sleep(4)

meatype = input("Type 'AddTaco' to make new taco")
if meatype == AddTaco:
    print ("Great! Now choose a meat")
    time.sleep(2)
meat = input("Type the meat you want to have")
print ("Next")
topping = input("What topping do you want")
print ("Done!!")
taco.finished()






