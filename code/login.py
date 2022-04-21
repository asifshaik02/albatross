from tkinter import *
from functools import partial
from tkinter import messagebox
from PIL import ImageTk,Image
from Database import Database
from Supervisor import Supervisor
from Owner import Owner
from Workers import Workers
# from Employee import Employee

def validateLogin(username, password):
    usr = username.get()
    pwd = password.get()

    sq = Database()
    res = sq.execute(f"select pass,role from login where username='{usr}'")
    passw = res[0][0]
    role = res[0][1]
    # print(passw)
    if pwd == passw:
        # print(role)
        if role == "owner":
            res = sq.execute(f"select o_name,o_id,o_phone,o_pass from owners where o_id='{usr}'")
            Owner(res[0][0],res[0][1],res[0][2],res[0][3])
        elif role == "supervisor":
            res = sq.execute(f"select e_name,e_id,e_password,e_phone,e_role from employee where e_id='{usr}'")
            Supervisor(res[0][0],res[0][1],res[0][2],res[0][3],res[0][4])
        elif role == "worker":
            res = sq.execute(f"select e_name,e_id,e_password,e_phone,e_role from employee where e_id='{usr}'")
            Workers("","","",res[0][0],res[0][1],res[0][2],res[0][3],res[0][4])
        root.destroy()
    else:
        print("No")
        messagebox.showerror("Error","Wrong credntials")

    return

#window
root = Tk()  
root.geometry('600x450')  
root.title('Login Form')
# root.eval("tk::PlaceWindow . center")

canvas = Canvas(root,width=600, height=800)
canvas.pack(expand=YES, fill=BOTH)

image = ImageTk.PhotoImage(file="code/static/bg.png")
canvas.create_image(0, 0, image=image, anchor=NW)

def resize_bg(event):
    global bgg, resized, bg2
    # open image to resize it
    bgg = Image.open("code/static/bg.png")
    # resize the image with width and height of root
    resized = bgg.resize((event.width, event.height),Image.ANTIALIAS)
    
    bg2 = ImageTk.PhotoImage(resized)
    canvas.create_image(0, 0, image=bg2, anchor='nw')

frame = Frame(root,bd=5,highlightthickness=2,highlightbackground="black",padx=50,pady=50)
frame.place(relx=.5, rely=.5,anchor= CENTER)



#username label and text entry box
usernameLabel = Label(frame, text="User Name",pady=10).grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(frame, textvariable=username).grid(row=0, column=1)

Label(frame).grid(row=0,column=2)

#password label and password entry box
passwordLabel = Label(frame,text="Password",pady=10).grid(row=1, column=0)
password = StringVar()
passwordEntry = Entry(frame, textvariable=password, show='*').grid(row=1, column=1)

validateLogin = partial(validateLogin, username, password)

#login button
loginButton = Button(frame, text="Login", command=validateLogin).grid(row=2, column=1)

root.bind("<Configure>", resize_bg)
root.mainloop()