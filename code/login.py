from tkinter import *
from functools import partial
from PIL import ImageTk,Image

def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
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