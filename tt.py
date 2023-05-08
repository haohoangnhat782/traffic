import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox, ttk
import pandas as pd
import mysql.connector
from PIL import Image, ImageTk
from sqlalchemy import create_engine

def GetValue(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)

    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0,select['id'])
    e2.insert(0,select['NumberPlate'])
    e3.insert(0,select['Speed'])
    e4.insert(0,select['Vehicle'])
    e5.insert(0,select['Submit'])
 
 
def Add():
    id = e1.get()
    NumberPlate = e2.get()
    Speed = e3.get()
    Vehicle = e4.get()
    Submit = e5.get()
 
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="traffic")
    mycursor=mysqldb.cursor()
 
    try:
       sql = "INSERT INTO  listvp (id,NumberPlate,Vehicle,Speed,Submit) VALUES (%s, %s, %s, %s,%s)"
       val = (id,NumberPlate,Speed,Vehicle,Submit)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "Employee inserted successfully...")
       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e5.delete(0, END)
       e1.focus_set()
       listBox.delete(*listBox.get_children())
       show()
    except Exception as e:
       print(e)
       mysqldb.rollback()
       mysqldb.close()
 
 
def update():
    id = e1.get()
    NumberPlate = e2.get()
    Speed = e3.get()
    Vehicle = e4.get()
    Submit = e5.get()

    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="traffic")
    mycursor=mysqldb.cursor()

    try:
        sql = "Update  listvp set NumberPlate= %s,Speed= %s,Vehicle= %s ,Submit= %s where id= %s"
        val = (NumberPlate,Speed,Vehicle,Submit,id)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("information", "Record Updated successfully...")

        # Xóa giá trị trong ô input
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)

        # Cập nhật lại dữ liệu trong listBox
        listBox.delete(*listBox.get_children())
        show()

    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()
 
def delete():
    id = e1.get()
 
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="",database="traffic")
    mycursor=mysqldb.cursor()
 
    try:
       sql = "delete from listvp where id = %s"
       val = (id,)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("information", "Record Deleteeeee successfully...")
 
       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e5.delete(0, END)
       e1.focus_set()
       listBox.delete(*listBox.get_children())
       show()

 
    except Exception as e:
       
 
       print(e)
       mysqldb.rollback()
       mysqldb.close()
 
# def show():
#         mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="traffic")
#         mycursor = mysqldb.cursor()
#         mycursor.execute("SELECT id,NumberPlate,Speed,Vehicle,Submit FROM listvp")
#         records = mycursor.fetchall()
#         print(records)
 
#         for i, (id,NumberPlate,Speed,Vehicle,Submit) in enumerate(records, start=1):
#             listBox.insert("", "end", values=(id,NumberPlate,Speed,Vehicle,Submit))
#             mysqldb.close()


def search():
    # Lấy giá trị biển số xe từ Entry
    NumberPlate = e2.get()
    
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="traffic")
    mycursor = mysqldb.cursor()
    # Thực hiện truy vấn SELECT với điều kiện WHERE là biển số xe
    mycursor.execute("SELECT id,NumberPlate,Speed,Vehicle,Submit FROM listvp WHERE NumberPlate=%s", (NumberPlate,))
    records = mycursor.fetchall()
    print(records)
    
    # Xóa dữ liệu trong listBox
    listBox.delete(*listBox.get_children())
    
    for i, (id,NumberPlate,Speed,Vehicle,Submit) in enumerate(records, start=1):
        listBox.insert("", "end", values=(id,NumberPlate,Speed,Vehicle,Submit))
    
    mysqldb.close()
    



def excel():
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="traffic")

# Tạo engine từ kết nối
    engine = create_engine('mysql+mysqlconnector://root:@localhost:3306/traffic')

# Tạo DataFrame từ dữ liệu trong database
    df = pd.read_sql("SELECT * FROM listvp", con=engine)

# Lưu DataFrame vào file Excel
    df.to_excel("C:/py/text/Nhom10/Nhom10/speed111/data/traffic_data.xlsx", index=False)

# Đóng kết nối với database
    mysqldb.close()

    messagebox.showinfo('Thông báo', 'Lưu file Excel thành công!')

def show():
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="traffic")
    mycursor = mysqldb.cursor()
    mycursor.execute("SELECT id,NumberPlate,Speed,Vehicle,Submit FROM listvp")
    records = mycursor.fetchall()
    print(records)

    for i, (id,NumberPlate,Speed,Vehicle,Submit) in enumerate(records, start=1):
        listBox.insert("", "end", values=(id,NumberPlate,Speed,Vehicle,Submit))
    
    mysqldb.close()
 
root = Tk()
root.title("Traffic Violation")
root.geometry("800x500")
global e1
global e2
global e3
global e4
global e5
 
# tk.Label(root, text="Traffic ", fg="red", font=(None, 30)).place(x=300, y=5)
 
def open_image():
    # Mở hộp thoại chọn tệp ảnh
    file_path = filedialog.askopenfilename()
    file_name = file_path.split("/")[-1]

    # Tạo đối tượng hình ảnh từ tệp ảnh
    image = Image.open(file_path)
    # Thay đổi kích thước của ảnh
    image = image.resize((180, 200))
    photo = ImageTk.PhotoImage(image)
    file_label = tk.Label(root, text=file_name)
    file_label.place(x=580, y=193)
    # Tạo label để hiển thị ảnh
    label = tk.Label(root)
    label.config(image=photo)
    label.image = photo  # Gán tham chiếu đến ảnh cho label để giữ ảnh sống
    # Thiết lập vị trí và kích thước của label
    label.place(x=490, y=5, width=200, height=180)


def back():
    root.destroy()
    import interface 

button = tk.Button(root, text="Hiện ảnh", command=open_image)
button.pack()
button.place(x=500, y=190)

tk.Label(root, text="ID").place(x=10, y=10)
Label(root, text="Number Plate").place(x=10, y=40)
Label(root, text="Speed").place(x=10, y=70)
Label(root, text="Vehicle").place(x=10, y=100)
Label(root, text="Submit").place(x=10, y=130)
 
e1 = Entry(root)
e1.place(x=140, y=10)
 
e2 = Entry(root)
e2.place(x=140, y=40)
 
e3 = Entry(root)
e3.place(x=140, y=70)
 
e4 = Entry(root)
e4.place(x=140, y=100)
e5 = Entry(root)
e5.place(x=140, y=130)
 
Button(root, text="Add",command = Add,height=1, width= 8).place(x=30, y=170)
Button(root, text="update",command = update,height=1, width= 8).place(x=100, y=170)
Button(root, text="Delete",command = delete,height=1, width= 8).place(x=170, y=170)
Button(root, text="Search",command = search,height=1, width= 8).place(x=240, y=170)
Button(root, text="Excel",command = excel,height=1, width= 8).place(x=310, y=170)
Button(root, text="Back" ,command = back,height=1, width= 8).place(x=720, y=470)



cols = ('id', 'NumberPlate', 'Speed','Vehicle','Submit')
listBox = ttk.Treeview(root, columns=cols, show='headings' )
 
# for col in cols:
#     listBox.heading(col, text=col)
#     listBox.grid(row=1, column=0, columnspan=2)
#     listBox.place(x=10, y=240)

for i, col in enumerate(cols):
    listBox.heading(col, text=col)
    listBox.column(i, width=155)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=10, y=240)
show()
listBox.bind('<Double-Button-1>',GetValue)
 
root.mainloop()