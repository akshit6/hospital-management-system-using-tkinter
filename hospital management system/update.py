# update the appointments
# import modules
from tkinter import *   ## notice lowercase 't' in tkinter here
import tkinter as tk
import sqlite3
import tkinter.messagebox

conn = sqlite3.connect('datab.db')
c = conn.cursor()

class App:
    def __init__(self, master):
        self.master = master
        # heading label
        self.heading = Label(master, text="Update Appointments",  fg='steelblue', font=('arial 40 bold'))
        self.heading.place(x=150, y=0)

        # search criteria -->name 
        self.name = Label(master, text="Enter Patient's Name", font=('arial 18 bold'))
        self.name.place(x=0, y=60)

        # entry for  the name
        self.namenet = Entry(master, width=30)
        self.namenet.place(x=280, y=62)

        # search button
        self.search = Button(master, text="Search", width=12, height=1, bg='steelblue', command=self.search_db)
        self.search.place(x=350, y=102)
    
    
    # function to search
    def search_db(self):
        self.input = self.namenet.get()

        # execute sql 
        sql = "SELECT * FROM appointments WHERE name LIKE ?"
        self.res = c.execute(sql, (self.input,))
        for self.row in self.res:
            self.name1 = self.row[1]
            self.age = self.row[2]
            self.gender = self.row[3]
            self.location = self.row[4]
            self.time = self.row[6]
            self.phone = self.row[5]
        
        # creating the update form
        self.uname = Label(self.master, text="Patient's Name", font=('arial 18 bold'))
        self.uname.place(x=0, y=140)

        self.uage = Label(self.master, text="Age", font=('arial 18 bold'))
        self.uage.place(x=0, y=180)

        self.ugender = Label(self.master, text="Gender", font=('arial 18 bold'))
        self.ugender.place(x=0, y=220)

        self.ulocation = Label(self.master, text="Location", font=('arial 18 bold'))
        self.ulocation.place(x=0, y=260)

        self.utime = Label(self.master, text="Appointment Time", font=('arial 18 bold'))
        self.utime.place(x=0, y=300)

        self.uphone = Label(self.master, text="Phone Number", font=('arial 18 bold'))
        self.uphone.place(x=0, y=340)

        # entries for each labels==========================================================
        # ===================filling the search result in the entry box to update
        self.ent1 = Entry(self.master, width=30)
        self.ent1.place(x=300, y=140)
        self.ent1.insert(END, str(self.name1))

        self.ent2 = Entry(self.master, width=30)
        self.ent2.place(x=300, y=180)
        self.ent2.insert(END, str(self.age))

        self.ent3 = Entry(self.master, width=30)
        self.ent3.place(x=300, y=220)
        self.ent3.insert(END, str(self.gender))

        self.ent4 = Entry(self.master, width=30)
        self.ent4.place(x=300, y=260)
        self.ent4.insert(END, str(self.location))

        self.ent5 = Entry(self.master, width=30)
        self.ent5.place(x=300, y=300)
        self.ent5.insert(END, str(self.time))

        self.ent6 = Entry(self.master, width=30)
        self.ent6.place(x=300, y=340)
        self.ent6.insert(END, str(self.phone))

        # button to execute update
        self.update = Button(self.master, text="Update", width=20, height=2, bg='lightblue', command=self.update_db)
        self.update.place(x=400, y=380)

        # button to delete
        self.delete = Button(self.master, text="Delete", width=20, height=2, bg='red', command=self.delete_db)
        self.delete.place(x=150, y=380)
    
    
    def update_db(self):
        # declaring the variables to update
        self.var1 = self.ent1.get() #updated name

        try:
            self.var2 = int(self.ent2.get())
        except ValueError:
            tkinter.messagebox.showwarning("Warning","Please fill up age correctly")
        self.var3 = self.ent3.get() #updated gender
        self.var4 = self.ent4.get() #updated location
        self.var5 = self.ent5.get() #updated phone
        self.var6 = self.ent6.get() #updated time
        if self.var1 == '' or self.var2 == '' or self.var3 == '' or self.var4 == '' or self.var5 == '' or self.var6 == '':
            tkinter.messagebox.showwarning("Warning","Please fill up all the boxes")

        elif (self.var3!="male"  and self.var3 !="female"):     #condition for gender
            tkinter.messagebox.showwarning("Warning","Please fill up a valid gender")

        elif (self.var2>105 or self.var2<0):                    #condition for age
            tkinter.messagebox.showwarning("Warning","Please fill up a valid age")

        elif (not(self.var6).isdecimal() or len(self.var6)!=10):      #condition for mobile number
            tkinter.messagebox.showwarning("Warning","Please fill up a valid mobile number")

        else:

            query = "UPDATE appointments SET name=?, age=?, gender=?, location=?, phone=?, scheduled_time=? WHERE name LIKE ?"
            c.execute(query, (self.var1, self.var2, self.var3, self.var4, self.var6, self.var5, self.namenet.get(),))
            conn.commit()
            tkinter.messagebox.showinfo("Updated", "Successfully Updated.")
    
    
    def delete_db(self):
        # delete the appointment
        sql2 = "DELETE FROM appointments WHERE name LIKE ?"
        c.execute(sql2, (self.namenet.get(),))
        conn.commit()
        tkinter.messagebox.showinfo("Success", "Deleted Successfully")
        self.ent1.destroy()
        self.ent2.destroy()
        self.ent3.destroy()
        self.ent4.destroy()
        self.ent5.destroy()
        self.ent6.destroy()


#creating the object
root = tk.Tk()
b = App(root)
root.geometry("1000x620+0+0")
root.resizable(False, False)
root.title("Hospital management system")
root.iconphoto(False, tk.PhotoImage(file='resources/icon.png'))

# end the loop
root.mainloop()
