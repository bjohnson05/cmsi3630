###
# filename: GuessingGame.py
# purpose:  demonstrate sets, while loops,
#           break, split, and replace
# author:   Dr. Johnson
# date:     2023-01-05
###


class GuessingGame:
   # note that the currly braces make this a set, not a list
   countries = {'vaticancity', 'nauru', 'tuvalu', \
                'palau', 'sanmarino', \
                'liechtenstein', 'monaco', 'st kitts', \
                'marshall islands', 'dominica'}

   def main( self ):
      print( "\n   Welcome to the Country Guessing Game. Guess the 10 smallest" )
      print( "   countries by population.  If at any time you want to give up," )
      print( "   just enter the single letter 'q' at the prompt.\n" )

      message = "Guess a country: "
      while( len( self.countries ) != 0 ):
         response = input( message )
         response = self.cleanupGuess(response)
         if( response == 'q' ):
            break
         elif( response in self.countries ):
            self.countries.remove( response )
            message = "Great, {} more to go!  Next guess: ".format( len( self.countries ) )
         else:
            message = "Try again: "
      if( len( self.countries ) == 0 ):
         print( "\n\n   YOU WIN!  Wow amazing job!" )
      else:
      # Be nice, and show the ones still in the set
         print( "\n\n   That's okay, you only missed ", self.countries )

    #
    # We want to be liberal with what we receive from the user, trying our best to
    # "normalize" it. We lowercase then remove all non-letter characters for ease
    # of comparison. But there are some special cases to consider also.
   def cleanupGuess( self, guess ):
      guess = guess.lower()
      return guess

gg = GuessingGame()
gg.main()
