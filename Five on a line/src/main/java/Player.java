public class Player {
    private String name;
    private int moves = 0;
    private boolean turn;
    private boolean winer = false;

    public boolean isWiner() {
        return winer;
    }

    public void setWiner(boolean winer) {
        this.winer = winer;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void Increment_Moves() {
        this.moves++;
    }

    public void set_Moves(int moves) {
        this.moves = moves;
    }

    public void setTurn(boolean turn) {
        this.turn = turn;
    }

    public String getName() {
        return name;
    }

    public int getMoves() {
        return moves;
    }

    public boolean getTurn() {
        return turn;
    }
}
