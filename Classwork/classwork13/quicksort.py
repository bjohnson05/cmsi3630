###
# filename: quicksort.py
# purpose: demonstrate quicksort algorithm
# author: Dr. Johnson
# date: 2023-04-04
###

DEBUG = False

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
   if( DEBUG ):
      print( "   lowBound: ", lowBound, " ..highBound: ", highBound )

   if lowBound < highBound:

      # Find pivotPoint element such that
      # element smaller than pivotPoint are on the left
      # element greater than pivotPoint are on the right
      pi = makePartition( dataList, lowBound, highBound )

      # Recursive call on the left of pivotPoint
      quickSort( dataList, lowBound, pi - 1 )

      # Recursive call on the right of pivotPoint
      quickSort( dataList, pi + 1, highBound )

'''
' the following code is from:
'    https://www.youtube.com/watch?v=pM-6r5xsNEY
' this link provides a VERY clear and good explanation
' of how quicksort works\
'''
def quickSort2( dataList, start, end ):
   if( start < end ):
      mid = int( (start + end) / 2 )
      pivot = dataList[mid]
      index = partition2( dataList, start, end, pivot )
      if( DEBUG ):
         print( "     in quicksort2, mid: ", mid, " pivot: ", pivot, " index: ", index )
      quickSort2( dataList, start, index-1 )
      quickSort2( dataList, index, end )

def quickSortAlgo( dataList ):
   quickSort2( dataList, 0, len(dataList) - 1 )

def partition2( dataList, left, right, pivot ):
   if( DEBUG ):
      print( "     In partition2, l: ", left, " r: ", right, " pivot: ", pivot )
   while left <= right:
      while dataList[left] < pivot:
         left += 1
      while dataList[right] > pivot:
         right -= 1
      if( left <= right ):
         dataList[left], dataList[right] = dataList[right], dataList[left]
         left += 1
         right -= 1
   return left
