from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText


import datetime
import sqlite3




class Menu_Bar:
    def __init__(self,win,Main_Body):

        self.menu=Menu(win)
        win.config(menu=self.menu)

        #Name of the menu bar items

        self.File_Menu=Menu(self.menu,tearoff=False)
        self.Edit_Menu=Menu(self.menu,tearoff=False)
        self.View_Menu=Menu(self.menu,tearoff=False)
        self.Search_Menu = Menu(self.menu, tearoff=False)
        self.Help_Menu=Menu(self.menu,tearoff=False)

        #cascading Menus of the Menu bar
        self.menu.add_cascade(label="File",menu=self.File_Menu)
        self.menu.add_cascade(label="Edit", menu=self.Edit_Menu)
        self.menu.add_cascade(label="View", menu=self.View_Menu)
        self.menu.add_cascade(label="Search", menu=self.Search_Menu)
        self.menu.add_cascade(label="Help", menu=self.Help_Menu)

        #for sub menu of  file-menu

        self.File_Menu.add_command(label="Add Items",command=Main_Body.Add_Items)
        self.File_Menu.add_separator()
        self.File_Menu.add_command(label="Save",command=Main_Body.Save_Record)
        self.File_Menu.add_command(label="print",state=DISABLED)
        self.File_Menu.add_separator()
        self.File_Menu.add_command(label="Exit",command=Main_Body.Quit)

        #for sub menu of Edit-Menu

        self.Edit_Menu.add_command(label="Login Username",state=DISABLED)
        self.Edit_Menu.add_command(label="Login Password",state=DISABLED)
        self.Edit_Menu.add_separator()
        self.Edit_Menu.add_command(label="Delear information",state=DISABLED)
        self.Edit_Menu.add_command(label="Retailer information",state=DISABLED)
        self.Edit_Menu.add_separator()
        self.Edit_Menu.add_command(label="Depters Accout",state=DISABLED)
        self.Edit_Menu.add_separator()
        self.Edit_Menu.add_command(label="Update Items",command=Main_Body.Update_Items)
        self.Edit_Menu.add_command(label="Update Item's Rate",command=Main_Body.Update_Rate)

        #for sub menu of view menu
        self.View_Menu.add_command(label="Stock Goods",state=DISABLED)
        self.View_Menu.add_command(label="Sold Goods",state=DISABLED)
        self.View_Menu.add_separator()
        self.View_Menu.add_command(label="Delear Information",state=DISABLED)
        self.View_Menu.add_command(label="Depters Account",state=DISABLED)


        #for sub menu of Search  menu
        self.Search_Menu.add_command(label="Rate search by name",command=Main_Body.Search_Byname)
        self.Search_Menu.add_command(label="Show Record", command=Records.Show_Record)

        self.Search_Menu.add_separator()
        self.Search_Menu.add_command(label="DEPTER OPTION :",state=DISABLED)
        self.Search_Menu.add_command(label="Search by Name",state=DISABLED)
        self.Search_Menu.add_command(label="Search by credit",state=DISABLED)


        #for sub menu of Help menu
        self.Help_Menu.add_command(label="How to..",state=DISABLED)
        self.Help_Menu.add_command(label="Guide ",state=DISABLED)
        self.Help_Menu.add_separator()
        self.Help_Menu.add_command(label="About us ",command=Aboutus.About_Us)
        self.Help_Menu.add_command(label="About software ",command=Aboutus.About_Software)
        self.Help_Menu.add_separator()
        self.Help_Menu.add_command(label="Contact Us",state=DISABLED)
    #---------------------------------funtions-------------------------------



    ############################################################################


class Body:
    def __init__(self,win):
      #################################VERIABLE DECLARING#########################################################
        self.Name_Var=StringVar(win)
        self.Item_var=StringVar(win)
        self.Quantity_var = StringVar(win)
        self.Submit1_var = StringVar(win)
        self.Submit2_var = StringVar(win)
        self.Submit3_var = StringVar(win)
        self.Discountper_var = StringVar(win)
        self.Amountgiven_var = StringVar(win)




    ########################################################################################

     #---------------------------creating frames ---------------------------------------
        self.frame=Frame(win,width=200,height=1000,background="grey")
        self.frame.pack(fill=Y,side=LEFT)
        self.Left_Frame=Frame(win,width=900,height=1000,background="lightgrey",highlightbackground="black", highlightcolor="black", highlightthickness=1)
        self.Left_Frame.pack(fill=Y,side=LEFT)

       # self.Center_Frame = Frame(win, width=50, height=1000, background="grey")
       # self.Center_Frame.pack(fill=Y, side=LEFT)

        self.Right_Frame=Frame(win,width=700,height=1000,background="grey")
        self.Right_Frame.pack(fill=Y,side=LEFT)

        self.Rightmost_Frame = Frame(win, width=200, height=1000, background="lightgrey")
        self.Rightmost_Frame.pack(fill=Y, side=LEFT)

    #----------------customer name label and entry box-------------------------------------
        self.Name_Label=Label(self.Left_Frame,text=" Customer's Name :",width=20,bg="lightgrey",font=("Helvetica",10,"bold"))
        self.Name_Label.grid(row=0,column=0,padx=0,pady=50)
        self.Name_Entry=ttk.Entry(self.Left_Frame,width=30,textvariable=self.Name_Var)
        self.Name_Entry.grid(row=0,column=1)




        self.Name_Entry.focus()
    #-------------------------ITem combo box----------------------------------------------------------
        self.Item_Label = Label(self.Left_Frame, text="  \tItem:",bg="lightgrey",font=("Helvetica",9))
        self.Item_Label.grid(row=2, column=0)

        self.Item_Combobox=ttk.Combobox(self.Left_Frame,textvariable=self.Item_var)
        self.Item_Combobox.grid(row=2,column=1,sticky=W)
        self.Item_Combobox.focus()

   #--------------------- FETCHING Item list FROM DATABASE TO THE COMBOBOX -----------------------------------------------
        db = sqlite3.connect("STOCK_RECORD.db")
        self.Cursor = db.cursor()
        self.Cursor.execute("SELECT ITEM FROM STOCKITEMs ")
        self.Item_Iist=[]
        for row in self.Cursor.fetchall():
            self.Item_Iist.append(row)


        self.Item_Combobox['value'] = self.Item_Iist

        self.Cursor.close()
        db.close()

     #----------------------------------------OK button ---------------------------------------------
        self.First_Submit = ttk.Button(self.Left_Frame, text="Ok",command=self.Ok)
        self.First_Submit.grid(row=2, column=1, pady=0, ipady=2, ipadx=0,sticky=E,padx=30)

      #----------------------------------------------------------------------------------------------



     #   self.Item_Combobox.bind("<Return>",self.fun)       #binding item variable data


    #--------------------------quantity combobox--------------------------------------------------------
        self.Quentity_Label = Label(self.Left_Frame, text=" \tQuantity:", bg="lightgrey", font=("Helvetica", 9))
        self.Quentity_Label.grid(row=3, column=0,padx=0,pady=30)
        self.Quantity_Combobox = ttk.Combobox(self.Left_Frame,textvariable=self.Quantity_var)
        self.Quantity_Combobox.grid(row=3, column=1,sticky=W)



####################################################################################################################
    #-------------------------first submit button--------------------------------------------------------
        self.First_Submit =ttk.Button(self.Left_Frame, text="SUBMIT",command=self.Submit1)
        self.First_Submit.grid(row=4, column=1,pady=0,ipady=7,ipadx=10)

    #---------------------------Discount rate------------------------------------------------------------
        self.Discountper_Label=Label(self.Left_Frame,text="DISCOUNT RATE:",font=("Times New Rome", 9),bg="lightblue",fg="red")
        self.Discountper_Label.grid(row=5,column=0,pady=30)
        self.Discountper_Entry=ttk.Entry(self.Left_Frame,textvariable=self.Discountper_var)
        self.Discountper_Entry.grid(row=5,column=1,padx=0,ipadx=0,sticky=W)



        self._per = Label(self.Left_Frame, text="%", font=("Times New Rome", 9), bg="lightgrey",
                                fg="red")
        self._per.grid(row=5,column=1,padx=150,pady=0,sticky=W)
    #------------------------second submit button-----------------------------------------------------------------
        self.Second_Submit = ttk.Button(self.Left_Frame, text="SUBMIT",command=self.Submit2)
        self.Second_Submit.grid(row=6, column=1, pady=0, ipady=7, ipadx=10)

    #--------------------------- amound given---------------------------------------------------------------
        self.Amountgiven_Label=Label(self.Left_Frame,text="\tAmount Given:",font=("Helvetica", 9,"bold"),bg="lightgrey",fg="brown")
        self.Amountgiven_Label.grid(row=7,column=0,pady=70)

        self.Amountgiven_Entry = ttk.Entry(self.Left_Frame,textvariable=self.Amountgiven_var)
        self.Amountgiven_Entry.grid(row=7, column=1, ipadx=0,sticky=W)

    #---------------------------third submit button------------------------------------------------
        self.Third_Submit = ttk.Button(self.Left_Frame, text="SUBMIT",command=self.Submit3)
        self.Third_Submit.grid(row=8, column=1, pady=10, ipady=7, ipadx=10)
     #--------##################################################################----------------------------------------------------------------
    #--------------------------------Right Frame------------------------------------------------------
    #--------------------------------------Total amount calculated-------------------------------------------------------------
        self.Totalamount_Label = Label(self.Right_Frame, text="\tTotal Amount:", font=("Helvetica", 9), bg="grey",justify="left")
        self.Totalamount_Label.grid(row=0, column=0, pady=130)

        self.Totalamount_Entry = ttk.Entry(self.Right_Frame, width=20)
        self.Totalamount_Entry.grid(row=0, column=1, ipadx=0, padx=0, sticky=W)
#--------------------------------for space--------------------------------------------------------
        self.space=Label(self.Right_Frame,text="  ",justify='left',bg='grey',width=5)
        self.space.grid(row=0,column=3)

    #-----------------------------------------Discount amount Calculated--------------------------------------------------------------
        self.Discountamount_Label = Label(self.Right_Frame, text="\tDiscount Amount:", font=("Helvetica", 9), bg="grey",justify="left")
        self.Discountamount_Label.grid(row=1, column=0)

        self.Discountamount_Entry = ttk.Entry(self.Right_Frame)
        self.Discountamount_Entry.grid(row=1, column=1, ipadx=0, padx=0,sticky=W)

   #----------------------------------------------Total amount calculated--------------------------------------------------------------
        self.Netamount_Label = Label(self.Right_Frame, text="\tNET AMOUNT:", font=("Helvetica", 9),fg='blue', bg="#DD7181", justify="left")
        self.Netamount_Label.grid(row=2, column=0)

        self.Netamount_Entry = ttk.Entry(self.Right_Frame,width=20)
        self.Netamount_Entry.grid(row=2, column=1, ipadx=0, padx=0,pady=40,sticky=W)

  #------------------------------------------------Return Amount calcutaled------------------------------------------------------------------------
        self.Returnamount_Label = Label(self.Right_Frame, text="\tRETURN AMOUNT:", font=("Helvetica", 9,"bold"),fg="Yellow", bg="grey",justify='left')
        self.Returnamount_Label.grid(row=3, column=0,ipadx=50)

        self.Returnamount_Entry = ttk.Entry(self.Right_Frame)
        self.Returnamount_Entry.grid(row=3, column=1, ipadx=0, padx=0, pady=50,sticky=W)
    #-----------------------------------------------save data---------------------------------------------------------------------------------
        self.Save_Button = ttk.Button(self.Right_Frame, text="SAVE",command=self.Save_Record)
        self.Save_Button.grid(row=4,column=2, pady=10, ipady=7, ipadx=20)
    #--------------------------------------------RESET ENTRIES ------------------------------------------------------------------------------
        self.Reset_Button = ttk.Button(self.Right_Frame, text="RESET",command=self.Reset_Entries)           # () must not be provided whiling calling function in the command
        self.Reset_Button.grid(row=4, column=0, pady=10, ipady=7, padx=10)



    #-----------------------------------------------------------------------------------------------------------------------------------------

  #  def Costumer(self):
    #    pass

   # def Item(self):
     #   pass
   # def Quantity(self):
    #    pass

 #-----------------------------------FUNCTION FOR OK BUTTON-----binding event function for item combobox  (help to fill the combobox of quantity------------

    def Ok(self):
        try:
            db = sqlite3.connect("STOCK_RECORD.db")
            self.Cursor = db.cursor()
            self.Cursor.execute("SELECT QUANTITY FROM STOCKITEMs WHERE ITEM= ? ", (self.Item_var.get(),))

            for row in self.Cursor.fetchall():
                self.Q = int(row[0])
            self.Quantity_Combobox['value'] = tuple(i for i in range(1, self.Q + 1))
        except ValueError:
            messagebox.showerror("Error Notification", "Either you left the entry blank or Wrong type entry")
            self.Quantity_Combobox.delete(0, 'end')
        except AttributeError as AE:
            messagebox.showerror("Error Notification", " No item found of that name ! ")

        # -------------------------------------------------------function to check whether the quantity is int or not----------------------------------
    def Try_Qty(self):
            try:
                self.Qty = int(self.Quantity_var.get())

            except ValueError:
                messagebox.showerror("Error Notification", "Either you left the entry blank or Wrong type entry")
                self.Quantity_Combobox.delete(0, 'end')
            except AttributeError as AE:
                messagebox.showerror("Error Notification", AE)

        # ------------------------------------------------------------------------------------------------------------------------------------

    #-------------------------------------------------function for first submit button------------------------------------------
    def Submit1(self):

            self.Try_Qty()

            self.Totalamount_Entry.delete(0, "end")  #delete the content of the total amount entry box entry box

            db = sqlite3.connect("STOCK_RECORD.db")
            self.Cursor = db.cursor()
            self.Cursor.execute("SELECT RATE FROM STOCKITEMs WHERE ITEM= ? ", (self.Item_var.get(),))
            for row in self.Cursor.fetchall():
                self.R=int(row[0])


            self.Totalamount_Entry.insert(0,self.R*self.Qty)
            print(self.R)
#----------------------------------------------------function for second submit button------------------------------------------------------------------------------

    def Submit2(self):

         self.Discountamount_Entry.delete(0,'end')
         self.Netamount_Entry.delete(0,'end')
         try:
            self.dis_per=float(self.Discountper_var.get())
            self.disA=(self.dis_per/100)*self.R*self.Qty
            self.Discountamount_Entry.insert(0,self.disA)

            self.Total_P=self.R*self.Qty-self.disA   #variable for total price

            self.Netamount_Entry.insert(0,self.Total_P)


         except ValueError:
            messagebox.showerror("Error Notification", "Either you left the entry blank or Wrong type entry")
            self.Discountper_Entry.delete(0,'end')

         except AttributeError as AE:
            messagebox.showerror("Error Notification", AE)


#-------------------------------------------------------------------function for third submit button----------------------------------------------------------------
    def Submit3(self):

        self.Returnamount_Entry.delete(0,'end')

        try:
            self.Amount_G = int(self.Amountgiven_var.get())
            self.Returnamount_Entry.insert(0,self.Amount_G-self.Total_P)
            self.Submit_count = 100  # to check if all submit is pressed or not
        except ValueError:
            messagebox.showerror("Error Notification", "Either you left the entry blank or Wrong type entry")
            self.Amountgiven_Entry.delete(0,'end')
        except AttributeError as AE:
            messagebox.showerror("Error Notification"," Attribute  Error ! ")

#-------------------------------------------------------------------------SAVE THE RECORD--------------------------------------------------------------------------

    def Save_Record(self):
        if self.Name_Var.get()=='':
            self.Costumer_Name="UNKNOWN"
        else:
            self.Costumer_Name=self.Name_Var.get()
        try:
            if self.Submit_count==100:
                self.DATE=datetime.datetime.now().strftime("%d-%m-%y")


                self.file=open(self.DATE+".txt","a")
                self.file.write("-------------------------------------------\n"
                                "\tCostumer Name : {} \n\tItem : {}"
                                " \n\tQuantity: {} \n\tTotal Amount:{} "
                                "\n\tDiscount Amount:{}\n\tNet Amount:{} "
                                "\n-------------------------------------------"
                                "\n".format(self.Costumer_Name,self.Item_var.get(),self.Qty,self.R*self.Qty,self.disA,self.Total_P))

                self.Update_Quantity()    #function call to update the quantity of the sold item
                self.Submit_count=100
                messagebox.showinfo("Notification","Record has been successfully saved")

            else:
                messagebox.showerror("Error Notification", " Error to save the Record ")
        except ValueError:
            messagebox.showerror("Error Notification", "Either you left the entry blank or Wrong type entry")
            self.Quantity_Combobox.delete(0, 'end')
        except AttributeError as AE:
            messagebox.showerror("Error Notification", " Attribute  Error ! ")

#---------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------- CLEAR THE DATA OF THE ENTRIES-----------------------------------------------------------------
    def Reset_Entries(self):
           self.Name_Entry.delete(0,'end')
           self.Item_Combobox.delete(0,'end')
           self.Quantity_Combobox.delete(0,'end')
           self.Netamount_Entry.delete(0,'end')
           self.Totalamount_Entry.delete(0,'end')
           self.Discountper_Entry.delete(0,'end')
           self.Discountamount_Entry.delete(0,'end')
           self.Amountgiven_Entry.delete(0,'end')
           self.Returnamount_Entry.delete(0,'end')


#-----------------------------------------------------------function to update the quantity of the sold item---------------------------
    def Update_Quantity(self):
        db = sqlite3.connect("STOCK_RECORD.db")
        self.Cursor = db.cursor()

        self.Cursor.execute("UPDATE  STOCKITEMs SET QUANTITY=? WHERE ITEM=?",(self.Q-self.Qty,self.Item_var.get())) #(self.Q=total quantity of the item and self.Qty=total quantity purchased)
        db.commit()
#-----------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------FUNCTION FOR ADD ITEM MENU --------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------
    def Add_Items(self):

        #-----------------------------------NEW WINDOWS for stock goods entry-----------------------------------------------------
        win_Stock=Tk()
        win_Stock.title("ADD ITEMS")
        win_Stock.geometry("700x400+300+200")
        win_Stock.resizable(0,0)
        #win_Stock.maxsize(width=700,height=400)

     #------------------------------------------frame--------------------------------------------------------------------------------
        self.frameL = Frame(win_Stock, width=160, height=400, background="white")
        self.frameL.pack(fill=Y, side=LEFT)

        self.frame=Frame(win_Stock,width=700,height=400,background="lightgrey",highlightbackground="blue", highlightcolor="lightblue", highlightthickness=2)
        self.frame.pack(fill=Y,side=LEFT)
        # --------------------------------------VARIABLES -------------------------------------------------------------------------

        self.I_Var = StringVar(win_Stock)
        self.R_Var = StringVar(win_Stock)
        self.Qnty_Var = StringVar(win_Stock)

        #-------------------------------------------------------------------------------------------------------------------------------------------------

        self.label_Item=Label(self.frame,text="ITEM :",bg="lightgrey")
        self.label_Item.grid(row=3,column=0,pady=80,padx=50)
        self.Entry_Item=ttk.Entry(self.frame,textvariable=self.I_Var)
        self.Entry_Item.grid(row=3,column=1,padx=50)
        self.Entry_Item.focus()

        self.label_Rate = Label(self.frame, text=" RATE :", bg="lightgrey")
        self.label_Rate.grid(row=4, column=0, pady=0, padx=0)
        self.Entry_Rate = ttk.Entry(self.frame,textvariable=self.R_Var)


        self.Entry_Rate.grid(row=4, column=1, padx=10)

        self.label_Quantity = Label(self.frame, text=" QUANTITY  :", bg="lightgrey")
        self.label_Quantity.grid(row=5, column=0, pady=0, padx=0)
        self.Entry_Quantity = ttk.Combobox(self.frame,width=5,textvariable=self.Qnty_Var)
        self.Entry_Quantity.grid(row=5, column=1, padx=10,pady=40)
        self.Entry_Quantity['value']=tuple(i for i in range(10))

        self.button=ttk.Button(self.frame,text="ADD",command=self.check)
        self.button.grid(row=6,column=1,pady=30,ipadx=20,sticky=E)

        win_Stock.mainloop()
#--------------------------------------checking if the entry is blank or valueerror or not------------------------------------------------------------------------------------
    def check(self):

          try:
              float(self.R_Var.get())
              int (self.Qnty_Var.get())
              self.save_goodsRec()
              print("value enter sucessful")


          except ValueError as EX:
              messagebox.showerror("Error Notification", "ERROR : EITHER YOU LEFT THE ENTRY BLANK OR WRONG TYPE ENTRY")
          except AttributeError as AE:
              messagebox.showerror("Error Notification", " Attribute  Error ! ")



          #-----------------------------------------------storing New items  using sqlite3---------------------------------------------------------------------------------------------
    def save_goodsRec(self):

            self.db=sqlite3.connect("STOCK_RECORD.db")
            self.Cursor=self.db.cursor()

            self.db.execute("CREATE TABLE IF NOT EXISTS STOCKITEMs (ITEM TEXT PRIMARY KEY NOT NULL,RATE FLOAT NOT NULL, QUANTITY INTEGER NOT NULL)")
                                                                                                                            #use 'primary key' keyword for unique entry

            self.Cursor.execute("INSERT INTO STOCKITEMs (ITEM,RATE,QUANTITY)VALUES(?,?,?)",(self.I_Var.get(),self.R_Var.get(),self.Qnty_Var.get()))

            self.db.commit()
            self.Cursor.close()
            self.db.close()
            self.Clear_Entry()
  #----------------------------------------------function to clear entries of NEw item or Update item menu--------------------------------------------
    def Clear_Entry(self):                                #for clearing all entries
        self.Entry_Item.delete(0,"end")
        self.Entry_Rate.delete(0,"end")
        self.Entry_Quantity.delete(0,"end")



#----------------------------------------------------------------------------------------------------------------------------------
    #----------------------------------------- UPDATE ITEMS ---------------------------------------------------------

    def Update_Items(self):

        # -----------------------------------NEW WINDOWS for stock goods entry-----------------------------------------------------
        win_Stock = Tk()
        win_Stock.title("Update ITEMS")
        win_Stock.geometry("700x400+300+200")
        win_Stock.resizable(0,0)
        #win_Stock.maxsize(width=700, height=400)
        win_Stock.configure(background="lightblue")
        # ------------------------------------------frame--------------------------------------------------------------------------------
        self.frameL = Frame(win_Stock, width=160, height=400, background="lightblue")
        self.frameL.pack(fill=Y, side=LEFT)

        self.frame = Frame(win_Stock, width=700, height=400, background="lightgrey", highlightbackground="black",
                           highlightcolor="red", highlightthickness=2)
        self.frame.pack(fill=Y, side=LEFT,)
        # --------------------------------------VARIABLES -------------------------------------------------------------------------

        self.I_Var = StringVar(win_Stock)
        self.R_Var = StringVar(win_Stock)
        self.Qnty_Var = StringVar(win_Stock)

        # -------------------------------------------------------------------------------------------------------------------------------------------------

        self.label_Item = Label(self.frame, text="Old Item :", bg="lightgrey")
        self.label_Item.grid(row=3, column=0, pady=80, padx=50)

        self.Item_Combobox = ttk.Combobox(self.frame, textvariable=self.I_Var)
        self.Item_Combobox.grid(row=3, column=1,padx=50)
        self.Item_Combobox.focus()

        # --------------------- FETCHING Item list FROM DATABASE TO THE COMBOBOX -----------------------------------------------
        db = sqlite3.connect("STOCK_RECORD.db")
        self.Cursor = db.cursor()
        self.Cursor.execute("SELECT ITEM FROM STOCKITEMs ")
        self.Item_Iist = []
        for row in self.Cursor.fetchall():
            self.Item_Iist.append(row)

        self.Item_Combobox['value'] = self.Item_Iist
       #-----------------------------------------------------------------------------------------------------------------------------
        self.label_Rate = Label(self.frame, text="New RATE :", bg="lightgrey")
        self.label_Rate.grid(row=4, column=0, pady=0, padx=0)
        self.Entry_Rate = ttk.Entry(self.frame, textvariable=self.R_Var)

        self.Entry_Rate.grid(row=4, column=1, padx=10)

        self.label_Quantity = Label(self.frame, text="New QUANTITY  :", bg="lightgrey")
        self.label_Quantity.grid(row=5, column=0, pady=0, padx=0)
        self.Entry_Quantity = ttk.Combobox(self.frame, width=5, textvariable=self.Qnty_Var)
        self.Entry_Quantity.grid(row=5, column=1, padx=10, pady=40)
        self.Entry_Quantity['value'] = tuple(i for i in range(10))

        self.button = ttk.Button(self.frame, text="UPDATE", command=self.check)
        self.button.grid(row=6, column=1, pady=30, ipadx=20, sticky=E)

        win_Stock.mainloop()

    #-----------------------------------------------UPDATE  OLD ITEMS using sqlite3---------------------------------------------------------------------------------------------
    def Update_goodsRec(self):

            self.db=sqlite3.connect("STOCK_RECORD.db")
            self.Cursor=self.db.cursor()

            self.db.execute("CREATE TABLE IF NOT EXISTS STOCKITEMs (ITEM TEXT  NOT NULL,RATE FLOAT NOT NULL, QUANTITY INTEGER NOT NULL)")
                                                                                                                            #use 'primary key' keyword for unique entry

    #==============================================================================use self.cursor.execute("update)==================================================

            self.Cursor.execute("INSERT INTO STOCKITEMs (ITEM,RATE,QUANTITY)VALUES(?,?,?)",(self.I_Var.get(),self.R_Var.get(),self.Qnty_Var.get()))
     #================================================================================================================================================================
            self.db.commit()
            self.Cursor.close()
            self.db.close()
            self.Clear_Entry()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------UPDATE RATE------------------------------------------------------------------------------------
    def Update_Rate(self):
         #------------------------new window for Update rate-----------------
         win_UpRate = Tk()
         win_UpRate.title("Update Item's Rate")
         win_UpRate.geometry("700x250+300+200")
         win_UpRate.resizable(0,0)
        # win_UpRate.maxsize(width=700, height=250)
         win_UpRate.configure(background="white")
         # ------------------------------------------frame--------------------------------------------------------------------------------
         self.frameL = Frame(win_UpRate, width=160, height=400, background="white")
         self.frameL.pack(fill=Y, side=LEFT)
         self.frame = Frame(win_UpRate, width=700, height=400, background="lightgrey", highlightbackground="black",
                            highlightcolor="red", highlightthickness=2)
         self.frame.pack(fill=Y, side=LEFT, )
         # --------------------------------------VARIABLES -------------------------------------------------------------------------

         self.It_Var = StringVar(win_UpRate)
         self.Ra_Var = StringVar(win_UpRate)

         # -------------------------------------------------------------------------------------------------------------------------------------------------
         self.label_Item = Label(self.frame, text="Old Item :", bg="lightgrey")
         self.label_Item.grid(row=3, column=0, pady=60, padx=50)
         self.Item_Combobox = ttk.Combobox(self.frame, textvariable=self.It_Var)
         self.Item_Combobox.grid(row=3, column=1, sticky=W)
         self.Item_Combobox.focus()

         # --------------------- FETCHING Item list FROM DATABASE TO THE COMBOBOX -----------------------------------------------
         db = sqlite3.connect("STOCK_RECORD.db")
         self.Cursor = db.cursor()
         self.Cursor.execute("SELECT ITEM FROM STOCKITEMs ")
         self.Item_Iist = []
         for row in self.Cursor.fetchall():
             self.Item_Iist.append(row)

         self.Item_Combobox['value'] = self.Item_Iist
        #------------------------------------------------------------------------------------------
         self.label_Rate = Label(self.frame, text="New RATE :", bg="lightgrey")
         self.label_Rate.grid(row=4, column=0, pady=0, padx=0)
         self.Entry_Rate = ttk.Entry(self.frame, textvariable=self.Ra_Var)

         self.Entry_Rate.grid(row=4, column=1, padx=10)

         self.button = ttk.Button(self.frame, text="UPDATE", command=self.check2)
         self.button.grid(row=6, column=1, pady=30, ipadx=20, sticky=E)

         win_UpRate.mainloop()

#----------------------------------------------------------------------------------------------------------------------------------------------------------

        # --------------------------------------checking if the entry is blank or valueerror or not------------------------------------------------------------------------------------

    def check2(self):
            try:
                float(self.Ra_Var.get())
                self.Update_R()
                messagebox.showinfo("Success Notification", "value update successful")

            except ValueError:
                messagebox.showerror("Error Notification", "ERROR : EITHER YOU LEFT THE ENTRY BLANK OR WRONG TYPE ENTRY")
            except AttributeError:
                messagebox.showerror("Error Notification", " Attribute  Error ! ")
        # -----------------------------------------------storing New items  using sqlite3---------------------------------------------------------------------------------------------
    def Update_R(self):
            self.db = sqlite3.connect("STOCK_RECORD.db")
            self.Cursor = self.db.cursor()


            self.Cursor.execute("UPDATE  STOCKITEMs SET RATE=? WHERE ITEM=?",
                                (self.Ra_Var.get(), self.It_Var.get()))

            self.db.commit()
            self.Cursor.close()
            self.db.close()
            self.Clear_Entry2()

        # ----------------------------------------------function to clear entries of NEw item or Update item menu--------------------------------------------
    def Clear_Entry2(self):  # for clearing all entries
            self.Item_Combobox.delete(0, "end")
            self.Entry_Rate.delete(0, "end")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------FUNCTION FOR ITEM'S RATE SEARCH BY NAME----------------------------------------------------------------------
    def Search_Byname(self):
    # ------------------------new window for Update rate-----------------
            win_UpRate = Tk()
            win_UpRate.title("Update Item's Rate")
            win_UpRate.geometry("700x250+300+200")
            win_UpRate.resizable(0,0)
           # win_UpRate.maxsize(width=700, height=250)
            win_UpRate.configure(background="white")
            # ------------------------------------------frame--------------------------------------------------------------------------------
            self.frameL = Frame(win_UpRate, width=160, height=400, background="white")
            self.frameL.pack(fill=Y, side=LEFT)
            self.frame = Frame(win_UpRate, width=700, height=400, background="lightgrey", highlightbackground="black",
                               highlightcolor="grey", highlightthickness=2)
            self.frame.pack(fill=Y, side=LEFT, )
            # --------------------------------------VARIABLE for item of item entry-------------------------------------------------------------------------

            self.It_Var = StringVar(win_UpRate)
            # -------------------------------------------------------------------------------------------------------------------------------------------------
            self.label_Item = Label(self.frame, text=" Item :", bg="lightgrey")
            self.label_Item.grid(row=3, column=0, pady=40, padx=30)
            self.Item_Combobox = ttk.Combobox(self.frame, textvariable=self.It_Var)
            self.Item_Combobox.grid(row=3, column=1, sticky=W)
            self.Item_Combobox.focus()

            # --------------------- FETCHING Item list FROM DATABASE TO THE COMBOBOX -----------------------------------------------
            db = sqlite3.connect("STOCK_RECORD.db")
            self.Cursor = db.cursor()
            self.Cursor.execute("SELECT ITEM FROM STOCKITEMs ")
            self.Item_Iist = []
            for row in self.Cursor.fetchall():
                self.Item_Iist.append(row)

            self.Item_Combobox['value'] = self.Item_Iist
            # ------------------------------------------------------------------------------------------

            self.button = ttk.Button(self.frame, text="SEARCH", command=self.Show_Rate)
            self.button.grid(row=4, column=1, pady=10,padx=40, ipadx=20, sticky=E)
           #------------------------------------------------------------------------------------------
            self.label_Rate = Label(self.frame, text=" RATE :", bg="lightgrey")
            self.label_Rate.grid(row=5, column=0, pady=30, padx=0)
            self.Entry_Rate = ttk.Entry(self.frame,)

            self.Entry_Rate.grid(row=5, column=1, padx=0,sticky=W)

            win_UpRate.mainloop()



    # ---------------------------------------------FUNCTION TO SHOW RATE---------------------------------------------------------------------------------------------

    def Show_Rate(self):
        try:
            self.Entry_Rate.delete(0,'end')
            self.db = sqlite3.connect("STOCK_RECORD.db")
            self.Cursor = self.db.cursor()

            self.Cursor.execute("SELECT RATE FROM STOCKITEMs WHERE ITEM= ? ", (self.It_Var.get(),))
            for row in self.Cursor.fetchall():
                self.Rate = int(row[0])

            self.Entry_Rate.insert(0, self.Rate)

            self.db.commit()
            self.Cursor.close()
            self.db.close()

        except AttributeError:
            messagebox.showerror("Error Notification", " Attribute  Error ! ")
            self.Item_Combobox.delete(0, 'end')
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------FUNTION FOR QUIT MENU----------------------------------------------------------------------------------
    def Quit(self):
        MsgBox = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application',
                                        icon='warning')
        if MsgBox == 'yes':
            win.destroy()


class Record:
    def Show_Record(self):

        win_Record=Tk()
        win_Record.title("View sales Record")

        win_Record.geometry("700x600+420+120")

        win_Record.maxsize(width=500, height=500)
        win_Record.configure(background="lightgrey")
        win_Record.resizable(0,0)

        self.frame=Frame(win_Record,width=700,height=400,background="lightgrey")
        self.frame.pack()
#--------------------------variable declare------------------------------------------------------------------------------
        self.Rec_Date = StringVar(self.frame)

#-----------------------labels------------------------------------------------------------------------------------------------
        self.label_Date = Label(self.frame, text="  Enter Date :",font=("timesnewrome",10,"bold"), bg="lightgrey",fg="brown")
        self.label_Date.grid(row=1, column=0,pady=30)



        self.Entry_Date =ttk.Entry(self.frame,textvariable=self.Rec_Date)
        self.Entry_Date.grid(row=1, columnspan=1, sticky=E)
        self.Entry_Date.focus()

        self.button=ttk.Button(self.frame,text="ok",command=self.onclick)
        self.button.grid(row=3,columnspan=1,pady=30,sticky=E)



        self.T=ScrolledText(self.frame,width=50,height=18)
        self.T.insert(END, "")
        self.T.grid(row=5,columnspan=1)

        win_Record.mainloop()

    def onclick(self):

        file=open(self.Rec_Date.get()+".txt",'r')
        self.T.insert(END,file.read())
        file.close()



'''''''''
def Authorization():
    db = sqlite3.connect("Useraccount.db")
    Cursor =db.cursor()

    db.execute(
        "CREATE TABLE IF NOT EXISTS Useraccount (USERNAME TEXT PRIMARY KEY NOT NULL,PASSWORD TEXT NOT NULL)")
    # use 'primary key' keyword for unique entry

    Cursor.execute("INSERT INTO Useraccount (USERNAME,PASSWORD)VALUES(?,?)",
                        ("admin","admin"))

    db.commit()
    Cursor.close()
    db.close()
'''''''''''''''''
#----------------------------------------------------FOR ABOUT MENU ---------------------------------------------------------------
class About:
    def About_Us(self):
        win_Aboutus=Tk()
        win_Aboutus.title("About Us")
        win_Aboutus.geometry("700x600+420+120")
        win_Aboutus.maxsize(width=500, height=500)
        win_Aboutus.configure(background="grey")
        win_Aboutus.resizable(0,0)



        self.frame = Frame(win_Aboutus, width=700, height=40, background="grey")
        self.frame.pack()

        self.space=Label(self.frame,text=":::::::ABOUT US::::::::",bg="lightblue")
        self.space.grid(row=1,column=0,pady=19)

        self.T = ScrolledText(self.frame, width=50, height=25)
        self.T.insert(END, "")
        self.T.grid(row=3, columnspan=1)


        file=open("AboutUs.txt","r")
        self.T.insert(END,file.read())
        file.close()

        win_Aboutus.mainloop()


    def About_Software(self):
        win_Aboutus = Tk()
        win_Aboutus.title("About Software")
        win_Aboutus.geometry("700x600+420+120")
        win_Aboutus.maxsize(width=500, height=500)
        win_Aboutus.configure(background="grey")
        win_Aboutus.resizable(0, 0)

        self.frame = Frame(win_Aboutus, width=700, height=40, background="grey")
        self.frame.pack()

        self.space = Label(self.frame, text=":::::::ABOUT SOFTWARE::::::::", bg="lightblue")
        self.space.grid(row=1, column=0, pady=19)

        self.T = ScrolledText(self.frame, width=50, height=25)
        self.T.insert(END, "")
        self.T.grid(row=3, columnspan=1)

        file = open("AboutSoftware.txt", "r")
        self.T.insert(END, file.read())
        file.close()

        win_Aboutus.mainloop()







#Authorization()


win=Tk()
w, h = win.winfo_screenwidth(), win.winfo_screenheight()


# use the next line if you also want to get rid of the titlebar
win.overrideredirect(1)
win.geometry("%dx%d+0+0" % (w, h))

#win.geometry('500x450+90+90')
win.title("APPLICATION_SOFTWARE")

    #win.maxsize(width=2400,height=900)
Title_Label=Label(win,text="APPLICATION SOFTWARE",font=("gothic",20,"underline"),bg="#008000",width="100")
Title_Label.pack()
Title_line=Label(win,text=("==============================[  {}  ]::::::::::::::::::[  {}   ]==========================".format(datetime.datetime.now().strftime("%Y-%m-%d-----%H hr:%M min"),datetime.date.today().strftime("%A"))),font=("gothic",10,"bold"),fg="red",bg="lightblue",width="190")
Title_line.pack()

Main_Body=Body(win)

Records = Record()

Aboutus=About()

menu_bar=Menu_Bar(win,Main_Body)


win.mainloop()





