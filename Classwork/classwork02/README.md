# In-class Assignment #2

In this week's class assignment we will make a small file copier.
The intent of the exercise is: 1) for you to get experience with python modules and 2) with file input/output using python; 3) with having different classes perform different operations as part of the program's functionality; 4) pseudocoding an algorithm for use
in designing the program; and 5) desk-checking of your algorithm to make sure it makes logical and operational sense. 

The file copier will be command line or terminal window driven. For help with file operations, you can do a search 
using "writing a file in python" and "reading a file in python". 

Note that the Stack Overflow entries may NOT be as useful as you may think! 

The specifications are as follows:

1. On a piece of paper, using english words, write a line-by-line definition of what your program should do, as follows:
   1. The program should open two files, one for reading and one for writing; open the one for reading first
   1. The program should then read the contents of the first file and return the contents as a string to the caller
   1. The program should then write the data out to the second file
   1. At the end, make sure to close both files and exit the program.
1. There will be three files in this program:
   1. <code>MyFileCopier.py</code> which is the main program and will be in the classwork02 directory
   1. <code>SourceFile.pya</code> which will be in the <code>copiersuppor</code> subdirectory; it handles reading the source file contents and returning them
   1. <code>TargetFile.py</code> which will also be in the <code>copiersuppor</code> subdirectory; it handles taking the contents passed in to it and writing them out to a <q>copy</q> file
1. The first file will be the main program and will instantiate the other two as needed, based on the following 
   specifications.
1. Put the <code>SourceFile.java</code> and <code>TargetFile.java</code> into the <code>copiersupport</code> subdirectory.
1. Be sure to put an appropriate import statement in your <code>MyFileCopier.py</code> file.
1. Running the program should initially prompt the user for a file name, then should read the user's input and treat
   that as the file to be copied [the source file].
1. The main program should then instantiate the SourceFile class, passing the source file name to the constructor;
   the Source file should then read in the entire source code file, placing the contents in a String which will be 
   returned to the main program.
1. Once the file has been read, the main program should then instantiate the TargetFile passing the file name to 
   the constructor ALONG WITH the String buffer with the file contents.
1. The TargetFile instance should then open a new file with a file name which is the same as the name passed in, 
   with the word <q>copy</q> appended to the name. In other words, if the file name is <code>input.txt</code>, the target 
   file is named <code>input.txt.copy</code>.
1. Now the TargetFile object must write the contents of the string buffer it is passed to the new file.
1. The main should then make sure that BOTH files are closed.
1. Test your program by creating a new file called <code>inputfile.txt</code>. Edit the file and put some text 
   into it, save it, then list the file contents using either the <code>more</code> or the <code>less</code>
   command in the terminal window.
1. Then test your program again by copying the <code>inputfile.txt</code> file and producing the output file named 
   <code>inputfile.txt.copy</code>. List the file contents of the target file to see that it is a duplicate of the 
   source file.
1. Upload and commit your completed <code>MyFileCopier.java</code>, <code>SourceFile.java</code>, and 
   <code>TargetFile.java</code> source code files to your GitHub repo for "classwork02"
1. Pat yourself on the back for a job well done! [Just don't hurt yourself…]
