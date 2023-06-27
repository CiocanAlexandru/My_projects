import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
import java.sql.*;

public class Istoric implements ActionListener {
    //informatii;
    DataBaseInfo info[] = new DataBaseInfo[10];
    JFrame Istoric;
    JButton Back;
    //Listare
    DefaultListModel<String> model=new DefaultListModel<>();
    JList<String> lista =new JList<>(model);
    DefaultListCellRenderer renderer =  (DefaultListCellRenderer) lista.getCellRenderer();
    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == this.Back) {
            this.model.removeAllElements();
            Istoric.removeAll();
            Istoric.dispose();
            Sound.buttonPress();
        }
    }
    Istoric(){
        this.getBaseInfo();
        this.Istoric = new JFrame("Istoric");
        this.Istoric.setVisible(false);
        this.Istoric.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        this.Istoric.setLayout(null);
        this.Istoric.setFocusable(false);
        this.Istoric.getContentPane().setBackground(new Color(63, 140, 164));
        this.Istoric.setSize(800, 800);
        this.Back = new JButton();
        this.Back.setVisible(true);
        this.Back.setText("Back");
        this.Back.setBounds(300, 700, 150, 50);
        this.Back.addActionListener(this);
        this.Istoric.add(Back);
        //Listare
        this.renderer.setHorizontalAlignment(SwingConstants.CENTER);
        this.lista.setBackground(Color.gray);
        this.lista.setBounds(100,60,550,500);
        this.model.addElement(" ");
        this.model.addElement("<html><font size=5> Istoric</font></html>");
        this.model.addElement(" ");
        this.model.addElement("<html><font size=5 color=red>Player1  Piese1  Piese2 Player2 Winer</font></html>");
        this.model.addElement(" ");
        for (int i = 0; i < 9; i++) {
            this.model.addElement("<html><font size=5>"+info[i].toString()+"</font></html>");
            this.model.addElement(" ");
        }
        this.Istoric.add(this.lista);
    }
    void showIstoric() {
        this.getBaseInfo();
        this.Istoric=new JFrame();
        this.Istoric.setVisible(true);
        this.Istoric.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        this.Istoric.setLayout(null);
        this.Istoric.setFocusable(false);
        this.Istoric.getContentPane().setBackground(new Color(63, 140, 164));
        this.Istoric.setSize(800, 800);
        this.Back = new JButton();
        this.Back.setVisible(true);
        this.Back.setText("Back");
        this.Back.setBounds(300, 700, 150, 50);
        this.Back.addActionListener(this);
        this.Istoric.add(Back);
        //Listare
        this.renderer.setHorizontalAlignment(SwingConstants.CENTER);
        this.lista.setBackground(Color.gray);
        this.lista.setBounds(100,60,550,500);
        this.model.addElement(" ");
        this.model.addElement("<html><font size=5> Istoric</font></html>");
        this.model.addElement(" ");
        this.model.addElement("<html><font size=5 color=red>Player1  Piese1  Piese2 Player2 Winer</font></html>");
        this.model.addElement(" ");
        for (int i = 0; i < 9; i++) {
            this.model.addElement("<html><font size=5>"+info[i].toString()+"</font></html>");
            this.model.addElement(" ");
        }
        this.Istoric.add(this.lista);
    }

    void add(String name1, int piese1, int piese2, String name2, String winer) {
        // aduag ceva nou ;
        try {
            Connection conn=DataBase.getConn();
            Statement rs = conn.createStatement();
            ResultSet rz = rs.executeQuery("select * from Istoric where rownum<=1");
            if (rz.next()) {
                int id;
                rz = rs.executeQuery("select id from Istoric where rownum<=1");
                rz.next();
                id = rz.getInt("id");
                id++;
                PreparedStatement stm = conn.prepareStatement("INSERT INTO Istoric(name1,piese1,piese2,name2,castigator,id) VALUES(?,?,?,?,?,?)");
                stm.setString(1, name1);
                stm.setInt(2, piese1);
                stm.setInt(3, piese2);
                stm.setString(4, name2);
                stm.setString(5, winer);
                stm.setInt(6, id);
                stm.executeUpdate();
            } else {

                PreparedStatement stm = conn.prepareStatement("INSERT INTO Istoric(name1,piese1,piese2,name2,castigator,id) VALUES(?,?,?,?,?,?)");
                stm.setString(1, name1);
                stm.setInt(2, piese1);
                stm.setInt(3, piese2);
                stm.setString(4, name2);
                stm.setString(5, winer);
                stm.setInt(6, 1);
                stm.executeUpdate();

            }

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    void getBaseInfo() {
        int k = 0;
        for (int i = 0; i < 9; i++) {
            this.info[i] = new DataBaseInfo();
        }
        try {
            Connection conn=DataBase.getConn();
            Statement stm = conn.createStatement();
            ResultSet rs = stm.executeQuery("select * from (select * from Istoric order by id desc) where rownum<=9");
            while (rs.next()) {
                this.info[k].nume1 = rs.getString("name1");
                this.info[k].nume2 = rs.getString("name2");
                this.info[k].piese1 = rs.getInt("piese1");
                this.info[k].piese2 = rs.getInt("piese2");
                this.info[k].winer = rs.getString("castigator");
                k++;
            }

        } catch (SQLException e) {
            e.printStackTrace();
        }

    }
}
