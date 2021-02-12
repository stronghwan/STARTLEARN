class Animal:
    def __init__(self, new_name):
        self.__name = new_name

    def eat(self):
        print("吃东西")
    def getName(self):
        return self.__name
    def setName(self, value):
        self.__name = value
        return self.__name
class Cat(Animal):
    def __init__(self, new_value):
        self.__name = new_value;

test1 = Animal("dog")
print(test1.eat())
print(test1.getName())
test1.setName("cat")
print(test1.getName())
print("-"*20)
test2 = Cat("cat")
test2.eat()
