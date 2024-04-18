/*
 * File name: SorterTester.java
 * Purpose  : demonstrates bubble sort and odd/even sort
 * @author  : B.J. Johnson
 * @date    : 2018-11-02
 * @version : 1.0.0
 * to run this program: C>java SorterTester
 *
 */

class SorterTester {

   public static void main( String[] args ) {

      int maxSizeB = 10;
      int maxSizeO = 20;
      int maxSizeD =  7;
      BubbleSorter arrayToSort = new BubbleSorter( maxSizeB) ;
      OddEvenSorter otherArray = new OddEvenSorter( maxSizeO );
      OddEvenSorter demoArray  = new OddEvenSorter( maxSizeD );
      OddEvenSorter demoArray2 = new OddEvenSorter( maxSizeD + 1 );

     /*
      *  Insert ten items of somewhat random order into
      *    arrayToSort and display the array
      */
      System.out.println( "\n\nCreating an array for BubbleSorter with 10 elements:\n" +
                          "   inserted 77,99,44,55,22,88,11,00,66, & 33" );
      arrayToSort.insert( 77 );
      arrayToSort.insert( 99 );
      arrayToSort.insert( 44 );
      arrayToSort.insert( 55 );
      arrayToSort.insert( 22 );
      arrayToSort.insert( 88 );
      arrayToSort.insert( 11 );
      arrayToSort.insert( 00 );
      arrayToSort.insert( 66 );
      arrayToSort.insert( 33 );
      System.out.print( "   Array contents are: " );
      arrayToSort.display();

     /*
      *  Insert nine items of somewhat random order into
      *    otherArray and display the array
      */
      System.out.println( "\n\nCreating an array for OddEvenSorter with 20 elements:\n" +
                          "   inserted 484, 181, 383, 111, 787, 222, 585, 282, 333, 121212, 444, 686, 555, 666, 989, 777, 888, 111111, 999, 101010" );
      otherArray.insert( 484 );
      otherArray.insert( 181 );
      otherArray.insert( 383 );
      otherArray.insert( 111 );
      otherArray.insert( 787 );
      otherArray.insert( 222 );
      otherArray.insert( 585 );
      otherArray.insert( 282 );
      otherArray.insert( 333 );
      otherArray.insert( 121212 );
      otherArray.insert( 444 );
      otherArray.insert( 686 );
      otherArray.insert( 555 );
      otherArray.insert( 666 );
      otherArray.insert( 989 );
      otherArray.insert( 777 );
      otherArray.insert( 888 );
      otherArray.insert( 111111 );
      otherArray.insert( 999 );
      otherArray.insert( 101010 );
      System.out.print( "   Array contents are: " );
      otherArray.display();

     /*
      *  Insert sevem items of somewhat random order into
      *    demoArray and display the array
      */
      System.out.println( "\n\nCreating an array for OddEvenSorter with 7 elements:\n" +
                          "   inserted 5, 2, 7, 3, 9, 8, and 6" );
      demoArray.insert( 5 );
      demoArray.insert( 2 );
      demoArray.insert( 7 );
      demoArray.insert( 3 );
      demoArray.insert( 9 );
      demoArray.insert( 8 );
      demoArray.insert( 6 );
      System.out.print( "   Array contents are: " );
      demoArray.display();

     /*
      *  Insert sevem items of somewhat random order into
      *    demoArray and display the array
      */
      System.out.println( "\n\nCreating an array for OddEvenSorter with 8 elements:\n" +
                          "   inserted 5, 2, 7, 3, 9, 8, 6, and 4" );
      demoArray2.insert( 5 );
      demoArray2.insert( 2 );
      demoArray2.insert( 7 );
      demoArray2.insert( 3 );
      demoArray2.insert( 9 );
      demoArray2.insert( 8 );
      demoArray2.insert( 6 );
      demoArray2.insert( 4 );
      System.out.print( "   Array contents are: " );
      demoArray2.display();

     /*
      *  Perform a bubble sort on arrayToSort and display the result
      */
      System.out.println( "\n\n   Bubble sorting the bubblesorter array..." );
      arrayToSort.bubbleSort();
      System.out.print( "   Array contents are: " );
      arrayToSort.display();

     /*
      *  Perform an odd-even sort on otherArray and display the result
      */
      System.out.println( "\n\n   Odd/Even sorting the oddevensorter 'otherArray'..." );
      otherArray.oddEvenSort();
      System.out.print( "   Array contents are: " );
      otherArray.display();

     /*
      *  Perform an odd-even sort on demoArray and display the result
      */
      System.out.println( "\n\n   Odd/Even sorting the oddevensorter 'demoArray'..." );
      demoArray.oddEvenSort();
      System.out.print( "   Array contents are: " );
      demoArray.display();

     /*
      *  Perform an odd-even sort on demoArray and display the result
      */
      System.out.println( "\n\n   Odd/Even sorting the oddevensorter demoArray2..." );
      demoArray2.oddEvenSort();
      System.out.print( "   Array contents are: " );
      demoArray2.display();
   }
}

