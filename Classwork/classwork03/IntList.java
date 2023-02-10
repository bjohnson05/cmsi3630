/*
 *  File:  IntList.java
 *  Purpose:  implements an integer sequential list
 *  @author:  B.J. Johnson
 *  date:  2018-09-14
 *  @version:  1.0.0
 */
   public class IntList implements IntListInterface {
      private int[] theList;
      private int   size;

      private static final int STARTING_SIZE = 19;    // defines starting size; don't worry, we'll deal

      public IntList() {
         theList = new int[STARTING_SIZE];
         size = 0;
      }

     // check the index value for validity and throw an exception if it's bad
      public void checkIndex( int index ) throws ArrayIndexOutOfBoundsException {
         if( index > theList.length ) {
            throw new ArrayIndexOutOfBoundsException( "The index value is too large" );
         } else if( index < 0 ) {
            throw new ArrayIndexOutOfBoundsException( "The index value is too small");
         }
      }

     // get the value in the list at the index that's passed in
     //  checks error conditions
      public int getValueAtIndex( int index ) throws ArrayIndexOutOfBoundsException {
         if( size == 0 ) {
            throw new ArrayIndexOutOfBoundsException( "The list is empty!" );   // maybe not the best...
         } else {
            checkIndex( index );
            return theList[index];
         }
      }

     // add an item to the end of the list
     //  if there's not enough room, add more slots
      public boolean append( int valueToAdd ) {
         if( size < theList.length ) {
            theList[size] = valueToAdd;
            size++;
            return true;
         } else {
            int[] newList = new int[theList.length + STARTING_SIZE];
            for( int i = 0; i < theList.length; i++ ) {
               newList[i] = theList[i];
            }
            newList[theList.length] = valueToAdd;
            size++;
            theList = newList;
            return true;
         }
      }

     // insert a value at an index in the list
     //  if there's not enough room, add more slots
      public boolean insertValueAtIndex( int value, int index ) {
         moveDownFromIndex( index );
         theList[index] = value;
         size++;
         return true;
      }

     // move everything down to make a hole at an index which will
     //  be filled by the "insertValueAtIndex()" method above
      public void moveDownFromIndex( int index ) {
         if( size < theList.length - 1 ) {
            for( int i = theList.length - 2; i >= index; i-- ) {
               theList[i+1] = theList[i];
            }
         } else {
            int[] newList = new int[theList.length + STARTING_SIZE];
            for( int i = 0; i < theList.length; i++ ) {
               newList[i] = theList[i];
            }
            for( int i = theList.length - 1; i > index; i-- ) {
               newList[i+1] = newList[i];
            }
            theList = newList;
         }
      }

     // insert a value at the START of the list
     //  note that everything has to be moved down, so this can
     //  simply be a call to "insertValueAtIndex( 0 )"
      public boolean prepend( int valueToAdd ) {
         return insertValueAtIndex( valueToAdd, 0 );
      }

     // remove a value from the list at the indicated index
     //  if the list is empty, throw an exception
      public int removeValueAtIndex( int index ) throws ArrayIndexOutOfBoundsException {
         int value = -7;            // just some value, pulled out of the atmosphere
         checkIndex( index );
         if( size == 0 ) {
            throw new ArrayIndexOutOfBoundsException( "The list is empty!" );   // maybe not the best...
         } else {
            value = theList[index];
            holeFiller( index );
         }
         theList[size] = 0;
         return value;
      }

     // close up the list, filling in the hole where an item
     //  has been removed
      private void holeFiller( int index ) {
         for( int i = index; i < size + 1; i++ ) {
            theList[i] = theList[i+1];
         }
         size--;
      }

     // find out what the current size of the list is
     //  i.e., how many elements are in it
      public int getSize() { return size; }

     // make a String representation of the list for being able to
     //  check what's in there; handy for debugging as well
      public String toString() {
         String output = "";
         for( int i = 0; i < theList.length; i++ ) {
            output += "[" + theList[i] + "]";
         }
         return output + "\n";

      }

     // main() method to test all the methods in the class
      public static void main( String[] args ) {
         System.out.println( "\n   CHECKING THE 'INTLIST' PROGRAM OPERATION" );
         System.out.println( "   ========================================" );
         IntList list = new IntList();
         list.append(  2 );
         list.append(  3 );
         list.append(  5 );
         list.append(  7 );
         System.out.println( "   List dimension: " + list.theList.length );
         System.out.println( "   List size: " + list.getSize() );
         System.out.println( "   Contents : " + list.toString() );
         System.out.println( "   value at index 3: " + list.getValueAtIndex( 3 ) );   // should return the value 7
         list.append( 11 );
         list.append( 13 );
         list.append( 17 );
         list.append( 19 );
         System.out.println( "   ADDED FOUR MORE VALUES...." );
         System.out.println( "   List dimension: " + list.theList.length );
         System.out.println( "   List size: " + list.getSize() );
         System.out.println( "   Contents : " + list.toString() );
         System.out.println( "   value at index 5: " + list.getValueAtIndex( 5 ) );      // should return the value 19
         System.out.println( "   value removed at index 3: " + list.removeValueAtIndex( 3 ) );   // should return the value 7
         System.out.println( "   List dimension: " + list.theList.length );
         System.out.println( "   List size: " + list.getSize() );
         System.out.println( "   Contents : " + list.toString() );
         System.out.println( "   value at index 3: " + list.getValueAtIndex( 3 ) );      // should return the value 11
         System.out.println( "   List size: " + list.getSize() );
         System.out.println( "   Contents : " + list.toString() );
         list.append( 23 );
         list.append( 29 );
         list.append( 31 );
         list.append( 37 );
         list.append( 41 );
         list.append( 43 );
         list.append( 47 );
         list.append( 53 );
         list.append( 61 );
         list.append( 67 );
         list.append( 71 );
         list.append( 73 );
         System.out.println( "   ADDED TWELVE MORE VALUES...." );
         System.out.println( "      [note that this fits due to removals]" );
         System.out.println( "   List dimension: " + list.theList.length );
         System.out.println( "   List size: " + list.getSize() );
         System.out.println( "   Contents : " + list.toString() );
         list.append( 71 );
         System.out.println( "   LIST IS NOW FULL...." );
         System.out.println( "   ADDED ONE MORE VALUE...." );
         System.out.println( "      [note that list length is automatically increased]" );
         System.out.println( "   List dimension: " + list.theList.length );
         System.out.println( "   List size: " + list.getSize() );
         System.out.println( "   Contents : " + list.toString() );
         System.out.println( "   value removed at index 7: " + list.removeValueAtIndex( 7 ) );   // should return the value 23
         System.out.println( "   List size: " + list.getSize() );
         System.out.println( "   Contents : " + list.toString() );
         list.append( 79 );
         list.append( 83 );
         list.append( 89 );
         list.append( 97 );
         list.append( 101 );
         System.out.println( "   ADDED FIVE MORE VALUES...." );
         System.out.println( "   List size: " + list.getSize() );
         System.out.println( "   Contents : " + list.toString() );
         System.out.println( "   value removed at index 7: " + list.removeValueAtIndex( 7 ) );   // should return the value 29
         System.out.println( "   List size: " + list.getSize() );
         System.out.println( "   Contents : " + list.toString() );
         list.insertValueAtIndex( 103, 11 );
         System.out.println( "   INSERTED VALUE 103 AT INDEX 11" );
         System.out.println( "   List size: " + list.getSize() );
         System.out.println( "   Contents : " + list.toString() );
         list.append( 123 );
         list.append( 129 );
         list.append( 131 );
         list.append( 137 );
         list.append( 141 );
         list.append( 143 );
         list.append( 147 );
         list.append( 151 );
         list.append( 153 );
         list.append( 157 );
         list.append( 161 );
         list.append( 167 );
         list.append( 171 );
         list.append( 173 );
         System.out.println( "   ADDED FOURTEEN MORE VALUES...." );
         System.out.println( "   List dimension: " + list.theList.length );
         System.out.println( "   List size: " + list.getSize() );
         System.out.println( "   Contents : " + list.toString() );
         list.insertValueAtIndex( 201, 17 );
         System.out.println( "   INSERTED VALUE 201 AT INDEX 17" );
         System.out.println( "   List dimension: " + list.theList.length );
         System.out.println( "   List size: " + list.getSize() );
         System.out.println( "   Contents : " + list.toString() );
         list.prepend( 301 );
         System.out.println( "   PREPENDED VALUE 301" );
         System.out.println( "   List dimension: " + list.theList.length );
         System.out.println( "   List size: " + list.getSize() );
         System.out.println( "   Contents : " + list.toString() );
         list.prepend( 302 );
         System.out.println( "   PREPENDED VALUE 302" );
         System.out.println( "   List dimension: " + list.theList.length );
         System.out.println( "   List size: " + list.getSize() );
         System.out.println( "   Contents : " + list.toString() );
         list.prepend( 303 );
         System.out.println( "   PREPENDED VALUE 303" );
         System.out.println( "   List dimension: " + list.theList.length );
         System.out.println( "   List size: " + list.getSize() );
         System.out.println( "   Contents : " + list.toString() );
      }
   }
