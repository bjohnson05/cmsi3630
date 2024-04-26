###
#  filename: one-liner.py
#  purpose: demonstration
#  author: Dr. Johnson
#  date: 2024-04-23
###

a = 23
b = 17
c = 31
d = 11
e = 29
print( "a: ", a, " b: ", b, " c: ", c, " d: ", d, " e: ", e )

temp = a
a = b
b = temp
print( "a: ", a, " b: ", b, " c: ", c, " d: ", d, " e: ", e )

a, b = b, a
print( "a: ", a, " b: ", b, " c: ", c, " d: ", d, " e: ", e )

a, b, c = c, a, b
print( "a: ", a, " b: ", b, " c: ", c, " d: ", d, " e: ", e )

a, b, c, d = d, c, a, b
print( "a: ", a, " b: ", b, " c: ", c, " d: ", d, " e: ", e )

