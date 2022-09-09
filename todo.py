import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *
 
def GetValue(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0,select['time'])
    e2.insert(0,select['work'])
    e3.insert(0,select['venue'])

 
 
def Add():
    time = e1.get()
    work = e2.get()
    venue = e3.get()
 
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="swastikabose",database="todo")
    mycursor=mysqldb.cursor()
 
    try:
       sql = "INSERT INTO  todo2 (time, work, venue) VALUES (%s, %s, %s)"
       val = (time, work, venue)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "Employee inserted successfully...")
       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e1.focus_set()
    except Exception as e:
       print(e)
       mysqldb.rollback()
       mysqldb.close()
 
 
def update():
    time = e1.get()
    work = e2.get()
    venue = e3.get()
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="swastikabose",database="todo")
    mycursor=mysqldb.cursor()
 
    try:
       sql = "Update todo2 set time= %s,work= %s,venue= %s where work= %s"
       val = (time, work, venue, work)
       mycursor.execute(sql, val)

       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "Record Updateddddd successfully...")
 
       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e1.focus_set()
 
    except Exception as e:
 
       print(e)
       mysqldb.rollback()
       mysqldb.close()
 
def delete():
    studid = e1.get()
 
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="swastikabose",database="todo")
    mycursor=mysqldb.cursor()
 
    try:
       sql="delete from todo1 where work=%s"
       val = (studid,)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "Record Delete successfully...")
 
       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e1.focus_set()
 
    except Exception as e:

 
       print(e)
       mysqldb.rollback()
       mysqldb.close()
 
def show():
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="swastikabose", database="todo")
        mycursor = mysqldb.cursor()
        mycursor.execute("select * from todo2")
        records = mycursor.fetchall()
        print(records)
 
        for i, (time,work,venue ) in enumerate(records, start=1):
            listBox.insert("", "end", values=(time, work, venue))
            mysqldb.close()
 
root = Tk()
root.geometry("800x500")
global e1
global e2
global e3
 
tk.Label(root, text="To-Do list", fg="red", font=(None, 30)).place(x=300, y=5)
 
tk.Label(root, text="Time").place(x=10, y=10)
Label(root, text="Work").place(x=10, y=40)
Label(root, text="Venue").place(x=10, y=70)

 
e1 = Entry(root)
e1.place(x=140, y=10)
 
e2 = Entry(root)
e2.place(x=140, y=40)
 
e3 = Entry(root)
e3.place(x=140, y=70)
 
 
Button(root, text="Add",command = Add,height=3, width= 13).place(x=30, y=130)
Button(root, text="update",command = update,height=3, width= 13).place(x=140, y=130)
Button(root, text="Delete",command = delete,height=3, width= 13).place(x=250, y=130)
 
cols = ('time', 'work', 'venue')
listBox = ttk.Treeview(root, columns=cols, show='headings' )
 
for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=10, y=200)
 
show()
listBox.bind('<Double-Button-1>',GetValue)
 
root.mainloop()

