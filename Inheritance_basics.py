class Animal:
    def eat(self):
        print("Animal eating")

    def walk(self):
        print("Animal walking")

class dog(Animal):

    def barks(self):
        print("Animal barks")

d1 = dog()
d1.eat()
d1.walk()
d1.barks()


   