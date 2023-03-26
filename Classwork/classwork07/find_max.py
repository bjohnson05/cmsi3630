###
# filename: find_max.py
# purpose:  demonstration for algorithm counting
# author:   Dr. Johnson
# date:     2023-02-12
###

def find_max_in_list( a ):
   current_max = 0
   for i in range( len( a ) ):
      if( current_max < a[i] ):
         current_max = a[i]

   return current_max

first_list = [ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
second_list = [47, 43, 41, 37, 31, 29, 23, 19, 17, 13, 11, 7, 5, 3, 2]
third_list = [23, 19, 17, 13, 11, 7, 5, 3, 2, 47, 43, 41, 37, 31, 29]

print( "max in  first list: ", find_max_in_list( first_list ) )
print( "max in second list: ", find_max_in_list( second_list ) )
print( "max in  third list: ", find_max_in_list( third_list ) )
