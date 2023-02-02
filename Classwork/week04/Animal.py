### 
# filename: Animal.py 
# purpose:  demonstrate subclassing
# author:   Dr. Johnson 
# date:     2023-01-15
### 

from abc import ABC, abstractmethod

class Animal( ABC ):             # this is a subclass of ABC
   animalName = None

   def __init__( self, name ):
      self.animalName = name

   def speak( self ):
#      phrase = self.animalName + " says " + self.sound()
      phrase = f"\n   {self.animalName}{' says '}{self.sound()}"
      return phrase

   @abstractmethod
   def sound( self ):
      pass                       # this indicates an empty method


class Cow( Animal ):             # this is a subclass of Animal
   # overriding the abstract method for Cows
   def sound( self ):
      return "MOO!"

class Horse( Animal ):             # this is a subclass of Animal
   # overriding the abstract method for Cows
   def sound( self ):
      return "NEIGH!"

class Goat( Animal ):             # this is a subclass of Animal
   # overriding the abstract method for Cows
   def sound( self ):
      return "MAA-AA-AA!"

class Sheep( Animal ):             # this is a subclass of Animal
   # overriding the abstract method for Cows
   def sound( self ):
      return "BAA BAA BAA!"


## test code
groucho = Cow( "Groucho")
print( groucho.speak() )
harpo = Horse( "Harpo")
print( harpo.speak() )
chico = Goat( "Chico")
print( chico.speak() )
zeppo = Sheep( "Zeppo")
print( zeppo.speak() )
