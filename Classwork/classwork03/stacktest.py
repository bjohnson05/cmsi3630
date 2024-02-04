
class Stack:
   myStack = list()
   size = 0

   def push( self, value ):
      self.myStack.append( value )
      self.size = self.size + 1 

   def pop( self ):
      self.size = self.size -1
      return self.myStack[self.size]

s = Stack()
s.push( 2 )
s.push( 3 )
s.push( 5 )
s.push( 7 )
s.push( 11 )
s.push( 13 )
print( s.myStack )
print( s.pop() )
print( s.myStack )


