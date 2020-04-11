class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old.")

    def speak(self):
        print("I don't know what to speak.")


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")


class Dog(Animal):
    def speak(self):
        print("Bark")


a = Animal("animal", 8)
a.show()
a.speak()

c = Cat("pussy", 4, "brown")
c.show()
c.speak()

d = Dog("tommy", 5)
d.show()
d.speak()
