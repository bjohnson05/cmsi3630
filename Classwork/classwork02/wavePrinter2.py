
import math

NUMBER_OF_ROWS = 64
PERIOD = 16.0
AMPLITUDE = 12
numberOfStars = 0
for row in range( NUMBER_OF_ROWS ):
#   waveHeight = math.fabs( math.sin( row * math.pi / period ) + 1 )
#   waveHeight =  math.fabs( math.sin( row * math.pi / period ) + 1 )
#   numberOfStars = int( round( amplitude * waveHeight, 0 ) )
   numberOfStars += 1
   for col in range( numberOfStars ):
      if( numberOfStars == AMPLITUDE ):
         numberOfStars = 0
         break
      print( "*", end = "" )
   print()
