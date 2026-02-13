###
# filename: filedemo.py
# purpose:  file I/O demo
# authro:   Dr. Johnson
# date:     2023-01-04
###

filename = 'test.txt'
myFile = open( filename, "w" )
myFile.write( "\nHello, World!\n" )
myFile.write( "This is a line to write to the file.\n" )
myFile.write( "This is another line to write.\n" )
myFile.write( "This is the last line, followed by a bunch of newlines.\n" )
myFile.write( "\n\n\n\n\n\n\n" )
myFile.write( "EOF\n" )
myFile.close()

