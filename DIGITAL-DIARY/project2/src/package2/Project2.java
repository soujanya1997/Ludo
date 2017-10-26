/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package package2 ;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;
import javax.swing.JFrame;
import java.util.Calendar ;
import java.util.GregorianCalendar ;


/**
 *
 * @author soujanya
 */
class Project2 {
    
    static NewJFrame initial;
    static WINDOW0 zero ;
    static WINDOW1 first ;
    static WINDOW2 second ;
    static WINDOW3 third ;
    static WINDOW4 fourth ;
    static SETTINGS settings ;
    
    public static void main(String[] args) throws IOException {
        // TODO code application logic here
        

        
        
        File temp = new File("name.txt") ;
        
        if(temp.exists())
        {
        zero = new WINDOW0() ;
        first = new WINDOW1() ;
        second = new WINDOW2() ;
        third = new WINDOW3() ;
        fourth = new WINDOW4() ;
        settings = new SETTINGS() ;
        zero.setBounds(500,200,1000,700) ; 
        zero.setTitle("DEAR DIARY                                            @STUPEFY CORPORATIONS");
        zero.setResizable(false);
        zero.setVisible(true);
        zero.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        }
        else
        {   
        initial = new NewJFrame() ;
        initial.setBounds(500,200,1000,700) ;
        initial.setTitle("DEAR DIARY                                         @STUPEFY CORPORATIONS");
        initial.setResizable(false);
        initial.setVisible(true);
        initial.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
         zero = new WINDOW0() ;
         first = new WINDOW1() ;
         second = new WINDOW2() ;
         third = new WINDOW3() ;
         fourth = new WINDOW4() ;
         settings = new SETTINGS() ;
        }
    }
    
}
