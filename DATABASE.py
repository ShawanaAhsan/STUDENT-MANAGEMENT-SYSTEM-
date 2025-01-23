from customtkinter import *
from PIL import Image
import time
import ttkthemes
from tkinter import ttk
from tkinter import messagebox
import pymysql



def connect_database():

        
    global mycursor,conn
    try:
        conn=pymysql.connect(host='127.0.0.1',user='root',password='shawana123')
        mycursor=conn.cursor()
    except:
        messagebox.showerror('Error','Something went wrong,Please open my sql app before running again')
        return
    mycursor.execute('CREATE DATABASE IF NOT EXISTS students_data')
    mycursor.execute('USE students_data')
    mycursor.execute('CREATE TABLE IF NOT EXISTS data(id VARCHAR(20),name VARCHAR(25),fathername VARCHAR(25),cnic INT(20), year VARCHAR(20), dob VARCHAR(20), address VARCHAR(20), phonenumber INT(20))')


def insert(id,name,fathername,cnic,year,dob,address,phone):
    mycursor.execute('INSERT INTO data VALUES (%s,%s,%s,%s,%s,%s,%s,%s)',(id,name,fathername,cnic,year,dob,address,phone))
    conn.commit()

def id_exists(id):
    mycursor.execute('SELECT COUNT(*) FROM data WHERE id=%s',id)
    result=mycursor.fetchone()
    return result[0]>0

def fetch_students():
    mycursor.execute('SELECT * FROM data')
    result=mycursor.fetchall()
    return result



def update(id,new_name,new_fathername,new_cnic,new_year,new_dob,new_address,new_phone):
    mycursor.execute('UPDATE data SET name=%s,fathername=%s,cnic=%s,year=%s,dob=%s,address=%s,phonenumber=%s WHERE id=%s',(new_name,new_fathername,new_cnic,new_year,new_dob,new_address,new_phone,id))
    conn.commit()

def delete(id):
    mycursor.execute('DELETE FROM data WHERE id=%s',id)
    conn.commit()

def search(option,value):
    mycursor.execute(f'SELECT * FROM data WHERE {option}=%s',value)
    result=mycursor.fetchall()
    return result
def deleteall_records():
    mycursor.execute('TRUNCATE TABLE data ')
    conn.commit()


connect_database()