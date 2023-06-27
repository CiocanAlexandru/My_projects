import java.awt.*;
import javax.swing.*;
import java.awt.event.*;

public class Meniu implements ActionListener {
    JFrame meniu;
    JPanel title;
    JTextField text;
    JButton start;
    JButton istoric;
    JButton exit;
    boolean start_press;
    boolean istoric_press;
    boolean exit_press;
    Meniu()
    {
        this.start_press=false;
        this.istoric_press=false;
        this.exit_press=false;
    }
    public void setStart_press(boolean start_press) {
        this.start_press = start_press;
    }

    public void setExit_press(boolean exit_press) {
        this.exit_press = exit_press;
    }

    public void setIstoric_press(boolean istoric_press) {
        this.istoric_press = istoric_press;
    }

    public boolean isStart_press() {
        return start_press;
    }

    public boolean isIstoric_press() {
        return istoric_press;
    }

    public boolean isExit_press() {
        return exit_press;
    }
    public void closeMeniu()
    {

            this.meniu.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
            this.meniu.dispose();

    }
    void drawnMeniu()
    {
        // Creare frame  al meniului
        this.title=new JPanel();
        this.text=new JTextField();
        this.text.setBackground(new Color(25,25,25));
        this.text.setFont(new Font("Ink Free",Font.BOLD,75));
        this.text.setHorizontalAlignment(JLabel.CENTER);
        this.text.setText("Meniu");
        this.text.setOpaque(true);
        this.text.setEnabled(false);
        this.title.setLayout(new BorderLayout());
        this.title.setBounds(235,100,300,100);
        this.title.add(this.text);
        this.meniu=new JFrame("Cinci pe linie");
        this.meniu.setVisible(true);
        this.meniu.setSize(800,800);
        this.meniu.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.meniu.getContentPane().setBackground(new Color(63,140,164));
        this.meniu.setLayout(null);
        // Ajustare butoane si adaugare in meniu
        //start button
        this.start=new JButton("Start");
        this.start.addActionListener(this);
        this.start.setSize(100,100);
        this.start.setFocusable(false);
        this.start.setBounds(275,260,200,40);
        this.start.setBackground(Color.RED);
        //istoric button
        this.istoric=new JButton("Istoric");
        this.istoric.addActionListener(this);
        this.istoric.setSize(100,100);
        this.istoric.setFocusable(false);
        this.istoric.setBounds(275,360,200,40);
        this.istoric.setBackground(Color.RED);
        // exit button
        this.exit=new JButton("Exit");
        this.exit.addActionListener(this);
        this.exit.setSize(100,100);
        this.exit.setFocusable(false);
        this.exit.setBounds(275,460,200,40);
        this.exit.setBackground(Color.RED);
        //adaugare in meniu
        this.meniu.add(this.start);
        this.meniu.add(this.istoric);
        this.meniu.add(this.exit);
        this.meniu.add(title);

    }
    @Override
    public void actionPerformed(ActionEvent e) {
       if(e.getSource()==this.start)
       {
           this.setStart_press(true);
           Sound.buttonPress();
       }
        if(e.getSource()==this.istoric)
        {
           this.setIstoric_press(true);
           Sound.buttonPress();
        }
        if(e.getSource()==this.exit)
        {
            this.setExit_press(true);
            Sound.buttonPress();
        }
    }

}


