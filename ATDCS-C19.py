# -*- coding: utf-8 -*-
"""
Created on Wed May  6 21:29:20 2020

@author: Vijay
"""

import re
import csv
from tkinter import * ;

from tkinter.ttk import *
from fpdf import FPDF
from datetime import datetime
from datetime import date
  
# importing askopenfile function 
# from class filedialog 
from tkinter.filedialog import askopenfile 
root = Tk()
root.title("ATDCS-V.C19") 
root.iconbitmap(r"sahyadri.ico")
root.geometry('1000x600') 
#filename = PhotoImage(file = "C:\\Users\\Vijay\\Pictures\d3.png")
#background_label = Label(root, image=filename)
#background_label.place(x=0, y=0, relwidth=1, relheight=1)
  
# This function will be used to open 

# file in read mode and only Python files 
# will be opened 

li=[] 
st_pre=[] 
sem_sec=None
def gen_absen():
    fname=askopenfile(mode ='r', filetypes =[("all files","*.*")])
    
    for line in fname:
        line=line.rstrip();
        line=re.findall('[0-9][a-zA-Z]{2}[0-9]{2}[a-zA-Z]{2}[0-9]{3}',line)
        if len(line)is not 0:
            for i in line:
                if i.upper() not in st_pre:
                    st_pre.append(i.upper())
    st_pre.sort()
    print("list of students who are present")
    print(st_pre)
    print("number of stdeunts present",len(st_pre))
    

    
        #print(li)
    
t=Text(root)
def semester():
    sem_sec=sem_ent.get()
    if sem_sec in "4A":
        fname1="4A.csv"
    elif sem_sec in "4B":
        fname1="4B.csv"
    elif sem_sec in "4C":
        fname1="4C.csv"
    elif sem_sec in "6A":
        fname1="6A.csv"
    elif sem_sec in "6B":
        fname1="6B.csv"
    elif sem_sec in "6C":
        fname1="6C.csv"
    elif sem_sec in "8A":
        fname1="8A.csv"
    elif sem_sec in "8B":
        fname1="8B.csv"
    else:
        fname1="8C.csv"
    with open(fname1)as n_4A:
        csv_read=csv.reader(n_4A,delimiter=",")
        for k in st_pre:
            for j in csv_read:
              print(k,j)
                
            
   # print(li)                 
        #print("list of absentees")
    btn2=Button(root,text='List of absentees',command=lambda:display())
    btn2.pack(side=TOP,pady=30)

def display():
    t.insert(END,"List of Absentees"+'\t'+'\n')
    t.insert(END,"-----------------------"+'\n')
    t.insert(END,"USN   "+"\t"+"NAME"+'\n')
    t.insert(END,"-----------------------"+'\n')
    for x in li:
        t.insert(END, x[0]+'\t'+x[1] + '\n')
    t.insert(END,"-----------------------"+'\n')
    t.insert(END,"Number of Absentees="+'\t'+str(len(li))+'\n')
    
    t.pack()
def simple_table(spacing=1):
    
    
    pdf = FPDF()
    pdf.set_font("Arial", size=12)
    pdf.add_page()
    pdf.cell(200, 10, txt="List of Absentees Department of Computer science and Engineering\n ", ln=1, align="C")
    col_width = pdf.w / 2.5
    row_height = pdf.font_size
    head=[['USN','NAME']];
    for row in head:
        for item1 in row:
            pdf.cell(col_width, row_height*spacing,
                     txt=item1, border=1,align="C")
        pdf.ln(row_height*spacing)
    for row in li:
        for item in row:
            pdf.cell(col_width, row_height*spacing,
                     txt=item, border=1,align="C")
        pdf.ln(row_height*spacing)
    to=str(date.today())
    pdf.cell(200, 10, txt="Computer  Generated Report on"+"\t"+str(datetime.now()), ln=1, align="C")
    col_width = pdf.w / 3.0
    fname=sem_ent.get()+to+'.pdf'
    pdf.output(fname)
     
    
#btn = Button(root, text ='Open', command = lambda:open_file()) 
btn1=Button(root,text='Open a Text File',command=lambda:gen_absen())
btn1.pack(side=TOP,pady=20)
Lab_1=Label(root,text="Enter semester with Section(Example:4A)");
sem_ent=Entry(root)
Lab_1.pack(side=TOP,pady=25)
sem_ent.pack(side=TOP,pady=5)
bt3=Button(root,text='ok',command=lambda:semester())
bt3.pack(side=TOP,pady=0)
#Lab_1=Label(root,text="Enter semester");
#sem_ent=Entry(root)
#btn2=Button(root,text='List of absentees',command=lambda:display())


#btn.pack(side = TOP, pady = 10) 

#Lab_1.pack(side=TOP,pady=25)
#sem_ent.pack(side=TOP,pady=5)


label = Label(root, text='Designed by Mr.Vijay C.P Assitant Professor Department of CSE,Sahyadri College of Engineering and Managment', font='Helvetica 12 bold')
label.pack(side=BOTTOM,pady=0)
bt4=Button(root,text='Generate PDF',command=lambda:simple_table())
bt4.pack(side=BOTTOM,pady=20)
  
root.mainloop() 


"""with open('4A.csv')as n_4A:
        csv_reader=cs.reader(n_4A,delimiter=",")
        for j in csv_reader:
            print(j)"""