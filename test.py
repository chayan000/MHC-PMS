#import modules
 
from cProfile import label
from tkinter import *
from tkinter import ttk
import os
from turtle import bgcolor, color
import tkinter.messagebox

# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("400x350")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Employee ID* ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password* ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
 

# Implementing event on login button 
 
def login_verify():
        username1 = username_verify.get()
        password1 = password_verify.get()
        username_login_entry.delete(0, END)
        password_login_entry.delete(0, END)
 
    #list_of_files = os.listdir("chayan","1234")
    #if username1 in list_of_files:
        file1 = open("username_info.txt", "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
            appointments()
        else:
            password_not_recognised()
 
 
# Designing popup for login success
 
def login_sucess():
    tkinter.messagebox.showinfo("Welcome User",  "Login Successful !")
 
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()

def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
# show appointments

def appointments():
    global win
    win = Tk()
    win.geometry("900x800")
    win.title("appointments")
    Label(win, text="Dr. Edward Jenner",width=100,font=("Calibri", 20),height=5).pack()
    Label(win, text="Todays Appointments",width=300,font=("Calibri", 20)).pack()
    
    style = ttk.Style()
    style.theme_use('clam')
    tree = ttk.Treeview(win,column=("Serial no","ID", "Name","Age", "Risk Factor"), show='headings', height=5)
    tree.column("# 1", anchor=CENTER,width=100)
    tree.heading("# 1", text="Serial No")
    tree.column("# 2", anchor=CENTER,width=100)
    tree.heading("# 2", text="ID")
    tree.column("# 3", anchor=CENTER,width=160)
    tree.heading("# 3", text="Name")
    tree.column("# 4", anchor=CENTER,width=100)
    tree.heading("# 4", text="Age")
    tree.column("# 5", anchor=CENTER,width=100)
    tree.heading("# 5", text="Risk Factor")
    tree.insert('', 'end', text="1", values=('1','432','Pritam De','76','****'))
    tree.insert('', 'end', text="1", values=('2','671', 'Devanka Khan','27','**'))
    tree.insert('', 'end', text="1", values=('3','711', 'Diganta Ghosh','45','***'))
    tree.insert('', 'end', text="1", values=('4','125', 'Debarghya Pal','39','******'))
    tree.pack(pady=100)

    Label(win, text="enter patient's ID to View/Edit",width=300,font=("Calibri", 13)).pack()
    ID=Entry(win,bd=8).pack()
    Button(win,text="View",font=("Calibri",10), height="2",width="10",bg="cyan",activebackground="red").pack()
    Button(win,text="Edit",font=("Calibri",10), height="2",width="10",bg="cyan",activebackground="red",command=edit).pack(pady=3)

    win.mainloop()

#Edit appointment
def edit():
    global edit
    edit=Tk()    
    edit.geometry("900x800")
    Label(edit, text="Patient ID: 432",width=300,font=("Calibri", 20)).pack(pady=40)
    Label(edit, text="Name: Pritam De",width=300,font=("Calibri", 17)).pack(pady=5)
    Label(edit, text="Age: 76                  Risk Factor: ****",width=300,font=("Calibri", 17)).pack(pady=5)
    Label(edit, text="Present Medical Condition: Alzheimer's disease",width=300,font=("Calibri", 17)).pack(pady=5)
    
    Label(edit, text="Update Patient's Condition",width=300,font=("Calibri", 17)).pack(pady=5)
    variable = StringVar(edit)
    variable.set("Select Mental Condition of Patient") # default value
    wi = OptionMenu(edit, variable, "Attention-Deficit Hyperactivity Disorder (ADHD)", "Anxiety Disorders",
     "Dissociative Disorders","Alzheimer's disease","Somatic Symptom Disorders")
    wi.pack(pady=5)

    Label(edit, text="Patient's Medicine",width=300,font=("Calibri", 17)).pack(pady=5)
    Label(edit, text="Galantamine, rivastigmine,Donepezil,Memantine ",width=300,font=("Calibri", 17)).pack(pady=5)
    Label(edit, text="Update Patient's Medicine",width=300,font=("Calibri", 17)).pack(pady=5)
    ID=Entry(edit,width=100).pack(pady=5)
     
    Button(edit,text="SAVE & EXIT",font=("Calibri",10), height="4", width="20",bg="cyan",activebackground="red",command=savesuccess ).pack(pady=20)
    Button(edit,text="Print Prescription",font=("Calibri",10), height="4", width="20",bg="cyan",activebackground="red" ).pack(pady=5)
    edit.mainloop()

#save successfully popup
def savesuccess():
    tkinter.messagebox.showinfo("Success",  "Saved Successfully !")


# Designing Main(first) window
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("900x800")
    main_screen.title("Account Login")
    Label(text="welcome to Mental Healthcare Patient Management Syatem(MHC-PMS)",  width="500", height="6", font=("Calibri", 20)).pack()
    Label(text="Select Your Role to LOGIN", width="300", height="2", font=("Calibri", 15)).pack()
    Button(text="Clinical Staff",font=("Calibri",10), height="6",width="30",bg="cyan",activebackground="red", command = login).pack()
    Label(text="").pack()
    Button(text="Receptionist",font=("Calibri",10), height="6", width="30",bg="cyan",activebackground="red" ).pack()
    Label(text="").pack()
    Button(text="Medical Report Staff",font=("Calibri",10), height="6", width="30",bg="cyan",activebackground="red").pack()
    Label(text="").pack()
    Button(text="Health Service Mananger",font=("Calibri",10), height="6", width="30",bg="cyan",activebackground="red").pack()

    main_screen.mainloop() 
main_account_screen()