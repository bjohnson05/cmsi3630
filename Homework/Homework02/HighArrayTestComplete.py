###
# filename: HighArrayTest.py
# purpose:  @see homework02 description at:
#    https:#bjohnson.lmu.build/cmsi3530web/homework02.html
# author:   Dr. Johnson
# date:     2023-01-04
###

from HighArray import HighArray

print( "\n   Welcome to the HighArray Program [Python Version]" )
print( "   =================================================" )
print( "   Initializing the list" )
arr = HighArray()
print( arr )

print( "   Adding ten items" )
arr.insert( 77 )                 # insert 10 items
arr.insert( 99 )
arr.insert( 44 )
arr.insert( 55 )
arr.insert( 22 )
arr.insert( 88 )
arr.insert( 11 )
arr.insert( 00 )
arr.insert( 66 )
arr.insert( 33 )

print( "\n   Current list contents:" )
arr.display()

print( "\n   Searching for 37:" )
found = arr.find( 37 )
if( found ):
   print( "Found it!" )
else:
   print( "Bummer, dude..." )

print( "\n   Searching for 11:" )
found = arr.find( 11 )
if( found ):
   print( "Found it!" )
else:
   print( "Bummer, dude..." )

print( "\n   Adding and removing to test get_max function..." )
arr.delete( 00 )          # delete 3 items
arr.delete( 55 )
arr.delete( 99 )
arr.display()             # display items again
print( "   Current max value is: ", arr.get_max() )    # should return 88
print( "   Adding 99 back in" )
arr.insert( 99 )
print( "   Current max value is: ", arr.get_max() )    # should return 99
arr.display()
print( "   Removing max value...", arr.delete(arr.get_max()) )
print( "   Removing max value...", arr.delete(arr.get_max()) )
print( "   Removing max value...", arr.delete(arr.get_max()) )
arr.display()
print( "\n   Adding 11, 00, 66, and 33 to make duplicates..." )
arr.insert( 11 )
arr.insert( 00 )
arr.insert( 66 )
arr.insert( 33 )
arr.display()
print( "   Current max value is: ", arr.get_max() )    # should return 77
arr.insert( 222 )
arr.insert( 111 )
arr.display()
print( "   Current max value is: ", arr.get_max() )    # should return 222
arr.delete( 222 )
arr.display()
print( "   Current max value is: ", arr.get_max() )    # should return 111
print( "\n   Adding 11, 00, 66, and 33 to make duplicates..." )
arr.insert( 11 )
arr.insert( 00 )
arr.insert( 66 )
arr.insert( 33 )
arr.display()
print( "\n   Removing dupes")
arr.a = arr.no_dupes()
arr.display()
print( "\n   Adding five copies of 33..." )
arr.insert( 33 )
arr.insert( 33 )
arr.insert( 33 )
arr.insert( 33 )
arr.insert( 33 )
arr.display()
print( "\n   Removing dupes")
arr.a = arr.no_dupes()
arr.display()

###
#  Removing duplicate values another way
###
print( "\n   Adding five copies of 33 to test no_dupes2()..." )
arr.insert( 33 )
arr.insert( 33 )
arr.insert( 33 )
arr.insert( 33 )
arr.insert( 33 )
arr.display()
print( "\n   Removing dupes 2")
arr.a = arr.no_dupes2()
arr.display()
print( "\n   TESTING COMPLETE!  THANKS FOR DROPPING BY..." )
