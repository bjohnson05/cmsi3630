# Mini-Hackathon Number 2 &ndash; Enigma Machine
## Learning Outcomes and Project Description

The purpose of this assignment is to broaden your understanding of data structures by implementing a working simulation of the Enigma Machine, which is an encryption device developed and used in the early- to mid-20th century to protect commercial, diplomatic and military communication.  It was employed extensively by Nazi Germany during World War II, in all branches of the German military.  This is the famous machine that Alan Turing, the "Father of Computer Science", made his reputation with by solving the encryption method and decoding the messages.

Enigma has an electromechanical rotor mechanism that scrambles the 26 letters of the alphabet.  In typical use, one person enters text on the Enigmaï¿½s keyboard and another person writes down which of 26 lights above the keyboard lights up at each key press.  If plain text is entered, the lit-up letters are the encoded ciphertext.  Entering ciphertext transforms it back into readable plaintext.  The rotor mechanism changes the electrical connections between the keys and the lights with each keypress.  The security of the system depends on Enigma machine settings that were changed daily, based on secret key lists distributed in advance, and on other settings that change for each message.  The receiving station has to know and use the exact settings employed by the transmitting station to successfully decrypt a message.

As used in practice, the Enigma encryption proved vulnerable to cryptanalytic attacks by Germany's adversaries, at first Polish and French intelligence and, later, a massive effort mounted by the United Kingdom at Bletchley Park.  While Germany introduced a series of improvements to Enigma, and these hampered decryption efforts to varying degrees, they did not ultimately prevent Britain and its allies from exploiting Enigma-encoded messages as a major source of intelligence during the war.  Many commentators say this flow of communications intelligence shortened the war significantly and may even have altered its outcome.

# Specification

In this assignment you will implement a program <code>*EnigmaSim*</code> in Java which will accept as its input the name of a file containing a message to be encoded.  Your program will read the file [possibly containing multiple lines], encode the message and output the encoded message to the display.  Your program will then take that encoded message and pass it back through the enigma encoding to DECODE the message back to its original content [called "clear text"] and output the de-encoded message on the display.

The enigma used a simple offset substitution that mapped characters to the alphabet by number.  "A" was number 1 and "Z" was number 26, and the values "wrapped around".  An offset was provided to change the letters.  For example the message "HELLO" would be letters "8-5-12-12-15", and with an offset of "3" [for example] applied it would be "11-8-15-15-18" which would become the word "KHOOR".

An added layer of complexity came from the fact that the machine had multiple encoding wheels in each device, anywhere from three to five wheels, or "rotors" as they were called.  Further, there was a "plugboard" that could be used to additionally scramble things before the letters went to the rotors for offsetting.

## Input File Specification

For this assignment you may assume that the input file contains a text message that is formatted as ASCII text.  There may be multiple lines in the file, so you will need to read all of the lines to get the entire message.  You may put the single string "EOF" at the end of the text, on its own line, if desired, to allow an indication that it's the end of the message.  This situation will allow you to include comment lines after that which will be ignored.  You can also come up with your own scheme to interpret which lines are data.

## Program Focus

The idea of this program is for you to implement, using the "*Alphabetical offset*" method, an encoder which is based on the Enigma Machine.  Your machine must have at least three rotors; the number of rotors will be the first argument on the command line.  The second command line argument will be the offset to use.  Remember that the offset will "wrap around" the alphabet so that if the letter's numeric value plus the offset is greater than 26, it will start counting at 1 again.  For example, if the offset is 5, the letter "Y" would be encoded as "D".

## Usage

The program <code>EnigmaSim</code> is intended to be run via the following command-line invocation:
<pre>
     $ java EnigmaSim <rotors> <offset> messagefile.txt
</pre>

If no input file is specified or if the input file is not found, an appropriate error message must be displayed. For example:
<pre>
     $ java EnigmaSim  3  17
     
        EnigmaSim: no input file was specified!
           Please try again
           
     $ java EnigmaSim   3  17  bogusfile.txt
     
        EnigmaSim: input file 'bogusfile.txt' does not exist or cannot be opened.
           Please try again
           
</pre>

*If a valid file is specified as input*, then for every sentence in the file you must output its encrypted verson.  All sentences in the file must be processed and output to the display.  Following that, all encrypted sentences must be decrypted and the original file message must be output to the display.

# Compilation Notes

Your program must compile from the command line or terminal using the following invocation:
<pre>
   $ javac *.java
</pre>

Do not submit any IDE specific files and in the interest of simplicity do not use packages for this assignment.  If your program does not compile using the command mentioned above you will receive no credit.

# Additional Development Notes

Please remember that when implementing this project you may be using elements of it in subsequent assignments or in other classes in your career.  In particular, you could be using the foundations for encryption/decryption using this scheme in a distributed fashion!

# Good Luck!!
