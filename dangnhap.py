from tkinter import *
from tkinter import messagebox
import ast

root = Tk()
root.title('Đăng nhập')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

def signin():
    username = user.get()
    password = code.get()

    file = open('datasheet.txt', 'r')
    d = file.read()
    r = ast.literal_eval(d)
    file.close()

    # print(r.keys())
    # print(r.values())

    if username in r.keys() and password == r[username]:
        root.destroy()
        import interface 
        
    else:
        messagebox.showerror('Không hợp lệ', 'tên đăng nhập hoặc mật khẩu sai')



def signup():
    root.destroy()
    import dangky



img = PhotoImage(file="speed111//login1.png")
Label(root,image=img,bg='white').place(x=50,y=50)


frame = Frame(root, width=350, height=350, bg='white')
frame.place(x=480,y=70)

heading = Label(frame, text='Đăng nhập', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x = 100, y = 5)


########---------------------------------

def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Tên đăng nhập')


user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
user.place(x=30,y=80)
user.insert(0, 'Tên đăng nhập')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

########---------------------------------

def on_enter(e):
    code.delete(0, 'end')

def on_leave(e):
    name = code.get()
    if name == '':
        code.insert(0, 'Mật khẩu')

code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
code.place(x=30,y=150)
code.insert(0, 'Mật khẩu')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

########---------------------------------


Button(frame,width=39,pady=7,text='Đăng nhập',bg='#57a1f8',fg='white',border=0, command=signin).place(x=35, y=204)

label = Label(frame, text="Chưa có tài khoản", fg='black',bg='white',font=('Microsoft YaHei UI Light', 9))
label.place(x=75,y=270)

sign_up = Button(frame,width=12,text='Đăng ký', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=signup)
sign_up.place(x=215,y=270)


root.mainloop()