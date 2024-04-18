###
# filename: oddevensorter.py
# purpose: performs odd/even sort tasks
# author:   Dr. Johnson
# date:     2023-03-27
###

def display( a_list ):
   for i in range( len( a_list ) ):
      print( "[{0:4d}]".format(a_list[i]), end="" )
   print()

# odd-even sort basically does a two-pass bubble sort
#  where for each pass, the odd values are bubbled,
#  then the even values are bubbled
def oddEvenSort( a_list ):
    isSorted = False
    n = len( a_list )
    while( not isSorted ):
        isSorted = True
        temp = 0
        for i in range( 1, n - 1, 2 ):
            if a_list[i] > a_list[i + 1]:
                a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
                isSorted = False

        for i in range( 0, n - 1, 2 ):
            if a_list[i] > a_list[i + 1]:
                a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]
                isSorted = False
    return
