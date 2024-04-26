###
#  filename: triangle.py
#  purpose: demonstration
#  author: Dr. Johnson
#  date: 2024-04-23
###

def print_triangle( sideLength ):
   if sideLength < 1 :
      return
   else:
      print_triangle( sideLength - 1 )

   print( "*" * sideLength )

def main():
   length = int( input( "\n   Enter the number of units: " ) )
   print()
   print_triangle( length )

main()
