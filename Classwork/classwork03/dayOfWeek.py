import sys
import time

dayOfWeek = [ 'Monday', 'Tuesday', 'Wednesday', \
              'Thursday', 'Friday', 'Saturday', 'Sunday' ]

if( len( sys.argv ) < 2 ):
   print( "\n   You must supply a date of form yyyy-mm-dd.\n" )
else:
   theDate = sys.argv[1]
   print( "\n     Finding day of week for date:", theDate )
   day_variable = time.strptime( theDate, "%Y-%m-%d" )
   print( "   That date's day of the week is:", dayOfWeek[day_variable.tm_wday] )


