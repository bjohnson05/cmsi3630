/** ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 *  filename: HuffmanNode.java
 *  purpose: implement a node for the Huffman coding problem
 *  @uathor  Dr. Johnson
 *  @date    2020-11-09
 *  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ */

/**
 * HuffmanNode class of the HuffmanCode program
 */
public class HuffmanNode implements Comparable<HuffmanNode> {

  //global parameters for Node class
   private final char letter;
   private final int frequency;
   private HuffmanNode left;
   private HuffmanNode right;

  /**
   * separates the data for node respectively for decoding
   * @param c  is the character
   * @param f  frequency of the character
   * @param l  whether left child
   * @param r  whether right chold
   */
   public HuffmanNode( char c, int f, HuffmanNode l, HuffmanNode r ) {
      letter = c;
      frequency = f;
      left = l;
      right = r;
   }

  /**
   * gets the letter value of this HuffmanNode
   * @return char value of the letter for this HuffmanNode
   */
   public char getLetter() {
      return letter;
   }

  /**
   * gets the frequency value of this HuffmanNode
   * @return int value of the frequency count for letter of this HuffmanNode
   */
   public int getFrequency() {
      return frequency;
   }

  /**
   * gets the letter value of this HuffmanNode
   */
   public void setLeft( HuffmanNode n ) {
      this.left = n;
   }

  /**
   * gets the frequency value of this HuffmanNode
   */
   public void setRight( HuffmanNode n ) {
      this.right = n;
   }

  /**
   * gets the letter value of this HuffmanNode
   * @return HuffmanNode which is the left child of this node
   */
   public HuffmanNode getLeft() {
      return left;
   }

  /**
   * gets the frequency value of this HuffmanNode
   * @return HuffmanNode which is the right child of this node
   */
   public HuffmanNode getRight() {
      return right;
   }

  /**
   * Checks to see if the children are empty
   * @return boolean whether the children are empty
   */
   public boolean isLeaf() {
      return left == null && right == null;
   }

  /**
   * returns a String representation of this HuffmanNode
   * @return boolean whether the children are empty
   */
   public String toString() {
      return "[" + letter + "|" + frequency + "]";
   }

  /**
   * Override is needed for the comparison of these complicated variables
   * @param other HuffmanNode entity to compare to this HuffmanNode
   */
   @Override
   public int compareTo( HuffmanNode other) {
      if( !(this.frequency == other.frequency) ) {
         return this.frequency - other.frequency;
      } else {
         return this.letter - other.letter;
      }
   }

}

