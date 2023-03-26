### 
# filename: upanddown.py 
# purpose:  algorithm analysis demo code
# author:   Dr. Johnson 
# date:     2023-02-23
### 

import math

def up_and_down( n ):
   print( "math.ceil(", n, ")  is: ", math.ceil(n) )
   print( "math.floor(", n, ") is: ", math.floor(n) )


def main():
   number = float( input( "Enter a floating point number: " ) )
   up_and_down( number )

main()
