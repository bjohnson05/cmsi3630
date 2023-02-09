###
# filename: intsorter.py
# purpose:  demonstrator of bubble sort algorithm
# author:   Dr. Johnson
# date:     2023-02-07
###

class int_sorter:
   a = []

   def __init__( self, values ):
      self.a = values.copy()

   def swap_ints_at( self, index1, index2 ):
      temp = self.a[index1]
      self.a[index1] = self.a[index2]
      self.a[index2] = temp
      return

   def to_string( self ):
      b = str( self.a )
      return b

   def bubble_sort( self ):
      for i in range( len( self.a ) ):
         for j in range( 0, len( self.a ) - i - 1 ):
            if( self.a[j] > self.a[j + 1] ):
               self.swap_ints_at( j, j + 1 )
      return

   def insertion_sort( self ):
      for i in range( 1, len( self.a ) ):
         temp = self.a[i]
         j = i - 1
         while( j >= 0 and temp < self.a[j] ):
            self.a[j+1] = self.a[j]
            j = j - 1
         self.a[j+1] = temp
      return

# OK, here's some test code for testing it out...
test_list = [77, 66, 55, 44, 33, 22, 11]
sorter = int_sorter(test_list)
print( "\n test_list before swap is: ", sorter.to_string() )
sorter.swap_ints_at( 0, 1 )
print( "\n test_list after  swap is: ", sorter.to_string() )
sorter.bubble_sort()
print( "\n test_list after  sort is: ", sorter.to_string() )

test_list.clear()
test_list.append( 99 )
test_list.append( 23 )
test_list.append( 79 )
test_list.append(  2 )
test_list.append( 19 )
test_list.append(  5 )
test_list.append( 11 )
test_list.append( 13 )
test_list.append(  7 )
test_list.append( 17 )
test_list.append(  3 )
sorter = int_sorter(test_list)
print( "\n test_list before swap is: ", sorter.to_string() )
sorter.bubble_sort()
print( "\n test_list after  sort is: ", sorter.to_string() )

test_list.clear()
test_list.append( 99 )
test_list.append( 23 )
test_list.append( 79 )
test_list.append(  2 )
test_list.append( 19 )
test_list.append(  5 )
test_list.append( 11 )
test_list.append( 13 )
test_list.append(  7 )
test_list.append( 17 )
test_list.append(  3 )
sorter = int_sorter(test_list)
print( "\n test_list before swap is: ", sorter.to_string() )
sorter.insertion_sort()
print( "\n test_list after  sort is: ", sorter.to_string() )
