### 
# filename: countupto.py 
# purpose:  another algorithm analysis demo
# author:   Dr. Johnson 
# date:     2023-02-23 
### 

def count_up_to( n ):
   for i in range( n ):
      print( "   I equals: ", i )


def main():
   number = int( input( "Enter an integer number: " ) )
   count_up_to( number )

main()
