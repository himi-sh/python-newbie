# Class Method Vs Static Method

# Class => can access and modify class params, @classmethod decorator, method's first argument is cls variable,
# used for cases like building factory patterns
# static => can't access & modify params, @staticmethod decorator, no specific arg requirement, used as utility methods

from _datetime import date

class Person:

    def __init__(self, name, age):
        print("__init__ log")
        self.name = name
        self.age = age

    @classmethod
    def ageFromBirthYear(cls, name, doy):
        print("class method log ")
        print("cls => %s" % (cls))
        return cls(name, date.today().year - doy)

    @staticmethod
    def isAdult(age):
        return age >= 18

person1 = Person('Himani', 20)
person2 = Person.ageFromBirthYear('Ayush', 2011)
print(person1.age)
print(person2.age)
print("Static method ", Person.isAdult(20))
