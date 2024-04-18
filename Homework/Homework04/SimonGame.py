###
# filename: SimonGame.py
# purpose: plays the old 80's game 'Simon'
# author:   Dr. Johnson
# date:     2023-03-27
###

import random
import time
import datetime
import sys
import os


letters = 'BYRG'

def compare( game, user ):
   for i in range( len( game ) ):
      if( game[i] != user[i] ):
         return False
   return True

def hide( count ):
   for i in range( count + 3 ):
      print( "   ", end="", flush=True )
   print( "\r" )

def play():
   print( "\n\n   WELCOME TO SIMON!" )
   print( "   =================" )
   print( "\n\n   Simon will display a random letter which you must match." )
   print( "   When it is your turn, Simon will prompt you to enter your letter." )
   print( "   If your letter matches, the game will continue." )
   print( "   Simon will add one new letter to the series with every turn." )
   print( "   As long as you keep guessing the correct letter, the game continues." )
   print( "   If you are incorrect, the game is over and Simon wins." )
   print( "   Simon will play as long as you keep guessing correctly.")
   print( "\n   Would you like to play? [Y/N]", end="" )
   doit = input( "     ==>  " ).upper()
   if( doit == 'N' ):
      exit()
   else:
      doit = 'Y'
     # print some lines so the display isn't at the bottom
      print( "\n\n\n\n\n\n\n" )
     # set up a random selection, seeded with the system clock
      x = datetime.datetime.now()
      random.seed( x.strftime("%S") )
      count = 1
      sleepTime = 2
      gameLine  = ""

     # this is the game loop.... it continues as long as the user's input\
     #   matches the game's saved string of letters
      os.system( "cls" )
      while( doit == 'Y' ):
         i = letters[random.randint(0,3)]
         if count == 1:
            gameLine = i
         else:
            gameLine = gameLine + letters[random.randint(0,3)]
         print( "   ", gameLine, end="\r", flush=True )
         time.sleep( sleepTime )
         hide( count )
         print( "   now you: ", end="", flush=True )
         entry = input( "" ).upper()
         os.system( "cls" )
         if( len( entry ) != len( gameLine ) ) or ( not compare( gameLine, entry ) ):
            print( "\n\n   Sorry, you lose ~ Simon wins!!" )
            time.sleep( 3 )
            print( "\n\n   Would you like to play again? [Y/N]", end="" )
            doit = input( "     ==>  " ).upper()
            if( doit == 'N' ):
               break;
            else:
               sleepTime = 2
               gameLine = ""
               os.system( "cls" )
         count += 1
play()
