###
# filename: intsorter.py
# purpose:  demonstrator of bubble sort algorithm
# author:   Dr. Johnson
# date:     2023-02-07
###

class int_sorter:
   a = []         # this is the list that will be sorted

   # 'constructor'
   def __init__( self, values ):
      self.a = values.copy()

   # swap values at the two index arguments
   def swap_ints_at( self, index1, index2 ):
      temp = self.a[index1]
      self.a[index1] = self.a[index2]
      self.a[index2] = temp
      return

   # a 'to string' method to make the list a string
   #  not really necessary, kind of a holdover from Java
   def to_string( self ):
      b = str( self.a )
      return b

   # the bubble sort implementation
   def bubble_sort( self ):
      for i in range( len( self.a ) ):
         for j in range( 0, len( self.a ) - i - 1 ):
            if( self.a[j] > self.a[j + 1] ):
               self.swap_ints_at( j, j + 1 )
      return

   # the insertion sort implementation
   def insertion_sort( self ):
      for i in range( 1, len( self.a ) ):
         temp = self.a[i]
         j = i - 1
         while( j >= 0 and temp < self.a[j] ):
            self.a[j+1] = self.a[j]
            j = j - 1
         self.a[j+1] = temp
      return

   # an 'instrumented' insertion sort implementation
   #  same algorithm, just with 'print()' statements
   #  allows you to see what's going on during execution
   def insertion_sort_P( self ):
      print( "  insertion sort ~ list: ", self.a )
      for i in range( 1, len( self.a ) ):
         temp = self.a[i]
         j = i - 1
         while( j >= 0 and temp < self.a[j] ):
            print( "  insertion sort loop ~ i: ", i, " ~ j: ", j, " ~ temp: ", temp )
            print( "     ", self.a, " becomes: ", end="" )
            self.a[j+1] = self.a[j]
            print( self.a, " and then: ", end="" )
            j = j - 1
         self.a[j+1] = temp
         print( self.a )
      print( "  insertion sort ~ list: ", self.a )
      return

# OK, here's some test code for testing it out...
#  not in a 'main()' but could be if you wanted to do it
#
#  first, make a list and use it to make an instance of
#     'int_sorter'; then check the 'swap_ints_at()' function
#     before calling 'bubble_sort()'
test_list = [77, 66, 55, 44, 33, 22, 11]
sorter = int_sorter(test_list)
print( "\n test_list before swap is: ", sorter.to_string() )
sorter.swap_ints_at( 0, 1 )
print( "\n test_list after  swap is: ", sorter.to_string() )
sorter.bubble_sort()
print( "\n test_list after  sort is: ", sorter.to_string() )

# now clear the list and insert a bunch more values for a
#  second test of just the bubble sort
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

# now clear the list and insert the values again for a test
#  of the insertion sort
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

# now another test of the bubble sort
test_list.clear()
test_list.append( 99 )
test_list.append( 79 )
test_list.append( 23 )
test_list.append( 19 )
test_list.append(  2 )
sorter = int_sorter(test_list)
print( "\n test_list before swap is: ", sorter.to_string() )
sorter.bubble_sort()
print( "\n test_list after  sort is: ", sorter.to_string() )

# finally another test of insertion sort, but this time with
#  printing the interim values using the instrumented code
test_list.clear()
test_list.append( 99 )
test_list.append( 79 )
test_list.append( 23 )
test_list.append( 19 )
test_list.append(  2 )
sorter = int_sorter(test_list)
print( "\n test_list before swap is: ", sorter.to_string() )
sorter.insertion_sort_P()
print( "\n test_list after  sort is: ", sorter.to_string() )
