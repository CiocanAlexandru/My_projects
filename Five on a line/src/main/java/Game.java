import java.awt.*;
import javax.swing.*;
import java.awt.event.*;

public class Game implements ActionListener {
    //players
    Player player1;
    Player player2;
    //meniu
    Meniu meniu;
    //castigatorul
    JFrame winer;
    JTextField text;
    JPanel winer_text;
    JButton back_to_meniu;
    JButton exit;
    //tabla si joc
    JFrame Game;
    JButton[][] boxes;
    JPanel layout;
    JPanel move_turn;
    JTextField what_move;
    //valori booleene
    boolean exit_win;
    boolean back_start;
    //Istoric
    Istoric istoric;

    Game() {
        istoric = new Istoric();
        boxes = new JButton[8][8];
        Game = new JFrame("Cinci pe linie");
        Game.setVisible(false);
    }

    public boolean isExit_win() {
        return exit_win;
    }

    public boolean isBack_start() {
        return back_start;
    }

    public void drawTable() {
        this.back_start = false;
        this.exit_win = false;
        this.Game = new JFrame("Cinci pe linie");
        this.Game.setSize(800, 800);
        this.Game.getContentPane().setBackground(new Color(50, 50, 50));
        this.Game.setLayout(new BorderLayout());
        this.Game.setVisible(true);
        this.Game.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.layout = new JPanel();
        this.layout.setLayout(new GridLayout(8, 8));
        this.layout.setBackground(new Color(50, 100, 34));
        this.move_turn = new JPanel();
        this.move_turn.setLayout(new BorderLayout());
        this.move_turn.setBackground(new Color(25, 140, 150));
        this.what_move = new JTextField();
        this.what_move.setText("Cinci pe linie");
        this.what_move.setOpaque(true);
        this.what_move.setHorizontalAlignment(JTextField.CENTER);
        this.what_move.setFont(new Font("Ink Free", Font.BOLD, 75));
        this.what_move.setForeground(new Color(25, 255, 25));
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                this.boxes[i][j] = new JButton();
                this.layout.add(this.boxes[i][j]);
                this.boxes[i][j].setFont(new Font("MV Boli", Font.BOLD, 120));
                this.boxes[i][j].setFocusable(false);
                this.boxes[i][j].addActionListener(this);
            }
        }
        this.move_turn.add(what_move);
        this.Game.add(layout);
        this.Game.add(move_turn, BorderLayout.SOUTH);
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {

        }
        this.what_move.setText("X turn");
    }

    boolean playerInfo() {
        this.player1 = new Player();
        this.player2 = new Player();
        this.player1.setWiner(false);
        this.player2.setWiner(false);
        JTextField field1 = new JTextField();
        JTextField field2 = new JTextField();
        Object[] Casute = {
                "Player1_name", field1,
                "Player2_name", field2

        };
        JOptionPane.showConfirmDialog(null, Casute, "Players Info", JOptionPane.DEFAULT_OPTION);
        if (field1.getText().equals("")) {
            this.player1.setName("Player1");
        } else {
            this.player1.setName(field1.getText());
        }
        if (field2.getText().equals("")) {
            this.player2.setName("Player2");
        } else {
            this.player2.setName(field2.getText());
        }
        this.player1.setTurn(true);
        this.player2.setTurn(false);
        this.player1.set_Moves(0);
        this.player2.set_Moves(0);
        return true;
    }

    void afisareCastigator() {
        winer = new JFrame("Castigator");
        text = new JTextField();
        this.winer_text = new JPanel();
        if (this.player1.isWiner()) {
            text.setOpaque(true);
            text.setBackground(Color.RED);
            this.winer.getContentPane().setBackground(Color.RED);
            text.setFont(new Font("Ink Free", Font.BOLD, 65));
            text.setText(player1.getName() + "-Winer");
            text.setBorder(null);
            text.setEnabled(false);
            this.istoric.add(player1.getName(), player1.getMoves(), player2.getMoves(), player2.getName(), player1.getName());
            for (int i = 0; i < 8; i++) {
                for (int j = 0; j < 8; j++) {
                    this.boxes[i][j].setEnabled(false);
                }
            }
            this.winer.setSize(500, 400);
            this.winer.setVisible(true);
            this.winer.setLayout(null);
            this.winer_text.setBounds(30, 0, 450, 100);
            this.winer_text.setLayout(new BorderLayout());
            this.winer_text.add(this.text);
            this.winer.add(winer_text);
            //butoane back_meniu si exit
            this.back_to_meniu = new JButton();
            this.exit = new JButton();
            this.back_to_meniu.setText("Meniu");
            this.back_to_meniu.addActionListener(this);
            this.back_to_meniu.setVisible(true);
            this.back_to_meniu.setFocusable(false);
            this.back_to_meniu.setBounds(10, 200, 200, 50);
            this.exit.setText("Exit");
            this.exit.addActionListener(this);
            this.exit.setVisible(true);
            this.exit.setBounds(250, 200, 200, 50);
            this.winer.add(exit);
            this.winer.add(back_to_meniu);
            Sound.winSound();
        }
        if (this.player2.isWiner()) {
            text.setOpaque(true);
            text.setBackground(Color.BLUE);
            this.winer.getContentPane().setBackground(Color.BLUE);
            this.text.setBorder(null);
            this.text.setFont(new Font("Ink Free", Font.BOLD, 65));
            text.setText(player2.getName() + "-Winer");
            text.setEnabled(false);
            this.istoric.add(player1.getName(), player1.getMoves(), player2.getMoves(), player2.getName(), player2.getName());
            for (int i = 0; i < 8; i++) {
                for (int j = 0; j < 8; j++) {
                    this.boxes[i][j].setEnabled(false);
                }
            }
            this.winer.setSize(500, 400);
            this.winer.setVisible(true);
            this.winer.setLayout(null);
            this.winer_text.setBounds(30, 0, 450, 100);
            this.winer_text.setLayout(new BorderLayout());
            this.winer_text.add(this.text);
            this.winer.add(winer_text);
            //butoane back_meniu si exit
            this.back_to_meniu = new JButton();
            this.exit = new JButton();
            this.back_to_meniu.setText("Meniu");
            this.back_to_meniu.addActionListener(this);
            this.back_to_meniu.setVisible(true);
            this.back_to_meniu.setFocusable(false);
            this.back_to_meniu.setBounds(10, 200, 200, 50);
            this.exit.setText("Exit");
            this.exit.addActionListener(this);
            this.exit.setVisible(true);
            this.exit.setBounds(250, 200, 200, 50);
            this.winer.add(exit);
            this.winer.add(back_to_meniu);
            Sound.winSound();
        }
        if (this.player1.getMoves() + this.player2.getMoves() == 64) {
            text.setOpaque(true);
            text.setBackground(Color.gray);
            this.winer.getContentPane().setBackground(Color.gray);
            this.text.setBorder(null);
            this.text.setFont(new Font("Ink Free", Font.BOLD, 65));
            text.setText("Draw");
            text.setEnabled(false);
            this.istoric.add(player1.getName(), 32, 32, player2.getName(), "Draw");
            for (int i = 0; i < 8; i++) {
                for (int j = 0; j < 8; j++) {
                    this.boxes[i][j].setEnabled(false);
                }
            }
            this.winer.setSize(500, 400);
            this.winer.setVisible(true);
            this.winer.setLayout(null);
            this.winer_text.setBounds(150, 0, 450, 100);
            this.winer_text.setLayout(new BorderLayout());
            this.winer_text.add(this.text);
            this.winer.add(winer_text);
            //butoane back_meniu si exit
            this.back_to_meniu = new JButton();
            this.exit = new JButton();
            this.back_to_meniu.setText("Meniu");
            this.back_to_meniu.addActionListener(this);
            this.back_to_meniu.setVisible(true);
            this.back_to_meniu.setFocusable(false);
            this.back_to_meniu.setBounds(10, 200, 200, 50);
            this.exit.setText("Exit");
            this.exit.addActionListener(this);
            this.exit.setVisible(true);
            this.exit.setBounds(250, 200, 200, 50);
            this.winer.add(exit);
            this.winer.add(back_to_meniu);
            Sound.drawSound();
        }


    }

    void check() {
        int sus, jos, st, dr, nord_est, sud_est, nord_vest, sud_vest;
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                sus = 1;
                jos = 1;
                st = 1;
                dr = 1;
                nord_est = 1;
                sud_est = 1;
                nord_vest = 1;
                sud_vest = 1;
                if (this.boxes[i][j].getText().equals("X")) {
                    //jos
                    for (int l = 1; l < 5; l++) {
                        if (l + i >= 8) {
                            break;
                        }
                        if (this.boxes[i + l][j].getText().equals("X")) {
                            jos++;
                        }
                    }
                    if (jos == 5) {
                        for (int l = 0; l < 5; l++) {
                            this.boxes[i + l][j].setBackground(Color.GREEN);
                        }
                        this.player1.setWiner(true);

                    }
                    //sus
                    for (int l = 1; l < 5; l++) {
                        if (i - l < 0) {
                            break;
                        }
                        if (this.boxes[i - l][j].getText().equals("X")) {
                            sus++;
                        }
                    }
                    if (sus == 5) {
                        for (int l = 0; l < 5; l++) {
                            this.boxes[i - l][j].setBackground(Color.GREEN);
                        }
                        this.player1.setWiner(true);

                    }
                    //stanga
                    for (int l = 1; l < 5; l++) {
                        if (j - l < 0) {
                            break;
                        }
                        if (this.boxes[i][j - l].getText().equals("X")) {
                            st++;
                        }
                    }
                    if (st == 5) {
                        for (int l = 0; l < 5; l++) {
                            this.boxes[i][j - l].setBackground(Color.GREEN);
                        }
                        this.player1.setWiner(true);

                    }
                    //dreapta
                    for (int l = 1; l < 5; l++) {
                        if (j + l >= 8) {
                            break;
                        }
                        if (this.boxes[i][j + l].getText().equals("X")) {
                            dr++;
                        }
                    }
                    if (dr == 5) {
                        for (int l = 0; l < 5; l++) {
                            this.boxes[i][j + l].setBackground(Color.GREEN);
                        }
                        this.player1.setWiner(true);

                    }
                    //nord_est
                    for (int l = 1; l < 5; l++) {
                        if (i - l < 0 || j + l >= 8) {
                            break;
                        }
                        if (this.boxes[i - l][j + l].getText().equals("X")) {
                            nord_est++;
                        }
                    }
                    if (nord_est == 5) {
                        for (int l = 0; l < 5; l++) {
                            this.boxes[i - l][j + l].setBackground(Color.GREEN);
                        }
                        this.player1.setWiner(true);

                    }
                    for (int l = 1; l < 5; l++) {
                        if (i + l >= 8 || j + l >= 8) {
                            break;
                        }
                        if (this.boxes[i + l][j + l].getText().equals("X")) {
                            sud_est++;
                        }
                    }
                    if (sud_est == 5) {
                        for (int l = 0; l < 5; l++) {
                            this.boxes[i + l][j + l].setBackground(Color.GREEN);
                        }
                        this.player1.setWiner(true);

                    }
                }
                for (int l = 1; l < 5; l++) {
                    if (i - l < 0 || j - l < 0) {
                        break;
                    }
                    if (this.boxes[i - l][j - l].getText().equals("X")) {
                        nord_vest++;
                    }
                }
                if (nord_vest == 5) {
                    for (int l = 0; l < 5; l++) {
                        this.boxes[i - l][j - l].setBackground(Color.GREEN);
                    }
                    this.player1.setWiner(true);

                }
                for (int l = 1; l < 5; l++) {
                    if (i + l >= 8 || j - l < 0) {
                        break;
                    }
                    if (this.boxes[i + l][j - l].getText().equals("X")) {
                        sud_vest++;
                    }

                }
                if (sud_vest == 5) {
                    for (int l = 0; l < 5; l++) {
                        this.boxes[i + l][j - l].setBackground(Color.GREEN);
                    }
                    this.player1.setWiner(true);

                }
                sus = 1;
                jos = 1;
                st = 1;
                dr = 1;
                nord_est = 1;
                sud_est = 1;
                nord_vest = 1;
                sud_vest = 1;
                if (this.boxes[i][j].getText().equals("O")) {
                    //jos
                    for (int l = 1; l < 5; l++) {
                        if (l + i >= 8) {
                            break;
                        }
                        if (this.boxes[i + l][j].getText().equals("O")) {
                            jos++;
                        }
                    }
                    if (jos == 5) {
                        for (int l = 0; l < 5; l++) {
                            this.boxes[i + l][j].setBackground(Color.GREEN);
                        }
                        this.player2.setWiner(true);

                    }
                    //sus
                    for (int l = 1; l < 5; l++) {
                        if (i - l < 0) {
                            break;
                        }
                        if (this.boxes[i - l][j].getText().equals("O")) {
                            sus++;
                        }
                    }
                    if (sus == 5) {
                        for (int l = 0; l < 5; l++) {
                            this.boxes[i - l][j].setBackground(Color.GREEN);
                        }
                        this.player2.setWiner(true);

                    }
                    //stanga
                    for (int l = 1; l < 5; l++) {
                        if (j - l < 0) {
                            break;
                        }
                        if (this.boxes[i][j - l].getText().equals("O")) {
                            st++;
                        }
                    }
                    if (st == 5) {
                        for (int l = 0; l < 5; l++) {
                            this.boxes[i][j - l].setBackground(Color.GREEN);
                        }
                        this.player2.setWiner(true);

                    }
                    //dreapta
                    for (int l = 1; l < 5; l++) {
                        if (j + l >= 8) {
                            break;
                        }
                        if (this.boxes[i][j + l].getText().equals("O")) {
                            dr++;
                        }
                    }
                    if (dr == 5) {
                        for (int l = 0; l < 5; l++) {
                            this.boxes[i][j + l].setBackground(Color.GREEN);
                        }
                        this.player2.setWiner(true);

                    }
                    //nord_est
                    for (int l = 1; l < 5; l++) {
                        if (i - l < 0 || j + l >= 8) {
                            break;
                        }
                        if (this.boxes[i - l][j + l].getText().equals("O")) {
                            nord_est++;
                        }
                    }
                    if (nord_est == 5) {
                        for (int l = 0; l < 5; l++) {
                            this.boxes[i - l][j + l].setBackground(Color.GREEN);
                        }
                        this.player2.setWiner(true);

                    }
                    for (int l = 1; l < 5; l++) {
                        if (i + l >= 8 || j + l >= 8) {
                            break;
                        }
                        if (this.boxes[i + l][j + l].getText().equals("O")) {
                            sud_est++;
                        }
                    }
                    if (sud_est == 5) {
                        for (int l = 0; l < 5; l++) {
                            this.boxes[i + l][j + l].setBackground(Color.GREEN);
                        }
                        this.player2.setWiner(true);

                    }
                }
                for (int l = 1; l < 5; l++) {
                    if (i - l < 0 || j - l < 0) {
                        break;
                    }
                    if (this.boxes[i - l][j - l].getText().equals("O")) {
                        nord_vest++;
                    }
                }
                if (nord_vest == 5) {
                    for (int l = 0; l < 5; l++) {
                        this.boxes[i - l][j - l].setBackground(Color.GREEN);
                    }
                    this.player2.setWiner(true);

                }
                for (int l = 1; l < 5; l++) {
                    if (i + l >= 8 || j - l < 0) {
                        break;
                    }
                    if (this.boxes[i + l][j - l].getText().equals("O")) {
                        sud_vest++;
                    }

                }
                if (sud_vest == 5) {
                    for (int l = 0; l < 5; l++) {
                        this.boxes[i + l][j - l].setBackground(Color.GREEN);
                    }
                    this.player2.setWiner(true);

                }
            }
        }
    }

    void startTheGame() {

        this.meniu = new Meniu();
        this.meniu.drawnMeniu();
        while (true) {
            if (this.meniu.isExit_press()) {

                this.meniu.closeMeniu();
                break;
            }
            if (this.meniu.isStart_press()) {
                if (this.playerInfo()) {
                    this.drawTable();

                }
                this.meniu.closeMeniu();
                this.meniu.setStart_press(false);

            } else {
                System.out.println("");
            }
            if (this.meniu.isIstoric_press()) {
                this.meniu.setIstoric_press(false);
                this.istoric.showIstoric();
            }
            if (exit_win == true || back_start == true) {
                exit_win = false;
                break;
            }

        }
        if (back_start == true) {
            back_start = false;
            this.startTheGame();
        }
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                if (e.getSource() == this.boxes[i][j]) {
                    if (this.player1.getTurn()) {
                        if (this.boxes[i][j].getText() == "") {
                            this.boxes[i][j].setForeground(new Color(255, 0, 0));
                            this.boxes[i][j].setFont(new Font("Arial", Font.PLAIN, 40));
                            this.boxes[i][j].setText("X");
                            this.player1.setTurn(false);
                            this.player1.Increment_Moves();
                            this.player2.setTurn(true);
                            this.what_move.setText("O turn");
                            this.check();
                            this.afisareCastigator();
                            Sound.piecePlaced();

                        }
                    } else {
                        if (this.boxes[i][j].getText() == "") {
                            this.boxes[i][j].setForeground(new Color(0, 0, 255));
                            this.boxes[i][j].setFont(new Font("Arial", Font.PLAIN, 40));
                            this.boxes[i][j].setText("O");
                            this.player1.setTurn(true);
                            this.player2.setTurn(false);
                            this.player2.Increment_Moves();
                            this.check();
                            this.afisareCastigator();
                            this.what_move.setText("X turn");
                            Sound.piecePlaced();

                        }
                    }

                }
            }
        }
        if (e.getSource() == this.exit) {
            this.winer.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
            this.winer.dispose();
            this.exit_win = true;
            this.Game.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
            this.Game.dispose();
            Sound.buttonPress();
        }
        if (e.getSource() == this.back_to_meniu) {
            this.winer.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
            this.winer.dispose();
            this.back_start = true;
            this.Game.setDefaultCloseOperation(WindowConstants.DISPOSE_ON_CLOSE);
            this.Game.dispose();
            Sound.buttonPress();

        }
    }
}
