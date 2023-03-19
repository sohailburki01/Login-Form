from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox


def handleLogin():
    email = email_input.get()
    password = password_input.get()
    if email == 'KHAN_@academy01' and password == '1234':
        messagebox.showinfo('Yayyy', 'Login Successful')
    else:
        messagebox.showerror('Error', 'Login Failed')


root = Tk()

root.title('Login Form')
root.geometry('350x500')
root.configure(bg='#0096DC')

img = Image.open('pic.jpg')
resized_img = img.resize((70, 70), Image.LANCZOS)
img = ImageTk.PhotoImage(resized_img)
img_label = Label(root, image=img)
img_label.pack(pady=(10, 10))

text_label = Label(root, text='KHAN ACADEMY', fg='white', bg='#0096DC')
text_label.pack()
text_label.config(font=('verdana', 24))

email_label = Label(root, text='Enter Email', fg='white', bg='#0096DC')
email_label.pack(pady=(20, 5))
email_label.config(font=('verdana', 12))

email_input = Entry(root, width=50)
email_input.pack(ipady=6, pady=(1, 15))

password_label = Label(root, text='Enter Password', fg='white', bg='#0096DC')
password_label.pack(pady=(20, 5))
password_label.config(font=('verdana', 12))

password_input = Entry(root, width=50)
password_input.pack(ipady=6, pady=(1, 15))

login_btn = Button(root, text='Login Here', bg='white', fg='black', width=10, height=2, command=handleLogin)
login_btn.pack(pady=(10, 20))
login_btn.config(font=('verdana', 10))

root.mainloop()
