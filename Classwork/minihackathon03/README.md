# Mini-Hackathon Number 3 &ndash; Hamming Encoding and Distance
## Learning Outcomes and Project Description

The purpose of this assignment is to broaden your understanding of data structures by understanding how _HAMMING DISTANCES_ and the _(7, 4) Hamming Code_ scheme is implemented.  The Hamming Code is one way of doing *ERROR DETECTION AND CORRECTION* [or "EDAC"] which is used in network transmissions of all kinds to detect if an error has occurred during transmission, and correct it if possible.

In this assignment you will implement a program in Java which will accept as its input the name of a file containing a list of strings corresponding to seven bit sequences and will determine whether or not they correspond to valid, or invalid signals.  In addition, for those strings that are determined to be invalid, the likely correct string is to be provided as well.  In other words, if the bit string is valid [no errors] output the proper string including it's Hamming code bits showing both the original file line and the expanded Hamming coded line.

## Specification

Define a program called <code>HammingCheck</code> which will accept as its input the name of a file containing a collection of strings corresponding to seven bit sequences will determine whether or not they correspond to valid or invalid signals.  In each case, the likely message is to be output as well.

Hamming Encoding uses the idea of **parity** to detect if a bit pattern contains the correct bit values.  You can find an explanation of how it works at [this location](https://www.tutorialspoint.com/hamming-code-for-single-error-correction-double-error-detection).

## Input File Specification

For this assignment you may assume that the input file is formatted with exactly one string per line and that the strings are guaranteed to correspond to typical seven-bit sequences.  As an example, the following is one possible input file:

<pre>
   1110000
   0101010
   1101011
   1111111
   0000000
   0000001
   EOF
</pre>

The "EOF" is optional and can be used to indicate the end of the data in the file if you like.  This will allow you to include comments in your file *AFTER* the data lines if you wish.  You can also omit the data and comments and only have the seven-bit sequences.  You can also come up with your own scheme to interpret
which lines are data, you can add comments after the data on each line, pretty much whatever you like, but the data lines MUST start with the seven-bit sequence.

## Program Focus

The idea of this program is for you to implement, using the *Hamming Distance* method, an *EDAC* program that can check a file stream and detect if there are errors.  If there is a "single-bit error" you can use the Hamming Code to correct it.  If there is more than a single-bit error, the Hamming Code will detect it, but you won't be able to correct it.

## Usage

The program <code>HammingCheck</code> is intended to be run via the following command-line invocation:
<pre>
     $ java HammingCheck input.txt
</pre>

If no input file is specified or if the input file is not found, an appropriate error message must be displayed. For example:
<pre>
     $ java HammingCheck
     
        HammingCheck: no input file was specified!
           Please try again
           
     $ java HammingCheck bogusfile.txt
     
        HammingCheck: input file 'bogusfile.txt' does not exist or cannot be opened.
           Please try again
           
</pre>

*If a valid file is specified as input*, then for every string in the file you must output its classification [either valid or invalid], and the decrypted string if applicable.  Using the file input.txt mentioned above, your program should behave as follows:

<pre>
   $ java HammingCheck input.txt
      1110000 - valid, data sent was 1000
      0101010 - valid, data sent was 0010
      1101011 - invalid, data sent was 0001
      1111111 - valid, data sent was 1111
      0000000 - valid, data sent was 0000
      0000001 - invalid, data sent was 0000
</pre>

# Compilation Notes

Your program must compile from the command line or terminal using the following invocation:
<pre>
   $ javac *.java
</pre>

Do not submit any IDE specific files and in the interest of simplicity do not use packages for this assignment.  If your program does not compile using the command mentioned above you will receive no credit.

# Additional Development Notes

Please remember that when implementing this project you may be using elements of it in subsequent assignments or in other classes in your career.  In particular, you could be using the foundations for parity generation and checking using this scheme in a distributed fashion!

# Good Luck!!
