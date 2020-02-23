import javax.swing.*;
import javax.swing.GroupLayout.Alignment;

import java.awt.*;
import java.awt.event.*;
import java.awt.Image.*;

class index {
    public static void main(String args[]) {
        
        //Creating the Frame
        JFrame frame = new JFrame("Chat Frame");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 400);

        //Creating the MenuBar and adding components
        JMenuBar mb = new JMenuBar();
        JMenu m1 = new JMenu("FILE");
        JMenu m2 = new JMenu("Help");
        mb.add(m1);
        mb.add(m2);
        JMenuItem m11 = new JMenuItem("Open");
        JMenuItem m22 = new JMenuItem("Save as");
        m1.add(m11);
        m1.add(m22);

        // Text Area at the Center
        JPanel ta = new JPanel();
        ImageIcon scanning = new ImageIcon("ajax-loader.gif");
        JLabel scanstatus = new JLabel("Scanning... ", scanning, JLabel.CENTER);
        ta.add(scanstatus);
        scanstatus.setVisible(false);
        
        //Creating the panel at bottom and adding components
        //JPanel btnlayer = new JPanel(); // the panel is not visible in output
        JPanel btnlayer = new JPanel(); // the panel is not visible in output
        
        JLabel logo = new JLabel(new ImageIcon("logo.jpeg"));
        logo.setSize(50,50);
        logo.setAlignmentX(Component.LEFT_ALIGNMENT);
        JButton addbtn = new JButton("Add Device");
        addbtn.setAlignmentX(Component.RIGHT_ALIGNMENT);
        JButton scanbtn = new JButton("Scan");
        scanbtn.setAlignmentX(Component.RIGHT_ALIGNMENT);
        JButton analysebtn = new JButton("Analyse");
        analysebtn.setAlignmentX(Component.RIGHT_ALIGNMENT);
        
        // Components Added using Flow Layout
        btnlayer.add(logo);
        btnlayer.add(addbtn);
        btnlayer.add(scanbtn);
        btnlayer.add(analysebtn);
        
        //Adding Components to the frame.
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.getContentPane().add(BorderLayout.CENTER, btnlayer);
        frame.getContentPane().add(BorderLayout.NORTH, mb);
        frame.getContentPane().add(BorderLayout.SOUTH, ta);
        frame.setVisible(true);
        
        scanbtn.addActionListener(new ActionListener() {
            
            public void actionPerformed(ActionEvent evt) {
                scanstatus.setVisible(true);
            }
          
        });
    }
    /*
    JFrame frame = new JFrame("Test");

    ImageIcon scanning = new ImageIcon("ajax-loader.gif");
    frame.add(new JLabel("Scanning... ", scanning, JLabel.CENTER));

    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setSize(400, 300);
    frame.setVisible(true);
    */
}