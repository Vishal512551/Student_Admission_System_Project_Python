import time
from tkinter import*
from tkinter import Toplevel,messagebox
from tkinter.ttk import Treeview
from tkinter import ttk

import pymysql

root=Tk()
root.geometry('1174x700+200+50')
root.title('student admission system')
root.configure(bg='teal')
root.resizable(False,False)
def addstudents():
    def submitadd():
        id=idval.get()
        name=nameval.get()
        mobile=mobileval.get()
        classs=classval.get()
        address=addressval.get()
        gender=genderval.get()
        dob=dobval.get()
        addedtime=time.strftime("%H:%M:%S")
        addeddate=time.strftime("%d/%m/%Y")
        print(id,name)

        try:
            strr = 'insert into studentdata values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr(id, name, mobile, classs, address, gender, dob, addeddate, addedtime))
            con.commit()
            messagebox.showinfo('Notification','Id {}  Name {} Class {} Added sucessfully..and want to cleare the form'.format(id, name, classs), parent=addroot)
            res = messagebox.askyesnocancel('Notification', 'want to clear the the form', parent=addroot)
            if (res == True):
                idval.set('')
                nameval.set('')
                mobileval.set('')
                classval.set('')
                addressval.set('')
                genderval.set('')
                dobval.set('')
        except:
            pass


    addroot=Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('480x480+220+200')
    addroot.title('student admission system')
    addroot.configure(bg='teal')
    addroot.resizable(False,False)
    
    #*************************************add students labels
    
    idlabel=Label(addroot,text='Enter ID:',bg='yellow',font=('forte',20,'bold'),relief=GROOVE,borderwidth=7,width=12,anchor='w')
    idlabel.place(x=10,y=10)
    
    namelabel=Label(addroot,text='Enter Name:',bg='yellow',font=('forte',20,'bold'),relief=GROOVE,borderwidth=7,width=12,anchor='w')
    namelabel.place(x=10,y=70)
    
    mobilelabel=Label(addroot,text='Enter Mobile:',bg='yellow',font=('forte',20,'bold'),relief=GROOVE,borderwidth=7,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)
    
    classlabel=Label(addroot,text='Enter Class:',bg='yellow',font=('forte',20,'bold'),relief=GROOVE,borderwidth=7,width=12,anchor='w')
    classlabel.place(x=10,y=190)
    
    addresslabel=Label(addroot,text='Enter Address:',bg='yellow',font=('forte',20,'bold'),relief=GROOVE,borderwidth=7,width=12,anchor='w')
    addresslabel.place(x=10,y=250)
    
    genderlabel=Label(addroot,text='Enter Gender:',bg='yellow',font=('forte',20,'bold'),relief=GROOVE,borderwidth=7,width=12,anchor='w')
    genderlabel.place(x=10,y=310)

    doblabel=Label(addroot,text='Enter DOB:',bg='yellow',font=('forte',20,'bold'),relief=GROOVE,borderwidth=7,width=12,anchor='w')
    doblabel.place(x=10,y=370)

    #*************************************************add students entry
    idval=StringVar()
    nameval=StringVar()
    mobileval=StringVar()
    classval=StringVar()
    addressval=StringVar()
    genderval=StringVar()
    dobval=StringVar()

    
    identry=Entry(addroot,font=('forte',15,'bold'),bd=6,width=17,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry=Entry(addroot,font=('forte',15,'bold'),bd=6,width=17,textvariable=nameval)
    nameentry.place(x=250,y=70)

    mobileentry=Entry(addroot,font=('forte',15,'bold'),bd=6,width=17,textvariable=mobileval)
    mobileentry.place(x=250,y=130)

    classentry=Entry(addroot,font=('forte',15,'bold'),bd=6,width=17,textvariable=classval)
    classentry.place(x=250,y=190)

    addressentry=Entry(addroot,font=('forte',15,'bold'),bd=6,width=17,textvariable=addressval)
    addressentry.place(x=250,y=250)

    genderentry=Entry(addroot,font=('forte',15,'bold'),bd=6,width=17,textvariable=genderval)
    genderentry.place(x=250,y=310)

    dobentry=Entry(addroot,font=('forte',15,'bold'),bd=6,width=17,textvariable=dobval)
    dobentry.place(x=250,y=370)

    #*********************************************add botton

    submitbtn=Button(addroot,text='submit',font=('forte',15,'bold'),width=15,bd=5,activebackground='blue',activeforeground='white',bg='red',command=submitadd)
    submitbtn.place(x=150,y=420)
    addroot.mainloop()
    
def searchstudents():
    def search():
        print('search')
    searchroot=Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('470x540+220+200')
    searchroot.title('student admission system')
    searchroot.configure(bg='teal')
    searchroot.resizable(False,False)
    
    #*************************************add students labels
    
    idlabel=Label(searchroot,text='Enter ID:',bg='yellow',font=('forte',20,'bold'),relief=GROOVE,borderwidth=7,width=12,anchor='w')
    idlabel.place(x=10,y=10)
    
    namelabel=Label(searchroot,text='Enter Name:',bg='yellow',font=('forte',20,'bold'),relief=GROOVE,borderwidth=7,width=12,anchor='w')
    namelabel.place(x=10,y=70)
    
    mobilelabel=Label(searchroot,text='Enter Mobile:',bg='yellow',font=('forte',20,'bold'),relief=GROOVE,borderwidth=7,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)
    
    classlabel=Label(searchroot,text='Enter Class:',bg='yellow',font=('forte',20,'bold'),relief=GROOVE,borderwidth=7,width=12,anchor='w')
    classlabel.place(x=10,y=190)
    
    addresslabel=Label(searchroot,text='Enter Address:',bg='yellow',font=('forte',20,'bold'),relief=GROOVE,borderwidth=7,width=12,anchor='w')
    addresslabel.place(x=10,y=250)
    
    genderlabel=Label(searchroot,text='Enter Gender:',bg='yellow',font=('forte',20,'bold'),relief=GROOVE,borderwidth=7,width=12,anchor='w')
    genderlabel.place(x=10,y=310)

    doblabel=Label(searchroot,text='Enter DOB:',bg='yellow',font=('forte',20,'bold'),relief=GROOVE,borderwidth=7,width=12,anchor='w')
    doblabel.place(x=10,y=370)

    datelabel=Label(searchroot,text='Enter DATE:',bg='yellow',font=('forte',20,'bold'),relief=GROOVE,borderwidth=7,width=12,anchor='w')
    datelabel.place(x=10,y=430)

    #*************************************************add students entry
    idval=StringVar()
    nameval=StringVar()
    mobileval=StringVar()
    classval=StringVar()
    addressval=StringVar()
    genderval=StringVar()
    dobval=StringVar()
    dateval=StringVar()
    
    identry=Entry(searchroot,font=('forte',15,'bold'),bd=6,width=17,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry=Entry(searchroot,font=('forte',15,'bold'),bd=6,width=17,textvariable=nameval)
    nameentry.place(x=250,y=70)

    mobileentry=Entry(searchroot,font=('forte',15,'bold'),bd=6,width=17,textvariable=mobileval)
    mobileentry.place(x=250,y=130)

    classentry=Entry(searchroot,font=('forte',15,'bold'),bd=6,width=17,textvariable=classval)
    classentry.place(x=250,y=190)

    addressentry=Entry(searchroot,font=('forte',15,'bold'),bd=6,width=17,textvariable=addressval)
    addressentry.place(x=250,y=250)

    genderentry=Entry(searchroot,font=('forte',15,'bold'),bd=6,width=17,textvariable=genderval)
    genderentry.place(x=250,y=310)


    dobentry = Entry(searchroot, font=('forte', 15, 'bold'), bd=6, width=17, textvariable=dateval)
    dobentry.place(x=250, y=370)

    dateentry=Entry(searchroot,font=('forte',15,'bold'),bd=6,width=17,textvariable=dateval)
    dateentry.place(x=250,y=440)
    #*********************************************add botton

    submitbtn=Button(searchroot,text='submit',font=('forte',15,'bold'),width=15,bd=5,activebackground='blue',activeforeground='white',bg='red',command=search)
    submitbtn.place(x=150,y=485)
    searchroot.mainloop()

def deletestudents():
    def delete():
        print('delete')
    deleteroot=Toplevel(master=DataEntryFrame)
    deleteroot.grab_set()
    deleteroot.geometry('510x590+200+180')
    deleteroot.title('student admission system')
    deleteroot.configure(bg='teal')
    deleteroot.resizable(False,False)
    #*************************************add students labels
    
    idlabel=Label(deleteroot,text='Enter ID:',bg='yellow',font=('forte',20,'bold'),relief=GROOVE,borderwidth=7,width=12,anchor='w')
    idlabel.place(x=10,y=10)
    
    namelabel=Label(deleteroot,text='Enter Name:',bg='yellow',font=('forte',20,'bold'),relief=GROOVE,borderwidth=7,width=12,anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel=Label(deleteroot,text='Enter Mobile:',bg='yellow',font=('forte',20,'bold'),relief=GROOVE,borderwidth=7,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)
    
    classlabel=Label(deleteroot,text='Enter Class:',bg='yellow',font=('forte',20,'bold'),relief=GROOVE,borderwidth=7,width=12,anchor='w')
    classlabel.place(x=10,y=190)
    
    addresslabel=Label(deleteroot,text='Enter Address:',bg='yellow',font=('forte',20,'bold'),relief=GROOVE,borderwidth=7,width=12,anchor='w')
    addresslabel.place(x=10,y=250)

    genderlabel=Label(deleteroot,text='Enter Gender:',bg='yellow',font=('forte',20,'bold'),relief=GROOVE,borderwidth=7,width=12,anchor='w')
    genderlabel.place(x=10,y=310)

    doblabel=Label(deleteroot,text='Enter DOB:',bg='yellow',font=('forte',20,'bold'),relief=GROOVE,borderwidth=7,width=12,anchor='w')
    doblabel.place(x=10,y=370)

    datelabel=Label(deleteroot,text='Enter DATE:',bg='yellow',font=('forte',20,'bold'),relief=GROOVE,borderwidth=7,width=12,anchor='w')
    datelabel.place(x=10,y=430)
    
    #*************************************************add students entry
    idval=StringVar()
    nameval=StringVar()
    mobileval=StringVar()
    classval=StringVar()
    addressval=StringVar()
    genderval=StringVar()
    dobval=StringVar()
    dateval=StringVar()

    
    identry=Entry(deleteroot,font=('forte',15,'bold'),bd=6,width=17,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry=Entry(deleteroot,font=('forte',15,'bold'),bd=6,width=17,textvariable=nameval)
    nameentry.place(x=250,y=70)

    mobileentry=Entry(deleteroot,font=('forte',15,'bold'),bd=6,width=17,textvariable=mobileval)
    mobileentry.place(x=250,y=130)

    classentry=Entry(deleteroot,font=('forte',15,'bold'),bd=6,width=17,textvariable=classval)
    classentry.place(x=250,y=190)

    addressentry=Entry(deleteroot,font=('forte',15,'bold'),bd=6,width=17,textvariable=addressval)
    addressentry.place(x=250,y=250)

    genderentry=Entry(deleteroot,font=('forte',15,'bold'),bd=6,width=17,textvariable=genderval)
    genderentry.place(x=250,y=310)

    dobentry=Entry(deleteroot,font=('forte',15,'bold'),bd=6,width=17,textvariable=dobval)
    dobentry.place(x=250,y=370)

    dateentry=Entry(deleteroot,font=('forte',15,'bold'),bd=6,width=17,textvariable=dateval)
    dateentry.place(x=250,y=430)

    #*********************************************add botton

    submitbtn=Button(deleteroot,text='submit',font=('forte',15,'bold'),width=15,bd=5,activebackground='blue',activeforeground='white',bg='red',command=delete)
    submitbtn.place(x=140,y=510)
    deleteroot.mainloop()


    

    
    
    

def updatestudents():
    def update():
        print('update')
    updateroot=Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('510x590+200+180')
    updateroot.title('student admission system')
    updateroot.configure(bg='teal')
    updateroot.resizable(False,False)
    
    #*************************************add students labels
    
    idlabel=Label(updateroot,text='Enter ID:',bg='yellow',font=('forte',20,'bold'),relief=GROOVE,borderwidth=7,width=12,anchor='w')
    idlabel.place(x=10,y=10)
    
    namelabel=Label(updateroot,text='Enter Name:',bg='yellow',font=('forte',20,'bold'),relief=GROOVE,borderwidth=7,width=12,anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel=Label(updateroot,text='Enter Mobile:',bg='yellow',font=('forte',20,'bold'),relief=GROOVE,borderwidth=7,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)
    
    classlabel=Label(updateroot,text='Enter Class:',bg='yellow',font=('forte',20,'bold'),relief=GROOVE,borderwidth=7,width=12,anchor='w')
    classlabel.place(x=10,y=190)
    
    addresslabel=Label(updateroot,text='Enter Address:',bg='yellow',font=('forte',20,'bold'),relief=GROOVE,borderwidth=7,width=12,anchor='w')
    addresslabel.place(x=10,y=250)
    
    genderlabel=Label(updateroot,text='Enter Gender:',bg='yellow',font=('forte',20,'bold'),relief=GROOVE,borderwidth=7,width=12,anchor='w')
    genderlabel.place(x=10,y=310)

    doblabel=Label(updateroot,text='Enter DOB:',bg='yellow',font=('forte',20,'bold'),relief=GROOVE,borderwidth=7,width=12,anchor='w')
    doblabel.place(x=10,y=370)

    datelabel=Label(updateroot,text='Enter DATE:',bg='yellow',font=('forte',20,'bold'),relief=GROOVE,borderwidth=7,width=12,anchor='w')
    datelabel.place(x=10,y=430)

    timelabel=Label(updateroot,text='Enter TIME:',bg='yellow',font=('forte',20,'bold'),relief=GROOVE,borderwidth=7,width=12,anchor='w')
    timelabel.place(x=10,y=490)

    #*************************************************add students entry
    idval=StringVar()
    nameval=StringVar()
    mobileval=StringVar()
    classval=StringVar()
    addressval=StringVar()
    genderval=StringVar()
    dobval=StringVar()
    dateval=StringVar()
    timeval=StringVar()
    
    identry=Entry(updateroot,font=('forte',15,'bold'),bd=6,width=17,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry=Entry(updateroot,font=('forte',15,'bold'),bd=6,width=17,textvariable=nameval)
    nameentry.place(x=250,y=70)

    mobileentry=Entry(updateroot,font=('forte',15,'bold'),bd=6,width=17,textvariable=mobileval)
    mobileentry.place(x=250,y=130)

    classentry=Entry(updateroot,font=('forte',15,'bold'),bd=6,width=17,textvariable=classval)
    classentry.place(x=250,y=190)

    addressentry=Entry(updateroot,font=('forte',15,'bold'),bd=6,width=17,textvariable=addressval)
    addressentry.place(x=250,y=250)

    genderentry=Entry(updateroot,font=('forte',15,'bold'),bd=6,width=17,textvariable=genderval)
    genderentry.place(x=250,y=310)

    dobentry=Entry(updateroot,font=('forte',15,'bold'),bd=6,width=17,textvariable=dobval)
    dobentry.place(x=250,y=370)

    dateentry=Entry(updateroot,font=('forte',15,'bold'),bd=6,width=17,textvariable=dateval)
    dateentry.place(x=250,y=430)

    timeentry=Entry(updateroot,font=('forte',15,'bold'),bd=6,width=17,textvariable=timeval)
    timeentry.place(x=250,y=490)
    #*********************************************add botton

    submitbtn=Button(updateroot,text='submit',font=('forte',15,'bold'),width=15,bd=5,activebackground='blue',activeforeground='white',bg='red',command=update)
    submitbtn.place(x=150,y=540)
    updateroot.mainloop()
def showstudents():
    print('student show')
def exitstudents():
    res=messagebox.askyesnocancel('notification','do you want to exit')
    if(res==True):
        root.destroy()

#**************************************connection of database
def connectdb():
    def submitdb():
        global con,mycursor,strr
        host=hostval.get()
        user=userval.get()
        password=passwordval.get()

        try:
            con=pymysql.Connect(host=host,user=user,password=password)
            mycursor=con.cursor()
        except:
            messagebox.showerror('Notification','inncorrect data')
            return

        try:
            strr='create database studentadmission'
            mycursor.execute(strr)
            strr='use studentadmission'
            mycursor.execute(strr)
            strr='create table studentdata(id int ,name varchar(20), mobile varchar(12), class varchar(30),address varchar(100),gender varchar(50),dob varchar(50),date varchar(50),time varchar(50) )'
            mycursor.execute(strr)
            strr = 'alter table studentdata modify column id int not null'
            mycursor.execute(strr)
            strr = 'alter table studentdata modify column id int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('Notification', ' Database crested and now you are connected to the database...', parent=dbroot)



        except:
            strr='use studentadmission'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','Now you are connected to the database...', parent=dbroot)
        dbroot.destroy()




    dbroot= Toplevel()
    dbroot.grab_set()
    dbroot.geometry('470x250+800+230')
    dbroot.resizable(False,False)
    dbroot.configure(bg='teal')
#********************************connect db levels

    hostlevel=Label(dbroot,text="Enter Host:",bg='teal',font=('forte',18,'bold'),relief=GROOVE,borderwidth=3,width=15 ,anchor='w')
    hostlevel.place(x=10,y=10)

    userlevel=Label(dbroot,text="Enter User:",bg='teal',font=('forte',18,'bold'),relief=GROOVE,borderwidth=3,width=15 ,anchor='w')
    userlevel.place(x=10,y=70)

    passwordlevel=Label(dbroot,text="Enter Password:",bg='teal',font=('forte',18,'bold'),relief=GROOVE,borderwidth=3,width=15 ,anchor='w')
    passwordlevel.place(x=10,y=130)

#********************************connect db entry
    hostval=StringVar()
    userval=StringVar()
    passwordval=StringVar()

    hostentry=Entry(dbroot,font=('forte',15,'bold'),bd=5,width=15,textvariable=hostval)
    hostentry.place(x=250,y=10)

    userentry=Entry(dbroot,font=('forte',15,'bold'),bd=5,width=15,textvariable=userval)
    userentry.place(x=250,y=70)

    passwordentry=Entry(dbroot,font=('forte',15,'bold'),bd=5,width=15,textvariable=passwordval)
    passwordentry.place(x=250,y=130)

#********************************connect db button

    submitbutton=Button(dbroot,text='Submit',font=('forte',15,'bold'),bg='red',bd=5,width=17,activebackground='blue',
                        activeforeground='white',command=submitdb)
    submitbutton.place(x=130,y=190)


    dbroot.mainloop()


#********************************************
DataEntryFrame = Frame(root,bg='teal',relief=GROOVE,borderwidth=5)
DataEntryFrame.place(x=10,y=80,width=500,height=600) 
frontlabel=Label(DataEntryFrame,text='---------WELCOME---------',width=25,font=('forte',20,'bold'),bg='teal')
frontlabel.pack(side=TOP,expand=True)

addbtn=Button(DataEntryFrame,text='1. Add Student',width=25,font=('forte',20,'bold'),relief=GROOVE,bd=6,bg='pink',activebackground='blue',activeforeground='white',command=addstudents)
addbtn.pack(side=TOP,expand=True)

searchbtn=Button(DataEntryFrame,text='2. Search Student',width=25,font=('forte',20,'bold'),relief=GROOVE,bd=6,bg='pink',activebackground='blue',activeforeground='white',command=searchstudents)
searchbtn.pack(side=TOP,expand=True)

deletebtn=Button(DataEntryFrame,text='3. Delete Student',width=25,font=('forte',20,'bold'),relief=GROOVE,bd=6,bg='pink',activebackground='blue',activeforeground='white',command=deletestudents)
deletebtn.pack(side=TOP,expand=True)

updatebtn=Button(DataEntryFrame,text='4. Update Student',width=25,font=('forte',20,'bold'),relief=GROOVE,bd=6,bg='pink',activebackground='blue',activeforeground='white',command=updatestudents)
updatebtn.pack(side=TOP,expand=True)

showbtn=Button(DataEntryFrame,text='5. Show All',width=25,font=('forte',20,'bold'),relief=GROOVE,bd=6,bg='pink',activebackground='blue',activeforeground='white',command=showstudents)
showbtn.pack(side=TOP,expand=True)

exitbtn=Button(DataEntryFrame,text='6. Exit',width=25,font=('forte',20,'bold'),relief=GROOVE,bd=6,bg='pink',activebackground='blue',activeforeground='white',command=exitstudents)
exitbtn.pack(side=TOP,expand=True)

#*********************************************show data frames
style = ttk.Style()
style.configure('Treeview.Heading',font=('chiller',20,'bold'),foreground='blue')
style.configure('Treeview',font=('times',15,'bold'),foreground='black',background='cyan')
ShowDataFrame = Frame(root,bg='teal',relief=GROOVE,borderwidth=5)
ShowDataFrame.place(x=550,y=80,width=620,height=600)
scroll_x=Scrollbar(ShowDataFrame,orient=HORIZONTAL)
scroll_y=Scrollbar(ShowDataFrame,orient=VERTICAL)


studenttable = Treeview(ShowDataFrame,columns=('Id','Name','Mobile No','Class','Address','Gender','D.O.B','Added Date','Added Time'),yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=studenttable.xview)
scroll_y.config(command=studenttable.yview)
studenttable.heading('Id',text='Id')
studenttable.heading('Name',text='Name')
studenttable.heading('Mobile No',text='Mobile No')
studenttable.heading('Class',text='Class')
studenttable.heading('Address',text='Address')
studenttable.heading('Gender',text='Gender')
studenttable.heading('D.O.B',text='D.O.B')
studenttable.heading('Added Date',text='Added Date')
studenttable.heading('Added Time',text='Added Time')
studenttable['show']='headings'

studenttable.pack(fill=BOTH,expand=1)
                        

#********************************************slider
lbl1=Label(root,text='STUDENT ADMISSION SYSTEM',fg='black',bg='teal',font=('forte',25,'bold'))
lbl1.place(x=250,y=0)


#*******************************************
connectbutton=Button(root,text='connect to database',width=25,font=('forte',17,'bold'),relief=GROOVE,anchor='w',borderwidth=4,bg='teal',activebackground='blue',activeforeground='white',command=connectdb)
connectbutton.place(x=930,y=0)





root.mainloop()
