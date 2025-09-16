class Animal:
    def speak(self):
        print('animal speaking')
class Cat(Animal):
    def speak(self):
        print('мяяу')
class Dog(Animal):
    def speak(self):
        print('гавна')
class CatDog (Dog, Cat):
    def speak(self):
        print('гавмяуmuuu')

kotopes = CatDog()
kotopes.speak()
print(CatDog.__mro__)
print(Dog.__mro__)