# So this is basically an app made from tkinter that will provide infromation about python and Full stack development created by RAJPUTRoCkStAr

from tkinter import *
import mysql.connector
from tkinter import messagebox
from PIL import Image, ImageTk
import webbrowser

def toggle_password_visibility():
    if show_password_var.get():
        entpass.config(show="")
    else:
        entpass.config(show="*")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="regiform"
)
mycursor = mydb.cursor()

if(mydb):
    print("connection established")
else:
    print("connection rejected")


def submitbutton():
    def check_data_exists(mycursor, table_name, column_name, value_to_check):
        query = f"SELECT 1 FROM {table_name} WHERE {column_name} = %s"
        mycursor.execute(query, (value_to_check,))
        data_exists = mycursor.fetchone() is not None
        mycursor.fetchall()
        return data_exists
   
    cname     = entname.get()
    cage      = entage.get()
    cgender   = entgender.get()
    cemail    = entemail.get()
    cpassword = entpass.get()
    cphone    = entphone.get()
    phone_number = "".join(filter(str.isdigit, cphone))
    
    table_name = 'customers'
    column_name = 'email'
    value_to_check = cemail

    if check_data_exists(mycursor, table_name, column_name, value_to_check):
        messagebox.showinfo(title='INFO BOX',message='This data is already exists you can go for login')
    else:
            loginwindow = Tk()
            loginwindow.title("RAJPUTRoCkStAr")
            window_width = 600
            window_height = 200
            screen_width = loginwindow.winfo_screenwidth()
            screen_height = loginwindow.winfo_screenheight()
            x_position = (screen_width - window_width) // 2
            y_position = (screen_height - window_height) // 2
            loginwindow.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
            loginwindow.configure(bg="#e6e6e6")
            thank_you_label = Label(loginwindow, text="Thank You For Registering!", font=("Arial", 30, "bold"), fg="#333333", bg="#ffd699")
            thank_you_label.pack(pady=50)
            sql = "INSERT INTO customers(name,age,gender,email,password,phone) VALUES(%s, %s, %s, %s, %s, %s)"
            mycursor.execute(sql, (cname, cage, cgender, cemail, cpassword, phone_number))
            mydb.commit()
            print(mycursor.rowcount, "record(s) inserted.")
    
    
    # mailing part to start from here
    
    
    import smtplib
    from email.mime.text import MIMEText
    server = smtplib.SMTP('smtp.gmail.com',587)
    def send_email(sender_email, sender_password, receiver_email, subject,body):
        try:
            message = MIMEText(body)
            message['Subject'] = subject
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            server.quit()
            print("Email sent successfully!")
        except :
            print("Error while sending email:")
    sender_email = 'luciferdevil565656@gmail.com'
    sender_password = 'rhmunlelmweijdup'
    receiver_email = entemail.get()
    subject = 'Thanks from RAJPUTRoCkStAr'
    body = 'This is email is sent to you because you have successfully registered with RAJPUTRoCkStAr\n\n Thanking you'
    send_email(sender_email, sender_password, receiver_email, subject,body)




def loginbutton():


    root =Tk()
    

    def thankyou():
        loemail = logemail.get()
        lopass = logipass.get()


        def check_user_credentials(email, password):
            try:
                mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="regiform"
                )
                cursor = mydb.cursor()

                query = "SELECT email, password FROM customers WHERE email = %s"
                cursor.execute(query, (loemail,))
                result = cursor.fetchone()


                if result and result[1] == lopass:
                    def open_link(event):
                        webbrowser.open("https://github.com/RAJPUTRoCkStAr")
                    loginwindow = Tk()
                    loginwindow.title("RAJPUTRoCkStAr")
                    window_width = 580
                    window_height = 300
                    screen_width = loginwindow.winfo_screenwidth()
                    screen_height = loginwindow.winfo_screenheight()
                    x_position = (screen_width - window_width) // 2
                    y_position = (screen_height - window_height) // 2
                    loginwindow.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
                    loginwindow.configure(bg="#e6e6e6")
                    label_text = "Click here to visit the website"
                    thank_you_label = Label(loginwindow, text=label_text, font=("Arial", 30, "bold"), fg="#333333", bg="#ffd699")
                    thank_you_label.bind("<Button-1>", open_link)
                    thank_you_label.pack(pady=50)
                    updating_label = Label(loginwindow, text="Update in Progress !", font=("Arial", 30, "bold"), fg="#333333", bg="#ffd699")
                    updating_label.pack(pady=50,padx=50)
                    
                else:
                    messagebox.showwarning(title='Warning',message='Invalid credentials. Please try again.')
                    print("Invalid credentials. Please try again.")

        # Close the cursor and connection
                cursor.close()
                mydb.close()
            except:
                print("Error:")
# Call the function to check user credentials
        check_user_credentials(email, password)
    # declaring all text variable here
        loemail= StringVar
        lopass = StringVar
        def toggle_password_visibility():
            if show_password_var.get():
                logipass.config(show="")
            else:
                logipass.config(show="*")
    root.geometry('520x220')
    root.title("RAJPUTRoCkStAr")
    logine=Label(root, text='Log in',
                 font=('sans-serif,Italic',24),
                 fg='red')
    logine.grid(row=0,column=1)

    loginemail = Label(root, text='Email :',font=('Italic',16))
    loginemail.grid(row=1,column=0)
    logemail = Entry(root, textvariable='loemail',width=35,font=('Italic',14))
    logemail.grid(row=1,column=1)

    loginpass = Label(root, text='Password :',font=('Italic',16))
    loginpass.grid(row=2,column=0)
    logipass = Entry(root, textvariable='lopass',width=35,font=('Italic',14),show='*')
    logipass.grid(row=2,column=1)
    sho_password_var = BooleanVar()
    sho_password_var.set(False)  
    sho_password_checkbutton = Checkbutton(root, text="Show Password", variable=show_password_var, command=toggle_password_visibility)
    sho_password_checkbutton.grid(row=3,column=1)

    loginbtn = Button(root, text='Login',width=20,font=('Impact',10),bg='grey',fg='white',command=thankyou)
    loginbtn.grid(row=4,column=1)

    root.mainloop()

def enrollbutton():
    entname.delete(0,END)
    entage.delete(0,END)
    entgender.delete(0,END)
    entemail.delete(0,END)
    entpass.delete(0,END)
    entphone.delete(0,END)


window = Tk()
window.geometry('480x430')
window.title("RAJPUTRoCkStAr")
bg_image = Image.open('icon.jpg')
icon = ImageTk.PhotoImage(bg_image)
window.iconphoto(True,icon)


cname = StringVar
cage = IntVar
cgender = StringVar
cemail = StringVar
cphone = IntVar


mainlabel = Label(window,text='REGISTRATION',
                  font=("Verdana", 25),
                  fg='red')
mainlabel.grid(row=0,column=3,padx=10, pady=10)


name = Label(window,text='Name :',font=('Italic',16))
name.grid(row =1,column=0)
entname = Entry(window,textvariable='cname',width=50)
entname.grid(row =1,column=3,pady=2)

age = Label(window,text='Age :',font=('Italic',16))
age.grid(row =2,column=0)
entage = Entry(window,textvariable='cage',width=50)
entage.grid(row =2,column=3,pady=2)

gender = Label(window,text='Gender :',font=('Italic',16))
gender.grid(row =3,column=0)
entgender = Entry(window,textvar='cgender',width=50)
entgender.grid(row =3,column=3,pady=2)

email = Label(window,text='Email :',font=('Italic',16))
email.grid(row =4,column=0)
entemail = Entry(window,textvariable='cemail',width=50)
entemail.grid(row =4,column=3,pady=2)

password = Label(window,text='Password :',font=('Italic',16))
password.grid(row =5,column=0)
entpass = Entry(window,textvariable='cpass',width=50,show='*')
entpass.grid(row =5,column=3,pady=2)
show_password_var = BooleanVar()
show_password_var.set(False)  
show_password_checkbutton = Checkbutton(window, text="Show Password", variable=show_password_var, command=toggle_password_visibility)
show_password_checkbutton.grid(row=6,column=3)

phone = Label(window,text='Phone Number :',font=('Italic',16))
phone.grid(row =7,column=0)
entphone = Entry(window,textvariable='cphone',width=50)
entphone.grid(row=7,column=3,pady=2)


submitbutton = Button(window,text='Registartion',command=submitbutton,width=20,bg='green',fg='white',font=('Roboto',16),activeforeground="white", activebackground="green")
submitbutton.grid(row=8,column=3,pady=2)

loginbutton = Button(window,text='Login_window',command=loginbutton,width=20,bg='blue',fg='yellow',font=('Roboto',16),activeforeground="yellow", activebackground="blue")
loginbutton.grid(row=9,column=3,pady=2)

enroll = Button(window,text='Enroll Others',command=enrollbutton,width=20,bg='red',fg='yellow',font=('Roboto',16),activeforeground="yellow", activebackground="red")
enroll.grid(row=10,column=3,pady=2)
 

window.mainloop()