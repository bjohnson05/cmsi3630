###
# filename: Polygon.py
# purpose: demonstration of subclassing
# author:   Dr. Johnson
# date:     2024-04-16
###

import math

# Define a base class of Polygon
#  We'll use this to subclass all the other shapes
class Polygon:
   def __init__( self, sides ):
      self.sideCount  = sides
      self.sideLength = 0
      self.fillColor  = None

   def setColor( self, color ):
      self.fillColor = color

   def area( self ):
      pass     # 'pass' means we'll define it later

# Define a Triangle subclass from Polygon
#  Overrides the 'area()' from the superclass
class Triangle( Polygon ):
   def __init__( self, length ):
      super().__init__( 3 )
      self.sideLength = length

   def area( self ):
      sideSquared = self.sideLength * self.sideLength
      height = math.sqrt( sideSquared - (sideSquared / 4.0) )
      base = self.sideLength / 2.0
      return (base * height) / 2.0

# Define a Rectangle subclass from Polygon
#  Overrides the 'area()' from the superclass
class Rectangle( Polygon ):
   def __init__( self, length, width ):
      super().__init__( 4 )
      self.sideLength = length
      self.sideWidth  = width

   def area( self ):
      return self.sideLength * self.sideWidth

# Define a Square subclass from Polygon
#  Overrides the 'area()' from the superclass
class Square( Polygon ):
   def __init__( self, side ):
      super().__init__( 4 )
      self.sideLength = side

   def area( self ):
      return self.sideLength ** 2

# Define a Pentagon subclass from Polygon
#  Overrides the 'area()' from the superclass
class Pentagon( Polygon ):
   def __init__( self, side ):
      super().__init__( 5 )
      self.sideLength = side

   def area( self ):
      return self.sideLength ** 2

# Define a Hexagon subclass from Polygon
#  Overrides the 'area()' from the superclass
class Hexagon( Polygon ):
   def __init__( self, side ):
      super().__init__( 6 )
      self.sideLength = side

   def area( self ):
      return self.sideLength ** 2

p = Polygon( 17 )
print()
print( "   Polygon.sideCount : ", p.sideCount )
print( "   Polygon.sideLength: ", p.sideLength )
print( "   Polygon.fillColor : ", p.fillColor )
print( "   Polygon.area      : ", p.area() )

t = Triangle( 5 )
t.setColor( "red" )
print()
print( "   Triangle.sideCount : ", t.sideCount )
print( "   Triangle.sideLength: ", t.sideLength )
print( "   Triangle.fillColor : ", t.fillColor )
print( "   Triangle.area      : ", t.area() )

r = Rectangle( 17, 11 )
r.setColor( "orange" )
print()
print( "   Rectangle.sideCount : ", r.sideCount )
print( "   Rectangle.sideLength: ", r.sideLength )
print( "   Rectangle.fillColor : ", r.fillColor )
print( "   Rectangle.area      : ", r.area() )

s = Square( 19 )
s.setColor( "yellow" )
print()
print( "   Square.sideCount : ", s.sideCount )
print( "   Square.sideLength: ", s.sideLength )
print( "   Square.fillColor : ", s.fillColor )
print( "   Square.area      : ", s.area() )

pnt = Pentagon( 7 )
pnt.setColor( "green" )
print()
print( "   Pentagon.sideCount : ", pnt.sideCount )
print( "   Pentagon.sideLength: ", pnt.sideLength )
print( "   Pentagon.fillColor : ", pnt.fillColor )
print( "   Pentagon.area      : ", pnt.area() )

h = Hexagon( 13 )
h.setColor( "blue" )
print()
print( "   Hexagon.sideCount : ", h.sideCount )
print( "   Hexagon.sideLength: ", h.sideLength )
print( "   Hexagon.fillColor : ", h.fillColor )
print( "   Hexagon.area      : ", h.area() )
