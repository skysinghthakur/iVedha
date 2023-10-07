class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def setName(self, name):
        self.name = name

person1 = Person("Akash", 24)
person2 = Person("Naman", 25)

print(person1.getName(), person1.getAge())
print(person2.name, person2.age)
