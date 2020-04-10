class Dog:

    # Like constructor in java
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("bark")

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age


d = Dog("Tommy", 5)  # object of class Dog
print(type(d))  # type of the object d
d.bark()  # calling bark method of object d
print(d.get_name())
print(d.get_age())
d.age = 23
print(d.get_age())
