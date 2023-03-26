import java.awt.Color;
import java.awt.FontMetrics;
import java.awt.Graphics;
import java.awt.Point;
import java.awt.Rectangle;
import java.lang.reflect.Field;
import java.util.HashMap;
import java.util.Map;

import javax.swing.JPanel;

/**
 * A panel that maintains a picture of a binary tree.
 */
public class BinaryTreePanel extends JPanel {
    private BinaryTreeNode<?> tree;
    private int gridwidth;
    private int gridheight;

    /**
     * Stores the pixel values for each node in the tree.
     */
    private Map<BinaryTreeNode<?>, Point> coordinates = new HashMap<BinaryTreeNode<?>, Point>();

    /**
     * Constructs a panel, saving the tree and drawing parameters.
     */
    public BinaryTreePanel(BinaryTreeNode<?> tree, int gridwidth, int gridheight) {
        this.tree = tree;
        this.gridwidth = gridwidth;
        this.gridheight = gridheight;
    }

    /**
     * Changes the tree rendered by this panel.
     */
    public void setTree(BinaryTreeNode<?> root) {
        tree = root;
        repaint();
    }

    /**
     * Draws the tree in the panel. First it computes the coordinates of all the
     * nodes with an inorder traversal, then draws them with a postorder traversal.
     */
    public void paintComponent(final Graphics g) {
        super.paintComponent(g);

        if (tree == null) {
            return;
        }

        tree.traverseInorder(new BinaryTreeNode.Visitor() {
            private int x = gridwidth;

            public void visit(BinaryTreeNode node) {
                coordinates.put(node, new Point(x, gridheight * (depth(node) + 1)));
                x += gridwidth;
            }
        });

        tree.traversePostorder(new BinaryTreeNode.Visitor() {
            public void visit(BinaryTreeNode node) {
                String data = node.getData().toString();
                Point center = (Point) coordinates.get(node);
                if (node.getParent() != null) {
                    Point parentPoint = (Point) coordinates.get(node.getParent());
                    g.setColor(Color.black);
                    g.drawLine(center.x, center.y, parentPoint.x, parentPoint.y);
                }
                FontMetrics fm = g.getFontMetrics();
                Rectangle r = fm.getStringBounds(data, g).getBounds();
                r.setLocation(center.x - r.width / 2, center.y - r.height / 2);
                Color color = getNodeColor(node);
                Color textColor = (color.getRed() + color.getBlue() + color.getGreen() < 382) ? Color.white
                        : Color.black;
                g.setColor(color);
                g.fillRect(r.x - 2, r.y - 2, r.width + 4, r.height + 4);
                g.setColor(textColor);
                g.drawString(data, r.x, r.y + r.height);
            }
        });
    }

    /**
     * Returns a color for the node. If the node is of a class with a field called
     * "color", and that field currently contains a non-null value, then that value
     * is returned. Otherwise a default color of yellow is returned.
     */
    Color getNodeColor(BinaryTreeNode<?> node) {
        try {
            Field field = node.getClass().getDeclaredField("color");
            return (Color) field.get(node);
        } catch (Exception e) {
            return Color.yellow;
        }
    }

    private int depth(BinaryTreeNode<?> node) {
        return (node.getParent() == null) ? 0 : 1 + depth(node.getParent());
    }
}
