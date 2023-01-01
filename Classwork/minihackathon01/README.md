# Mini-Hackathon Number 1 &ndash; Towers of Hanoi Game
## Learning Outcomes and Project Description

The purpose of this assignment is to broaden your understanding of data structures by implementing the game called *TOWERS OF HANOI*.  In this game you are give a stack of disks of increasing diameters that are stacked up in order with the smallest-diameter disk on the top of the stack.  The disks have a hole in the middle so that they can be stacked up on a post.  You are provided with three posts on which to stack these disks.  All the disks start out in a single stack on a single post.  The game is to move the entire stack from one post to another based on the following rules:

1. you can only move one disk at a time
1. you can never put a disk with larger diameter on a disk with smaller diameter
1. the game is over when all the disks are again properly stacked according to size on a different post than the one on which they started

## Specification
You will write a program, <code>*TowersOfHanoi*</code>, which will allow a user to play the game.  Your program will require one command line argument, which is the number of disks to be used with the game.  Obviously, the trivial cases of one or two disks are good for testing, but are not really great as actual game instances.  The minimum that should be used for playing actual games is three disks.  There is no upper limit to disk count.

Disks are numbered from one to <code>N</code> with <code>N</code> representing the largest disk.  For example, if you have three disks, they would be numbered from one to three, one being the smallest-diameter disk.

Posts are lettered with "A", "B", and "C".  The starting post is "A", which is where all the disks begin.

If there is no argument supplied when starting the program, or if there is an error in the disk count value [such as a letter instead of a number] your program must output a message that indicates the error condition.

# Usage

The user must be prompted for the number of the disk to move, followed by a prompt for the letter of the post to move the disk to.  For example:

<pre>
   enter the disk to move:  1
   enter the post to move to: B
</pre>

After every move entry, the game state must be updated, and then the program must output the current state.  As an example, from the start of the game, showing the first move:

<pre>
   post 0:  [1][2][3]
   post 1:  [empty]
   post 2:  [empty]
   after show in constructor: posts[0].peek() is: 1

  Enter the disk to be moved, 1 through 3 =>> 1
  Enter the post to move the disk onto, A, B, or C =>> B
   post 0:  [2][3]
   post 1:  [1]
   post 2:  [empty]
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
