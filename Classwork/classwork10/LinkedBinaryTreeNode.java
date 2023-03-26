/**
 * An implementation of the BinaryTreeNode interface in which each node stores
 * direct links to its left child, its right child, and its parent.
 *
 * <p>
 * LinkedBinaryTreeNode objects are pretty mean: if one tries to mix them up
 * with different kinds of binary tree nodes, and exception may be thrown.
 * </p>
 */
public class LinkedBinaryTreeNode<E> implements BinaryTreeNode<E> {
    protected E data;
    protected LinkedBinaryTreeNode<E> parent;
    protected LinkedBinaryTreeNode<E> left;
    protected LinkedBinaryTreeNode<E> right;

    /**
     * Constructs a node as the root of its own one-element tree. This is the only
     * public constructor. The only trees that clients can make directly are simple
     * one-element trees.
     */
    public LinkedBinaryTreeNode(E data) {
        this.data = data;
    }

    /**
     * Returns the data stored in this node.
     */
    public E getData() {
        return data;
    }

    /**
     * Modifies the data stored in this node.
     */
    public void setData(E data) {
        this.data = data;
    }

    /**
     * Returns the parent of this node, or null if this node is a root.
     */
    public BinaryTreeNode<E> getParent() {
        return parent;
    }

    /**
     * Returns the left child of this node, or null if it does not have one.
     */
    public BinaryTreeNode<E> getLeft() {
        return left;
    }

    /**
     * Removes child from its current parent and inserts it as the left child of
     * this node. If this node already has a left child it is removed.
     *
     * @exception IllegalArgumentException if the child is an ancestor of this node,
     *                                     since that would make a cycle in the
     *                                     tree.
     */
    public void setLeft(BinaryTreeNode<E> child) {
        // Ensure the child is not an ancestor.
        for (LinkedBinaryTreeNode<E> n = this; n != null; n = n.parent) {
            if (n == child) {
                throw new IllegalArgumentException();
            }
        }

        // Ensure that the child is an instance of LinkedBinaryTreeNode.
        LinkedBinaryTreeNode<E> childNode = (LinkedBinaryTreeNode<E>) child;

        // Break old links, then reconnect properly.
        if (this.left != null) {
            left.parent = null;
        }
        if (childNode != null) {
            childNode.removeFromParent();
            childNode.parent = this;
        }
        this.left = childNode;
    }

    /**
     * Returns the right child of this node, or null if it does not have one.
     */
    public BinaryTreeNode<E> getRight() {
        return right;
    }

    /**
     * Removes child from its current parent and inserts it as the right child of
     * this node. If this node already has a right child it is removed.
     *
     * @exception IllegalArgumentException if the child is an ancestor of this node,
     *                                     since that would make a cycle in the
     *                                     tree.
     */
    public void setRight(BinaryTreeNode<E> child) {
        // Ensure the child is not an ancestor.
        for (LinkedBinaryTreeNode<E> n = this; n != null; n = n.parent) {
            if (n == child) {
                throw new IllegalArgumentException();
            }
        }

        // Ensure that the child is an instance of LinkedBinaryTreeNode.
        LinkedBinaryTreeNode<E> childNode = (LinkedBinaryTreeNode<E>) child;

        // Break old links, then reconnect properly.
        if (right != null) {
            right.parent = null;
        }
        if (childNode != null) {
            childNode.removeFromParent();
            childNode.parent = this;
        }
        this.right = childNode;
    }

    /**
     * Removes this node, and all its descendants, from whatever tree it is in. Does
     * nothing if this node is a root.
     */
    public void removeFromParent() {
        if (parent != null) {
            if (parent.left == this) {
                parent.left = null;
            } else if (parent.right == this) {
                parent.right = null;
            }
            this.parent = null;
        }
    }

    /**
     * Visits the nodes in this tree in preorder.
     */
    public void traversePreorder(BinaryTreeNode.Visitor visitor) {
        visitor.visit(this);
        if (left != null)
            left.traversePreorder(visitor);
        if (right != null)
            right.traversePreorder(visitor);
    }

    /**
     * Visits the nodes in this tree in postorder.
     */
    public void traversePostorder(Visitor visitor) {
        if (left != null)
            left.traversePostorder(visitor);
        if (right != null)
            right.traversePostorder(visitor);
        visitor.visit(this);
    }

    /**
     * Visits the nodes in this tree in inorder.
     */
    public void traverseInorder(Visitor visitor) {
        if (left != null)
            left.traverseInorder(visitor);
        visitor.visit(this);
        if (right != null)
            right.traverseInorder(visitor);
    }
}
