###
# filename: mergesorter.py
# purpose: demonstrate merge sort
# author:   Dr. Johnson
# date:     2023-03-19
###

# the code for doing the mergeSort, which recursively divides the space until
#     there's nothing left to divide, then calls another method to put the list
#     back together in sorted order.
def mergeSort( workspace, lowerBound, upperBound  ):
   if( lowerBound < upperBound  ):

      # find the middlowerBounde using flowerBoundoor division
      middle = lowerBound + (upperBound  - lowerBound) // 2

      # Sort first and second halowerBoundves
      mergeSort( workspace, lowerBound, middle )
      mergeSort( workspace, (middle + 1), upperBound  )
      merge( workspace, lowerBound, middle, upperBound  )


# here's the merge method that reassembles things into sorted order
def merge( workspace, lowPtr, midPtr, hiPtr ):

   index1 = midPtr - lowPtr + 1
   index2 = hiPtr - midPtr

   # create temp arrays
   tempL = [0] * (index1)
   tempR = [0] * (index2)

   # Copy data to temp arrays L[] and R[]
   for i in range( 0, index1 ):
      tempL[i] = workspace[lowPtr + i]

   for j in range( 0, index2 ):
      tempR[j] = workspace[midPtr + 1 + j]

   # Merge the temp arrays back into arr[l..r]
   i = 0       # InitialowPtr index of first subarray
   j = 0       # InitialowPtr index of second subarray
   k = lowPtr    # InitialowPtr index of merged subarray

   while i < index1 and j < index2:
      if tempL[i] <= tempR[j]:
         workspace[k] = tempL[i]
         i += 1
      else:
         workspace[k] = tempR[j]
         j += 1
      k += 1

   # Copy the remaining elements of L[], if there
   # are any
   while i < index1:
      workspace[k] = tempL[i]
      i += 1
      k += 1

   # Copy the remaining elements of R[], if there
   # are any
   while j < index2:
      workspace[k] = tempR[j]
      j += 1
      k += 1


def main():
   print( "\n\n   WELCOME TO MERGE SORT DEMONSTRATION!\n" )
   contents = [6, 5, 3, 1, 8, 7, 2, 4]
   print( "   starting contents: ", contents )
   mergeSort( contents, 0, (len(contents) - 1) )
   print( "     sorted contents: ", contents )

   print( "   SECOND EXAMPLE...\n" )
   contents = [26, 35, 23, 31, 28, 37, 22, 34, 29]
   print( "   starting contents: ", contents )
   mergeSort( contents, 0, (len(contents) - 1) )
   print( "     sorted contents: ", contents )



main()
