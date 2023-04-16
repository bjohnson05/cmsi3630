/*
 * File name: SimonGame.java
 * Purpose  : demonstrates use of a linked list in a game
 * @author  : B.J. Johnson
 * @date    : 2018-11-03
 * @version : 1.0.0
 *
 * Description:  In the game "Simon" a four-colored disk can play a random sequence of
 *  tones and lights. Each color on the disk is actually a button that can be pressed,
 *  with a light behind it. As the game makes a tone, it also flashes the light with that
 *  tone. The game is for the user to press the buttons in the sequence that is played by
 *  the game's controller. The sequence starts with a single light/tone, then increases
 *  the number of lights/tones by adding one new trial to the sequence each time the
 *  player gets the entire order correct. The game is over when the user makes a mistake
 *  in entering the sequence.
 *  Using the letters "R" for Red, "G" for Green, "Y" for Yellow, and "B" for Blue,
 *  implement the game. When the player makes a mistake in the sequence, ask if they
 *  would like to play again. Implement the game as follows:
 *
 *  Be sure that the sequence is random. Make your program display the string each time,
 *  letter by letter, with the letters separated by spaces. Try to make a short delay
 *  before each letter is displayed. Once all the letters in the sequence are displayed
 *  wait one second and then make your program output backspace characters to erase the
 *  displayed string. Then read the user's input and display each character as it is
 *  entered. When the user makes an error output a "mistake" message.
 *
 */

import java.util.Scanner;
import java.util.Random;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.IOException;

class SimonGame {

   private static final int MAX_GAME_COUNT = 100;  // we want zero to 100 inclusive

   private static char[] gameList = new char[MAX_GAME_COUNT];

   private static int move = 1;
   private static boolean correct = true;

  // Fill up the list with random values from "B", "G", "R", and "Y"
  //   for blue, green, red, and yellow
   public SimonGame () {
      char[] charList = {'B', 'G', 'R', 'Y'};
      Random r = new Random();
      for( int i = 0; i < MAX_GAME_COUNT; i++ ) {
         gameList[i] = charList[ r.nextInt( 4 ) ];
      }
      move = 1;
   }

  // helper method to display the complete game list
   public void displayGameList( int end ) {
      for( int i = 0; i < (end + 1); i++ ) {
         System.out.print( "[" + gameList[i] + "]" );
      }
      System.out.println( "" );
   }

  // helper method to check if the user entry is correct; NOTE that
  //  the "move" value is incremented each time the entire sequence is right
   public boolean checkIfCorrect( String response) {
      String currentSequence = "";
      for( int i = 0; i < move; i++ ) {
         currentSequence += gameList[i];
      }
      if( currentSequence.equals(response) ) {
         return true;
      }
      return false;
   }

  // helper method to clear the screen for the next move
   public void clearScreen() {
      try {
         new ProcessBuilder( "cmd", "/c", "cls" ).inheritIO().start().waitFor();
      }
      catch( IOException ioe ) {}
      catch( InterruptedException ie ) {}
      System.out.println( "\n\n\n\n\n\n\n" );
   }

   public static void main( String[] args ) throws InterruptedException, IOException {

     // Get everything set up
      SimonGame      sg = new SimonGame();
      String         entry = "";
      Scanner        myInput = new Scanner( System.in );
      BufferedReader br = new BufferedReader( new InputStreamReader( System.in ) );
      int c = 0;
      // sg.displayGameList( 20 );

      while( move < MAX_GAME_COUNT ) {
         sg.clearScreen();
         for( int i = 0; i < move; i++ ) {
            System.out.print( "[" + gameList[i] + "]" );
            try {
              Thread.sleep( 333 );
            }
            catch(InterruptedException ex) {
              Thread.currentThread().interrupt();
            }
         }
         try {
           Thread.sleep( 1500 );
         }
         catch(InterruptedException ex) {
           Thread.currentThread().interrupt();
         }
         for( int i = 0; i < move; i++ ) {
            System.out.print( "\b\b\b   \b\b\b" );
         }

         System.out.print( "   Enter your guess letter[s] in a string: " );
         entry = myInput.next().toUpperCase();
         try {
           Thread.sleep( 1000 );
         }
         catch(InterruptedException ex) {
           Thread.currentThread().interrupt();
         }
         if( sg.checkIfCorrect( entry ) ) {
           System.out.println( "^MAGot it!!");
         } else {
            System.out.println( "Sorry, SIMON WINS!!" );
            System.out.print( "Do you want to play again? {y/n}: " );
            entry = myInput.next().toUpperCase();
            if( entry.equals( "N" ) ) {
               System.exit( 0 );
            } else {
               move = 0;
            }
         }
         move++;
      }

   }
}

