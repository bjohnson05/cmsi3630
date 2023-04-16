###
# filename: mergesorttest.py
# purpose: tester to call mergesort.py
# author: Dr. Johnson
# date: 2023-04-04
###

from mergesort import mergeSort

def main():
   data = [ 123, 987, 234, 876, 345, 765, 456, 654, 567, 543, 678, 432, 789, 321, 0]

   print( "\n\n   MergeSort demonstrator program\n" )
   print( "   Prior to sort : ", data )
   mergeSort( data, 0, (len(data) - 1) )
   print( "   After the sort: ", data )

main()
