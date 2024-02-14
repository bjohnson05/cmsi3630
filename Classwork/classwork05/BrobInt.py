###
# filename: BrobInt.py
# purpose:  a python 'Big Integer' class
# author:   Dr. Johnson
# date:     2023-02-08
###


class BrobInt:

   backwards  = []
   my_value   = []
   string_rep = ''

   def __init__( self, value ):
      self.string_rep = value
      self.my_value   = [*self.string_rep]      # this is the 'unpacking' operator
      self.backwards  = self.reverse_me( self.my_value )

   def reverse_me( self, a ):
      b = []
      j = len( a ) - 1
      for i in a:
         b.append( a[j] )
         j -= 1
      return b
         
   def add( self, other_brob_int ):
      carry = 0
      sum = []
      shorter = []
      longer = []
      if( len(self.my_value) < len(other_brob_int.my_value) ):
         shorter = self.backwards.copy()
         longer = other_brob_int.backwards.copy()
      else:
         longer = self.backwards.copy()
         shorter = other_brob_int.backwards.copy()
      short_len = min( len(longer), len(shorter) )
      long_len = max( len(longer), len(shorter) )
      for i in range( short_len ):
         temp = int(longer[i]) + int(shorter[i]) + carry
         if( temp >= 10 ):
            temp -= 10
            carry = 1
         else:
            carry = 0
         sum.append( str(temp) )
      if( long_len != short_len ):
         for i in range( short_len, long_len ):
            temp = int(longer[i]) + carry
            if( temp >= 10 ):
               temp -= 10
               carry = 1
            else:
               carry = 0
            sum.append( str(temp) )
      if( carry == 1 ):
         sum.append( '1' )
      sum = self.reverse_me( sum )
      return_value = "".join( sum )
      return return_value


b1 = BrobInt( '123456789' )
b2 = BrobInt( '13579' )
b3 = BrobInt( '2468')
b4 = BrobInt( '102030405060708090')
b5 = BrobInt( '123456784567890234567456782345623453456782345611234567')
b6 = BrobInt( '9999' )
print( "sum of b1 and b2:\n   expecting: 123470368\n         got:", b1.add( b2 ) )
print( "sum of b2 and b1:\n   expecting: 123470368\n         got:", b2.add( b1 ) )
print( "sum of b3 and b4:\n   expecting: 102030405060710558\n         got:", b3.add( b4 ) )
print( "sum of b4 and b5:\n   expecting: 123456784567890234567456782345623453558812750671942657\n         got:", b4.add( b5 ) )
print( "sum of b3 and b6:\n   expecting: 12467\n         got:", b3.add( b6 ) )
