###
# filename: democode.py
# purpose:  show unpacking and joining
#           show slicing
# author:   Dr. Johnson
# date:     2023-02-09
###

# section showing the 'unpack' operation
a = '123456789'
b = [*a]
print( "a is: ", a )
print( "b is: ", b )

# section showing the 'slice' operation
c = a[0:3]
d = b[4:6]
print( "c is slice of a from 0 to 3: ", c )
print( "d is slice of b from 4 to 6: ", d )

# section showing the 'join()' operation
e = "".join(d)
print( "e is join of d with no spaces: ", e )

# section showing 'cnunkification' of a number
CHUNK_SIZE = 3
i = len( a )
j = len( a ) - CHUNK_SIZE
s = []
while( j > -CHUNK_SIZE ):
   s.append( a[j:i] )
   j -= CHUNK_SIZE
   i -= CHUNK_SIZE
print( "s is a chunkified by 3: ", s )

# another chunk, but with a string that is NOT
#  of an even number of chunks; one left
f = '1234567891472583'
print( "f is: ", f )
i = len( f )
j = len( f ) - CHUNK_SIZE
t = []
while( j >= 0 ):
   t.append( f[j:i] )
   j -= CHUNK_SIZE
   i -= CHUNK_SIZE
if( len(f) % CHUNK_SIZE != 0 ):
   t.append( f[0: (len(f) % CHUNK_SIZE)] )
print( "t is f chunkified by 3 with 1 leftover: ", t )

# another chunk, but with a string that is NOT
#  of an even number of chunks; two left
g = '12345678914725830'
print( "g is: ", g )
i = len( g )
j = len( g ) - CHUNK_SIZE
w = []
while( j >= 0 ):
   w.append( g[j:i] )
   j -= CHUNK_SIZE
   i -= CHUNK_SIZE
if( len(g) % CHUNK_SIZE != 0 ):
   w.append( g[0: (len(g) % CHUNK_SIZE)] )
print( "w is g chunkified by 3 with 2 leftover: ", w )



















