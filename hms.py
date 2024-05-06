import tkinter.messagebox
from tkinter import  *
import mysql.connector as sqlcon
import random as rd
from PIL import ImageTk, Image 
con=sqlcon.connect(host="localhost",user="root",password="root")#connection to mysql 
cur=con.cursor()
cur = con.cursor(buffered=True)
if (con):
    # Carry out normal procedure
    print ("Connection successful")
else:
    print ("Connection unsuccessful")
cur.execute("create database if not exists Hospital")
cur.execute("use Hospital")
cur.execute("create table if not exists appointment"
            "("
            "idno varchar(12) primary key,"
            "name char(50),"
            "age char(3),"
            "gender char(1),"
            "phone varchar(10),"
            "bg varchar(3))")
cur.execute("create table if not exists appointment_details"
            "("
            "idno varchar(12) primary key,"
            "doctor varchar(50),"
            "date varchar(20),"
            "time varchar(20),"
            "appointment_no varchar(10))")
#  Message for registration
def entry():
    global e1,e2,e3,e4,e5,e6
    p1=e1.get()
    p2=e2.get()
    p3=e3.get()
    p4=e4.get()
    p5=e5.get()
    p6=e6.get()

    query = 'insert into appointment values("{}", "{}", "{}", "{}", "{}", "{}")'.format(p1, p2, p3, p4, p5, p6)
    try:
        cur.execute(query)
        con.commit()
    except sqlcon.Error as err:
        tkinter.messagebox.showerror("Registration Error", f"Error: {err}")
    else:
        tkinter.messagebox.showinfo("Registration Success", "You have been registered!")
        
    
#  For registration 
def register():
    global e1, e2, e3, e4, e5, e6
    root1 = Tk()
    root1.title("Registration Form")
    root1.geometry("400x400")

    label = Label(root1, text="REGISTER YOURSELF", font='Arial 25 bold', fg='blue')  # Set font color to blue
    label.pack()

    frame = Frame(root1, height=500, width=200)
    frame.pack()

    l1 = Label(root1, text="AADHAR CARD NO.", fg='green')  # Set label text color to green
    l1.place(x=10, y=130)
    e1 = Entry(root1)
    e1.place(x=150, y=130)

    l2 = Label(root1, text="NAME", fg='green')
    l2.place(x=10, y=170)
    e2 = Entry(root1)
    e2.place(x=150, y=170)

    l3 = Label(root1, text="AGE", fg='green')
    l3.place(x=10, y=210)
    e3 = Entry(root1)
    e3.place(x=150, y=210)

    l4 = Label(root1, text="GENDER M\\F", fg='green')
    l4.place(x=10, y=250)
    e4 = Entry(root1)
    e4.place(x=150, y=250)

    l5 = Label(root1, text="PHONE", fg='green')
    l5.place(x=10, y=290)
    e5 = Entry(root1)
    e5.place(x=150, y=290)

    l6 = Label(root1, text="BLOOD GROUP", fg='green')
    l6.place(x=10, y=330)
    e6 = Entry(root1)
    e6.place(x=150, y=330)

    b1 = Button(root1, text="SUBMIT", command=entry, bg='yellow', fg='red')  # Set button background to yellow and text color to red
    b1.place(x=150, y=370)

    root1.mainloop()

#  Message for appointment
def apo_details():
    global x1,x2,h,p1,p2,p3,o,x4,x3
    p1=x2.get()
    p2=x3.get()
    p3=x4.get()
    if int(p1)==1:
        i=("Dr. sharma \nRoom no:- 10")
        j=("Dr. Verma \nRoom no:- 11")
        q=(i,j)
        h=rd.choice(q) 
        u=(23,34,12,67,53,72)
        o=rd.choice(u)
        det=("Your appointment is fixed with",h,
             "\nDate:-",p2,
             "\nTime:-",p3,
             '\nappointment no:-',o)

        query='insert into appointment_details values("{}", "{}", "{}", "{}", "{}")'.format(p1,h,p2,p3,o)
        cur.execute(query)
        tkinter.messagebox.showinfo("APPOINTMENT DETAILS",det)
     
    elif int(p1)==2:
        i=("Dr. Sidharth \nRoom no. 16")
        j=("Dr. Tendulkar \nRoom no. 17")
        q=(i,j)
        h=rd.choice(q) 
        u=(23,34,12,67,53,72)
        o=rd.choice(u)        
        det=("Your appointment is fixed with",h,
             "\nDate:-",p2,
             "\nTime:-",p3,
             '\nappointment no:-',o)
        query='insert into appointment_details values("{}", "{}", "{}", "{}", "{}")'.format(p1,h,p2,p3,o)
        cur.execute(query) 
        tkinter.messagebox.showinfo("APPOINTMENT DETAILS",det)
     
    elif int(p1)==3:
        i=("Dr. Kumar \nRoom no. 12")
        j=("Dr. Khan \nRoom no. 13")
        q=(i,j)
        h=rd.choice(q) 
        u=(23,34,12,67,53,72)
        o=rd.choice(u)        
        det=("Your appointment is fixed with",h,
             "\nDate:-",p2,
             "\nTime:-",p3,
             '\nappointment no:-',o)
        query='insert into appointment_details values("{}", "{}", "{}", "{}", "{}")'.format(p1,h,p2,p3,o)
        cur.execute(query) 
        tkinter.messagebox.showinfo("APPOINTMENT DETAILS",det)

    elif int(p1)==4:
        i=("Dr. Virat, \nRoom no. 18")
        j=("Dr. Leo \nRoom no. 19")
        q=(i,j)
        h=rd.choice(q) 
        u=(23,34,12,67,53,72)
        o=rd.choice(u)        
        det=("Your appointment is fixed with",h,
             "\nDate:-",p2,
             "\nTime:-",p3,
             '\nappointment no:-',o)
        query='insert into appointment_details values("{}", "{}", "{}", "{}", "{}")'.format(p1,h,p2,p3,o)
        cur.execute(query)
        tkinter.messagebox.showinfo("APPOINTMENT DETAILS",det)
    elif int(p1)==5:
        i=("Dr. Kohli \nRoom no. 14")
        j=("Dr. singh \nRoom no. 15")
        q=(i,j)
        h=rd.choice(q) 
        u=(23,34,12,67,53,72)
        o=rd.choice(u)        
        det=("Your appointment is fixed with",h,
             "\nDate:-",p2,
             "\nTime:-",p3,
             '\nappointment no:-',o)
        query='insert into appointment_details values("{}", "{}", "{}", "{}", "{}")'.format(p1,h,p2,p3,o)
        cur.execute(query)
        tkinter.messagebox.showinfo("APPOINTMENT DETAILS",det)   
    elif int(p1)==6:
        i=("Dr. Irfan \nRoom no. 001")
        j=("Dr. John \nRoom no. 002")
        k=("Dr. Sanjay \nRoom no. 003")
        l=("Dr. Shahid \nRoom no. 004")
        q=(i,j,k,l)
        h=rd.choice(q) 
        u=(23,34,12,67,53,72)
        o=rd.choice(u)        
        det=("Your appointment is fixed with",h,
             "\nDate:-",p2,
             "\nTime:-",p3,
             '\nappointment no:-',o)
        query='insert into appointment_details values("{}", "{}", "{}", "{}", "{}")'.format(p1,h,p2,p3,o)
        cur.execute(query)
        tkinter.messagebox.showinfo("APPOINTMENT DETAILS",det)   
    else:
        tkinter.messagebox.showwarning('WRONG INPUT','PLEASE ENTER VALID VALUE')

#  For appointment
def get_apoint():
    global x1, x2, x3, x4
    p1 = x1.get()  
    # Assuming 'cur' is your cursor object
    cur.execute('select * from appointment where idno=(%s)', (p1,))
    dat = cur.fetchall()
    
    if len(dat) == 0:
        tkinter.messagebox.showwarning("ERROR", "NO DATA FOUND!!")
    else:
        root3 = Tk()
        root3.title("Book an Appointment")
        root3.geometry("700x760")
        root3.configure(bg="#f0f0f0")  # Set background color
        
        label = Label(root3, text="APPOINTMENT", font='Arial 25 bold', bg="#f0f0f0")
        label.pack(pady=20)
        
        frame1 = Frame(root3, bg="#ffffff", pady=20)
        frame1.pack()
        
        for i in dat:
            if i[3] == 'M' or i[3] == 'm':
                x = "Mr."
            else:
                x = "Mrs/Ms."
            
            welcome_label = Label(frame1, text=f'Welcome {x} {i[1]}', font='Arial 14')
            welcome_label.grid(row=0, column=0, pady=10)

            age_label = Label(frame1, text=f'AGE: {i[2]}', font='Arial 12')
            age_label.grid(row=1, column=0, pady=5)

            phone_label = Label(frame1, text=f'PHONE: {i[4]}', font='Arial 12')
            phone_label.grid(row=2, column=0, pady=5)

            bg_label = Label(frame1, text=f'BLOOD GROUP: {i[5]}', font='Arial 12')
            bg_label.grid(row=3, column=0, pady=5)
        
        frame2 = Frame(root3, bg="#ffffff", pady=20)
        frame2.pack()

        departments_label = Label(frame2, text='DEPARTMENTS', font='Arial 14')
        departments_label.grid(row=0, column=0, pady=10)

        departments_info = [
            "Orthopaedic surgeon",
            "Physician",
            "Nephrologist",
            "Neurologist",
            "Gynaecologist",
            "X-ray"
        ]
        for index, dept in enumerate(departments_info, start=1):
            dept_label = Label(frame2, text=f"{index}. {dept}", font='Arial 12')
            dept_label.grid(row=index, column=0, pady=5)

        choice_label = Label(frame2, text='Enter your choice', font='Arial 12')
        choice_label.grid(row=7, column=0, pady=10)

        x2 = Entry(frame2, font='Arial 12')
        x2.grid(row=7, column=1, pady=10)

        date_label = Label(frame2, text='Enter date', font='Arial 12')
        date_label.grid(row=8, column=0, pady=10)

        x3 = Entry(frame2, font='Arial 12')
        x3.grid(row=8, column=1, pady=10)

        time_label = Label(frame2, text='Enter time (24-hour format)', font='Arial 12')
        time_label.grid(row=9, column=0, pady=10)

        x4 = Entry(frame2, font='Arial 12')
        x4.grid(row=9, column=1, pady=10)

        submit_button = Button(root3, text='Submit', command=apo_details, bg="#007bff", fg="#ffffff", font='Arial 12')
        submit_button.pack(pady=20)
        
        root3.resizable(False, False)
        root3.mainloop()



#  For AADHAAR no input
def apoint():
    global x1
    root2 = Tk()
    root2.title("Appointment Form")
    root2.geometry("400x200")
    root2.configure(bg="deep sky blue")  # Set background color

    label_title = Label(root2, text="APPOINTMENT", font='Arial 25 bold', bg="#f0f0f0")
    label_title.pack(pady=10)

    frame = Frame(root2, height=200, width=200, bg="light blue")  # Frame for form elements
    frame.pack(pady=10)

    label_aadhaar = Label(frame, text="AADHAAR NO.", bg="#ffffff", fg="#333333", font='Arial 12')
    label_aadhaar.grid(row=0, column=0, padx=10, pady=10)

    x1 = Entry(frame, bg="#f0f0f0", fg="#333333", font='Arial 12')
    x1.grid(row=0, column=1, padx=10, pady=10)

    button_submit = Button(frame, text='Submit', command=get_apoint, bg="#007bff", fg="#ffffff", font='Arial 12')
    button_submit.grid(row=1, columnspan=2, pady=10)

    root.resizable(False, False)
    root.mainloop()
#  List of doctors
def lst_doc():
    root4 = Tk()
    root4.title("List of Doctors")
    root4.geometry("500x500")
    root4.configure(bg="#90ee90")  # Set background color

    doctors = [
        "Dr. Sharma", "Dr. Verma", "Dr. Kumar", "Dr. Khan", "Dr. Kohli", "Dr. Singh", 
        "Dr. Sidharth", "Dr. Tendulkar", "Dr. Virat", "Dr. Leo", "Dr. Irfan", "Dr. John", 
        "Dr. Sanjay", "Dr. Shahid"
    ]
    departments = [
        "Orthopaedic Surgeon", "Orthopaedic Surgeon", "Nephrologist", "Nephrologist", 
        "Gynaecologist", "Gynaecologist", "Physician", "Physician", "Neurologist", 
        "Neurologist", "X-ray", "X-ray", "X-ray", "X-ray"
    ]
    room_numbers = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]

    frame = Frame(root4, bg="#ffffff")
    frame.pack(pady=20, padx=20)

    l1 = Label(frame, text='NAME OF DOCTORS', font=("Arial", 12, "bold"), bg="#ffffff")
    l1.grid(row=0, column=0, padx=10, pady=10)

    l2 = Label(frame, text='DEPARTMENT', font=("Arial", 12, "bold"), bg="#ffffff")
    l2.grid(row=0, column=1, padx=10, pady=10)

    l3 = Label(frame, text='ROOM NO', font=("Arial", 12, "bold"), bg="#ffffff")
    l3.grid(row=0, column=2, padx=10, pady=10)

    for index, (doctor, department, room) in enumerate(zip(doctors, departments, room_numbers), start=1):
        bg_color = "#f0f0f0" if index % 2 == 0 else "#e6e6e6"  # Alternate row colors
        Label(frame, text=doctor, font=("Arial", 10), bg=bg_color).grid(row=index, column=0, padx=10, pady=5)
        Label(frame, text=department, font=("Arial", 10), bg=bg_color).grid(row=index, column=1, padx=10, pady=5)
        Label(frame, text=room, font=("Arial", 10), bg=bg_color).grid(row=index, column=2, padx=10, pady=5)

    root4.mainloop()

def ser_avail():
    root5 = Tk()
    root5.title("Services Available")
    root5.geometry("500x500")
    root5.configure(bg="deep sky blue")  # Set background color

    frame = Frame(root5, bg="#ffffff")
    frame.pack(pady=20, padx=20)

    l1 = Label(frame, text='SERVICES AVAILABLE', font=("Arial", 14, "bold"), bg="#ffffff")
    l1.grid(row=0, column=0, padx=10, pady=10)

    services = ["ULTRASOUND", "X-RAY", "CT Scan", "MRI", "BLOOD COLLECTION", 
                "DIALYSIS", "ECG", "CHEMIST", "LAB"]
    room_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for index, (service, room) in enumerate(zip(services, room_numbers), start=1):
        bg_color = "#e6e6e6" if index % 2 == 0 else "#f0f0f0"  # Alternate row colors
        Label(frame, text=service, font=("Arial", 12), bg=bg_color).grid(row=index, column=0, padx=10, pady=5)
        Label(frame, text=room, font=("Arial", 12), bg=bg_color).grid(row=index, column=1, padx=10, pady=5)

    contact_label = Label(root5, text='To avail any of these, please contact us at: 7042****55', font=("Arial", 10), bg="#f0f0f0")
    contact_label.pack(pady=10)

    root5.mainloop()
def modify():
    global x3,x4,choice,new,x5,root6
    p1=x3.get()
    cur.execute('select * from appointment where idno=(%s)',(p1,))
    
    dat=cur.fetchall()
    a=[]
    for i in dat:
        a.append(i)   
    if len(a)==0:
        tkinter.messagebox.showwarning("ERROR", "NO DATA FOUND!!")
    else: 
      root6=Tk()
      frame=Frame(root6,height=500,width=500)
      frame.pack()
      l1=Label(root6,text='DATA MODIFICATION',font="arial 15 bold")
      l1.place(x=75,y=10)
      l2=Label(root6,text='WHAT YOU WANT TO CHANGE')
      l2.place(x=50,y=200)
      l3=Label(root6,text='1.NAME')
      l3.place(x=50,y=220)
      l4=Label(root6,text='2.AGE')
      l4.place(x=50,y=240)
      l5=Label(root6,text='3.GENDER')
      l5.place(x=50,y=260)
      l6=Label(root6,text='4.PHONE')
      l6.place(x=50,y=280)
      l7=Label(root6,text='5.BLOOD GROUP')
      l7.place(x=50,y=300)
      x2=Label(root6,text='Enter')
      x2.place(x=50,y=330)
      x4=tkinter.Entry(root6)
      choice=x4.get()
      x4.place(x=100,y=330)
      for i in dat:
            name=Label(root6,text='NAME:-')
            name.place(x=50,y=80)
            name1=Label(root6,text=i[1])
            name1.place(x=150,y=80)
            age=Label(root6,text='AGE:-')
            age.place(x=50,y=100)
            age1=Label(root6,text=i[2])
            age1.place(x=150,y=100)
            gen=Label(root6,text='GENDER:-')
            gen.place(x=50,y=120)
            gen1=Label(root6,text=i[3])
            gen1.place(x=150,y=120)
            pho=Label(root6,text='PHONE:-')
            pho.place(x=50,y=140)
            pho1=Label(root6,text=i[4])
            pho1.place(x=150,y=140)
            bg=Label(root6,text='BLOOD GROUP:-')
            bg.place(x=50,y=160)
            bg1=Label(root6,text=i[5])
            bg1.place(x=150,y=160)
      b=Button(root6,text='Submit',command=do_modify)
      b.place(x=50,y=400)
      L1=Label(root6,text='OLD DETAILS')
      L1.place(x=50,y=50)
      L2=Label(root6,text='ENTER NEW DETAIL')
      L2.place(x=50,y=360)
      x5=tkinter.Entry(root6)
      new=x5.get()
      x5.place(x=160,y=360)

      root6.resizable(False,False)
      root6.mainloop()

def do_modify():
    global ad,x3,x4,x5
    ad=x3.get()
    choice=x4.get()
    new=x5.get()
    if choice=='1':
        cur.execute('update appointment set name={} where idno={}'.format(new,ad))
    elif choice=='2':
        cur.execute('update appointment set age={} where idno={}'.format(new,ad))        
    elif choice=='3':
        cur.execute('update appointment set gender={} where idno={}'.format(new,ad))
    elif choice=='4':
        cur.execute('update appointment set phone={} where idno={}'.format(new,ad))    
    elif choice=='5':
        cur.execute('update appointment set bg={} where idno={}'.format(new,ad))
    else:
        pass
    root6.destroy()
    tkinter.messagebox.showinfo("DONE", "YOUR DATA HAS BEEN MODIFIED")
    
choice=None
new=None    
ad=None
def mod_sub():
    global x3, ad
    root7 = Tk()
    root7.title("MODIFICATION")
    root7.geometry("400x200")
    root7.configure(bg='#f0f0f0')

    label = Label(root7, text="MODIFICATION", font='Arial 25 bold', bg='#f0f0f0')
    label.pack()

    frame = Frame(root7, bg='#f0f0f0')
    frame.pack()

    l1 = Label(root7, text="AADHAAR NO.", bg='#f0f0f0')
    l1.place(x=10, y=130)
    x3 = Entry(root7)
    x3.place(x=100, y=130)

    ad = x3.get()

    b1 = Button(root7, text='Submit', command=modify, bg='#ffc107', fg='#ffffff', bd=0, padx=10, pady=5)
    b1.place(x=100, y=160)

    root7.resizable(False, False)
    root7.mainloop()  

def search_data():
    global x3, ad
    root7 = Tk()
    root7.title("SEARCH DATA of PATIENT")
    root7.geometry("400x200")
    root7.configure(bg='#f0f0f0')

    label = Label(root7, text="SEARCH DATA", font='Arial 25 bold', bg='#f0f0f0')
    label.pack()

    frame = Frame(root7, bg='#f0f0f0')
    frame.pack()

    l1 = Label(root7, text="AADHAAR NO.", bg='#f0f0f0')
    l1.place(x=10, y=130)
    x3 = Entry(root7)
    x3.place(x=100, y=130)

    ad = x3.get()

    b1 = Button(root7, text='Submit', command=view_data, bg='#ffc107', fg='#ffffff', bd=0, padx=10, pady=5)
    b1.place(x=100, y=160)

    root7.resizable(False, False)
    root7.mainloop()

def view_data():
    global p1
    p1 = x3.get()
    cur.execute('select * from appointment where idno=(%s)', (p1,))
    
    dat = cur.fetchall()
    if len(dat) == 0:
        tkinter.messagebox.showwarning("ERROR", "NO DATA FOUND!!")
    else:
        details = "\n".join([f"ID: {row[0]}\nName: {row[1]}\nAge: {row[2]}\nGender: {row[3]}\nPhone: {row[4]}\nBlood Group: {row[5]}\n" for row in dat])
        tkinter.messagebox.showinfo("Patient DETAILS", details)

root = Tk()
root.title("SRM HOSPITAL")
   
root = Tk()
root.title("SRM HOSPITAL")
root.geometry("800x600")
root.configure(bg='#f0f0f0')  # Set background color

# Gradient background frame
bg_frame = Frame(root, bg='#003366', width=800, height=150)
bg_frame.pack()

# Title label with gradient background
title_label = Label(bg_frame, text="SRM HOSPITAL", font=("Arial", 40, "bold"), bg='#003366', fg='#ffffff')
title_label.place(relx=0.5, rely=0.5, anchor='center')

# Main frame with light background
main_frame = Frame(root, bg='#f0f0f0', padx=20, pady=20)
main_frame.pack(expand=True, fill=BOTH)

# Buttons
buttons_frame = Frame(main_frame, bg='#f0f0f0')
buttons_frame.pack()

btn_register = Button(buttons_frame, text="Registration", font=("Arial", 20, "bold"), bg='yellow', command=register)
btn_register.pack(side=LEFT, padx=20)

btn_lst_doc = Button(buttons_frame, text="List of Doctors", font=("Arial", 20, "bold"), bg='yellow', command=lst_doc)
btn_lst_doc.pack(side=LEFT, padx=20)

btn_ser_avail = Button(buttons_frame, text="Services available", font=("Arial", 20, "bold"), bg='yellow', command=ser_avail)
btn_ser_avail.pack(side=LEFT, padx=20)

btn_apoint = Button(main_frame, text="Appointment", font=("Arial", 20, "bold"), bg='yellow', command=apoint)
btn_apoint.pack(pady=30)

btn_search_data = Button(main_frame, text="View data", font=("Arial", 20, "bold"), bg='yellow', command=search_data)
btn_search_data.pack()

btn_mod_sub = Button(main_frame, text="Modify existing data", font=("Arial", 20, "bold"), bg='yellow', command=mod_sub)
btn_mod_sub.pack(pady=30)

btn_exit = Button(root, text="Exit", font=("Arial", 20, "bold"), command=root.destroy, bg='violet')
btn_exit.pack(pady=20)

root.resizable(FALSE, False)
root.mainloop()
