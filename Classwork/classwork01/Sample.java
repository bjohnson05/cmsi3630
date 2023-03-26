/**
 * A simple Java Class file example
 * @author Professor Johnson
 * @version 1.0.0
 */
public class Sample {
   private String myString = "This is a string in the Java Language.";
   private int primeNumber = 23;          // 'primitive' data type, an 'integer'
   public  double myAmount = 234.56;      // 'primitive' data type, a double-precision number

  /**
   * Constructor
   * @param value String to set in the myString field
   */
   public Sample( String value) {
      myString = new String( value );
   }

  /**
   * Method to reset the "myAmount" field value
   * @param newAmount double precision value to set the field to
   * @return the integer value that is the reset amount
   */
   public double resetAmount( double newAmount ) {
      myAmount = newAmount;
      return myAmount;
   }
  /**
   * Method to determine if a number is prime
   * @param value an integer which is potentially a prime number
   * @return boolean value, true if the value passed is prime, false if not
   */
   public boolean isPrime( int value ) {
      boolean result = false;
      // some code that determines prime-ity
      return result;
   }
}
