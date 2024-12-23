# Mini-Hackathon Number 4 &ndash; MasterMind Logic Game
## Learning Outcomes and Project Description

The purpose of this assignment is to broaden your understanding of data structures and algorithms by using them to create the game _MASTERMIND_, which is a logic puzzle game usually played with two players.  One player sets up a hidden 'code' using four out of six different colored pegs.  The other player then has 12 chances to guess the proper order and color of the hidden pegs.  If you have ever played "Wordle", this is the same idea.

[Here](https://mastermindgame.org/) is a similar on-line version of the game using eight guesses and nine colors:

## Specification

In this assignment the computer will play the game as the *code-maker*.  The human player will play as the *code-breaker*.  The computer will randomly pick four of the six colors using the first letters of the color, either Red, Blue, Green, Yellow, Cyan, or White ['R', 'B', 'G', 'Y', 'C', 'W'].  The human player will then have 12 chances to guess the pattern.  The computer will respond to each guess, giving feedback to the human player as to correct color and location of each guess.  To make it easier for the human, no duplicate colors are allowed, and no blank spaces are allowed either.  By turns, the computer will prompt the human for a guess, then will evaluate the guess and provide feedback using an "X" for a correct color in the correct location, and an "O" for a correct color in an incorrect location.  The game proceeds until either the human guesses the correct pattern and wins, or all 12 guesses have elapsed and the computer wins.

The computer must interact with the human player by prompting with the word "Guess: ".  The human player must respond with four colors in a space-delimited list, such as "R B G Y" and then press the 'enter' key.  The computer will then respond with the feedback, either to the side of the guess or underneath it, and will then output the prompt again.  If the human guesses the code correctly within the 12 attempts, the computer will congratulate the human as the winner.  If all 12 guesses elapse without a correct solution, the computer will make an appropriate statement that the human has lost the game.

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

