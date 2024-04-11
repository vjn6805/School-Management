
from tkinter import *
import mysql.connector as sq
from tkinter import ttk,messagebox
import os

def open_lib():
	lib = Tk()
	lib.title('School Library')
	lib.geometry('1000x500')
	lib.configure(bg='#008080')
	l1 = Label(lib, text='Welcome to School Library !', font=('Times new roman',12), fg='white', bg='#008080')
	l1.place(x=20,y=20)
	myc = sq.connect(host='localhost',user='root',passwd='veersql@computer',database='project')
	cursor=myc.cursor()

def view_books():
	frame = LabelFrame(lib, text='List of Books',padx=15,pady=15, bg='light blue')
	frame.place(x=250,y=50)
	cursor.execute('select * from books')
	i=0
	for book in cursor:
		for j in range(len(book)):
			e = Entry(frame, width=23, bg='pink', font=('Times New Roman',8))
			e.grid(row=i, column=j)
			e.insert(END, book[j])
		i=i+1

def add_stu():
	def submit():
		sname1 = sname.get()
		stuid1 = stuid.get()
		bid1 = bid.get()
		try:
			sql = "insert into students(stuid,sname,bid) values (%s,%s,%s)"
			val = (stuid1,sname1,bid1)
			cursor.execute(sql,val)
			messagebox.showinfo('Information','Record added succesfully !')
			update = 'update books set qty=qty-1 where bookid="%s"' %(bid1)
			cursor.execute(update)
			myc.commit()
		except Exception as e:
			messagebox.showerror('Error',e)
			myc.rollback()
			myc.close()
	add = Tk()
	add.title('Add Student Record')
	add.geometry('350x300')
	add.configure(bg='#476b6b')
	global stuid
	global sname
	global bid
	stuid_label = Label(add, text='Student ID',bg='light blue')
	stuid_label.place(x=50,y=50)
	sname_label = Label(add, text='Student Name',bg='light blue')
	sname_label.place(x=50,y=100)
	bid_label = Label(add, text='Book ID',bg='light blue')
	bid_label.place(x=50,y=150)
	stuid = Entry(add, width=25,bg='light blue')
	stuid.place(x=150,y=50)
	sname = Entry(add, width=25,bg='light blue')
	sname.place(x=150,y=100)
	bid = Entry(add, width=25,bg='light blue')
	bid.place(x=150,y=150)
	submit_btn = Button(add, text='Add Student Record', command=submit,bg='light blue')
	submit_btn.place(x=100,y=200)

def view_books():
	frame = LabelFrame(lib, text='List of Books',padx=15,pady=15, bg='light blue')
	frame.place(x=300,y=50)
	cursor.execute('select * from books')
	i=0
	for book in cursor:
		for j in range(len(book)):
			e = Entry(frame, width=23, bg='#8080ff', font=('Times New Roman',8))
			e.grid(row=i, column=j)
			e.insert(END, book[j])
		i=i+1

def view_stu1():
	stu = Tk()
	stu.title('Issued')
	cursor.execute('select students.stuid,students.sname,books.bname from students,books where students.status="issued" and students.bid=books.bookid')
	i=0
	for book in cursor:
		for j in range(len(book)):
			e = Entry(stu, width=23, bg='#d699ff', font=('Times New Roman',8))
			e.grid(row=i, column=j)
			e.insert(END, book[j])
		i=i+1

def view_stu2():
	stu = Tk()
	stu.title('Returned')
	cursor.execute('select students.stuid,students.sname,books.bname from students,books where students.status="returned" and students.bid=books.bookid')
	i=0
	for book in cursor:
		for j in range(len(book)):
			e = Entry(stu, width=23, bg='#d699ff', font=('Times New Roman',8))
			e.grid(row=i, column=j)
			e.insert(END, book[j])
		i=i+1

def return_book():
	def submit():
		stu = estu.get()
		book = ebook.get()
		try:
			returnb = "update students set status='Returned' where bid='%s' and stuid='%s'" %(book,stu)
			cursor.execute(returnb)
			update = 'update books set qty=qty+1 where bookid="%s"' %(book)
			cursor.execute(update)
			myc.commit()
			messagebox.showinfo('Information','Book Returned !')
		except Exception as e:
			messagebox.showerror('Error',e)
			myc.rollback()
			myc.close()
	global ebook 
	global estu 
	ret = Tk()
	ret.title('Return Book')
	ret.geometry('400x300')
	ret.configure(bg='#ac3939')
	lstu = Label(ret, text='Enter Student ID',bg='light blue')
	lstu.place(x=50,y=50)
	estu = Entry(ret, width=25,bg='light blue')
	estu.place(x=150,y=50)
	lbook = Label(ret, text='Enter Book ID',bg='light blue')
	lbook.place(x=50,y=100)
	ebook = Entry(ret, width=25,bg='light blue')
	ebook.place(x=150,y=100)
	b = Button(ret, text='Return Book',command=submit,bg='light blue')
	b.place(x=150,y=200)

b1 = Button(lib, text = 'View list of books',command=view_books,bg='light blue')
b1.place(x=70,y=100)
b2 = Button(lib, text = 'Enter student record',command=add_stu,bg='light blue')
b2.place(x=70,y=150)
b3 = Button(lib, text = 'Update - Return Book',command=return_book,bg='light blue')
b3.place(x=70,y=200)
b4 = Button(lib, text = 'View list of students - Issued',command=view_stu1,bg='light blue')
b4.place(x=70,y=250)
b5 = Button(lib, text = 'View list of students - Returned',command=view_stu2,bg='light blue')
b5.place(x=70,y=300)
exitb = Button(lib, text='Exit',width=15, command=lib.destroy, bg='light blue')
exitb.place(x=70,y=350)

def act():
	act = Tk()
	act.title('Activities and Events')
	act.geometry('400x400')
	act.configure(bg='#cc7a00')
	label1 = Label(act,text='Welcome to Activities and Events Section !',bg='#cc7a00',font=('Times new roman',12))
	label1.place(x=20,y=20)

def up():
	up = Tk()
	up.title('Upcoming Events')
	myc = sq.connect(host='localhost',user='root',passwd='rheachainani',database='project')
	cursor = myc.cursor()
	cursor.execute('select curdate()')
	today = cursor.fetchone()
	upc = "select event,catagory,evdate from events where evdate >= '%s'" %(today)
	cursor.execute(upc)
	i=0
	for ev in cursor:
		for j in range(len(ev)):
			e = Entry(up, width=23, bg='#d699ff', font=('Times New Roman',8))
			e.grid(row=i, column=j)
			e.insert(END, ev[j])
		i=i+1

def past():
	past = Tk()
	past.title('Past Events')
	myc = sq.connect(host='localhost',user='root',passwd='rheachainani',database='project')
	cursor = myc.cursor()
	cursor.execute('select curdate()')
	today = cursor.fetchone()
	pev = "select event,catagory,evdate from events where evdate < '%s'" %(today)
	cursor.execute(pev)
	i=0
	for pastev in cursor:
		for j in range(len(pastev)):
			e = Entry(past, width=23, bg='#d699ff', font=('Times New Roman',8))
			e.grid(row=i, column=j)
			e.insert(END, pastev[j])
		i=i+1

def achieve():
	ach = Tk()
	ach.title('School Achievements')
	myc = sq.connect(host='localhost',user='root',passwd='rheachainani',database='project')
	cursor = myc.cursor()
	cursor.execute('select event,winner from events where winner is not null')
	i=0
	for win in cursor:
		for j in range(len(win)):
			e = Entry(ach, width=23, bg='#d699ff', font=('Times New Roman',8))
			e.grid(row=i, column=j)
			e.insert(END, win[j])
		i=i+1

b1 = Button(act,text='View Upcoming Events',width=35,bg='#ffad33',command=up).place(x=70,y=70)
b2 = Button(act,text='View Past Events',width=35,bg='#ffad33',command=past).place(x=70,y=110)
b3 = Button(act,text='School Achievements',width=35,bg='#ffad33',command=achieve).place(x=70,y=150)
b3 = Button(act,text='Exit',width=35,bg='#ffad33',command=act.destroy).place(x=70,y=230)

def hr():
	root=Tk()
	root.title('Human Resource Department')
	root.geometry('1280x720')
	bg_color='light yellow'

	#variables
	empid_var=IntVar()
	name_var=StringVar()
	gender_var=StringVar()
	email_var=StringVar()
	salary_var=StringVar()
	phone_var=StringVar()
	desig_var=StringVar()

	    #functions

def show():
    if empid_var.get()=='' or name_var.get()=='' or gender_var.get()=='' or salary_var.get()=='' or email_var.get()=='' or phone_var.get()=='' or desig_var.get()=='':
        messagebox.showerror('Empty Field(s)','Please fill all the records')
    else:
        textarea.delete(1.0,END)
        textarea.insert(END, '\n==============================================')
        textarea.insert(END,f'\nEmployee ID :\t\t{empid_var.get()}')
        textarea.insert(END, '\n==============================================')
        textarea.insert(END, f'\n\nFull Name :\t\t{name_var.get()}')
        textarea.insert(END, f'\nEmail Id  :\t\t{email_var.get()}')
        textarea.insert(END, f'\nGender    :\t\t{gender_var.get()}')
        textarea.insert(END, f'\nDesignation :\t\t{desig_var.get()}')
        textarea.insert(END, f'\nContact Number :\t\t{phone_var.get()}')
        textarea.insert(END, f'\nSalary :\t\t{salary_var.get()}')
        textarea.insert(END, f'\nAddress :\t\t{txt_add.get(1.0, END)}')
        textarea.insert(END, '\n\n============================================')
def save():
	data=[empid_var.get(),name_var.get(),email_var.get(),gender_var.get(),desig_var.get(),phone_var.get(),salary_var.get(),txt_add.get(1.0,END)]
	f1=open('hr_dep.txt','a')
	f1.write(' '.join([str(elem) for elem in data]))
	f1.close()
	messagebox.showinfo('Saved',f'EMPID No:{empid_var.get()} Saved Successfully')

def display():
	disp = Tk()
	disp.configure(bg='purple')
	disp.title('Employee Records')
	f1=open('hr_dep.txt','r')
	d=f1.read()
	Label(disp,text=d,bg='light blue',font=('Times New Roman',12)).pack(padx=15,pady=15)
	f1.close()

def reset():
	textarea.delete(1.0,END)
	txt_add.delete(1.0,END)
	empid_var.set(0)
	name_var.set('')
	gender_var.set('')
	phone_var.set('')
	email_var.set('')
	salary_var.set('')

def Exit():
	if messagebox.askyesno('Exit','Do you really want to exit ?'):
	    root.destroy()

	#Heading
title=Label(root,text='Employee Data',bg="purple",fg='white',font=('times new rommon',35,'bold'),relief=GROOVE,bd=12)
title.pack(fill=X)

#LEFT SIDE CODING
F1=Frame(root,bg=bg_color,relief=RIDGE,bd=15)
F1.place(x=10,y=80,width=650,height=540)

lbl_empid=Label(F1,text='Employee ID',font=('times new rommon',20,'bold'),fg='black',bg=bg_color)
lbl_empid.grid(row=0,column=0,padx=30,pady=10)
txt_empid=Entry(F1,font=('times new rommon',18,'bold'),relief=RIDGE,bd=7,textvariable=empid_var)
txt_empid.grid(row=0,column=1,pady=10,sticky='w')

lbl_name=Label(F1,text='Full Name',font=('times new rommon',20,'bold'),fg='black',bg=bg_color)
lbl_name.grid(row=1,column=0,padx=30,pady=10)
txt_name=Entry(F1,font=('times new rommon',18,'bold'),relief=RIDGE,bd=7,textvariable=name_var)
txt_name.grid(row=1,column=1,pady=10,sticky='w')

lbl_email=Label(F1,text='Email Id',font=('times new rommon',20,'bold'),fg='black',bg=bg_color)
lbl_email.grid(row=2,column=0,padx=30,pady=10)
txt_email=Entry(F1,font=('times new rommon',18,'bold'),relief=RIDGE,bd=7,textvariable=email_var)
txt_email.grid(row=2,column=1,pady=10,sticky='w')

lbl_Gender=Label(F1,text='Gender',font=('times new rommon',20,'bold'),fg='black',bg=bg_color)
lbl_Gender.grid(row=3,column=0,padx=30,pady=10)

combo_gender=ttk.Combobox(F1,font=('times new rommon',18),state='readonly',textvariable=gender_var)
combo_gender['value']=('Male','Female','Others')
combo_gender.grid(row=3,column=1,pady=10)

lbl_des=Label(F1,text='Department',font=('times new rommon',20,'bold'),fg='black',bg=bg_color)
lbl_des.grid(row=4,column=0,padx=30,pady=10)

combo_des=ttk.Combobox(F1,font=('times new rommon',18),state='readonly',textvariable=desig_var)
combo_des['value']=('HR DEPARTMENT','ACCOUNTS','SCIENCE(PCMB)','COMMERCE','ARTS','TRANSPORT','SPORTS')
combo_des.grid(row=4,column=1,pady=10)

lbl_no=Label(F1,text='Contact No.',font=('times new rommon',20,'bold'),fg='black',bg=bg_color)
lbl_no.grid(row=5,column=0,padx=30,pady=10)
txt_no=Entry(F1,font=('times new rommon',18,'bold'),relief=RIDGE,bd=7,textvariable=phone_var)
txt_no.grid(row=5,column=1,pady=10,sticky='w')

lbl_s=Label(F1,text='Salary',font=('times new rommon',20,'bold'),fg='black',bg=bg_color)
lbl_s.grid(row=6,column=0,padx=30,pady=10)
txt_s=Entry(F1,font=('times new rommon',18,'bold'),relief=RIDGE,bd=7,textvariable=salary_var)
txt_s.grid(row=6,column=1,pady=10,sticky='w')

lbl_add=Label(F1,text='Address',font=('times new rommon',20,'bold'),fg='black',bg=bg_color)
lbl_add.grid(row=7,column=0,padx=30,pady=10)
txt_add=Text(F1,width=40,height=2,font=('times new rommon',10),relief=RIDGE,bd=7)
txt_add.grid(row=7,column=1,pady=5,sticky='w')

	#RIGHT SIDE CODING
F2=Frame(root,bg=bg_color,relief=RIDGE,bd=15)
F2.place(x=665,y=80,width=610,height=540)

lbl_t=Label(F2,text='Employee Details',font=('arial 15 bold'),fg='black',bd=7,relief=GROOVE)
lbl_t.pack(fill=X)

scrol=Scrollbar(F2,orient=VERTICAL)
scrol.pack(side=RIGHT,fill=Y)
textarea=Text(F2,font='arial 15',yscrollcommand=scrol.set)
textarea.pack(fill=BOTH)
scrol.config(command=textarea.yview)

	#BUTTONS
F3=Frame(root,bg=bg_color,relief=RIDGE,bd=15)
F3.place(x=10,y=615,width=1260,height=100)

btn1=Button(F3,text='Show',font='arial 20 bold',bg='green',fg='black',width=10,command=show)
btn1.grid(row=0,column=0,padx=25,pady=7)

btn2=Button(F3,text='Save',font='arial 20 bold',bg='green',fg='black',width=10,command=save)
btn2.grid(row=0,column=1,padx=25,pady=7)

btn4=Button(F3,text='Reset',font='arial 20 bold',bg='green',fg='black',width=10,command=reset)
btn4.grid(row=0,column=3,padx=25,pady=7)

btn5=Button(F3,text='Display All',font='arial 20 bold',bg='green',fg='black',width=10,command=display)
btn5.grid(row=0,column=4,padx=25,pady=7)

btn6=Button(F3,text='Exit',font='arial 20 bold',bg='green',fg='black',width=10,command=Exit)
btn6.grid(row=0,column=5,padx=25,pady=7)

def acad():
	root=Tk()
	root.title('Academics')
	root.geometry('1280x720')
	bg_color='light yellow'

	#variables
	admn_var=IntVar()
	name_var=StringVar()
	class_var=StringVar()
	chem_var=IntVar()
	phy_var=IntVar()
	math_var=IntVar()
	cs_var=IntVar()
	eng_var=IntVar()

	admn_var.set('')

	#functions

def show():
    if empid_var.get()=='' or name_var.get()=='' or gender_var.get()=='' or salary_var.get()=='' or email_var.get()=='' or phone_var.get()=='' or desig_var.get()=='':
        messagebox.showerror('Empty Field(s)','Please fill all the records')
    else:
        textarea.delete(1.0,END)
        textarea.insert(END, '\n==============================================')
        textarea.insert(END,f'\nEmployee ID :\t\t{empid_var.get()}')
        textarea.insert(END, '\n==============================================')
        textarea.insert(END, f'\n\nFull Name :\t\t{name_var.get()}')
        textarea.insert(END, f'\nEmail Id  :\t\t{email_var.get()}')
        textarea.insert(END, f'\nGender    :\t\t{gender_var.get()}')
        textarea.insert(END, f'\nDesignation :\t\t{desig_var.get()}')
        textarea.insert(END, f'\nContact Number :\t\t{phone_var.get()}')
        textarea.insert(END, f'\nSalary :\t\t{salary_var.get()}')
        textarea.insert(END, f'\nAddress :\t\t{txt_add.get(1.0, END)}')
        textarea.insert(END, '\n\n============================================')

def save():
	avg=(int(chem_var.get())+int(phy_var.get())+int(cs_var.get())+int(math_var.get())+int(eng_var.get()))//5
	data=[admn_var.get(),name_var.get(),class_var.get(),chem_var.get(),phy_var.get(),math_var.get(),eng_var.get(),cs_var.get(),avg,'\n']
	f1=open('acad.txt','a')
	f1.write(' '.join([str(elem) for elem in data]))
	f1.close()
	messagebox.showinfo('Saved',f'Admn No:{admn_var.get()} Saved Successfully')

def display():
	disp = Tk()
	disp.configure(bg='purple')
	disp.title('Student Records')
	f1=open('acad.txt','r')
	d=f1.read()
	Label(disp,text='Admn\tName\t\tClass Chem Phy Math Eng CS Result',bg='light blue',font=('Times New Roman',9)).pack(padx=15,pady=15)
	Label(disp,text=d,bg='light blue',font=('Times New Roman',12)).pack(padx=15,pady=15)
	f1.close()

def reset():
	textarea.delete(1.0,END)
	txt_add.delete(1.0,END)
	empid_var.set('')
	name_var.set('')
	gender_var.set('')
	desig_var.set('')
	phone_var.set('')
	email_var.set('')
	salary_var.set('')

def Exit():
	if messagebox.askyesno('Exit','Do you really want to exit ?'):
	    root.destroy()

	#Heading
title=Label(root,text='Student Data',bg="purple",fg='white',font=('times new rommon',35,'bold'),relief=GROOVE,bd=12)
title.pack(fill=X)

	#LEFT SIDE CODING
F1=Frame(root,bg=bg_color,relief=RIDGE,bd=15)
F1.place(x=10,y=80,width=650,height=540)

lbl_admn=Label(F1,text='Admn No',font=('times new rommon',20,'bold'),fg='black',bg=bg_color)
lbl_admn.grid(row=0,column=0,padx=30,pady=10)
txt_admn=Entry(F1,font=('times new rommon',18,'bold'),relief=RIDGE,bd=7,textvariable=admn_var)
txt_admn.grid(row=0,column=1,pady=10,sticky='w')

lbl_name=Label(F1,text='Student Name',font=('times new rommon',20,'bold'),fg='black',bg=bg_color)
lbl_name.grid(row=1,column=0,padx=30,pady=10)
txt_name=Entry(F1,font=('times new rommon',18,'bold'),relief=RIDGE,bd=7,textvariable=name_var)
txt_name.grid(row=1,column=1,pady=10,sticky='w')

lbl_class=Label(F1,text='Class',font=('times new rommon',20,'bold'),fg='black',bg=bg_color)
lbl_class.grid(row=2,column=0,padx=30,pady=10)

combo_class=ttk.Combobox(F1,font=('times new rommon',18),state='readonly',textvariable=class_var)
combo_class['value']=('12A','12B','12C')
combo_class.grid(row=2,column=1,pady=10)

lbl_chem=Label(F1,text='Chemistry',font=('times new rommon',20,'bold'),fg='black',bg=bg_color)
lbl_chem.grid(row=3,column=0,padx=30,pady=10)
txt_chem=Entry(F1,font=('times new rommon',18,'bold'),relief=RIDGE,bd=7,textvariable=chem_var)
txt_chem.grid(row=3,column=1,pady=10,sticky='w')

lbl_phy=Label(F1,text='Physics',font=('times new rommon',20,'bold'),fg='black',bg=bg_color)
lbl_phy.grid(row=4,column=0,padx=30,pady=10)
txt_phy=Entry(F1,font=('times new rommon',18,'bold'),relief=RIDGE,bd=7,textvariable=phy_var)
txt_phy.grid(row=4,column=1,pady=10,sticky='w')

lbl_math=Label(F1,text='Maths',font=('times new rommon',20,'bold'),fg='black',bg=bg_color)
lbl_math.grid(row=5,column=0,padx=30,pady=10)
txt_math=Entry(F1,font=('times new rommon',18,'bold'),relief=RIDGE,bd=7,textvariable=math_var)
txt_math.grid(row=5,column=1,pady=10,sticky='w')

lbl_eng=Label(F1,text='English',font=('times new rommon',20,'bold'),fg='black',bg=bg_color)
lbl_eng.grid(row=6,column=0,padx=30,pady=10)
txt_eng=Entry(F1,font=('times new rommon',18,'bold'),relief=RIDGE,bd=7,textvariable=eng_var)
txt_eng.grid(row=6,column=1,pady=10,sticky='w')

lbl_cs=Label(F1,text='Comp Science',font=('times new rommon',20,'bold'),fg='black',bg=bg_color)
lbl_cs.grid(row=7,column=0,padx=30,pady=10)
txt_cs=Entry(F1,font=('times new rommon',18,'bold'),relief=RIDGE,bd=7,textvariable=cs_var)
txt_cs.grid(row=7,column=1,pady=10,sticky='w')

	#RIGHT SIDE CODING
F2=Frame(root,bg=bg_color,relief=RIDGE,bd=15)
F2.place(x=665,y=80,width=610,height=540)

lbl_t=Label(F2,text='Academic Details',font=('arial 15 bold'),fg='black',bd=7,relief=GROOVE)
lbl_t.pack(fill=X)

scrol=Scrollbar(F2,orient=VERTICAL)
scrol.pack(side=RIGHT,fill=Y)
textarea=Text(F2,font='arial 15',yscrollcommand=scrol.set)
textarea.pack(fill=BOTH)
scrol.config(command=textarea.yview)

	#BUTTONS
F3=Frame(root,bg=bg_color,relief=RIDGE,bd=15)
F3.place(x=10,y=615,width=1260,height=100)

btn1=Button(F3,text='Show',font='arial 20 bold',bg='green',fg='black',width=10,command=show)
btn1.grid(row=0,column=0,padx=25,pady=7)

btn2=Button(F3,text='Save',font='arial 20 bold',bg='green',fg='black',width=10,command=save)
btn2.grid(row=0,column=1,padx=25,pady=7)

btn3=Button(F3,text='Reset',font='arial 20 bold',bg='green',fg='black',width=10,command=reset)
btn3.grid(row=0,column=3,padx=25,pady=7)

btn4=Button(F3,text='Display All',font='arial 20 bold',bg='green',fg='black',width=10,command=display)
btn4.grid(row=0,column=4,padx=25,pady=7)

btn5=Button(F3,text='Exit',font='arial 20 bold',bg='green',fg='black',width=10,command=Exit)
btn5.grid(row=0,column=5,padx=25,pady=7)

def acc():
	root=Tk()
	root.title('Accounts and Finance')
	root.geometry('1280x720')
	bg_color='light blue'
	#variables
	admn_var=IntVar()
	name_var=StringVar()
	totfee=100000
	dep1_var=IntVar()   #fees deposited

	admn_var.set('')
	name_var.set('')
	dep1_var.set('')

	#functions

def show():
    if empid_var.get()=='' or name_var.get()=='' or gender_var.get()=='' or salary_var.get()=='' or email_var.get()=='' or phone_var.get()=='' or desig_var.get()=='':
        messagebox.showerror('Empty Field(s)','Please fill all the records')
    else:
        textarea.delete(1.0,END)
        textarea.insert(END, '\n==============================================')
        textarea.insert(END,f'\nEmployee ID :\t\t{empid_var.get()}')
        textarea.insert(END, '\n==============================================')
        textarea.insert(END, f'\n\nFull Name :\t\t{name_var.get()}')
        textarea.insert(END, f'\nEmail Id  :\t\t{email_var.get()}')
        textarea.insert(END, f'\nGender    :\t\t{gender_var.get()}')
        textarea.insert(END, f'\nDesignation :\t\t{desig_var.get()}')
        textarea.insert(END, f'\nContact Number :\t\t{phone_var.get()}')
        textarea.insert(END, f'\nSalary :\t\t{salary_var.get()}')
        textarea.insert(END, f'\nAddress :\t\t{txt_add.get(1.0, END)}')
        textarea.insert(END, '\n\n============================================')

def save():
	data=[admn_var.get(),name_var.get(),dep1_var.get(),totfee - int(dep1_var.get()),'\n']
	f1=open('stufee.txt','a')
	f1.write(' '.join([str(elem) for elem in data]))
	f1.close()
	messagebox.showinfo('Saved',f'Student :{admn_var.get()} Saved Successfully')

def display():
	disp = Tk()
	disp.configure(bg='purple')
	disp.title('Fee Data')
	f1=open('stufee.txt','r')
	d=f1.read()
	Label(disp,text='Admn Name Fee Deposited Fee Pending',bg='light blue',font=('Times New Roman',12)).pack(padx=15,pady=15)
	Label(disp,text=d,bg='light blue',font=('Times New Roman',12)).pack(padx=15,pady=15)
	f1.close()

def reset():
	textarea.delete(1.0,END)
	admn_var.set('')
	name_var.set('')
	dep1_var.set('')

def Exit():
	if messagebox.askyesno('Exit','Do you really want to exit ?'):
		 root.destroy()

	#Heading
title=Label(root,text='Fees Data',bg="purple",fg='white',font=('times new rommon',35,'bold'),relief=GROOVE,bd=12)
title.pack(fill=X)

	#LEFT SIDE CODING
F1=Frame(root,bg=bg_color,relief=RIDGE,bd=15)
F1.place(x=10,y=80,width=650,height=540)

lbl_admn=Label(F1,text='Admn No',font=('times new rommon',20,'bold'),fg='black',bg=bg_color)
lbl_admn.grid(row=0,column=0,padx=30,pady=10)
txt_admn=Entry(F1,font=('times new rommon',18,'bold'),relief=RIDGE,bd=7,textvariable=admn_var)
txt_admn.grid(row=0,column=1,pady=10,sticky='w')

lbl_name=Label(F1,text='Student Name',font=('times new rommon',20,'bold'),fg='black',bg=bg_color)
lbl_name.grid(row=1,column=0,padx=30,pady=10)
txt_name=Entry(F1,font=('times new rommon',18,'bold'),relief=RIDGE,bd=7,textvariable=name_var)
txt_name.grid(row=1,column=1,pady=10,sticky='w')

lbl_dep1=Label(F1,text='Fee Deposited',font=('times new rommon',20,'bold'),fg='black',bg=bg_color)
lbl_dep1.grid(row=2,column=0,padx=30,pady=10)
txt_dep1=Entry(F1,font=('times new rommon',18,'bold'),relief=RIDGE,bd=7,textvariable=dep1_var)
txt_dep1.grid(row=2,column=1,pady=10,sticky='w')

	#RIGHT SIDE CODING
F2=Frame(root,bg=bg_color,relief=RIDGE,bd=15)
F2.place(x=665,y=80,width=610,height=540)

lbl_t=Label(F2,text='Fee Details',font=('arial 15 bold'),fg='black',bd=7,relief=GROOVE)
lbl_t.pack(fill=X)

scrol=Scrollbar(F2,orient=VERTICAL)
scrol.pack(side=RIGHT,fill=Y)
textarea=Text(F2,font='arial 15',yscrollcommand=scrol.set)
textarea.pack(fill=BOTH)
scrol.config(command=textarea.yview)

	#BUTTONS
F3=Frame(root,bg=bg_color,relief=RIDGE,bd=15)
F3.place(x=10,y=615,width=1260,height=100)

btn1=Button(F3,text='Show',font='arial 20 bold',fg='black',width=10,command=show)
btn1.grid(row=0,column=0,padx=25,pady=7)

btn2=Button(F3,text='Save',font='arial 20 bold',fg='black',width=10,command=save)
btn2.grid(row=0,column=1,padx=25,pady=7)

btn3=Button(F3,text='Reset',font='arial 20 bold',fg='black',width=10,command=reset)
btn3.grid(row=0,column=2,padx=25,pady=7)

btn4=Button(F3,text='Display All',font='arial 20 bold',fg='black',width=10,command=display)
btn4.grid(row=0,column=3,padx=25,pady=7)

btn5=Button(F3,text='Exit',font='arial 20 bold',fg='black',width=10,command=Exit)
btn5.grid(row=0,column=4,padx=25,pady=7)

def main_page():
	root = Tk()
	root.title('School Management System')
	root.geometry('550x330')
	root.configure(bg='#666699')
	frame1 = LabelFrame(root, bg='#b3b3cc', padx=25, pady=25)
	frame1.grid(row=0,column=0)
	b1 = Button(frame1, text="Accounts and Finance",bg='light blue',command=acc)
	b1.pack()
	frame2 = LabelFrame(root, bg='#b3b3cc', padx=45, pady=25)
	frame2.grid(row=1,column=1)
	b2 = Button(frame2, text="Academics",bg='light blue',command=acad)
	b2.pack()
	frame3 = LabelFrame(root, bg='#b3b3cc', padx=55, pady=25)
	frame3.grid(row=0,column=2)
	b3 = Button(frame3, text="Library",command=open_lib,bg='light blue')
	b3.pack()
	frame4 = LabelFrame(root, bg='#b3b3cc', padx=28, pady=25)
	frame4.grid(row=2,column=0)
	b4 = Button(frame4, text="Human Resources",bg='light blue',command=hr)
	b4.pack()
	frame5 = LabelFrame(root, bg='#b3b3cc', padx=28, pady=25)
	frame5.grid(row=3,column=1)
	b5 = Button(frame5, text="Activities and Events",bg='light blue',command=act)
	b5.pack()
	exitf = LabelFrame(root, bg='light blue', padx=45, pady=25)
	exitf.grid(row=2,column=2)
	exitb = Button(exitf, text='Exit',width=10, command=root.destroy,bg='#b3b3cc')
	exitb.pack()	

def check():
	if E1.get()=='school' and E2.get()=='abc123':
		main_page()
		login.destroy()
	else:
		messagebox.showerror('Error','Invalid Credentials')

login = Tk()
login.geometry('550x200')
login.configure(bg='#339966')
login.title('Password Authentication')

L = Label(login, text='Please enter the correct user id and password in order to login into the system', font=('Times New Roman',12),bg='#339966')
L.place(x=20,y=20)
L1 = Label(login, text='Enter UserID ',bg='#339966')
L1.place(x=20,y=70)
E1 = Entry(login, width=25, bg='#8cd9b3')
E1.place(x=150,y=70)
L2 = Label(login, text='Enter Password ',bg='#339966')
L2.place(x=20,y=100)
E2 = Entry(login, width=25, bg='#8cd9b3', show='*')
E2.place(x=150,y=100)
B1 = Button(login, text='Log In', bg='#8cd9b3', command=check)
B1.place(x=180,y=150)
login.mainloop()

     
 


 
  
 
       

 
 
 

