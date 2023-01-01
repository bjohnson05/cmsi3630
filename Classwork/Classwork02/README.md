# In-class Assignment #2

In this week's class assignment we will make a small file copier. 
The intent of the exercise is for you to get experience with packages, and with having different classes perform 
different operations as part of the program's functionality. 

The file copier will be command line or terminal window driven. For help with file operations, you can do a search 
using "writing a file in java" and "reading a file in java". 

Note that the Stack Overflow entries may NOT be as useful as you may think! 

The specifications are as follows:

1. Name your program <code>MyFileCopier.java</code> and include two other classes, with the names of 
   <code>SourceFile.java</code> and <code>TargetFile.java</code>
1. The first file will be the main program and will instantiate the other two as needed, based on the following 
   specifications.
1. Put the <code>SourceFile.java</code> and <code>TargetFile.java</code> into a subdirectory called 
   <code>copiersupport</code>. Be sure to put the "package" statement at the top of both of the files.
1. Be sure to put an appropriate import statement in your <code>MyFileCopier.java</code> file.
1. Running the program should initially prompt the user for a file name, then should read the user's input and treat
   that as the file to be copied [the source file].
1. The main program should then instantiate the SourceFile class, passing the source file name to the constructor;
   the Source file should then read in the entire source code file, placing the contents in a String which will be 
   returned to the main program.
1. Once the file has been read, the main program should then instantiate the TargetFile passing the file name to 
   the constructor ALONG WITH the String buffer with the file contents.
1. The TargetFile instance should then open a new file with a file name which is the same as the name passed in, 
   with the word copy appended to the name. In other words, if the file name is <code>input.txt</code>, the target 
   file is named <code>input.txt.copy</code>.
1. Now the TargetFile object must write the contents of the String buffer to the new file.
1. The main should then close BOTH files.
1. Test your program by creating a new file called <code>inputfile.txt</code>. Edit the file and put some text 
   into it, save it, then list the file contents using either the <code>more</code> or the <code>less</code>
   command in the terminal window.
1. Then test your program again by copying the <code>inputfile.txt</code> file and producing the output file named 
   <code>inputfile.txt.copy</code>. List the file contents of the target file to see that it is a duplicate of the 
   source file.
1. Upload and commit your completed <code>MyFileCopier.java</code>, <code>SourceFile.java</code>, and 
   <code>TargetFile.java</code> source code files to your GitHub repo for "classwork02"
1. Pat yourself on the back for a job well done! [Just don't hurt yourself…]
