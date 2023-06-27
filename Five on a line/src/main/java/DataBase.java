import java.sql.*;
public class DataBase {
    private static Connection conn=null;
    private static String URL="jdbc:oracle:thin:@localhost:1521:xe";
    private static String Name="Student";
    private static String Password="STUDENT";

    private DataBase(){}

    public static Connection getConn() {
        createConnection();
        return conn;
    }
    public static void createConnection()
    {
        try{
            conn=DriverManager.getConnection(URL,Name,Password);
        }
        catch (SQLException e)
        {
          e.printStackTrace();
        }
    }
    public static void closeConnection()
    {
        try{
            if(conn!=null)
            {
                conn.close();
            }
        }
        catch (SQLException e)
        {
            e.printStackTrace();
        }
    }

}
