import sys

def bozo():
   r1 = int( sys.argv[1] )
   r2 = int( sys.argv[2] )
   r3 = int( sys.argv[3] )
   rt = 1/(1/r1 + 1/r2 + 1/r3)
   return rt

print( bozo() )
