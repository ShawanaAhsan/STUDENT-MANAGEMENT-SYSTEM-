from customtkinter import *
from PIL import Image 
import pymysql
import time
import ttkthemes
from tkinter import ttk
from tkinter import messagebox

import DATABASE





#functions

def delete_all():
    result=messagebox.askyesno('Confim','Do you really want to delete all records?')
    if result:
        DATABASE.deleteall_records()
    else:
        pass    


def show_all():
    treeview_data()
    searchEntry.delete(0,END)
    searchBox.set('Search BY')

def search_student():
    if searchEntry.get()=='':
        messagebox.showerror('Error','Enter value to search')
    elif searchBox.get()=='Search By':
        messagebox.showerror('Error', 'Please select an option')
    else:
        searched_data=DATABASE.search(searchBox.get(),searchEntry.get())
        tree.delete(*tree.get_children())
        for student in searched_data:
            tree.insert('',END,values=student)





def delete_student():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror('Error','Select data to delete')
    else:
        DATABASE.delete(idEntry.get())
        treeview_data()
        clear()
        messagebox.showerror('Error','Data is deleted')


def update_student():
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror('Error','Select data to update')
    else:
        DATABASE.update(idEntry.get(),nameEntry.get(),fathernameEntry.get(),cnicEntry.get(),yearbox.get(),dobEntry.get(),addressEntry.get(),phoneEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo('Success','data is updated')

def selection(event):
    selected_item=tree.selection()
    if selected_item:
        row=tree.item(selected_item)['values']
        clear()
        idEntry.insert(0,row[0])
        nameEntry.insert(0,row[1])
        fathernameEntry.insert(0,row[2])
        cnicEntry.insert(0,row[3])
        yearbox.set(row[4])
        dobEntry.insert(0,row[5])
        addressEntry.insert(0,row[6])
        phoneEntry.insert(0,row[7])

def clear(value=False):
    if value:
        tree.selection_remove(tree.focus())
    idEntry.delete(0,END)
    nameEntry.delete(0,END)
    fathernameEntry.delete(0,END)
    cnicEntry.delete(0,END)
    yearbox.set('first year')
    dobEntry.delete(0,END)
    addressEntry.delete(0,END)
    phoneEntry.delete(0,END)


def treeview_data():
    students=DATABASE.fetch_students()
    tree.delete(*tree.get_children())
    for student in students:
        tree.insert('',END,values=student)



def add_student():
    if idEntry.get()==''or nameEntry.get()=='' or fathernameEntry.get()=='' or cnicEntry.get()=='' or dobEntry.get()=='' or addressEntry.get()=='' or phoneEntry.get()=='':
        messagebox.showerror('Error','All fields are required')
    elif DATABASE.id_exists(idEntry.get()):
        messagebox.showerror('Error','Id allready exists')


    else:
        DATABASE.insert(idEntry.get(),nameEntry.get(),fathernameEntry.get(),cnicEntry.get(),yearbox.get(),dobEntry.get(),addressEntry.get(),phoneEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo('Success','Data is added')

def clock():
    global date,currenttime
    date=time.strftime('%d/%m/%Y')
    currenttime=time.strftime('%H:%M:%S')
    datetimelabel.configure(text=f'   Date:{date}\nTime:{currenttime}')
    datetimelabel.after(1000,clock)


        



#GUI part
window=CTk()

window.geometry('1500x700+100+100')
window.resizable(False,False)
window.title('STUDENT MANAGEMENT SYSTEM')
logo=CTkImage(Image.open('images/2022-02-07.jpg'),size=(1500,700))
logoLabel=CTkLabel(window,image=logo,text='')
logoLabel.grid(row=0,column=0,columnspan=2)


leftframe=CTkFrame(window,fg_color='black')
leftframe.place(x=20,y=100)

#creating date and time at the left top corner
datetimelabel=CTkLabel(window,font=('times new roman',20,'bold'))
datetimelabel.place(x=5,y=5)
clock()




idLabel=CTkLabel(leftframe, text='Id',font=('arial',18,'bold'),text_color='white')
idLabel.grid(row=0,column=0,padx=20, pady=15,sticky='w')

idEntry=CTkEntry(leftframe, font=('arial',18,'bold'),width=180)
idEntry.grid(row=0,column=1)

nameLabel=CTkLabel(leftframe, text='NAME',font=('arial',18,'bold'),text_color='white')
nameLabel.grid(row=1,column=0,padx=20, pady=15,sticky='w')

nameEntry=CTkEntry(leftframe, font=('arial',18,'bold'),width=180)
nameEntry.grid(row=1,column=1)

fathernameLabel=CTkLabel(leftframe, text='FATHERNAME',font=('arial',18,'bold'),text_color='white')
fathernameLabel.grid(row=2,column=0,padx=20, pady=15,sticky='w')

fathernameEntry=CTkEntry(leftframe, font=('arial',18,'bold'),width=180)
fathernameEntry.grid(row=2,column=1)

cnicLabel=CTkLabel(leftframe, text='CNIC',font=('arial',18,'bold'),text_color='white')
cnicLabel.grid(row=3,column=0,padx=20, pady=15,sticky='w')

cnicEntry=CTkEntry(leftframe, font=('arial',18,'bold'),width=180)
cnicEntry.grid(row=3,column=1)

yearLabel=CTkLabel(leftframe, text='YEAR',font=('arial',18,'bold'),text_color='white')
yearLabel.grid(row=4,column=0,padx=20, pady=15,sticky='w')

Select_year=['first year','second year', 'third year','final year']
yearbox=CTkComboBox(leftframe,values=Select_year, font=('arial',18,'bold'),width=180)
yearbox.grid(row=4,column=1)
yearbox.set('first year')

dobLabel=CTkLabel(leftframe, text='DATE OF BIRTH',font=('arial',18,'bold'),text_color='white')
dobLabel.grid(row=5,column=0,padx=20, pady=15,sticky='w')

dobEntry=CTkEntry(leftframe, font=('arial',18,'bold'),width=180)
dobEntry.grid(row=5,column=1)

addressLabel=CTkLabel(leftframe, text='ADDRESS',font=('arial',18,'bold'),text_color='white')
addressLabel.grid(row=6,column=0,padx=20, pady=15,sticky='w')

addressEntry=CTkEntry(leftframe, font=('arial',18,'bold'),width=180)
addressEntry.grid(row=6,column=1)

phoneLabel=CTkLabel(leftframe, text='PHONE NUMBER',font=('arial',18,'bold'),text_color='white')
phoneLabel.grid(row=7,column=0,padx=20, pady=15,sticky='w')

phoneEntry=CTkEntry(leftframe, font=('arial',18,'bold'),width=180)
phoneEntry.grid(row=7,column=1)

rightframe=CTkFrame(window,fg_color='black')
rightframe.place(x=400,y=100)



search_options=['id','Name','Fathername','CNIC', 'Year','Date of birth','Address','phone number']
searchBox=CTkComboBox(rightframe,values=search_options,state='readonly',width=200)
searchBox.grid(row=0,column=0)
searchBox.set('Search By')

searchEntry=CTkEntry(rightframe,width=200)
searchEntry.grid(row=0,column=1)

searchButton=CTkButton(rightframe,text='Search',width=200,command=search_student)
searchButton.grid(row=0, column=2)

showallButton=CTkButton(rightframe,text='Show All',width=200,command=show_all)
showallButton.grid(row=0, column=3, pady=5)

tree=ttk.Treeview(rightframe, height=15)
tree.grid(row=1,column=0,columnspan=4)


tree['columns']=('Id','Name','Fathername','CNIC','Year','Date of birth','Address','phone number')


tree.heading('Id',text='Id')
tree.heading('Name',text='NAME')
tree.heading('Fathername',text='FATHERNAME')
tree.heading('CNIC',text='CNIC')
tree.heading('Year',text='YEAR')
tree.heading('Date of birth',text='DATE OF BIRTH')
tree.heading('Address',text='ADDRESS')
tree.heading('phone number',text='PHONE NUMBER')
tree.config(show='headings')

tree.column('Id',width='80')
tree.column('Name',width='180')
tree.column('Fathername',width='180')
tree.column('CNIC',width='180')
tree.column('Year',width='100')
tree.column('Date of birth',width='150')
tree.column('Address',width='250')
tree.column('phone number',width='160')

style=ttk.Style()

style.configure('Treeview.Heading', font=('arial',12,'bold'))
style.configure('Treeview', font=('arial',10,'bold'),rowheight=34)

scrollbarx=ttk.Scrollbar(rightframe,orient=VERTICAL,command=tree.yview)
scrollbarx.grid(row=1,column=4,sticky='ns')

tree.config(yscrollcommand=scrollbarx.set)




buttonframe=CTkFrame(window,fg_color='black',bg_color='black',width=40)
buttonframe.place(x=300,y=600)

newbutton=CTkButton(buttonframe,text='New Student',font=('arial',15,'bold'),width=180,corner_radius=15,command=lambda:clear(True))
newbutton.grid(row=0,column=0,pady=5)

addbutton=CTkButton(buttonframe,text='Add Student',font=('arial',15,'bold'),width=180,corner_radius=15,command=add_student)
addbutton.grid(row=0,column=1,pady=10, padx=10)

updatebutton=CTkButton(buttonframe,text='Update Student',font=('arial',15,'bold'),width=180,corner_radius=15, command=update_student)
updatebutton.grid(row=0,column=2,pady=5,padx=5)

deletebutton=CTkButton(buttonframe,text='Delete Student',font=('arial',15,'bold'),width=180,corner_radius=15,command=delete_student)
deletebutton.grid(row=0,column=3,pady=5, padx=5)

deleteallbutton=CTkButton(buttonframe,text='Delete All',font=('arial',15,'bold'),width=180,corner_radius=15, command=delete_all )
deleteallbutton.grid(row=0,column=4,pady=5, padx=5)

treeview_data()

window.bind('<ButtonRelease>',selection)

window.mainloop()