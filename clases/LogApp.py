from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    @abstractmethod
    def eat(self): pass

    @abstractmethod
    def sleep(self): pass

    def breathe(self):
                 print ('Respirando aire')


class Dog(Animal):
    def eat(self):
                 print ('Come huesos')

    def sleep(self):
                 print ('perrera para dormir')


class Cat(Animal):
    def eat(self):
                 print ('Come pescado')

    def sleep(self):
                 print ('Casa del gato dormido')

                 from abc import ABCMeta, abstractmethod