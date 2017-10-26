/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package package2;

import java.io.DataInputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Calendar;
import java.util.GregorianCalendar;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 *
 * @author soujanya
 */
public class WINDOW0 extends javax.swing.JFrame {

    String check1,check2,temp = null ;
    
    public WINDOW0() {
        
        initComponents();
        
        new Thread()
        {
            @Override
            public void run()
            {
                while(true)
                {
                    Calendar cal = new GregorianCalendar() ;
                    
                    int hour = cal.get(Calendar.HOUR) ;
                    int min = cal.get(Calendar.MINUTE) ;
                    int sec = cal.get(Calendar.SECOND) ;
                    int mer = cal.get(Calendar.AM_PM) ;
                    int day = cal.get(Calendar.DATE) ;
                    int month = cal.get(Calendar.MONTH)+1 ;
                    int year = cal.get(Calendar.YEAR) ;
                    
                    String meridian ;
                    
                    if(mer == 0)
                        meridian = "AM" ;
                    else
                    {
                        meridian = "PM" ;
                        
                        if(hour==0)
                            hour = 12 ;
                    }
                    
                    String time = hour + ":" + min + " " + meridian ;
                    String date = day + "." + month + "." + year ;
                    
                    Date.setText(date) ;
                    
                    File f1 = new File("name.txt") ;
                    if(f1.exists())
                    {
                     FileInputStream fis1 = null ;
                     try {
                         fis1 = new FileInputStream("name.txt");
                         } catch (FileNotFoundException ex) {
                           Logger.getLogger(WINDOW0.class.getName()).log(Level.SEVERE, null, ex);
                           }
                     DataInputStream dis1 = new DataInputStream(fis1) ;
                     try {
                         temp = dis1.readUTF();
                         temp = temp.toUpperCase() ;
                         } catch (IOException ex) {
                           Logger.getLogger(WINDOW0.class.getName()).log(Level.SEVERE, null, ex);
                           }
                     jLabel3.setText("HI ! " + temp);
                    }
                    else
                    {
                        jLabel3.setText("HI ! " + Project2.initial.name);
                    }
                    
                }
            }
        }.start() ;
    }

    
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jPanel1 = new javax.swing.JPanel();
        jPanel3 = new javax.swing.JPanel();
        jLabel1 = new javax.swing.JLabel();
        jLabel2 = new javax.swing.JLabel();
        jLabel3 = new javax.swing.JLabel();
        jPasswordField1 = new javax.swing.JPasswordField();
        jButton1 = new javax.swing.JButton();
        Date = new javax.swing.JLabel();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setBackground(new java.awt.Color(1, 1, 1));
        setForeground(new java.awt.Color(1, 1, 1));
        setLocation(new java.awt.Point(500, 200));

        jPanel1.setBackground(new java.awt.Color(240, 139, 167));

        jPanel3.setBackground(new java.awt.Color(89, 89, 89));

        jLabel1.setIcon(new javax.swing.ImageIcon(getClass().getResource("/package2/coollogo_com-6544767.png"))); // NOI18N

        jLabel2.setFont(new java.awt.Font("Ubuntu", 1, 24)); // NOI18N
        jLabel2.setForeground(new java.awt.Color(254, 254, 254));
        jLabel2.setText("ENTER YOUR PASSWORD :");
        jLabel2.setVerticalAlignment(javax.swing.SwingConstants.BOTTOM);

        jLabel3.setFont(new java.awt.Font("Ubuntu", 1, 24)); // NOI18N
        jLabel3.setForeground(new java.awt.Color(254, 254, 254));
        jLabel3.setHorizontalAlignment(javax.swing.SwingConstants.RIGHT);

        jPasswordField1.setFont(new java.awt.Font("Tibetan Machine Uni", 1, 18)); // NOI18N
        jPasswordField1.setHorizontalAlignment(javax.swing.JTextField.CENTER);

        jButton1.setBackground(new java.awt.Color(229, 229, 229));
        jButton1.setFont(new java.awt.Font("Ubuntu", 0, 36)); // NOI18N
        jButton1.setForeground(new java.awt.Color(236, 27, 105));
        jButton1.setText("ENTER");
        jButton1.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jButton1ActionPerformed(evt);
            }
        });
        jButton1.addKeyListener(new java.awt.event.KeyAdapter() {
            public void keyPressed(java.awt.event.KeyEvent evt) {
                jButton1KeyPressed(evt);
            }
        });

        javax.swing.GroupLayout jPanel3Layout = new javax.swing.GroupLayout(jPanel3);
        jPanel3.setLayout(jPanel3Layout);
        jPanel3Layout.setHorizontalGroup(
            jPanel3Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel3Layout.createSequentialGroup()
                .addGroup(jPanel3Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(jPanel3Layout.createSequentialGroup()
                        .addComponent(jLabel3, javax.swing.GroupLayout.PREFERRED_SIZE, 220, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(18, 18, 18)
                        .addComponent(jLabel2, javax.swing.GroupLayout.PREFERRED_SIZE, 445, javax.swing.GroupLayout.PREFERRED_SIZE))
                    .addGroup(jPanel3Layout.createSequentialGroup()
                        .addGap(180, 180, 180)
                        .addComponent(jLabel1)))
                .addGap(0, 100, Short.MAX_VALUE))
            .addGroup(jPanel3Layout.createSequentialGroup()
                .addGap(215, 215, 215)
                .addGroup(jPanel3Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                    .addComponent(jButton1, javax.swing.GroupLayout.PREFERRED_SIZE, 278, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addComponent(jPasswordField1, javax.swing.GroupLayout.PREFERRED_SIZE, 278, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );
        jPanel3Layout.setVerticalGroup(
            jPanel3Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(jPanel3Layout.createSequentialGroup()
                .addGap(38, 38, 38)
                .addComponent(jLabel1, javax.swing.GroupLayout.PREFERRED_SIZE, 340, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addGroup(jPanel3Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addComponent(jLabel3, javax.swing.GroupLayout.Alignment.TRAILING, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                    .addComponent(jLabel2, javax.swing.GroupLayout.PREFERRED_SIZE, 36, javax.swing.GroupLayout.PREFERRED_SIZE))
                .addGap(30, 30, 30)
                .addComponent(jPasswordField1, javax.swing.GroupLayout.PREFERRED_SIZE, 47, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(50, 50, 50)
                .addComponent(jButton1, javax.swing.GroupLayout.PREFERRED_SIZE, 60, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(93, Short.MAX_VALUE))
        );

        Date.setFont(new java.awt.Font("Kinnari", 1, 36)); // NOI18N
        Date.setForeground(new java.awt.Color(254, 254, 254));
        Date.setHorizontalAlignment(javax.swing.SwingConstants.CENTER);
        Date.setText("HI");

        javax.swing.GroupLayout jPanel1Layout = new javax.swing.GroupLayout(jPanel1);
        jPanel1.setLayout(jPanel1Layout);
        jPanel1Layout.setHorizontalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, jPanel1Layout.createSequentialGroup()
                .addContainerGap()
                .addComponent(Date, javax.swing.GroupLayout.DEFAULT_SIZE, 187, Short.MAX_VALUE)
                .addGap(18, 18, 18)
                .addComponent(jPanel3, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
        );
        jPanel1Layout.setVerticalGroup(
            jPanel1Layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addComponent(jPanel3, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
            .addGroup(jPanel1Layout.createSequentialGroup()
                .addGap(21, 21, 21)
                .addComponent(Date, javax.swing.GroupLayout.PREFERRED_SIZE, 58, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );

        getContentPane().add(jPanel1, java.awt.BorderLayout.CENTER);

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void jButton1ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jButton1ActionPerformed
        check1 = new String(jPasswordField1.getPassword()) ;
                    
                    try {
                        FileInputStream fis = new FileInputStream("password.txt") ;
                        DataInputStream dis = new DataInputStream(fis) ;
                        
                        check2 = dis.readUTF() ;
                        System.out.println(check1 + check2);
                        if(check1.equals(check2))
                        {
                            
                            Project2.zero.setVisible(false);
                            Project2.first.setVisible(true) ;
                        }
                        else
                        {
                            jLabel2.setText("RE-ENTER YOUR PASSWORD");
                        }
                        
                    } catch (FileNotFoundException ex) {
                        Logger.getLogger(WINDOW0.class.getName()).log(Level.SEVERE, null, ex);
                    } catch (IOException ex) {
                        Logger.getLogger(WINDOW0.class.getName()).log(Level.SEVERE, null, ex);
                    }
       

    }//GEN-LAST:event_jButton1ActionPerformed

    private void jButton1KeyPressed(java.awt.event.KeyEvent evt) {//GEN-FIRST:event_jButton1KeyPressed
        // TODO add your handling code here:
        check1 = new String(jPasswordField1.getPassword()) ;
                    
                    try {
                        FileInputStream fis = new FileInputStream("password.txt") ;
                        DataInputStream dis = new DataInputStream(fis) ;
                        
                        check2 = dis.readUTF() ;
                        System.out.println(check1 + check2);
                        if(check1.equals(check2))
                        {
                            
                            Project2.zero.setVisible(false);
                            Project2.first.setVisible(true) ;
                        }
                        else
                        {
                            jLabel2.setText("RE-ENTER YOUR PASSWORD");
                        }
                        
                    } catch (FileNotFoundException ex) {
                        Logger.getLogger(WINDOW0.class.getName()).log(Level.SEVERE, null, ex);
                    } catch (IOException ex) {
                        Logger.getLogger(WINDOW0.class.getName()).log(Level.SEVERE, null, ex);
                    }
    }//GEN-LAST:event_jButton1KeyPressed

    
    public void main(String args[]) throws FileNotFoundException, IOException {
        
        Project2.zero.setVisible(true) ;      
        
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
      
          }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JLabel Date;
    private javax.swing.JButton jButton1;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JLabel jLabel3;
    private javax.swing.JPanel jPanel1;
    private javax.swing.JPanel jPanel3;
    private javax.swing.JPasswordField jPasswordField1;
    // End of variables declaration//GEN-END:variables
}
