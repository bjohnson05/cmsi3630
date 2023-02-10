/**
 * File: IntListInterface.java
 * Purpose: Demonstrate the idea of an "interface" in Java
 */
   public interface IntListInterface {

      boolean append( int valueToAdd );
      boolean insertValueAtIndex( int value, int index );
      int getValueAtIndex( int index );
      int removeValueAtIndex( int index );

   }
