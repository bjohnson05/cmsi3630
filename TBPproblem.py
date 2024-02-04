
count = 0

for i in range( 100001 ):
   if ((2**i - i**2) % 7) == 0:
      print( "found one" )
      count += 1
print( count )
