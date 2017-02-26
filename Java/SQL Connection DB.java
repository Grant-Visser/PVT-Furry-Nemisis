package com.company;

import java.sql.*;

//Fixing Class not found error: http://nixmash.com/java/classnotfoundexception-com-mysql-jdbc-driver-fix-in-intellij-idea/
//Original Source Code

class MysqlCon {
    private static Connection c1;

    public static void main(String args[]) {
        try {
            if (connectDB()){select("select * from emp");}
            else System.out.println("Error in connecting to Database");
            disconnectDB();
        } catch (Exception e) {
            System.out.println(e);
        }
    }

    private static boolean connectDB() {
        try {
            Class.forName("com.mysql.jdbc.Driver");
            c1 = DriverManager.getConnection("jdbc:mysql://localhost:3306/sonoo", "root", "test");
            return true;
        } catch (Exception e) {
            System.out.println(e);
            return false;
        }
    }

    private static boolean disconnectDB() {
        try {
            c1.close();
            return true;
        } catch (Exception e) {
            System.out.println(e);
            return false;
        }
    }

    private static void select(String query){
        try {
            Statement stmt = c1.createStatement();
            ResultSet rs = stmt.executeQuery(query);
            while (rs.next())
                System.out.println(rs.getInt(1) + "  " + rs.getString(2) + "  " + rs.getString(3));
        } catch (Exception e){
            System.out.println(e);
        }

    }
}