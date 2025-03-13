def addstudent():                   #------------------------------ Add Button Functionality
    def submitadd():
            id=idval.get()
            name=nameval.get()
            contact=mobileval.get()
            email=emailval.get()
            address=addressval.get()
            gender=genderval.get()
            dob=dobval.get()
            addedtime = time.strftime("%H:%M:%S")
            addeddate = time.strftime("%d/%m/%Y")
            try:
                strr='insert into studentdata1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                mycursor.execute(strr,(id,name,contact,email,address,gender,dob,addeddate,addedtime))
                conn.commit()
                res=messagebox.askyesnocancel('Notification','Id {} Name {} Added Successfully.. & want to clean the form'.format(id,name),parent=addroot)
                if(res==True):
                    idval.set('')
                    nameval.set('')
                    mobileval.set('')
                    emailval.set('')
                    addressval.set('')
                    genderval.set('')
                    dobval.set('')
            
            except:
                messagebox.showerror('Notification','Id Already Exist try another id...',parent=addroot)
            strr='select * from studentdata1'
            mycursor.execute(strr)
            print(strr)
            datas=mycursor.fetchall()
            student_table.delete(*student_table.get_children())
            for i in datas:
                vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                student_table.insert('',END,values=vv)
                
                
    addroot=Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('470x470+220+200')
    addroot.title('Student Management System')
    addroot.config(bg='black')
    addroot.iconbitmap()
    addroot.resizable(False,False) 
    
    #------------------------------ Label
    
    hostlabel=Label(addroot,text='Enter Id : ',bg='black',foreground='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=1,width=13,anchor='n')#n
    hostlabel.place(x=10,y=10)
    
    namelabel=Label(addroot,text='Enter Name : ',bg='black',foreground='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=1,width=13,anchor='n')#n
    namelabel.place(x=10,y=70)
    
    contactlabel=Label(addroot,text='Enter Contact : ',bg='black',foreground='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=1,width=13,anchor='n')#n
    contactlabel.place(x=10,y=130)
    
    emaillabel=Label(addroot,text='Enter Email : ',bg='black',foreground='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=1,width=13,anchor='n')#n
    emaillabel.place(x=10,y=190)
    
    addresslabel=Label(addroot,text='Enter Address : ',bg='black',foreground='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=1,width=13,anchor='n')#n
    addresslabel.place(x=10,y=250)
    
    genderlabel=Label(addroot,text='Enter Gender : ',bg='black',foreground='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=1,width=13,anchor='n')#n
    genderlabel.place(x=10,y=310)
    
    doblabel=Label(addroot,text='Enter D.O.B : ',bg='black',foreground='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=1,width=13,anchor='n')#n
    doblabel.place(x=10,y=370)
    
    #------------------------------ Clear
    
    idval=StringVar()
    nameval=StringVar()
    mobileval=StringVar()
    emailval=StringVar()
    addressval=StringVar()
    genderval=StringVar()
    dobval=StringVar()
    
    #------------------------------ Entry
    
    identry=Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)
    
    nameentry=Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)
    
    mobileentry=Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)
    
    emailentry=Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=190)
    
    addressentry=Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250,y=250)
    
    genderentry=Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250,y=310)
    
    dobentry=Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=250,y=370)
    
    submitntn=Button(addroot,text='Submit',font=('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',bg='orange',command=submitadd)
    submitntn.place(x=150,y=420)
    
    addroot.mainloop()

#------------------------------ Search Button Functionality

def searchstudent():
    def search():
            id=idval.get()
            name=nameval.get()
            contact=mobileval.get()
            email=emailval.get()
            address=addressval.get()
            gender=genderval.get()
            dob=dobval.get()
            addeddate = time.strftime("%d/%m/%Y")
            if(id != ''):
                strr='select * from studentdata1 where id=%s'
                mycursor.execute(strr,(id))
                datas=mycursor.fetchall()
                student_table.delete(*student_table.get_children())
                for i in datas:
                    vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                    student_table.insert('',END,values=vv)
            elif (name != ''):
                strr='select * from studentdata1 where name=%s'
                mycursor.execute(strr,(name))
                datas=mycursor.fetchall()
                student_table.delete(*student_table.get_children())
                for i in datas:
                    vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                    student_table.insert('',END,values=vv)
            elif (contact != ''):
                strr='select * from studentdata1 where contact=%s'
                mycursor.execute(strr,(contact))
                datas=mycursor.fetchall()
                student_table.delete(*student_table.get_children())
                for i in datas:
                    vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                    student_table.insert('',END,values=vv)        
            elif (email != ''):
                strr='select * from studentdata1 where email=%s'
                mycursor.execute(strr,(email))
                datas=mycursor.fetchall()
                student_table.delete(*student_table.get_children())
                for i in datas:
                    vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                    student_table.insert('',END,values=vv)
            elif (address != ''):
                strr='select * from studentdata1 where address=%s'
                mycursor.execute(strr,(address))
                datas=mycursor.fetchall()
                student_table.delete(*student_table.get_children())
                for i in datas:
                    vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                    student_table.insert('',END,values=vv)
            elif (gender != ''):
                strr='select * from studentdata1 where gender=%s'
                mycursor.execute(strr,(gender))
                datas=mycursor.fetchall()
                student_table.delete(*student_table.get_children())
                for i in datas:
                    vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                    student_table.insert('',END,values=vv)
            elif (dob != ''):
                strr='select * from studentdata1 where dob=%s'
                mycursor.execute(strr,(dob))
                datas=mycursor.fetchall()
                student_table.delete(*student_table.get_children())
                for i in datas:
                    vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                    student_table.insert('',END,values=vv)
            elif (addeddate != ''):
                strr='select * from studentdata1 where addeddate=%s'
                mycursor.execute(strr,(addeddate))
                datas=mycursor.fetchall()
                student_table.delete(*student_table.get_children())
                for i in datas:
                    vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                    student_table.insert('',END,values=vv)
    searchroot=Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('470x540+220+200')
    searchroot.title('Student Management System')
    searchroot.config(bg='black')
    searchroot.iconbitmap()
    searchroot.resizable(False,False)
    
    #------------------------------ Label
    
    hostlabel=Label(searchroot,text='Enter Id : ',bg='black',foreground='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=1,width=13,anchor='n')#n
    hostlabel.place(x=10,y=10)
    
    namelabel=Label(searchroot,text='Enter Name : ',bg='black',foreground='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=1,width=13,anchor='n')#n
    namelabel.place(x=10,y=70)
    
    contactlabel=Label(searchroot,text='Enter Contact : ',bg='black',foreground='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=1,width=13,anchor='n')#n
    contactlabel.place(x=10,y=130)
    
    emaillabel=Label(searchroot,text='Enter Email : ',bg='black',foreground='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=1,width=13,anchor='n')#n
    emaillabel.place(x=10,y=190)
    
    addresslabel=Label(searchroot,text='Enter Address : ',bg='black',foreground='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=1,width=13,anchor='n')#n
    addresslabel.place(x=10,y=250)
    
    genderlabel=Label(searchroot,text='Enter Gender : ',bg='black',foreground='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=1,width=13,anchor='n')#n
    genderlabel.place(x=10,y=310)
    
    doblabel=Label(searchroot,text='Enter D.O.B : ',bg='black',foreground='white',font=('times',20,'bold'),relief=GROOVE,borderwidth=1,width=13,anchor='n')#n
    doblabel.place(x=10,y=370)
    
    datelabel=Label(searchroot,text='Date :',font=('times',20,'bold'),bg='black',foreground='white',relief=GROOVE,borderwidth=1,width=13,anchor='n')
    datelabel.place(x=10,y=430)
    
    #------------------------------ Clear
    
    idval=StringVar()
    nameval=StringVar()
    mobileval=StringVar()
    emailval=StringVar()
    addressval=StringVar()
    genderval=StringVar()
    dobval=StringVar()
    dateval=StringVar()
    
    #------------------------------ Entry
    
    identry=Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)
    
    nameentry=Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)
    
    mobileentry=Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)
    
    emailentry=Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=190)
    
    addressentry=Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250,y=250)
    
    genderentry=Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250,y=310)
    
    dobentry=Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=250,y=370)
    
    dateentry=Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=dateval)
    dateentry.place(x=250,y=430)
    
    submitntn=Button(searchroot,text='Submit',font=('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',bg='orange',command=search)
    submitntn.place(x=150,y=485)
    
    searchroot.mainloop()
        
#------------------------------ Delete Button Functionality

def deletestudent():
    cc=student_table.focus()
    content=student_table.item(cc)
    pp=content['values'][0]
    strr='delete from studentdata1 where id=%s'
    mycursor.execute(strr,(pp))
    conn.commit()
    messagebox.showinfo('Notification','Id {} deleted successfully...'.format(pp))
    strr='select * from studentdata1'
    mycursor.execute(strr)
    datas=mycursor.fetchall()
    student_table.delete(*student_table.get_children())
    for i in datas:
        vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
        student_table.insert('',END,values=vv)

#---------------------------- Update Button Functionality

def updatestudent():
    def update():
        id=idval.get()
        name=nameval.get()
        contact=mobileval.get()
        email=emailval.get()
        address=addressval.get()
        gender=genderval.get()
        dob=dobval.get()
        date = dateval.get()
        time = timeval.get()
        
        strr='update studentdata1 set name=%s,contact=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
        mycursor.execute(strr,(name,contact,email,address,gender,dob,date,time,id))
        conn.commit()
        messagebox.showinfo('Notification','Id {} Updated successfully...'.format(id),parent=updateroot)
        strr='select * from studentdata1'
        mycursor.execute(strr)
        datas=mycursor.fetchall()
        student_table.delete(*student_table.get_children())
        for i in datas:
            vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            student_table.insert('',END,values=vv)
        
        
    updateroot=Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('470x600+220+200')
    updateroot.title('Student Managment System')
    updateroot.config(bg='black')
    updateroot.iconbitmap()
    updateroot.resizable(False,False)
    
    #------------------------------ Label
    
    hostlabel=Label(updateroot,text='Enter Id : ',foreground='white',bg='black',font=('times',20,'bold'),relief=GROOVE,borderwidth=1,width=13,anchor='n')#n
    hostlabel.place(x=10,y=10)
    
    namelabel=Label(updateroot,text='Enter Name : ',foreground='white',bg='black',font=('times',20,'bold'),relief=GROOVE,borderwidth=1,width=13,anchor='n')#n
    namelabel.place(x=10,y=70)
    
    contactlabel=Label(updateroot,text='Enter Contact : ',foreground='white',bg='black',font=('times',20,'bold'),relief=GROOVE,borderwidth=1,width=13,anchor='n')#n
    contactlabel.place(x=10,y=130)
    
    emaillabel=Label(updateroot,text='Enter Email : ',foreground='white',bg='black',font=('times',20,'bold'),relief=GROOVE,borderwidth=1,width=13,anchor='n')#n
    emaillabel.place(x=10,y=190)
    
    addresslabel=Label(updateroot,text='Enter Address : ',foreground='white',bg='black',font=('times',20,'bold'),relief=GROOVE,borderwidth=1,width=13,anchor='n')#n
    addresslabel.place(x=10,y=250)
    
    genderlabel=Label(updateroot,text='Enter Gender : ',foreground='white',bg='black',font=('times',20,'bold'),relief=GROOVE,borderwidth=1,width=13,anchor='n')#n
    genderlabel.place(x=10,y=310)
    
    doblabel=Label(updateroot,text='Enter D.O.B : ',foreground='white',bg='black',font=('times',20,'bold'),relief=GROOVE,borderwidth=1,width=13,anchor='n')#n
    doblabel.place(x=10,y=370)
    
    datelabel=Label(updateroot,text='Date :',foreground='white',bg='black',font=('times',20,'bold'),relief=GROOVE,borderwidth=1,width=13,anchor='n')
    datelabel.place(x=10,y=430)
    
    timelabel=Label(updateroot,text='Enter Time : ',foreground='white',bg='black',font=('times',20,'bold'),relief=GROOVE,borderwidth=1,width=13,anchor='n')
    timelabel.place(x=10,y=490)
    
    #-------------------------------- Clear
    
    idval=StringVar()
    nameval=StringVar()
    mobileval=StringVar()
    emailval=StringVar()
    addressval=StringVar()
    genderval=StringVar()
    dobval=StringVar()
    dateval=StringVar()
    timeval=StringVar()
    
    #-------------------------------- Entry
    
    identry=Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)
    
    nameentry=Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)
    
    mobileentry=Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)
    
    emailentry=Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=190)
    
    addressentry=Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250,y=250)
    
    genderentry=Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250,y=310)
    
    dobentry=Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=250,y=370)
    
    dateentry=Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=dateval)
    dateentry.place(x=250,y=430)
    
    timeentry=Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=timeval)
    timeentry.place(x=250,y=490)
    
    submitntn=Button(updateroot,text='Update',font=('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',bg='orange',command=update)
    submitntn.place(x=150,y=545)
    
    cc= student_table.focus()
    content=student_table.item(cc)
    pp=content['values']
    if len(pp) != 0:
        idval.set(pp[0])
        nameval.set(pp[1])
        mobileval.set(pp[2])
        emailval.set(pp[3])
        addressval.set(pp[4])
        genderval.set(pp[5])
        dobval.set(pp[6])
        dateval.set(pp[7])
        timeval.set(pp[8])
    
    updateroot.mainloop()

#--------------------------------------- Show Button Functionality

def showstudent():
        strr='select * from studentdata1'
        mycursor.execute(strr)
        datas=mycursor.fetchall()
        student_table.delete(*student_table.get_children())
        for i in datas:
            vv=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            student_table.insert('',END,values=vv)

#-------------------------------- Saving of the data

def exportstudent():
    ff = filedialog.asksaveasfilename()
    gg = student_table.get_children()
    id,name,mobile,email,address,gender,dob,addeddate,addedtime=[],[],[],[],[],[],[],[],[]
    for i in gg:
        content = student_table.item(i)
        pp = content['values']
        id.append(pp[0]),name.append(pp[1]),mobile.append(pp[2]),email.append(pp[3]),address.append(pp[4]),gender.append(pp[5]),
        dob.append(pp[6]),addeddate.append(pp[7]),addedtime.append(pp[8])
    dd = ['Id','Name','Mobile','Email','Address','Gender','D.O.B','Added Date','Added Time']
    df = pd.DataFrame(list(zip(id,name,mobile,email,address,gender,dob,addeddate,addedtime)),columns=dd)
    paths = r'{}.csv'.format(ff)
    df.to_csv(paths,index=False)
    messagebox.showinfo('Notifications', 'Student data is Saved {}'.format(paths))

        

#------------------------------ Exit button functionality

def exitstudent():
    res = messagebox.askyesnocancel('Notification','Do you wnat to exit?')
    print(res)
    if(res == True):
        root.destroy()

#-------------------------------------------------- Connection2

def Connectdb():
    def submitdb():
        global conn,mycursor
        host=hostval.get()
        user=userval.get()
        password=passwordval.get()
        #host='localhost'
        #user='root'
        #password='your mysql password'

        try:
            conn=pymysql.connect(host=host,user=user,password=password)
            mycursor=conn.cursor()
        except:
            messagebox.showerror('Notification','Data is incorrect',parent=dbroot)
            return
        try:
            strr = 'create database SMS'
            mycursor.execute(strr)
            strr='use SMS'
            mycursor.execute(strr)
            strr='create table studentdata1(id int not null primary key,name varchar(20),contact varchar(12),email varchar(30),address varchar(50),gender varchar(10),dob varchar(20),date varchar(20),time varchar(20))'
            mycursor.execute(strr)
        except:
            strr='use SMS'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','Now You Are Connected To The Database')
            
    dbroot=Toplevel()
    dbroot.grab_set()
    dbroot.geometry('470x250+800+230')
    dbroot.iconbitmap()
    dbroot.resizable(False,False)
    dbroot.config(bg='black')
    
    #----------------------------- Labels
    
    hostlabel=Label(dbroot,text='Enter Host : ',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')#n
    hostlabel.place(x=10,y=10)
    
    userlabel=Label(dbroot,text='Enter User : ',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')#n
    userlabel.place(x=10,y=70)
    
    passwordlabel=Label(dbroot,text='Enter Password : ',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=13,anchor='w')#n
    passwordlabel.place(x=10,y=130)
    
    #-------------------------------------Entry Box

    hostval=StringVar()
    userval=StringVar()
    passwordval=StringVar()
    
    hostentry=Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=hostval)
    hostentry.place(x=250,y=10)
    
    userentry=Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=userval)
    userentry.place(x=250,y=70)
    
    passwordentry=Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=passwordval)
    passwordentry.place(x=250,y=130)
    

#----------------------------------------- Connect Button

    submitbutton=Button(dbroot,text='Submit',font=('roman',15,'bold'),width=20,activebackground='blue',activeforeground='white',bg='orange',bd=5,command=submitdb)
    submitbutton.place(x=150,y=190)

    dbroot.mainloop()

#------------------------------------------ Animation

def tick():
    time_string=time.strftime("%H:%M:%S")
    date_string=time.strftime("%d/%m/%Y")
    clock.config(text='Date :'+date_string+"\n"+"Time :"+time_string)
    clock.after(200,tick)

#------------------------------------------- Styling

import random
colors=['black']
def IntroLabelColorTick():
    fg=random.choice(colors)
    SliderLabel.config(fg=fg)
    SliderLabel.after(2,IntroLabelColorTick)

def IntroLabelTick():
    global count,text
    if(count>=len(ss)):
        count = 0
        text =''
        SliderLabel.config(text=text)
    else:
        text = text+ss[count]
        SliderLabel.config(text=text)
        count+=1
    SliderLabel.after(200,IntroLabelTick)
    
#--------------------------------------- Importing Modules

from tkinter import *
from tkinter import Toplevel
from tkinter import messagebox
from tkinter.ttk import Treeview
from tkinter import filedialog
from tkinter import ttk
import pandas as pd
import pymysql
import time

root=Tk()
root.title("Student Management System")
root.config(bg='black')
root.geometry('1174x700+200+50')
root.resizable(False,False)

#----------------------------------- Frame

DataEntryFrame=Frame(root,bg='black',relief=GROOVE,borderwidth=5)
DataEntryFrame.place(x=10,y=80,width=500,height=600)

#--------------------------------- Label

frontlabel=Label(DataEntryFrame,text='SMS',width=30,font=('roman',25,'italic bold'),bg='black',foreground='white')
frontlabel.pack(side=TOP,expand=True)

addbtn=Button(DataEntryFrame,text='1. Add Student',width=25,font=('roman',20,'bold','italic'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=addstudent)
addbtn.pack(side=TOP,expand=True)

searchbtn=Button(DataEntryFrame,text='2. Search Student',width=25,font=('roman',20,'bold','italic'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=searchstudent)
searchbtn.pack(side=TOP,expand=True)

deletedbtn=Button(DataEntryFrame,text='3. Delete Student',width=25,font=('roman',20,'bold','italic'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=deletestudent)
deletedbtn.pack(side=TOP,expand=True)

updatebtn=Button(DataEntryFrame,text='4. Update Student',width=25,font=('roman',20,'bold','italic'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=updatestudent)
updatebtn.pack(side=TOP,expand=True)

showallbtn=Button(DataEntryFrame,text='5. Show All',width=25,font=('roman',20,'bold','italic'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=showstudent)
showallbtn.pack(side=TOP,expand=True)

exportbtn=Button(DataEntryFrame,text='6. Export Data',width=25,font=('roman',20,'bold','italic'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=exportstudent)
exportbtn.pack(side=TOP,expand=True)

exitbtn=Button(DataEntryFrame,text='7. Exit',width=25,font=('roman',20,'bold','italic'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,activeforeground='white',command=exitstudent)
exitbtn.pack(side=TOP,expand=True)

#----------------------------- Show Frame

ShowDataFrame=Frame(root,bg='black',relief=GROOVE,borderwidth=5)
ShowDataFrame.place(x=550,y=80,width=620,height=600)

#-------------------------------- Styling

style=ttk.Style()
style.configure('Treeview.Heading',font=('Arial',13,'italic'),foreground='black')
style.configure('Treeview',font=('Arial',11,'italic bold'),foreground='black',background='lightgrey',anchor='n')
scroll_x=Scrollbar(ShowDataFrame,orient=HORIZONTAL)
scroll_y=Scrollbar(ShowDataFrame,orient=VERTICAL)
student_table=Treeview(ShowDataFrame,columns=('Id','Name','Contact','Email','Address','Gender','D.O.B','Date','Time'),yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)

scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=student_table.xview)
scroll_y.config(command=student_table.yview)
student_table.heading("Id",text='Id')
student_table.heading("Name",text='Name')
student_table.heading("Contact",text='Contact')
student_table.heading("Email",text="Email")
student_table.heading("Address",text='Address')
student_table.heading("Gender",text='Gender')
student_table.heading("D.O.B",text='D.O.B')
student_table.heading("Date",text="Date")
student_table.heading("Time",text="Time")
student_table['show']='headings'
student_table.column("Id",width=50)
student_table.column("Name",width=150)
student_table.column("Contact",width=100)
student_table.column("Email",width=250)
student_table.column("Address",width=150)
student_table.column("Gender",width=80)
student_table.column("D.O.B",width=90)
student_table.column('Date',width=90)
student_table.column('Time',width=90)
student_table.pack(fill=BOTH,expand=1)

#------------------------------------ Slider

ss='Welcome To Student Management System'
count=0
text=''
SliderLabel=Label(root,text=ss,font=('times',25,'italic bold'),relief=RIDGE,borderwidth=4,width=30,bg='white')
SliderLabel.place(x=260,y=0)
IntroLabelTick()

IntroLabelColorTick()

#------------------------------ Clock

clock=Label(root,font=('time',14,'bold'),relief=RIDGE,borderwidth=4,bg='white',foreground='black')
clock.place(x=0,y=0)
tick()

#--------------------------------- Connection1

connectbutton=Button(root,text='Connect To Database',width=23,font=('times',15,'italic bold'),relief=RIDGE,borderwidth=4,bg='white',activebackground='blue',activeforeground='white',command=Connectdb)
connectbutton.place(x=925,y=0)

#------------------------------------ Looping the program
root.mainloop()
