# import modules
from tkinter import *   ## notice lowercase 't' in tkinter here
import tkinter as tk
import sqlite3
import tkinter.messagebox
import os, sys, webbrowser
from PIL import Image, ImageTk

conn = sqlite3.connect('database.db')
c = conn.cursor()

class App:
    def __init__(self, master):
        self.master = master

        # menu bar
        Chooser = Menu()

        Chooser.add_command(label='About', command=self.aboutMaster)
        Chooser.add_command(label='Help')
        Chooser.add_command(label='Exit', command=lambda: exitRoot(root))

        root.config(menu=Chooser)
        
        self.loginLabel = Label(text="\nEnter login credentials\n", font=('arial 14 bold'), fg='black')
        self.loginLabel.pack()

        # login ID
        self.login_id = Label(text="Login ID*", font=('arial 12'), fg='black')
        self.login_id.place(x=60, y=70)

        # password
        self.password = Label(text="Password*", font=('arial 12'), fg='black')
        self.password.place(x=60, y=120)

        # entries for labels
        self.login_id_ent = Entry(width=20)
        self.login_id_ent.place(x=280, y=72)

        self.password_ent = Entry(width=20, show='*')
        self.password_ent.place(x=280, y=122)

        # button to login
        self.loginShield = PhotoImage(file = "resources/user-shield-100.png")
        self.buttonImage = self.loginShield.subsample(3, 3)
        self.submit = Button(text = 'Login', image=self.buttonImage, compound=LEFT, width=120, height=40, bg='steelblue', command=self.login1)
        self.submit.place(x=160, y=190)

    # function to login
    def login(self,event):
        # self.db_pass = ""
        self.id = self.login_id_ent.get()
        print(type(self.id))
        self.password = self.password_ent.get()
        
        if self.id=="" or self.password=="":
            tkinter.messagebox.showwarning("All credentials required","Please enter all fields. Fields marked (*) are required.")
        else:
            self.login_id_ent.delete(0, END)
            self.password_ent.delete(0, END)
            sql = "SELECT * FROM credentials WHERE name =? and pass =?"
            # self.input = self.id
            self.res = c.execute(sql, (self.id,self.password))
            row = self.res.fetchone()
            # for row in self.res:
            #     self.db_name = row[1]
            #     self.db_pass = row[2]
            #     self.db_designation = row[3]

            self.db_name = row[1]
            self.db_pass = row[2]
            self.db_designation = row[3]

    
            if self.db_pass == self.password:
                tkinter.messagebox.showinfo("Login Successful", "Hello "+self.db_name+"! You have successfully logged in as " + self.db_designation)
                self.drawWin()
            else:
                tkinter.messagebox.showerror("Login Unsuccessful", "Invalid credentials! Please login again")

    def login1(self):
        # self.db_pass = ""
        self.id = self.login_id_ent.get()
        print(type(self.id))
        self.password = self.password_ent.get()
        
        if self.id=="" or self.password=="":
            tkinter.messagebox.showwarning("All credentials required","Please enter all fields. Fields marked (*) are required.")
        else:
            self.login_id_ent.delete(0, END)
            self.password_ent.delete(0, END)
            sql = "SELECT * FROM credentials WHERE name =? and pass =?"
            # self.input = self.id
            self.res = c.execute(sql, (self.id,self.password))
            row = self.res.fetchone()
            # for row in self.res:
            #     self.db_name = row[1]
            #     self.db_pass = row[2]
            #     self.db_designation = row[3]

            self.db_name = row[1]
            self.db_pass = row[2]
            self.db_designation = row[3]

    
            if self.db_pass == self.password:
                tkinter.messagebox.showinfo("Login Successful", "Hello "+self.db_name+"! You have successfully logged in as " + self.db_designation)
                self.drawWin()
            else:
                tkinter.messagebox.showerror("Login Unsuccessful", "Invalid credentials! Please login again")
    
    #function to draw toplevel window
    def drawWin(self):
        # hiding root window
        hide_root()

        # drawing toplevel window
        top = Toplevel() 
        top.geometry("480x320+0+0") 
        top.title("Welcome") 
        
        # menu bar
        Chooser = Menu()
        itemone = Menu()

        if self.db_designation == 'System Administrator' or self.db_designation == 'Doctor':
            itemone.add_command(label='Add Appointment', command=self.appointment)
            itemone.add_command(label='Edit Appointment', command=self.update)
            itemone.add_command(label='Delete Appointment', command=self.update)
        
        itemone.add_command(label='View Appointment', command=self.display)
        itemone.add_separator()
        itemone.add_command(label='Logout', command=lambda: self.logout(top))

        Chooser.add_cascade(label='File', menu=itemone)
        Chooser.add_command(label='View Appointment', command=self.display)
        Chooser.add_command(label='Logout', command=lambda: self.logout(top))

        top.config(menu=Chooser)
        top.iconphoto(False, tk.PhotoImage(file="resources/icon.png"))

        self.left = Frame(top, width=130, height=130, bd=1, relief=RAISED)
        self.left.place(x=5, y=5)

        self.right = Frame(top, width=320, height=150)
        self.right.place(x=150, y=5)
        
        self.drawImage(top)

        self.userlogin = Label(self.right, text="You are logged in as:", font=('arial 12 bold'), fg='black')
        self.userlogin.place(x=5, y=20)

        self.Name = Label(self.right, text="Name: " + self.db_name, font=('arial 12'), fg='black')
        self.Name.place(x=5, y=50)

        self.Name = Label(self.right, text="Designation: " + self.db_designation, font=('arial 12'), fg='black')
        self.Name.place(x=5, y=80)

    def destroyTop(self, top):
        top.destroy()

    # function to close the top window
    def logout(self, top):
        MsgBox = tk.messagebox.askquestion('Logout Application','Are you sure you want to logout?', icon='warning')
        if MsgBox == 'yes':
            # self.path = self.name + ".jpg"
            self.destroyTop(top)
            show_root()

    # function to open the appointment window    
    def appointment(self):
        if sys.platform.startswith('linux'):
            print("OS = linux")
            os.system("python3 appointment.py")
        elif sys.platform.startswith('win32'):
            print("OS = win32")
            os.system("python appointment.py")

    # function to open the update window  
    def update(self):
        if sys.platform.startswith('linux'):
            print("OS = linux")
            os.system("python3 update.py")
        elif sys.platform.startswith('win32'):
            print("OS = win32")
            os.system("python update.py")

    # function to open the display window  
    def display(self):
        if sys.platform.startswith('linux'):
            print("OS = linux")
            os.system("python3 display.py")
        elif sys.platform.startswith('win32'):
            print("OS = win32")
            os.system("python display.py")

    def writeTofile(self):
        # Convert binary data to proper format and write it on Hard Disk
        with open(self.photoPath, 'wb') as file:
            file.write(self.photo)

    def drawImage(self, top):
        # function takes image from database and saves it to disk. Then, it draws it on toplevel window
        sql_fetch_blob_query = "SELECT * from credentials where id = ?"
        c.execute(sql_fetch_blob_query, (self.id,))
        self.record = c.fetchall()
        for row in self.record:
            # print("Id = ", row[0], "Name = ", row[1])
            self.name  = row[1]
            self.photo = row[4]

            self.photoPath = "/home/techmirtz/projects/Python Project Sem 6/Hospital-Management-System/" + self.name + ".jpg"
            # print(self.photoPath)

            # save file to directory
            self.writeTofile()
            
            self.fileName = self.name + ".jpg"
            file_name = str(self.fileName)

            # draw image on canvas
            self.canvas = Canvas(self.left, width=120, height=120)  
            self.canvas.pack()
            self.img = ImageTk.PhotoImage(Image.open(file_name)) 
            self.canvas.create_image(0,0, anchor=NW, image=self.img)    
            self.canvas.image = self.img

            # deleteProfilePic(self.fileName)
            os.remove(self.fileName)

    def aboutMaster(self):
        about = Toplevel()
        about.geometry("480x320+0+0") 
        about.title("About")
        about.iconphoto(False, tk.PhotoImage(file="resources/icon.png"))

        self.loginLabel = Label(about, text="\n\n\n\nThe application has been created using tkinter for GUI. \nThe data has been saved and accessed using SQLite3.\n\nMade by:", font=('arial 11'), fg='black')
        self.loginLabel.pack()

        self.gitProfile = Label(about, text="Vatsal , arjun, akshit", fg='blue', font=('arial 11 underline'), cursor="hand2")
        self.gitProfile.place(x=180, y=180)
        self.gitProfile.bind("<Button-1>", lambda e: webbrowser.open("https://www.github.com/akshit6"))

        self.photo = PhotoImage(file = "resources/github-100.png")
        self.photoimage = self.photo.subsample(3, 3)
        self.githubButton = Button(about, text = 'Open sourced on GitHub', image=self.photoimage, compound=LEFT, width=220, height=40, bg='black', fg='white', command=lambda : webbrowser.open('https://github.com/chauhannaman98/Hospital-Management-System'))
        self.githubButton.place(x=110, y=250)

# def deleteProfilePic(filepath):
#     print("Deleting: "+filepath)
#     os.remove(filepath)

root = tk.Tk()
b = App(root)
root.geometry("540x320+0+0")
root.resizable(False, False)
root.title("Hospital management system")
root.iconphoto(False, tk.PhotoImage(file="resources/icon.png"))
root.bind('<Return>', b.login)

def hide_root():
    # Hide root window
    root.withdraw()

def show_root():
    # Show root window
    root.deiconify()

def exitRoot(root):
    MsgBox = tk.messagebox.askquestion('Exit Application','Do you really want to exit?', icon='warning')
    if MsgBox == 'yes':
        root.destroy()

root.mainloop()
