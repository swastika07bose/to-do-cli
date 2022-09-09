from audioop import add
from msilib.schema import ListBox
from time import time
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
from turtle import update
from typing import List

import mysql.connector
#connecting to mysql
mydb=mysql.connector.connect(host="localhost",user="root",passwd="Sambit03@",database="todo");
#connecting to cursor
mycursor=mydb.cursor()

def GetValue(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0,select["time"])
    e2.insert(0,select["work"])    
    e3.insert(0,select["venue"])    
        

#main menu
# def menu():
#                 print("To-Do list")
#                 print("1. Insert to a to-do list")
#                 print("2. Display a to-do list")
#                 print("3. Update date for an event in to-do list")
#                 print("4. Update venue for an event in to-do list")
#                 print("5. Delete from to-do list")
#                 print("6. Exit")
#                 ch=int(input("Enter Choice"))
#                 if (ch==1):
#                     insert()
#                 elif (ch==2):
#                     display()
#                 elif (ch==3):
#                     upt_time()
#                 elif (ch==4):
#                     upt_venue()
#                 elif (ch==5):
#                     delete()
#                 else:
#                     print("Exit")

                             
def insert():
                # print("To-Do list")
                # ch='y'
                # while (ch=='y'):
                                l=[]
                                l.append(e1.get())
                                l.append(e2.get())
                                l.append(e3.get())
                                
                                todo=(l)
                                sql="insert into todo1 (time,work,ven)values(%s,%s,%s)"
                                mycursor.execute(sql,todo)
                                mydb.commit()
                                messagebox.showinfo("information", "Record added successfully")
                                listBox.insert("", "end", values=(e1.get(),e2.get(),e3.get()))
                                # print("insertion completed")
                                # print("Do you want to insert more work")
                                # ch=input("enter y/n")
                # print('\n' *10)
                # print("==============================================")
                # menu()


          
def delete():
                # print("Delete from To-Do list")
                # wo=input("enter work to be searched")
                # pn=(wo,) 
                iden = e2.get()
                sql="delete from todo1 where work=%s"
                mycursor.execute(sql,iden)
                mydb.commit()
                listBox.delete() #to be corrected, as this command will just delete the listbox, we need to delete only one value
                # print("Deletion completed")
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e1.focus_set()
                # print("Go back to menu")
                # print('\n' *10)
                # print("==============================================")
                # menu()

             
                
def display():
                print("To-Do List")
                sql="select * from todo1"
                mycursor.execute(sql,)
                res=mycursor.fetchall() 
                print(res)
                
                for i,(time, work, ven) in enumerate(res, start=1):
                    listBox.insert("", "end", values=(time,work,ven))
                # for x in res:
                #                 for i in x:
                #                                 print(i)   
                # print("Go back to menu")
                # print('\n')               
                # print("==============================================")
                # # menu()


def update():
    
                # print("Update Venue")
                # work=input("enter event for which venue to be updated: ")
                # venue=input("enter new venue: ")
                sql="update todo1 set time=%s ven=%s where work=%s"
                val=(e1.get(),e3.get(),e2.get())
                mycursor.execute(sql,val)
                mydb.commit()
                e1.delete(0, END)
                e2.delete(0, END)
                e3.delete(0, END)
                e1.focus_set()
                # print("Event Venue Updated")
                # print("Go back to menu")
                # print('\n')               
                # print("==============================================")
                # menu()
                
                
# def upt_time():
#                 print("Update Time")
#                 work=input("enter event for which time to be updated: ")
#                 time=input("enter new time: ")
#                 sql="update todo1 set time=%s where work=%s"
#                 val=(time, work)
#                 mycursor.execute(sql,val)
#                 mydb.commit()
#                 print("Event time Updated")
#                 print("Go back to menu")
#                 print('\n')               
#                 print("==============================================")
#                 # menu()   


root = Tk()
root.geometry("800x500")
global e1
global e2
global e3

tk.Label(root, text="TODO LIST", fg = "black", font =(None,10)).place(x=250, y=10)

tk.Label(root,text="Time", fg="black", font=(None, 10)).place(x=10, y=60)
tk.Label(root,text="Work", fg="black", font=(None, 10)).place(x=10, y=90)
tk.Label(root,text="Venue", fg="black", font=(None, 10)).place(x=10, y=120)

e1 = Entry(root)
e1.place(x=140,y=60)

e2 = Entry(root)
e2.place(x=140,y=90)

e3 = Entry(root)
e3.place(x=140,y=120)

Button(root, text="Add Task", command = insert, height= 3, width= 13).place(x=30, y=170)
Button(root, text="Delete task", command = delete, height= 3, width= 13).place(x=140, y=170)
Button(root, text="Update task", command = update, height= 3, width= 13).place(x=250, y=170)

cols = ("time", "work", "venue")
listBox = ttk.Treeview(root, columns = cols, show = "headings")

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=1, columnspan=2)
    listBox.place(x=10, y=250)

display()
listBox.bind("<Double-Button-1>",GetValue)

root.mainloop()

#main                
# menu()
