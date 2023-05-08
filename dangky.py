from tkinter import *
from tkinter import messagebox
import ast

win = Tk()
win.title('Đăng ký')
win.geometry('925x500+300+200')
win.configure(bg="#fff")
win.resizable(False, False)

def signup():
    username = user.get()
    password = code.get()
    confirm_password = confirm_code.get()

    if password == confirm_password:
        try:
            file = open('datasheet.txt', 'r+')
            d = file.read()
            r = ast.literal_eval(d)

            dict2 = {username:password}
            r.update(dict2)
            file.truncate(0)
            file.close()

            file = open('datasheet.txt','w')
            w = file.write(str(r))

            messagebox.showinfo('Đăng ký', 'Đăng ký thành công')

        except:
            file = open('datasheet.txt', 'w')
            pp = str({'Username':'Password'})
            file.write(pp)
            file.close()
    else:
        messagebox.showerror('Không hợp lệ', 'Cả hai mật khẩu phải khớp')





def login():
    win.destroy()
    import dangnhap 


img = PhotoImage(file="speed111//signup.png")
Label(win,image=img,bg='white').place(x=50,y=90)


frame = Frame(win, width=350, height=390, bg='white')
frame.place(x=480,y=50)

heading = Label(frame, text='Sign up', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
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

def on_enter(e):
    confirm_code.delete(0, 'end')

def on_leave(e):
    name = confirm_code.get()
    if name == '':
        confirm_code.insert(0, 'Xác nhận mật khẩu')

confirm_code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft YaHei UI Light', 11))
confirm_code.place(x=30,y=220)
confirm_code.insert(0, 'Xác nhận mật khẩu')
confirm_code.bind('<FocusIn>', on_enter)
confirm_code.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)

########---------------------------------


Button(frame,width=39,pady=7,text='Đăng ký',bg='#57a1f8',fg='white',border=0, command=signup).place(x=35, y=280)

label = Label(frame, text="Đã có tài khoản", fg='black',bg='white',font=('Microsoft YaHei UI Light', 9))
label.place(x=90,y=340)

sign_in = Button(frame,width=12,text='Đăng nhập', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=login)
sign_in.place(x=200,y=340)


win.mainloop()