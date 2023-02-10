###
# filename: Whoops.py
# purpose:  demonstrat scope for GC
# author:   Dr. Johnson
# date:     2023-01-05
###

class Whoops:
   def main( self ):
      i = 5
      if( i < 6 ):
         whoops = 6
      print( "\n   In Whoops.main, whoops is:", whoops )
      print( "\n\n" )

w = Whoops()
w.main()
print( w.whoops )
