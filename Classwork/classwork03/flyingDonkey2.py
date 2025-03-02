###
# another sample class file
###
class flyingDonkey:

   altitudeInFeet = 36000.123
   numberOfWings  = 4
   name = "Esmerelda"

   def __init__( self, itsCalled ):
      self.name = itsCalled

   def toString():
         print( "Flying Donkey:"  + self.name )

def main():
   print( "Kiss my grits!" )
   e = flyingDonkey( "Kevin" )
   f = flyingDonkey( "Jimmy Joe-don Bubba-Bob" )
   print( e )
   print( f )
   print( e.name )
   print( e.numberOfWings )
   print( e.altitudeInFeet )
   print( f.name )

main()
