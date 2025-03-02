###
#  filename: putoff.py
#  purpose: silly little program to calculate whether
#     you should put something off or do it today
#     from the book "Geek Logik" by Garth Sundem
#        ISBN:978-0-7611-4021-4
#  author: Dr. Johnson
#  date: 2025-01-23
#  description: the program asks the user for seven
#     'parameters' which are used in the equation to
#     determine if the task should be done today or
#     can be put off until tomorrow or another later
#     date.  If the output calculated value comes out
#     greater than one, you should do the task today
#     and get it over with.
#
#     The equation is:
#
#        50D
#        ---  +  P^2  +  U * E
#        T^2
#        ---------------------  =  DOIT
#              H * L * U
#
#     Please refer to the book page 90 - 91 for the
#     explanation of variables L, P, E, U, T, and H.
#     DOIT is, of course, the output value.
###

#  global variables
likelihood = 0 # Likelihood someone will be upset if you don't do the task
pissed = 0     # How pissed with that person be 0=not, 10=very
easier = 0     # If not done does task get easier or harder -5 to +5
unpleasant = 0 # How unpleasant is the task 0=not, 10=very
totality = 0   # Days task can be put off until it becomes essential
disaster = 0   # Disaster level if task becomes overdue 1=none, 10=armageddon
history=0      # Historic level of your procrastination 1=never, 10=always

def instructions():
   print( "\n\n   Calculate the probability of procrastination\n\n" )

def getValue( message ):
   return int( input( message ) )

def rangeCheck( value, min, max ):
   if( (value >= min) and (value <= max) ):
      return value
   else:
      return -9999

def main():
   instructions()

   print( "\n   What is the likelihood someone will be upset if you don't do this task?" )
   likelihood = getValue( "      Enter a value from 1 - 10, 10 being most upset: " )
   if( -9999 == rangeCheck( likelihood, 1, 10 ) ):
      instructions()
      return

   print( "\n   How pissed with that person be?" )
   pissed = getValue( "      Enter a value from 1 - 10, 10 being totally pissed: " )
   if( -9999 == rangeCheck( pissed, 1, 10 ) ):
      instructions()
      return

   print( "\n   If it's not done, does the task get easier or harder?" )
   easier = getValue( "      Enter a value from -5 to +5, with +5 being REALLY hard: " )
   if( -9999 == rangeCheck( easier, -5, 5 ) ):
      instructions()
      return

   print( "\n   How unpleasant is the task?" )
   unpleasant = getValue( "      Enter a value from 1 - 10, 10 being most unpleasant: " )
   if( -9999 == rangeCheck( unpleasant, 1, 10 ) ):
      instructions()
      return

   print( "\n   How many days can the task be put off until it becomes essential?" )
   totality = getValue( "      Enter a value from 1 - 10, 10 as long as possible: " )
   if( -9999 == rangeCheck( totality, 0, 365 ) ):
      instructions()
      return

   print( "\n   What is the disaster level if the task becomes overdue?" )
   disaster = getValue( "      Enter a value from 1 to 10, with 10 being armageddon: " )
   if( -9999 == rangeCheck( disaster, 1, 10 ) ):
      instructions()
      return

   print( "\n   What is your historic level of procrastination?" )
   history = getValue( "      Enter a value from 1 to 10, with 10 being always: " )
   if( -9999 == rangeCheck( history, 1, 10 ) ):
      instructions()
      return

   doit = (50 * disaster) / (totality * totality)
   doit = doit + (pissed * pissed) + (unpleasant * easier)
   doit = doit / (history * likelihood * unpleasant)

   print( "\n\n   OK, the probaility that you should do this task today is ", doit )
   if( doit > 1 ):
      print( "   ...so YOU'D BEST GET OFF YOUR BUTT AND GIT 'ER DUNNE!!!\n\n" )
   else:
      print( "   ...eh.... put it off until tomorrow at least...\n\n" )

main()
