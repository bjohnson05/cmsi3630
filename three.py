
def tick( seconds, minutes, hours, timeSlice ):
   totalSeconds = timeSlice
   returnValue = list()
   timeJunque = list()
   timeJunque.append( totalSeconds % 60 )
   timeJunque.append( int((totalSeconds / 60) % 60) )
   timeJunque.append( int(totalSeconds / 3600) )
   returnValue.append( totalSeconds % 60 )
   returnValue.append( int((totalSeconds / 60) % 60) )
   returnValue.append( int(totalSeconds / 3600) )
   return returnValue

print( tick( 23, 17, 11, 146400 ) )
