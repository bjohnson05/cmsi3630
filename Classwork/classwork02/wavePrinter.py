
import math

NUMBER_OF_ROWS = 64
PERIOD = 16.0
AMPLITUDE = 12
numberOfStars = 0
for row in range( NUMBER_OF_ROWS ):
   waveHeight = math.fabs( math.sin( row * math.pi / PERIOD ) + 1 )
   waveHeight =  math.fabs( math.sin( row * math.pi / PERIOD ) + 1 )
   numberOfStars = int( round( AMPLITUDE * waveHeight, 0 ) )
   for col in range( numberOfStars ):
      print( "*", end = "" )
   print()
