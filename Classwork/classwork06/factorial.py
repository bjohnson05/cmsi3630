'''
filename: factorial.py
purpose: demonstrate recursion
         also demonstrat step-by-step code development
         also probably show some debugging techniques
author: Dr. Johnson
date: 2025-02-21
'''

def fact( n ):
   if( n == 1 ):
      return 1
   else:
      return n * fact( n - 1 )

def main():
   value = int( input( "\n   Enter a number to calculate factorial: " ) )
   print( "\n   Factorial of ", value, " is: ", fact( value ) )

main()
