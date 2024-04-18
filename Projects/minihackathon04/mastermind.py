###
#  filename: mastermind.py
#  purpose: playes the 'mastermind' game
#     using the computer against a human
#
#  In this assignment you will implement a program in python to play the
#     _MASTERMIND_ game.  The computer will pick four of the six colors using
#     the first letters of the color, either Red, Blue, Green, Yellow, Cyan,
#     or White ['R', 'B', 'G', 'Y', 'C', 'W'].  The human player will then
#     have 12 chances to guess the pattern.
#
#  Author: Dr. Johnson
#  Date: 2024-04-15
###

import random

def setup:
   colors = ['R', 'B', 'G', 'Y', 'C', 'W']
   indices = [-1, -1, -1, -1, -1, -1]
   assigned = 0
   while( assigned = 4):
      choice = random.randint( 0, 6 )
      if( indices[choice] == -1 ):
         indices[i] = choice
