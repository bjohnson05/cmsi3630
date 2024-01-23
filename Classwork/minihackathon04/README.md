# Mini-Hackathon Number 4 &ndash; MasterMind Logic Game
## Learning Outcomes and Project Description

The purpose of this assignment is to broaden your understanding of data structures and algorithms by using them to create the game _MASTERMIND_, which is a logic puzzle game usually played with two players.  In this game, one player sets up a hidden 'code' using four out of six different colored pegs.  The other player then has 12 chances to guess the proper order and color of the hidden pegs.

In this assignment you will implement a program in python to play the _MASTERMIND_ game.  The computer will pick four of the six colors using the first letters of the color, either Red, Blue, Green, Yellow, Cyan, or White ['R', 'B', 'G', 'Y', 'C', 'W'].  The human player will then have 12 chances to guess the pattern.

In the real game, one player is the *code-maker* and the other is the *code-breaker*.  The board has 13 rows of holes for the colored pegs.  One row is used for the 'code' pegs.  There are also 12 rows of smaller holes for 'feedback' pegs, each of which aligns with a row of the larger 'guess' holes.  To start the game, the *code-maker* inserts four colored pegs into one end of the pegboard [the 13th row], then covers them with a shield so the *code-breaker* can't see them.  The *code-breaker* then has 12 chances to guess the proper color and order of the hidden pegs.  With each guess, the *code-maker* provides feedback using black and white pegs that fit into the smaller 'feedback' holes next to each row that the *code-breaker* has used for a guess.  A black feedback peg indicates a correct color peg in the correct position.  A white feedback peg indicates a correct color peg in an INCORRECT position.

## Specification

In this assignment you will implement the program <code>mastermind</code> in python in which the computer will play the game as the *code-maker*.  The human player will play as the *code-breaker*.  The computer will randomly pick four colors that the human player must guess.  To make it easier for the human, no duplicate colors are allowed, and no blank spaces are allowed either.  By turns, the computer will prompt the human for a guess, then will evaluate the guess and provide feedback using a lower-case "o" for a white peg and an upper-case "O" for a black peg.  The game proceeds until either the human guesses the correct pattern or all 12 guesses have elapsed.

## Program Focus

The idea of this program is for you to implement, using whatever data structure you feel is applicable, the _MASTERMIND_ game.  The program will take turns with the human player, prompting for every turn with the word "guess: ", to which the human player will enter four space-separated letters indicateing the peg colors.  The computer will then respond with the appropriate feedback pegs and will prompt the human for the next guess.  If the human guesses correctly, the computer will congratulate the human as the winner.  If all 12 guesses elapse without a correct solution, the computer will make an appropriate statement that the human has lost the game.

## Usage

The program <code>mastermind</code> is intended to be run via the following command-line invocation:
<pre>
     $ python mastermind
</pre>

## Historical Note

The computer scientist and mathemagician Donald Knuth was able to determine in 1977 that the codebreaker can solve the pattern in five moves or fewer using an algorithm tnat progressively reduces the number of possible patterns.  In this case, Knuth used a total of 6<sup>4</sup> = 1296 possible patterns with duplicate colors allowed.

# Compilation Notes

Your program must run from the command line or terminal using the syntax given above.

Do not submit any IDE specific files and in the interest of simplicity do not use packages for this assignment.  If your program does not run using the command mentioned above you will receive no credit.

# Additional Development Notes

Please remember that when implementing this project you may be using elements of it in subsequent assignments or in other classes in your career.  In particular, you could be using the foundations for parity generation and checking using this scheme in a distributed fashion!

# Good Luck!!

