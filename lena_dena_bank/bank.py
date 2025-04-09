import tkinter
from customtkinter import * #pip install customtkinter
from PIL import Image , ImageTk #pip install Pillow
from tkcalendar import DateEntry #pip install tkcalendar
from tkinter import messagebox as msg
from datetime import datetime as dt
from random import randint as rint
import os

class server():

    def __init__(self):
        if( not os.path.exists("server")):
            os.mkdir("server")
        self.main_server = {}
        self.new_user_details = ["","","","","","",[]]
        self.logged_account = "0"
        self.logged_user_details = ["Golu kumar","13/12/12","1","7739652381","1111","5700",[]]
        self.transfer_user_details = ["","","","","","",[]] 

    def add_new_user(self, name , dob , gender , pnum, pin ):
        self.new_user_details = ["","","","","","",[]]
        self.new_user_details[0] = name
        self.new_user_details[1]=dob
        self.new_user_details[2]=gender
        self.new_user_details[3] =pnum
        self.new_user_details[4] = str(pin)
        transaction_list = []
        self.new_user_details[6] =transaction_list
    
class gui_pages:

    def __init__(self):
        self.main_frame = CTkFrame(root)
        self.login_frame = CTkFrame(root)
        self.signin_frame = CTkFrame(root)
        self.sign_next_frame = CTkFrame(root)
        self.dashboard = CTkFrame(root)

    def log_back_sign(self):
        self.signin_frame.destroy()
        root.update
        self.create_loginpage()
        
    def sign_final_dashboard(self):
        self.sign_next_frame.destroy()
        root.update()
        self.create_loginpage()
    
    def log_to_dashboard(self):
        self.login_frame.destroy()
        root.update()
        self.create_dashboard()

    # function for creating the main page----------------------------------------
    def create_mainpage(self):

        self.main_frame = CTkFrame( root , width=799, height=533, corner_radius=5, bg_color="white" , fg_color="white" , border_width=2)

        mainpage_image = CTkImage(dark_image= Image.open("images\mainpage.png") , size= (799 , 533))
        mainpage_lbl = CTkLabel(self.main_frame, image=mainpage_image , text="").pack()

        # adding text label on main page 
        label_list = ["Welcome to Lena Dena Bank.","your every transaction is" ,"special for us.", "Now make your banking", "experience seamless and","simply the best...."]
        y_pos = 200

        for i in label_list:
            CTkLabel( self.main_frame, text=i , font=("lucida" , 18), text_color= "#4B4B4B", fg_color="transparent" ).place( x = 35, y = y_pos)
            y_pos += 28

        # adding button on the main page
        CTkButton(self.main_frame, cursor="hand2",width= 150 , height= 50 , fg_color="#766bff", text= "Get started>" , text_color="white" , font=("lucida" , 18 , "bold"),corner_radius=25, hover_color="#554dc9" , command= self.create_loginpage).place( x = 35, y = 400)

        self.main_frame.pack(expand = True)

    # creating login page----------------------------------------------------------------
    def create_loginpage(self):

        def verify_log_details():
            ac = ac_num.get()
            pn = ac_pin.get()
            if(len(ac) > 6 or len(ac) < 6):
                msg.showerror("Error","Please enter valid Account Number!")
            elif( len(pn) > 4 or len(pn) < 4):
                msg.showerror("Error","Please enter valid pin!")
            elif( tc_var.get() == 0):
                msg.showerror("Error", "Please agree all the terms and conditions!")
            else:
                try:
                    ac = int(ac)
                    try:
                       pn = int(pn)
                       verified = check_login_details(ac, pn)
                       if( verified):
                           self.log_to_dashboard()
                    except Exception:
                        msg.showerror("Error","Please enter correct Pin!")
                except Exception:
                    msg.showerror("Error","Please enter valid Account Number!")
            
        ac_num = StringVar()
        ac_pin = StringVar()
        tc_var = IntVar()

        self.login_frame = CTkFrame( root , width=800, height=534, corner_radius=5, bg_color="white" , fg_color="white" , border_width=0)

        colorbox = CTkFrame(master= self.login_frame , width= 320 , height= 534, fg_color= "#766bff" , border_width=0 , corner_radius= 0).place(x = 0, y = 0)
        
        mainlogo = CTkImage(dark_image= Image.open("images\mainlogo.png") , size= (320 , 180))
        mainlogo_lbl = CTkLabel(self.login_frame, image=mainlogo , text="").place(x=0,y=0)

        # adding label in login page
        label_list = ["Our services are fast and reliable","with a 24x7 customer support" ,"which helps you at any time you", "need.", " ","Toll Free Number :", "011255353, 21213214"]
        y_pos = 150

        for i in label_list:
            CTkLabel( self.login_frame, text=i , font=("lucida" , 15), text_color= "white", fg_color="#766bff" , bg_color= "#766bff").place( x = 35, y = y_pos)
            y_pos += 28

        CTkLabel( master= self.login_frame , text= "" , width= 280, height= 0.5, fg_color= "white" , bg_color="white", font=("lucida", 1)).place(x = 20, y=375)

        CTkLabel( self.login_frame, text="New User?" , font=("lucida" , 20, "bold"), text_color= "white", fg_color="#766bff" , bg_color= "#766bff").place( x = 110, y = 400)

        CTkButton(self.login_frame, cursor="hand2",width= 150 , height= 50 , fg_color="white",bg_color="#766bff",text= "Open Account" , text_color="black" , font=("lucida" , 18 , "bold"),corner_radius=25, hover_color="#d6d6d6" , command=self.create_signinpage).place( x = 70, y = 440)

        #creating login form
        usericon = CTkImage(dark_image= Image.open("images\\usericon.png"), size=(75 , 75))

        CTkLabel(self.login_frame, image=usericon , text="").place(x= 390,y=50)

        CTkLabel( self.login_frame, text="Login to" , font=("lucida" , 28, "bold"), text_color= "black",).place( x = 480, y = 55)

        CTkLabel( self.login_frame, text="Internet Banking" , font=("lucida" , 28, "bold"), text_color= "black",).place( x = 480, y = 90)

        CTkLabel( self.login_frame, text="Account Number :" , font=("lucida" , 18, "bold"), text_color= "gray",).place( x = 400, y = 150)

        CTkLabel( self.login_frame, text="Pin / Password :" , font=("lucida" , 18, "bold"), text_color= "gray",).place( x = 400, y = 250)

        acc_num = CTkEntry(master=self.login_frame , width=230 , height= 50, fg_color="#E5E5E5" , corner_radius= 15, border_width=0, text_color="black", font=("Agency" , 20), textvariable= ac_num).place(x = 400 , y = 180)

        pin = CTkEntry(master=self.login_frame , width=230 , height= 50, fg_color="#E5E5E5" , corner_radius= 15, border_width=0, text_color="black", font=("Agency" , 20), textvariable= ac_pin).place(x = 400 , y = 280)

        CTkCheckBox( self.login_frame , fg_color="#776bbf" , text="I hereby agree all the terms and conditions" , font=('lucida', 13) , text_color= "gray", variable= tc_var).place( x = 400, y= 345)

        CTkButton(self.login_frame, cursor="hand2",width= 150 , height= 50 , fg_color="#766bff",text= "Login" , text_color="white" , font=("lucida" , 20 , "bold"),corner_radius=25, hover_color="#554dc9", command= verify_log_details).place( x = 400, y = 390)

        CTkLabel( self.login_frame, text="*Please do not share your login credentials" , font=("lucida" , 14, "bold"), text_color= "red").place( x = 400, y = 470)
                 
        self.main_frame.destroy()
        root.update()   
        self.login_frame.pack(expand = True)      

    # creating signin page-------------------------------------------------------------------------
    def create_signinpage(self):

        def verify_details(*args):
            if(len(username.get()) < 1):
                msg.showerror("Error","Please enter your name!")
            elif(len(self.fdate) < 1):
                msg.showerror("Error","Please enter your Date of birth!")
            elif(gender.get() == 0):
                msg.showerror("Error","Please select your gender!")
            elif( len(pnum.get()) < 5):
                msg.showerror("Error","Please enter a valid phone number")
            elif( pin.get() != cpin.get()):
                msg.showerror("Error","Pin doesnot match!")
            elif( len(pin.get()) != 4):
                msg.showerror("Error","Pin should be of 4 digits")
            else:
                try:
                    p = int(pin.get())
                    if(tc.get() == 1):
                        check_signup_submit(username.get(), self.fdate, gender.get(), pnum.get(), p )
                        self.sign_next()
                    else:
                        msg.showerror("Error","Please agree all terms and conditions!")
                except Exception:
                    msg.showerror("Error","Pin should be a number!")
 
        def get_dob(*args):
            sdate = dob.get().split('/')
            if( len(sdate) > 2):
               self.fdate = f"{sdate[1]}-{sdate[0]}-{sdate[2]}"
            else: self.fdate = dob.get()

            date_label = CTkLabel(master=self.signin_frame , text_color="black", font=("Agency" , 18), text= self.fdate + "     ", width= 220, height= 42, fg_color="#E5E5E5" , corner_radius= 5).place(x = 31 , y = 271) 

        #creating variable
        username = StringVar() 
        gender = IntVar()
        dob = StringVar()
        pnum = StringVar()
        pin = StringVar()
        cpin = StringVar()
        tc = IntVar()
        self.fdate = ""

        # creating frame
        self.signin_frame = CTkFrame( root , width=800, height=534, corner_radius=5, bg_color="white" , fg_color="white" , border_width=0)

        CTkButton(self.signin_frame, cursor="hand2",width= 50, height= 50 , fg_color="#766bff",text= "❌" , text_color="white" , font=("lucida" , 12 , "bold"),corner_radius=0, hover_color="#766bff", command= self.log_back_sign).place( x = 750, y = 0)

        # signup form
        usericon = CTkImage(dark_image= Image.open("images\\usericon.png"), size=(65 , 65))

        CTkLabel(self.signin_frame, image=usericon , text="").place(x= 30,y=60)

        CTkLabel( self.signin_frame, text="Internet Banking" , font=("lucida" , 22, "bold"), text_color= "black",).place( x = 100, y = 70)

        CTkLabel( self.signin_frame, text="New User Registration" , font=("lucida" , 22, "bold"), text_color= "gray",).place( x = 100, y = 95)

        CTkLabel( self.signin_frame, text="Account Holder Name :" , font=("lucida" , 16, "bold"), text_color= "gray",).place( x = 30, y = 150)

        CTkLabel( self.signin_frame, text="Date of Birth :" , font=("lucida" , 16, "bold"), text_color= "gray",).place( x = 30, y = 235)
        
        CTkLabel( self.signin_frame, text="Gender :" , font=("lucida" , 16, "bold"), text_color= "gray",).place( x = 30, y = 325)

        CTkLabel( self.signin_frame, text="Phone Number :" , font=("lucida" , 16, "bold"), text_color= "gray",).place( x = 30, y = 395)

        CTkEntry(master=self.signin_frame , width=250 , height= 45, fg_color="#E5E5E5" , corner_radius= 12, border_width=0, text_color="black", font=("Agency" , 18), textvariable = username).place(x = 30 , y = 180)

        date_picker = DateEntry(self.signin_frame, selectmode ='day', font= ("lucida" , 25),fg_color = "gray", corner_radius = 5, text_color = "gray",textvariable = dob).place(x = 30 , y = 270)

        date_label = CTkLabel(master=self.signin_frame , text_color="gray", font=("Agency" , 16), text="DD/MM/YYYY", width= 220, height= 42, fg_color="#E5E5E5" , corner_radius= 5).place(x = 31 , y = 271)
        dob.trace('w', get_dob)

        CTkRadioButton( self.signin_frame , text= "Male", text_color= "gray" , font= ("lucida" , 15) , fg_color= "#776bff" , variable= gender, value= 1).place( x = 30 , y=360)

        CTkRadioButton( self.signin_frame , text= "Female", text_color= "gray" , font= ("lucida" , 15), fg_color="#776bff", variable= gender, value=2).place( x = 130 , y=360)

        CTkEntry(master=self.signin_frame , width=250 , height= 45, fg_color="#E5E5E5" , corner_radius= 12, border_width=0, text_color="black", font=("Agency" , 18), textvariable= pnum).place(x = 30 , y = 425)

        CTkLabel( self.signin_frame, text="-- Generate PIN --" , font=("lucida" , 19, "bold"), text_color= "black",).place( x =380, y = 150)

        CTkLabel( self.signin_frame, text="Enter 4-digit PIN :" , font=("lucida" , 16, "bold"), text_color= "gray",).place( x = 380, y = 185)

        CTkLabel( self.signin_frame, text="Confirm PIN :" , font=("lucida" , 16, "bold"), text_color= "gray",).place( x = 380, y = 280)

        CTkEntry(master=self.signin_frame , width=250 , height= 45, fg_color="#E5E5E5" , corner_radius= 12, border_width=0, text_color="black", font=("Agency" , 18), placeholder_text="xx-xx", textvariable= pin).place(x = 380 , y = 215)

        CTkEntry(master=self.signin_frame , width=250 , height= 45, fg_color="#E5E5E5" , corner_radius= 12, border_width=0, text_color="black", font=("Agency" , 18), textvariable= cpin, placeholder_text="xx-xx").place(x = 380 , y = 310)

        CTkCheckBox( self.signin_frame , fg_color="#776bbf" , text="I hereby agree all the terms and conditions" , font=('lucida', 13) , text_color= "gray", variable= tc).place( x = 380, y= 365)

        CTkButton(self.signin_frame, cursor="hand2",width= 150 , height= 50 , fg_color="#766bff",text= "Next" , text_color="white" , font=("lucida" , 20 , "bold"),corner_radius=25, hover_color="#554dc9", command=verify_details).place( x = 380, y = 410) 

        CTkLabel( self.signin_frame, text="*Please do not share your login credentials" , font=("lucida" , 14, "bold"), text_color= "red").place( x = 380, y = 490)

        self.login_frame.destroy()
        root.update()
        self.signin_frame.pack(expand = True)

    # creating signup verification page--------------------------------------------------------------
    def sign_next(self): 

        def confirm_submit():
            try:
                value = int(d_var.get())
                if value == 0:
                    msg.showerror("Error" , "Please enter a deposit amount!")
                elif value < 500:
                    msg.showerror("Error" , "Deposit amount should not be less than 500!")
                else:
                    check_signup_final(acc_num, value)
                    self.sign_final_dashboard()
            except Exception:
                msg.showerror("Error", "Please enter a valid amount!")
   
        acc_num = get_acc_num()
        d_var = StringVar()

        self.sign_next_frame = CTkFrame( root , width=800, height=534, corner_radius=5, bg_color="white" , fg_color="white" , border_width=0)

        sign_next_image = CTkImage(dark_image= Image.open("images\signnext.png") , size= (799 , 533))

        sign_next_img_lbl = CTkLabel(self.sign_next_frame, image=sign_next_image , text="").pack() 

        # confirmation page 
        confirm_frame = CTkFrame(self.sign_next_frame, width= 400, height= 400, bg_color= "transparent" , fg_color="white",  border_color= "gray" , border_width= 1).place( x = 200, y = 67)

        CTkLabel( self.sign_next_frame, text="✅                     " , font=("lucida" , 32, "bold"), text_color= "white",fg_color="#766bff" , bg_color="white", height= 100, width= 400).place( x = 200, y = 67)

        CTkLabel( self.sign_next_frame, text="SUCCESS" , font=("lucida" , 35, "bold"), text_color= "white",fg_color="#766bff" , bg_color="white").place( x = 340, y = 100)

        CTkLabel( self.sign_next_frame, text="Account created Successfully!" , font=("lucida" , 22 ), text_color= "black",bg_color="white").place( x = 250, y = 190)

        CTkLabel( self.sign_next_frame, text=f"  A/c Number : {acc_num[0:2]}-{acc_num[2:]} " , font=("lucida" , 25 ), text_color= "white",bg_color="white" , fg_color="lightgreen", height= 50).place( x = 200, y = 235)

        CTkLabel( self.sign_next_frame, text="Deposit Amount : " , font=("lucida" , 17 ), text_color= "gray",bg_color="white" , height= 50).place( x = 220, y = 295)

        d_amount = CTkEntry(master=self.sign_next_frame , width=230 , height= 45, fg_color="#E5E5E5" , corner_radius= 8, border_width=0, text_color="black", font=("Agency" , 16), placeholder_text="Amount", textvariable = d_var).place(x = 220 , y = 335)

        CTkButton(self.sign_next_frame, cursor="hand2",width= 130 , height= 50 , fg_color="#766bff",text= "Done" , text_color="white" , font=("lucida" , 20 , "bold"),corner_radius=25, hover_color="#554dc9", command=confirm_submit).place( x = 430, y = 390)

        self.signin_frame.destroy()
        root.update()
        self.sign_next_frame.pack(expand = True)

    def create_dashboard(self):

        self.dashboard = CTkFrame( root , width=800, height=534, corner_radius=5, bg_color="white" , fg_color="white" , border_width=0)

        self.acc_frame = CTkFrame(master= self.dashboard , width= 580 , height= 534, fg_color= "white" , border_width=0 , corner_radius= 0)

        self.service_frame = CTkFrame(master= self.dashboard , width= 580 , height= 534, fg_color= "white" , border_width=0 , corner_radius= 0)

        self.transfer_frame = CTkFrame(master= self.dashboard , width= 580 , height= 534, fg_color= "white" , border_width=0 , corner_radius= 0)

        self.record_frame = CTkFrame(master= self.dashboard , width= 580 , height= 534, fg_color= "white" , border_width=0 , corner_radius= 0)

        # creating accounts frame:
        def create_account_frame():
            self.acc_frame = CTkFrame(master= self.dashboard , width= 580 , height= 534, fg_color= "white" , border_width=0 , corner_radius= 0)

            CTkLabel( self.acc_frame, text="Welcome" , font=("lucida" , 18 ), text_color= "gray",bg_color="white" , height= 50).place(x = 20, y = 15)

            CTkLabel( self.acc_frame, text= get_logged_details(0), font=("lucida" , 25,"bold" ), text_color= "black",bg_color="white" , height= 50).place(x = 20, y = 50)

            CTkLabel( self.acc_frame, text="$" + get_logged_details(5)+".00", font=("lucida" , 37, "bold" ), text_color= "#00bf63",fg_color="#e6e4ff" , height= 100 , width= 500, corner_radius= 5).place(x = 40, y = 105)

            CTkLabel( self.acc_frame, text="Your Balance :", font=("lucida" , 18 ), text_color= "black",bg_color="#e6e4ff" , height= 50).place(x = 55, y = 105)

            CTkLabel( self.acc_frame, text="👤Account Details :" , font=("lucida" , 18 ), text_color= "gray",bg_color="white" , height= 50).place(x = 20, y = 210)

            CTkLabel( self.acc_frame, text="Account Holder Name :", font=("lucida" , 18 ), text_color= "black",bg_color="white" , height= 50).place(x = 20, y = 260)

            CTkLabel( self.acc_frame, text="Date of Birth :", font=("lucida" , 18 ), text_color= "black",bg_color="white" , height= 50).place(x = 20, y = 310)

            CTkLabel( self.acc_frame, text="Gender :", font=("lucida" , 18 ), text_color= "black",bg_color="white" , height= 50).place(x = 20, y = 360)

            CTkLabel( self.acc_frame, text="Phone Number :", font=("lucida" , 18 ), text_color= "black",bg_color="white" , height= 50).place(x = 20, y = 410)

            CTkLabel( self.acc_frame, text= get_logged_details(0), font=("lucida" , 21,"bold" ), text_color= "black",bg_color="white" , height= 50).place(x = 220, y = 260)

            CTkLabel( self.acc_frame, text=get_logged_details(1), font=("lucida" , 21,"bold" ), text_color= "black",bg_color="white" , height= 50).place(x = 220, y = 310)

            CTkLabel( self.acc_frame, text= "Male"if(get_logged_details(2) == '1')else"Female", font=("lucida" , 21 ,"bold"), text_color= "black",bg_color="white" , height= 50).place(x = 220, y = 360)

            CTkLabel( self.acc_frame, text=get_logged_details(3), font=("lucida" , 21,"bold" ), text_color= "black",bg_color="white" , height= 50).place(x = 220, y = 410)

            CTkLabel(self.acc_frame, text= "", bg_color="white", fg_color="#766bff" , width= 50, height= 50, corner_radius= 50).place( x = -32, y = 150)

            self.acc_frame.place(x = 220, y= 0)

        #creating services frame----------------

        #creating services functions-

        def deposit_func(deposit_ac, deposit_amt):

            if( len(deposit_ac) != 6 ): 
                msg.showerror("Error" , "Please enter valid account number")
            elif deposit_ac != get_logged_details(7777):
                msg.showerror("Error" , "Account Number didnot match.")

            elif ( len(deposit_amt) < 1 ):
                msg.showerror("Error" , "Please enter valid amount.")
            else :
                try:
                    amount = int(deposit_amt)
                    if( amount < 1):
                        msg.showerror("Error" , "Amount should be greater than 0")
                    else:
                        deposit_update(amount)
                        msg.showinfo("Success" , "Your Deposit request has been completed!")
                        self.service_frame.destroy()
                        root.update()
                        create_service_frame()
                        create_deposit_frame()
                
                except Exception:
                    msg.showerror("Error" , "Invalid Amount!")


        def withdraw_func(withdraw_amt = "", withdraw_pin = ""):
            if( len(withdraw_amt) < 1 ): 
                msg.showerror("Error" , "Please enter valid amount!") 

            elif len(withdraw_pin) != 4 or withdraw_pin != get_logged_details(4):
                msg.showerror("Error" , "Invalid Transaction Pin!")
            else :
                try:
                    amount = int(withdraw_amt)
                    if( amount < 1):
                        msg.showerror("Error" , "Amount should be greater than 0")
                    elif amount > int(get_logged_details(5)) :
                        msg.showerror("Error" , "Insufficient Balance!")

                    else:
                        withdraw_update(amount)
                        msg.showinfo("Success" , "Your Withdrawal request has been completed!")
                        self.service_frame.destroy()
                        root.update()
                        create_service_frame()
                        create_withdraw_frame()
                
                except Exception:
                    msg.showerror("Error" , "Invalid Amount!")

        def transfer_func(t_ac , t_pin, t_amt):
            if( len(t_ac) != 6):
                msg.showerror("Error" , "Invalid Account Number!")
            elif t_ac == get_logged_details(7777):
                msg.showerror("Error" , "Could not transfer to same account. Enter another account number to continue!")
            elif(len(t_pin) != 4):
                msg.showerror("Error" , "Invalid Transaction Pin!")
            elif( len(t_amt) < 1):
                msg.showerror("Error", "Please enter the amount!")
            else:
                try:
                    s_ac = int(t_ac)
                    s_pin = int(t_pin)
                    s_amt = int(t_amt)
                    transfer_money(s_ac, s_pin, s_amt)
                except Exception:
                    msg.showerror("Error" , "Please Enter valid details! and Try Again")
                
                create_transfer_frame()

        def create_service_frame():

            self.service_frame = CTkFrame(master= self.dashboard , width= 580 , height= 534, fg_color= "white" , border_width=0 , corner_radius= 0)

            self.withdraw_frame = CTkFrame( self.service_frame , width=440, height=340, corner_radius=5, bg_color="white" , fg_color="white" , border_width=0)

            self.deposit_frame = CTkFrame( self.service_frame , width=440, height=340, corner_radius=5, bg_color="white" , fg_color="white" , border_width=0)

            CTkLabel(self.service_frame, text= "", bg_color="white", fg_color="#766bff" , width= 50, height= 50, corner_radius= 50).place( x = -32, y = 220) 

            CTkLabel( self.service_frame, text="Banking Services" , font=("lucida" , 22), text_color= "black",bg_color="white" , height= 50).place(x = 20, y = 15)

            CTkLabel( self.service_frame, text="   $" + get_logged_details(5)+".00", font=("lucida" , 37, "bold" ), text_color= "#00bf63",fg_color="#f4f4f4" , height= 60 , width= 400, corner_radius= 5).place(x = 190, y = 80)

            CTkLabel( self.service_frame, text="Balance :", font=("lucida" , 18 ), text_color= "black",bg_color="#f4f4f4" , height= 30).place(x = 196, y = 80)

            create_withdraw_frame()
            
            self.service_frame.place(x = 220, y= 0)


        def create_withdraw_frame():

            self.deposit_frame.destroy()
            withdraw_amt = StringVar()
            withdraw_pin = StringVar()

            self.withdraw_frame = CTkFrame( self.service_frame , width=440, height=340, corner_radius=5, bg_color="white" , fg_color="white" , border_width=0)

            CTkLabel( self.withdraw_frame, text= "" , fg_color= "#766bff", width= 440, height=2, font= ("lucida", 2)).place(x = 0, y= 50) 

            CTkLabel( self.withdraw_frame, text="💸 Withdraw", font=("lucida" , 25, "bold" ), text_color= "black",fg_color="#e6e4ff" , height= 50 , width= 220, corner_radius= 2).place(x = 0, y = 0)

            CTkButton(self.withdraw_frame, cursor="hand2",width= 200 , height= 48 , fg_color="#817bcd",bg_color="white",text= "💰 Deposit" , text_color="white" , font=("lucida" , 19 , "bold"),corner_radius=5, hover_color="#554dc9", command= create_deposit_frame).place( x = 230, y = 0)

            CTkLabel( self.withdraw_frame, text="Withdraw Amount : " , font=("lucida" , 17 ), text_color= "gray",bg_color="white" , height= 50).place( x = 0, y = 60)

            CTkEntry(self.withdraw_frame, width=230 , height= 45, fg_color="#E5E5E5" , corner_radius= 8, border_width=0, text_color="black", font=("Agency" , 16), textvariable= withdraw_amt).place(x = 0 , y = 105)

            CTkLabel( self.withdraw_frame, text="Transaction Pin : " , font=("lucida" , 17 ), text_color= "gray",bg_color="white" , height= 50).place( x = 0, y = 155)

            CTkEntry(self.withdraw_frame, width=230 , height= 45, fg_color="#E5E5E5" , corner_radius= 8, border_width=0, text_color="black", font=("Agency" , 16), textvariable= withdraw_pin).place(x = 0 , y = 190)

            CTkButton(self.withdraw_frame, cursor="hand2",width= 190 , height= 50 , fg_color="lightgreen",text= "Withdraw" , text_color="white" , font=("lucida" , 20 , "bold"),corner_radius=25, hover_color="green", command= lambda: withdraw_func(withdraw_amt.get(), withdraw_pin.get())).place( x = 125, y = 275)

            self.withdraw_frame.place( x = 70, y = 170)

        def create_deposit_frame():

            self.withdraw_frame.destroy()
            deposit_ac = StringVar()
            deposit_amt = StringVar()

            self.deposit_frame = CTkFrame( self.service_frame , width=440, height=340, corner_radius=5, bg_color="white" , fg_color="white" , border_width=0)

            CTkLabel( self.deposit_frame, text= "" , fg_color= "#766bff", width= 440, height=2, font= ("lucida", 2)).place(x = 0, y= 50) 
            
            CTkButton(self.deposit_frame, cursor="hand2",width= 200 , height= 48 , fg_color="#817bcd",bg_color="white",text= "💸 Withdraw" , text_color="white" , font=("lucida" , 19 , "bold"),corner_radius=5, hover_color="#554dc9", command= create_withdraw_frame).place(x = 10, y = 0)

            CTkLabel( self.deposit_frame, text="💰 Deposit", font=("lucida" , 25, "bold" ), text_color= "black",fg_color="#e6e4ff" , height= 50 , width= 220, corner_radius= 2).place(x = 230, y = 0)

            CTkLabel( self.deposit_frame, text="Account Number : " , font=("lucida" , 17 ), text_color= "gray",bg_color="white" , height= 50).place( x = 0, y = 60)

            CTkEntry(self.deposit_frame, width=230 , height= 45, fg_color="#E5E5E5" , corner_radius= 8, border_width=0, text_color="black", font=("Agency" , 16), textvariable= deposit_ac).place(x = 0 , y = 105)

            CTkLabel( self.deposit_frame, text="Deposit Amount : " , font=("lucida" , 17 ), text_color= "gray",bg_color="white" , height= 50).place( x = 0, y = 155)

            CTkEntry(self.deposit_frame, width=230 , height= 45, fg_color="#E5E5E5" , corner_radius= 8, border_width=0, text_color="black", font=("Agency" , 16), textvariable= deposit_amt).place(x = 0 , y = 190)

            CTkButton(self.deposit_frame, cursor="hand2",width= 190 , height= 50 , fg_color="skyblue",text= "Deposit" , text_color="white" , font=("lucida" , 20 , "bold"),corner_radius=25, hover_color="#38b6ff", command= lambda: deposit_func(deposit_ac.get() , deposit_amt.get())).place( x = 125, y = 275)

            self.deposit_frame.place(x = 70 , y = 170)

        # creating fund transfer frame
        def create_transfer_frame():

            transfer_ac = StringVar()
            transfer_amt = StringVar()
            transfer_pin = StringVar()

            self.transfer_frame = CTkFrame(master= self.dashboard , width= 580 , height= 534, fg_color= "white" , border_width=0 , corner_radius= 0)

            CTkLabel(self.transfer_frame, text= "", bg_color="white", fg_color="#766bff" , width= 50, height= 50, corner_radius= 50).place( x = -35, y = 290) 

            CTkLabel( self.transfer_frame, text="Online Fund Transfer" , font=("lucida" , 22, "bold"), text_color= "black",bg_color="white" ,fg_color="lightgreen", height= 50, width= 530).place(x = 20, y = 15)

            CTkLabel( self.transfer_frame, text="Receiver Account Number : " , font=("lucida" , 17 ), text_color= "gray",bg_color="white" , height= 50).place( x = 60, y = 90)

            CTkEntry(self.transfer_frame, width=230 , height= 45, fg_color="#E5E5E5" , corner_radius= 8, border_width=0, text_color="black", font=("Agency" , 16), textvariable= transfer_ac).place(x = 60 , y = 135)

            CTkLabel( self.transfer_frame, text="Transfer Amount : " , font=("lucida" , 17 ), text_color= "gray",bg_color="white" , height= 50).place( x = 60, y = 195)

            CTkEntry(self.transfer_frame, width=230 , height= 45, fg_color="#E5E5E5" , corner_radius= 8, border_width=0, text_color="black", font=("Agency" , 16), textvariable= transfer_amt).place(x = 60 , y = 235)

            CTkLabel( self.transfer_frame, text="Transaction Pin : " , font=("lucida" , 17 ), text_color= "gray",bg_color="white" , height= 50).place( x = 60, y = 295)

            CTkEntry(self.transfer_frame, width=230 , height= 45, fg_color="#E5E5E5" , corner_radius= 8, border_width=0, text_color="black", font=("Agency" , 16), textvariable= transfer_pin).place(x = 60 , y = 335)

            CTkButton(self.transfer_frame, cursor="hand2",width= 250 , height= 50 , fg_color="#766bff",text= "Transfer" , text_color="white" , font=("lucida" , 20 , "bold"),corner_radius=25, hover_color="#554dc9", command= lambda: transfer_func(transfer_ac.get() , transfer_pin.get(), transfer_amt.get())).place( x = 155, y = 405)

            self.transfer_frame.place(x = 220, y= 0)

        def create_record_frame():

            records = get_logged_details(6)
            self.record_frame = CTkFrame(master= self.dashboard , width= 580 , height= 534, fg_color= "white" , border_width=0 , corner_radius= 0)

            CTkLabel(self.record_frame, text= "", bg_color="white", fg_color="#766bff" , width= 50, height= 50, corner_radius= 50).place( x = -35, y = 360) 

            CTkLabel( self.record_frame, text="All Transactions" , font=("lucida" , 20, "bold"), text_color= "white",bg_color="white" ,fg_color="#817bcd", height= 50, width= 530).place(x = 20, y = 15)

            rec_box = tkinter.Listbox(self.record_frame, width= 47, height= 16, font=("lucida" , 14), border= None, borderwidth= 0, selectbackground="grey" , highlightcolor="grey", highlightthickness=0, highlightbackground="grey")

            for i in records:
                rec_box.insert(END, i )
                rec_box.insert(END, "" )
            rec_box.place(x = 28 , y = 75)

            self.record_frame.place(x = 220, y= 0)

        CTkFrame(master= self.dashboard , width= 220 , height= 534, fg_color= "#766bff" , border_width=0 , corner_radius= 0).place(x = 0, y = 0)

        mainlogo = CTkImage(dark_image= Image.open("images\mainlogo.png") , size= (220 , 130))
        mainlogo_lbl = CTkLabel(self.dashboard, image=mainlogo , text="").place(x=0,y=0)

        def change_dashboard_frame(frame):
            if( frame == "out"):
                if( msg.askokcancel("Quit","Do you want to logout!")):
                    check_signup_final(get_logged_details(7777),-1)
                    self.dashboard.destroy()
                    self.create_loginpage()
                return
            
            self.acc_frame.destroy()
            self.service_frame.destroy()
            self.transfer_frame.destroy()
            self.record_frame.destroy()
            ser_frame_btn.configure(text_color = "white" , fg_color = "#766bff")
            acc_frame_btn.configure(text_color = "white" , fg_color = "#766bff")
            trf_frame_btn.configure(text_color = "white" , fg_color = "#766bff")
            rec_frame_btn.configure(text_color = "white" , fg_color = "#766bff")

            if( frame == "ser"):
                create_service_frame()
                ser_frame_btn.configure(text_color = "black", fg_color = "white")
            elif( frame == "acc"):
                acc_frame_btn.configure(text_color = "black", fg_color = "white")
                create_account_frame()
            elif( frame == "trf"):
                trf_frame_btn.configure(text_color = "black", fg_color = "white")
                create_transfer_frame()
            elif( frame == "rec"):
                rec_frame_btn.configure(text_color = "black", fg_color = "white")
                create_record_frame()

        # creating menu buttons
        acc_frame_btn = CTkButton(self.dashboard, cursor="hand2",width= 130 , height= 50 , fg_color="white",bg_color="#766bff",text= "👤 Accounts       " , text_color="black" , font=("lucida" , 18 , "bold"),corner_radius=25, hover_color="#554dc9", command= lambda: change_dashboard_frame("acc"))
        acc_frame_btn.place( x = 15, y = 150)

        ser_frame_btn = CTkButton(self.dashboard, cursor="hand2",width= 130 , height= 50 , fg_color="#766bff",bg_color="#766bff",text= "⚙️ Services       " , text_color="white" , font=("lucida" , 18 , "bold"),corner_radius=25, hover_color="#554dc9", command= lambda: change_dashboard_frame("ser"))
        ser_frame_btn.place( x = 15, y = 220)

        trf_frame_btn = CTkButton(self.dashboard, cursor="hand2",width= 130 , height= 50 , fg_color="#766bff",bg_color="#766bff",text= "💸 Fund Transfer" , text_color="white" , font=("lucida" , 18 , "bold"),corner_radius=25, hover_color="#554dc9", command= lambda: change_dashboard_frame("trf"))
        trf_frame_btn.place( x = 13, y = 290)

        rec_frame_btn = CTkButton(self.dashboard, cursor="hand2",width= 130 , height= 50 , fg_color="#766bff",bg_color="#766bff",text= "↗️ Transactions" , text_color="white" , font=("lucida" , 18 , "bold"),corner_radius=25, hover_color="#554dc9", command= lambda: change_dashboard_frame("rec"))
        rec_frame_btn.place( x = 15, y = 360)

        lout_frame_btn = CTkButton(self.dashboard, cursor="hand2",width= 130 , height= 50 , fg_color="#766bff",bg_color="#766bff",text= "⛔ Log Out" , text_color="white" , font=("lucida" , 18 , "bold"),corner_radius=25, hover_color="#554dc9", command= lambda: change_dashboard_frame("out"))
        lout_frame_btn.place( x = 20, y = 430)

        create_account_frame()
        self.dashboard.pack(expand = True)

#global functions and variables --------------------------------------------------

def get_logged_details(n):
    if n == 7777 : return server.logged_account
    return server.logged_user_details[n]
               
def check_login_details(ac, pin):
    if not os.path.exists(f"server\{ac}.txt"):
        msg.showerror("Error", "Account not found! Try again.")
    else:
        server.logged_user_details = ["","","","","","", []]
        f = open(f"server\{ac}.txt", 'r')
        for i in range(6):
            line = f.readline()
            server.logged_user_details[i] = line[0:-1]
        while True:
            line = f.readline()
            if( line == ""): break
            server.logged_user_details[6].append(line[0:-1])
        
        if not server.logged_user_details[4] == str(pin):
            msg.showerror("Error", "Wrong pin or password!")
            return False
        else: 
            server.logged_account = f"{ac}"    
            return True     

def check_signup_submit(name , dob, gender , pnum, pin):
    server.add_new_user(name, dob, gender, pnum, pin)

def get_acc_num():
    acc_num = rint(100001, 999999)
    while os.path.exists(f"server\{acc_num}.txt") : acc_num = rint(100001, 999999)
    return str(acc_num)
    
def check_signup_final(acc_number , amount):
    if amount < 0:
        server.new_user_details = server.logged_user_details.copy()
    elif( amount > 0):
        server.new_user_details[5] = str(amount)
        trecord = str( dt.now()).split('.')[0] + "           Depoist            +  $ " + str(amount)
        server.new_user_details[6].insert(0, trecord)
    else:
        if acc_number == 0:
            if msg.askokcancel("Quit", "Do you want to quit?"):
                root.destroy()
                quit()
            else:
                return
        else: server.new_user_details = server.logged_user_details.copy()

    with open(f"server\{acc_number}.txt", 'w') as f:
        f.writelines(f"{server.new_user_details[0]}\n")
        f.writelines(f"{server.new_user_details[1]}\n")
        f.writelines(f"{server.new_user_details[2]}\n")
        f.writelines(f"{server.new_user_details[3]}\n")
        f.writelines(f"{server.new_user_details[4]}\n")
        f.writelines(f"{server.new_user_details[5]}\n")
        for lines in server.new_user_details[6]:
            f.writelines(f"{lines}\n")

    if( amount == 0):
        if msg.askokcancel("Quit", "Do you want to quit?"):
                root.destroy()
                quit()

# updating logged details -----------
def deposit_update(amount):
    server.logged_user_details[5] = str( int(server.logged_user_details[5]) + amount)

    dep_update = str( dt.now()).split('.')[0] + "           Depoist            +  $ " + str(amount)
    server.logged_user_details[6].insert(0, dep_update)

def withdraw_update(amount):
    server.logged_user_details[5] = str( int(server.logged_user_details[5]) - amount)

    wid_update = str( dt.now()).split('.')[0] + "           Withdraw          -  $ " + str(amount)
    server.logged_user_details[6].insert(0, wid_update)

def transfer_money( ac , pin , amount):
    if not os.path.exists(f"server\{ac}.txt"):
        msg.showerror("Failed", "Account not found! Try again.")

    elif( str(pin) != server.logged_user_details[4]):
        msg.showerror("Failed" , "Invalid Account transaction Pin! Try Again...")

    elif( amount > 0):
        if( amount > int(server.logged_user_details[5])):
            msg.showerror("Error", "Insufficient Balance!!")
            return
        server.transfer_user_details = ["","","","","","",[]] 
        f = open(f"server\{ac}.txt", 'r')
        for i in range(6):
            line = f.readline()
            server.transfer_user_details[i] = line[0:-1]
        while True:
            line = f.readline()
            if( line == ""): break
            server.transfer_user_details[6].append(line[0:-1])

        server.transfer_user_details[5] = str(amount + int(server.transfer_user_details[5]))

        trecord = str( dt.now()).split('.')[0] + "           Received           +  $ " + str(amount)
        srecord = str( dt.now()).split('.')[0] + "           Transfer           -  $ " + str(amount)
        server.transfer_user_details[6].insert(0, trecord)

        with open(f"server\{ac}.txt", 'w') as f:
            f.writelines(f"{server.transfer_user_details[0]}\n")
            f.writelines(f"{server.transfer_user_details[1]}\n")
            f.writelines(f"{server.transfer_user_details[2]}\n")
            f.writelines(f"{server.transfer_user_details[3]}\n")
            f.writelines(f"{server.transfer_user_details[4]}\n")
            f.writelines(f"{server.transfer_user_details[5]}\n")
            for lines in server.transfer_user_details[6]:
                f.writelines(f"{lines}\n")

        server.logged_user_details[6].insert(0, srecord)
        server.logged_user_details[5] = str(int(server.logged_user_details[5]) - amount)
        msg.showinfo("Fund Transfer", "Money Transfer Successfully!!")
    
    else:
        msg.showerror("Failed" , "Amount should be greater than 0! Try Again...")

root = CTk()
root.geometry("800x534")
# root.resizable(False, False)
root.config(bg="#202020")
root.title("Lena Dena Bank")
root.protocol("WM_DELETE_WINDOW", lambda: check_signup_final(int(server.logged_account), 0))

server = server()
pages = gui_pages()

pages.create_mainpage()

root.mainloop()

# <<--------------------------------------------------developer - Fendrick :)----------------------------------------------------------------------->>
