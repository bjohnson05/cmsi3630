
length = 5
for i in range( length + 1 ):
   print( "*" * i )

def stars( length ):
   if length < 1:
      return
   else:
      stars( length -1 )
   print( "*" * length )

mylength = int( input( "Enter number of stars:" ) )
stars( mylength )
