from abc import ABC, abstractmethod

class Animal(ABC):
    
    def move(self):
        pass

class Human(Animal):
    
    def move(self):
        print("I can walk and run and jump")
        
class Snake(Animal):
    def move(self):
        print(" I can crawl")
    
class Dog(Animal):
    def move(self):
        print(" I can bark")

class Puma(Animal):
    def move(self):
        print(" I can dfdsfg")
        

    