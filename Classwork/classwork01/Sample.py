
class Sample:
   myString = "This is a string in the Python Language."
   primenumber = 23
   myAmount = 234.56

   def __init__( self, value ):        # this is the 'constructor
      self.myString = value

   def resetAmount( newAmount ):
      myAmount = newAmount
      return myAmount

   def isPrime( value ):
      result = False
      # some code to determine prime-ness of 'value'
      return result

# this is how we instantiate the class
s1 = Sample( "New string")
s2 = Sample( "Another new string")

# this is how we can access the values
print( s1.myString )
print( s1.primenumber )
print( s2.myAmount )
