### 
# filename: geeandeff.py 
# purpose:  yet another algo emo
# author:   Dr. Johnson 
# date:     2023-02-23
### 

def gee( a, n ):
   for i in a:                            # call this cost3
      print( "   value is: ", (i * n) )   # call this cost4
   print()

def eff( a ):
   for i in a:                            # call this cost1
      gee( a, i )                         # call this cost2

def main():
  my_a = [2, 3, 5, 7, 11, 13, 17, 19, 23]
  eff( my_a )

main()

