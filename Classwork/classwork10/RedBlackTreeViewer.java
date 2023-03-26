import java.awt.Color;
import java.awt.Dimension;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextField;
import javax.swing.border.BevelBorder;

/**
 * A little application that lets you interactively manipulate a binary search
 * tree.
 */
public class RedBlackTreeViewer extends JFrame {
    RedBlackTree tree = new RedBlackTree();

    JFrame frame = new JFrame("Red Black Tree Viewer");
    JTextField valueField = new JTextField(40);
    JPanel buttonPanel = new JPanel();
    BinaryTreePanel panel = new BinaryTreePanel(null, 40, 40);
    JScrollPane displayArea = new JScrollPane();
    JLabel messageLine = new JLabel();

    /**
     * An operation encapsulates a button and its action. The constructor will
     * create a button, add it to a button panel, and register itself as a listener
     * for the button. The listener first reads inputs from a textfield, then calls
     * a subclass-supplied method with those inputs, then displays the resulting
     * tree in the display area.
     */
    private abstract class Operation implements ActionListener {
        public Operation(String label) {
            JButton button = new JButton(label);
            buttonPanel.add(button);
            button.addActionListener(this);
        }

        public void actionPerformed(ActionEvent event) {
            String value = valueField.getText();
            messageLine.setText("");
            try {
                execute(value);
            } catch (Exception e) {
                e.printStackTrace();
            }
            // Update the picture and return the focus to the text field. Select
            // all the text in the textfield so it can easily be overwritten.
            panel.setTree(tree.getRoot());
            valueField.requestFocus();
            valueField.selectAll();
        }

        protected abstract void execute(String value);
    }

    /**
     * Constructs a viewer, laying out all the components in a very nice way, and
     * constructs and registers all the operation objects.
     */
    public RedBlackTreeViewer() {
        JPanel valuePanel = new JPanel();
        valuePanel.add(new JLabel("Value: "));
        valuePanel.add(valueField);

        JPanel controlPanel = new JPanel();
        controlPanel.setLayout(new GridLayout(0, 1));
        controlPanel.add(valuePanel);
        controlPanel.add(buttonPanel);

        // NOTE: Hardcoded preferred size! Fix this in the exercises.
        panel.setPreferredSize(new Dimension(2048, 2048));
        panel.setBackground(Color.white);
        panel.setBorder(new BevelBorder(BevelBorder.LOWERED));
        displayArea.setViewportView(panel);

        frame.setBackground(Color.lightGray);
        frame.getContentPane().add(controlPanel, "North");
        frame.getContentPane().add(displayArea, "Center");
        frame.getContentPane().add(messageLine, "South");
        frame.pack();

        new Operation("Add") {
            protected void execute(String value) {
                tree.add(value);
            }
        };
        new Operation("Add All") {
            protected void execute(String value) {
                for (String s : value.split("\\s+"))
                    tree.add(s);
            }
        };
        new Operation("Lookup") {
            protected void execute(String value) {
                messageLine.setText("The value \"" + value + "\" is " + (tree.contains(value) ? "" : "not ") + "found");
            }
        };
        new Operation("Remove") {
            protected void execute(String value) {
                tree.remove(value);
            }
        };
    }

    /**
     * Makes an application whose main window is a RedBlackTreeViewer.
     */
    public static void main(String[] args) {
        RedBlackTreeViewer viewer = new RedBlackTreeViewer();
        viewer.frame.setSize(540, 480);
        viewer.frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        viewer.frame.setVisible(true);
    }
}
