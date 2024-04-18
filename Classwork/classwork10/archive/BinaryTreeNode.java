/**
 * A simple interface for binary trees. An empty binary tree is represented with
 * the value null; a non-empty tree by its root node.
 */
public interface BinaryTreeNode<E> {

    /**
     * Returns the data stored in this node.
     */
    E getData();

    /**
     * Modifies the data stored in this node.
     */
    void setData(E data);

    /**
     * Returns the parent of this node, or null if this node is a root.
     */
    BinaryTreeNode<E> getParent();

    /**
     * Returns the left child of this node, or null if it does not have one.
     */
    BinaryTreeNode<E> getLeft();

    /**
     * Removes child from its current parent and inserts it as the left child of
     * this node. If this node already has a left child it is removed.
     *
     * @exception IllegalArgumentException if the child is an ancestor of this node,
     *                                     since that would make a cycle in the
     *                                     tree.
     */
    void setLeft(BinaryTreeNode<E> child);

    /**
     * Returns the right child of this node, or null if it does not have one.
     */
    BinaryTreeNode<E> getRight();

    /**
     * Removes child from its current parent and inserts it as the right child of
     * this node. If this node already has a right child it is removed.
     *
     * @exception IllegalArgumentException if the child is an ancestor of this node,
     *                                     since that would make a cycle in the
     *                                     tree.
     */
    void setRight(BinaryTreeNode<E> child);

    /**
     * Removes this node, and all its descendants, from whatever tree it is in. Does
     * nothing if this node is a root.
     */
    void removeFromParent();

    /**
     * Visits the nodes in this tree in preorder.
     */
    void traversePreorder(Visitor visitor);

    /**
     * Visits the nodes in this tree in postorder.
     */
    void traversePostorder(Visitor visitor);

    /**
     * Visits the nodes in this tree in inorder.
     */
    void traverseInorder(Visitor visitor);

    /**
     * Simple visitor interface.
     */
    public interface Visitor {
        <E> void visit(BinaryTreeNode<E> node);
    }
}
