### 
# filename: sillymultiply.py 
# purpose:  a third analysis demo
# author:   Dr. Johnson 
# date:     2023-02-23 
### 


def silly_multiply( n ):
   for i in range( n + 1 ):
      for j in range( n + 1 ):
         print( f"   {i:4d} times {j:4d} is: {(i*j):4d}".format(i, j, i * j) )

def main():
   number = int( input( "Enter an integer number: " ) )
   silly_multiply( number )

main()
