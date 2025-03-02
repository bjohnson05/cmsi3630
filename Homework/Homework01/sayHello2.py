###
#  filename: sayHello2.py
#  purpose: simple hello world startup program
#  author: Dr. Johnson
#  date: 2024-01-22
###
name = input( "\n  What is your name? " )
if len(name) != 0:
   print( '\n Hello, ', name, '!\n\n' )
else:
   print( '\n  Hello, world! \n\n' )
