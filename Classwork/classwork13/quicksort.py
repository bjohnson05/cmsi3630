###
# filename: quicksort.py
# purpose: demonstrate quicksort algorithm
# author: Dr. Johnson
# date: 2023-04-04
###

# Function to find the partition position
def makePartition( dataList, low, high ):

   # choose the rightmost element as the pivotPoint
   pivotPoint = dataList[high]

   # make a pointer for the greater element
   i = low - 1

   # traverse through all elements in a loop, and compare
   #  each element with the 'pivotPoint' value
   for j in range( low, high ):
      if dataList[j] <= pivotPoint:

         # If element smaller than pivotPoint is found
         # swap it with the greater element pointed to by i
         i = i + 1

         # Swapping element at i with element at j
         dataList[i], dataList[j] = dataList[j], dataList[i]

   # Swap the pivotPoint element with the greater element specified by i
   dataList[i + 1], dataList[high] = dataList[high], dataList[i + 1]

   # Return the position from where makePartition is done
   return i + 1

# function to perform the actual recursive quicksort
def quickSort( dataList, lowBound, highBound ):
   if lowBound < highBound:

      # Find pivotPoint element such that
      # element smaller than pivotPoint are on the left
      # element greater than pivotPoint are on the right
      pi = makePartition( dataList, lowBound, highBound )

      # Recursive call on the left of pivotPoint
      quickSort( dataList, lowBound, pi - 1 )

      # Recursive call on the right of pivotPoint
      quickSort( dataList, pi + 1, highBound )

