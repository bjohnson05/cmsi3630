###
# filename: mergesort.py
# purpose: demonstrate quicksort algorithm
# author: Dr. Johnson
# date: 2023-04-04
###

# the code for doing the merge sort, which recursively divides the space until
#     there's nothing left to divide, then calls another method to put the list
#     back together in sorted order.
def mergeSort( workspace, lowerBound, upperBound  ):
   if( lowerBound < upperBound  ):

      # find the middle using floor division
      middle = lowerBound + (upperBound - lowerBound) // 2

      # Sort first and second halowerBoundves
      mergeSort( workspace, lowerBound, middle )
      mergeSort( workspace, (middle + 1), upperBound  )
      merge( workspace, lowerBound, middle, upperBound  )


# here is the merge method that re-assembles things into sorted order
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
   k = lowPtr  # InitialowPtr index of merged subarray

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
