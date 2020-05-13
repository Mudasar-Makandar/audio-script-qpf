import sqlite3
import tkinter
from tkinter import *
from tkinter import filedialog
from fingerprint import ReferenceFingerprint, QueryFingerprint
from db import *
from tkinter import messagebox, Listbox
import os
import collections

root = Tk()
#root.filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
#print (root.filename)
def UploadFile(event=None):
    try:
        root.filename = filedialog.askopenfilename(initialdir = "/",title = "Select file")
        fp_r = ReferenceFingerprint(root.filename)
        fp_r.create()
        db = QfpDB()
        db.store(fp_r, ((root.filename).split('/'))[-1])
        messagebox.showinfo(title="Status", message="Succesfully Stored!")
        #print('Selected:', root.filename)
        #return root.filename
    except:
        messagebox.showwarning(title="Status", message="Something went wrong!")

def UploadDirectory(event=None):
    root.directory = filedialog.askdirectory(initialdir = "/",title = "Select Directory")
    #print('Selected:', root.directory)
    for i in os.listdir(root.directory):
        try:
            fp_r = ReferenceFingerprint(root.directory+"/"+i)
            fp_r.create()
            db = QfpDB()
            db.store(fp_r, i)
        except:
            messagebox.showwarning(title="Status", message="Can't Store this file!")
            pass
    messagebox.showinfo(title="Status", message="Succesfully Stored!")


def QueryFile(event=None):
    try:
        root.filename = filedialog.askopenfilename(initialdir = "/",title = "Select file")
        fp_q = QueryFingerprint(root.filename)
        fp_q.create1()
        db = QfpDB(db_path="qfp.db")
        db.query(fp_q)
        if fp_q.matches != []:
            Match = collections.namedtuple("Match", ["record","offset","vScore"])
            #print(fp_q.matches)
            result = fp_q.matches
            #print(result)
            records_matched = []
            for e in range(len(result)):
                records_matched.append(result[e].record)
            #print(records_matched)
            master = Tk()
            list = Listbox(master)
            list.insert(0, *records_matched)
            list.pack()
            btn = Button(master,text='Quit', width=25, command=master.destroy)
            btn.pack()
            btn.place(anchor=NW,height=40,width=80, rely=0.8, relx=0.2)
            master.mainloop()

        else:
            messagebox.showinfo(title="Status", message="Sorry!, There is no matching")

    except:
        messagebox.showwarning(title="Status", message="Something went wrong!")

root.geometry("800x300")
button = Button(root,text='File', width=25, command=UploadFile)
button.pack()
button.place(anchor=NW,height=40,width=80, rely=0.35, relx=0.15)

button1 = Button(root,text='Directory', width=25, command=UploadDirectory)
button1.pack()
button1.place(anchor=NW,height=40,width=80, rely=0.35, relx=0.3)

text1 = Text(root, width=25, height=2, background='lightgray')
text1.pack()
text1.insert(tkinter.END, "Select File or Directory for Fingerprint")
text1.place(anchor=SW,height=40,width=200, rely=0.3, relx=0.15)

text2 = Text(root, width=25, height=2, background='lightgray')
text2.pack()
text2.insert(tkinter.END, "Select a File to Query \n within DataBase")
text2.place(anchor=SW,height=40,width=200, rely=0.3, relx=0.65)

button2 = Button(root,text='Query', width=25, command=QueryFile)
button2.pack()
button2.place(anchor=NW,height=40,width=80, rely=0.35, relx=0.72)

button3 = Button(root,text='Quit', width=25, command=root.destroy)
button3.pack()
button3.place(anchor=NW,height=40,width=80, rely=0.8, relx=0.5)

root.mainloop()
