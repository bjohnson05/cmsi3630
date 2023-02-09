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
print( "c is: ", c )
print( "d is: ", d )

# section showing the 'join()' operation
e = "".join(d)
print( "e is: ", e )

# section showing 'cnunkification' of a number
CHUNK_SIZE = 3
i = len( a )
j = len( a ) - CHUNK_SIZE
s = []
while( j > -CHUNK_SIZE ):
   s.append( a[j:i] )
   j -= CHUNK_SIZE
   i -= CHUNK_SIZE
print( "s is: ", s )

# another chunk, but with a string that is NOT
#  of and even number of chunks
f = '1234567891472583'
print( "f is: ", f )
i = len( f )
j = len( f ) - CHUNK_SIZE
t = []
while( j > -CHUNK_SIZE ):
   t.append( f[j:i] )
   j -= CHUNK_SIZE
   i -= CHUNK_SIZE
if( len(f) % CHUNK_SIZE != 0 ):
   t.append( f[0: (len(f) % CHUNK_SIZE)] )
print( "t is: ", t )
