###
# filename: IMEIhash.py
# purpose: demonstrate the hashing algorithm invented
#           by Hans Luhn of IBM
# author:   Dr. Johnson
# date:     2023-04-06-2023
###

DEBUG = False
number = input( "   Enter a ten-digit number:" )
number = [*number]
if( DEBUG ):
   print( number )
sum = 0
for i in range( len( number ) ):
   number[i] = int( number[i] )
   if( DEBUG ):
      print( "   number[", i, "]:", number[i] )
   if( (i % 2) == 1 ):
      number[i] = number[i] * 2
      if( number[i] > 9 ):
         number[i] = 1 + (number[i]) % 10
   sum +=  number[i]
if( DEBUG ):
   print( "   post-if number[", i, "]:", number[i] )
sum *= 9
print( "\n\n   Modulus-10 algorithm sum:", sum )
print( "   Algorithm check digit: ", sum % 10 )
if( (sum % 10) == 0 ):
   print( "      indicates valid IMEI number.\n\n" )
else:
   print( "      indicates invalid IMEI number.\n\n" )

