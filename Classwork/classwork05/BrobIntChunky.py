###
# filename: BrobInt.py
# purpose:  a python 'Big Integer' class
# author:   Dr. Johnson
# date:     2023-02-08
###
import sys

class BrobInt:

   string_rep = ''      # string containing the original value
   my_value   = []      # list containing the 'unpacked' string values
   backwards  = []      # list containing REVERSE of unpacked values
                        #  which facilitates 'normal order' addition [R to L]
   CHUNK_SIZE = 9       # constant number of digits in each chunk

   # constructor initialized the class fields
   def __init__( self, value ):
      self.string_rep = value
      self.my_value   = [*self.string_rep]      # this is the 'unpacking' operator
      self.backwards  = self.reverse_me( self.my_value )
      self.string_bak = ''.join( self.backwards )
      self.chunked    = self.chunkify( self.backwards )

   # helper method to reverse the list
   def reverse_me( self, a ):
      b = list( a )
      b.reverse()
      return b

   # method to 'chunkify' the unpacked string
   #  based on 'backwards' list, returns chunkified list
   def chunkify( self, a ):
      c     = []
      count = int( len(a) / self.CHUNK_SIZE )
      left  = int( len(a) % self.CHUNK_SIZE )
      start = 0
      stop  = self.CHUNK_SIZE
      print( "\n   in chunkify: count: {} left: {} start: {} stop: {}".format( count, left, start, stop ) )
      c = a.copy()
      return c

   # the 'add()' function which is the purpose of the exercise
   def add( self, other_brob_int ):
      carry   = 0       # carry for each addition
      sum     = []      # list to hold the eventual sum
      shorter = []      # list holding shorter of the two numbers
      longer  = []      # list holding longer of the two numbers

      ## find the longer of the two numbers
      ##   put the two numbers into the appropriate lists
      if( len(self.my_value) < len(other_brob_int.my_value) ):
         shorter = self.backwards.copy()
         longer = other_brob_int.backwards.copy()
      else:
         longer = self.backwards.copy()
         shorter = other_brob_int.backwards.copy()

      ## assign the lengths of the two numbers for readability
      short_len = min( len(longer), len(shorter) )
      long_len = max( len(longer), len(shorter) )

      ## add up the two numbers,
      ##   stopping after the shorter one has been added
      ##   to the shortest part of the longer one
      for i in range( short_len ):
         temp = int(longer[i]) + int(shorter[i]) + carry
         if( temp >= 10 ):
            temp -= 10
            carry = 1
         else:
            carry = 0
         sum.append( str(temp) )

      ## Now if they are NOT the same length
      ##   add the carry [if needed] to the next digit of
      ##   the longer number, then continue adding in the
      ##   rest of the longer number
      if( long_len != short_len ):
         for i in range( short_len, long_len ):
            temp = int(longer[i]) + carry
            if( temp >= 10 ):
               temp -= 10
               carry = 1
            else:
               carry = 0
            sum.append( str(temp) )

      ## If there is still a carry, handle it
      if( carry == 1 ):
         sum.append( '1' )

      ## turn it back into a string and return the result
      sum = self.reverse_me( sum )
      return_value = "".join( sum )
      return return_value

##########
##  test code to check out the creation and addition
##########
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

##########
##  the main method gets the values to add from the command line
##    it checks to make sure there are enough values and outputs
##    a 'usage' message if there aren't
##########
def main():
   if( len(sys.argv) < 3 ):
      print( "\n  Usage:" )
      print( "   python BrobInt <number-1> <number-2>" )
      print( "   where the numbers each have at least 17 digits" )
      print( "   and must be positive integers ONLY" )
      print( "\n  Please try again!" )
   else:
      b1 = BrobInt( sys.argv[1] )
      b2 = BrobInt( sys.argv[2] )
      print( "\n     Adding: {0:>53}\n       plus: {1:>53}".format( sys.argv[1], sys.argv[2] ) )
      print( "             ------------------------------------------------------" )
      print( "   Total is: {0:>53}".format( b1.add( b2 ) ) )
#      print( "   Total is: {0:>len(sys.argv[1])}".format( b1.add( b2 ) ) )

main()
