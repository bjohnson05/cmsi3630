import java.awt.Color;
import java.util.Comparator;

/**
 * A simple red-black tree class.
 */
@SuppressWarnings("unchecked")
public class RedBlackTree extends BinarySearchTree {

    /**
     * Constructs an empty RedBlackTree that can only accept Comparables as items.
     */
    public RedBlackTree() {
        this(null);
    }

    /**
     * Constructs an empty RedBlackTree that orders its items according to the given
     * comparator.
     */
    public RedBlackTree(Comparator c) {
        super(c);
    }

    /**
     * The nodes in a red-black tree store a color together with the actual data in
     * the node.
     */
    class Node extends LinkedBinaryTreeNode {
        Color color = Color.black;

        public Node(Object data) {
            super(data);
        }
    }

    /**
     * Adds a single data item to the tree. If there is already an item in the tree
     * that compares equal to the item being inserted, it is "overwritten" by the
     * new item. Overrides BinarySearchTree.add because the tree needs to be
     * adjusted after insertion.
     */
    public void add(Object data) {
        if (root == null) {
            root = new Node(data);
        }
        BinaryTreeNode n = root;
        while (true) {
            int comparisonResult = compare(data, n.getData());
            if (comparisonResult == 0) {
                n.setData(data);
                return;
            } else if (comparisonResult < 0) {
                if (n.getLeft() == null) {
                    n.setLeft(new Node(data));
                    adjustAfterInsertion((Node) n.getLeft());
                    break;
                }
                n = n.getLeft();
            } else { // comparisonResult > 0
                if (n.getRight() == null) {
                    n.setRight(new Node(data));
                    adjustAfterInsertion((Node) n.getRight());
                    break;
                }
                n = n.getRight();
            }
        }
    }

    /**
     * Removes the node containing the given value. Does nothing if there is no such
     * node.
     */
    public void remove(Object data) {
        Node node = (Node) nodeContaining(data);
        if (node == null) {
            // No such object, do nothing.
            return;
        } else if (node.getLeft() != null && node.getRight() != null) {
            // Node has two children, Copy predecessor data in.
            BinaryTreeNode predecessor = predecessor(node);
            node.setData(predecessor.getData());
            node = (Node) predecessor;
        }
        // At this point node has zero or one child
        Node pullUp = leftOf(node) == null ? rightOf(node) : leftOf(node);
        if (pullUp != null) {
            // Splice out node, and adjust if pullUp is a double black.
            if (node == root) {
                setRoot(pullUp);
            } else if (node.getParent().getLeft() == node) {
                node.getParent().setLeft(pullUp);
            } else {
                node.getParent().setRight(pullUp);
            }
            if (isBlack(node)) {
                adjustAfterRemoval(pullUp);
            }
        } else if (node == root) {
            // Nothing to pull up when deleting a root means we emptied the tree
            setRoot(null);
        } else {
            // The node being deleted acts as a double black sentinel
            if (isBlack(node)) {
                adjustAfterRemoval(node);
            }
            node.removeFromParent();
        }
    }

    /**
     * Classic algorithm for fixing up a tree after inserting a node.
     */
    private void adjustAfterInsertion(Node n) {
        // Step 1: color the node red
        setColor(n, Color.red);

        // Step 2: Correct double red problems, if they exist
        if (n != null && n != root && isRed(parentOf(n))) {

            // Step 2a (simplest): Recolor, and move up to see if more work
            // needed
            if (isRed(siblingOf(parentOf(n)))) {
                setColor(parentOf(n), Color.black);
                setColor(siblingOf(parentOf(n)), Color.black);
                setColor(grandparentOf(n), Color.red);
                adjustAfterInsertion(grandparentOf(n));
            }

            // Step 2b: Restructure for a parent who is the left child of the
            // grandparent. This will require a single right rotation if n is
            // also
            // a left child, or a left-right rotation otherwise.
            else if (parentOf(n) == leftOf(grandparentOf(n))) {
                if (n == rightOf(parentOf(n))) {
                    rotateLeft(n = parentOf(n));
                }
                setColor(parentOf(n), Color.black);
                setColor(grandparentOf(n), Color.red);
                rotateRight(grandparentOf(n));
            }

            // Step 2c: Restructure for a parent who is the right child of the
            // grandparent. This will require a single left rotation if n is
            // also
            // a right child, or a right-left rotation otherwise.
            else if (parentOf(n) == rightOf(grandparentOf(n))) {
                if (n == leftOf(parentOf(n))) {
                    rotateRight(n = parentOf(n));
                }
                setColor(parentOf(n), Color.black);
                setColor(grandparentOf(n), Color.red);
                rotateLeft(grandparentOf(n));
            }
        }

        // Step 3: Color the root black
        setColor((Node) root, Color.black);
    }

    /**
     * Classic algorithm for fixing up a tree after removing a node; the parameter
     * to this method is the node that was pulled up to where the removed node was.
     */
    private void adjustAfterRemoval(Node n) {
        while (n != root && isBlack(n)) {
            if (n == leftOf(parentOf(n))) {
                // Pulled up node is a left child
                Node sibling = rightOf(parentOf(n));
                if (isRed(sibling)) {
                    setColor(sibling, Color.black);
                    setColor(parentOf(n), Color.red);
                    rotateLeft(parentOf(n));
                    sibling = rightOf(parentOf(n));
                }
                if (isBlack(leftOf(sibling)) && isBlack(rightOf(sibling))) {
                    setColor(sibling, Color.red);
                    n = parentOf(n);
                } else {
                    if (isBlack(rightOf(sibling))) {
                        setColor(leftOf(sibling), Color.black);
                        setColor(sibling, Color.red);
                        rotateRight(sibling);
                        sibling = rightOf(parentOf(n));
                    }
                    setColor(sibling, colorOf(parentOf(n)));
                    setColor(parentOf(n), Color.black);
                    setColor(rightOf(sibling), Color.black);
                    rotateLeft(parentOf(n));
                    n = (Node) root;
                }
            } else {
                // pulled up node is a right child
                Node sibling = leftOf(parentOf(n));
                if (isRed(sibling)) {
                    setColor(sibling, Color.black);
                    setColor(parentOf(n), Color.red);
                    rotateRight(parentOf(n));
                    sibling = leftOf(parentOf(n));
                }
                if (isBlack(leftOf(sibling)) && isBlack(rightOf(sibling))) {
                    setColor(sibling, Color.red);
                    n = parentOf(n);
                } else {
                    if (isBlack(leftOf(sibling))) {
                        setColor(rightOf(sibling), Color.black);
                        setColor(sibling, Color.red);
                        rotateLeft(sibling);
                        sibling = leftOf(parentOf(n));
                    }
                    setColor(sibling, colorOf(parentOf(n)));
                    setColor(parentOf(n), Color.black);
                    setColor(leftOf(sibling), Color.black);
                    rotateRight(parentOf(n));
                    n = (Node) root;
                }
            }
        }
        setColor(n, Color.black);
    }

    // The following helpers dramatically simplify the code by getting
    // all the null pointer checking out of the adjustment methods.

    private Color colorOf(Node n) {
        return n == null ? Color.black : n.color;
    }

    private boolean isRed(Node n) {
        return n != null && colorOf(n) == Color.red;
    }

    private boolean isBlack(Node n) {
        return n == null || colorOf(n) == Color.black;
    }

    private void setColor(Node n, Color c) {
        if (n != null)
            n.color = c;
    }

    private Node parentOf(Node n) {
        return n == null ? null : (Node) n.getParent();
    }

    private Node grandparentOf(Node n) {
        return (n == null || n.getParent() == null) ? null : (Node) n.getParent().getParent();
    }

    private Node siblingOf(Node n) {
        return (n == null || n.getParent() == null) ? null
                : (n == n.getParent().getLeft()) ? (Node) n.getParent().getRight() : (Node) n.getParent().getLeft();
    }

    private Node leftOf(Node n) {
        return n == null ? null : (Node) n.getLeft();
    }

    private Node rightOf(Node n) {
        return n == null ? null : (Node) n.getRight();
    }
}
