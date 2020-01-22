from tkinter import *


def register():
    reg = Toplevel()
    reg.title("Registration Page")
    reg.geometry("400x300+120+120")
    Label(reg, text="Registration will be done here...", font=("Times New Roman", 12)).pack()
    Label().pack()
    Label(reg, text="Username", font=("Times New Roman", 10)).pack()
    Entry(reg, textvariable="Username").pack()
    Label().pack()
    Label(reg, text="Password", font=("Times New Roman", 10)).pack()
    Entry(reg, show="*").pack()
    Label().pack()
    Label(reg, text="Email Id", font=("Times New Roman", 10)).pack()
    Entry(reg, textvariable="Email Id").pack()
    Label().pack()
    Label(reg, text="Date Of Birth", font=("Times New Roman", 10)).pack()
    Entry(reg, textvariable="Date Of Birth").pack()
    Label().pack()
    button1 = Button(reg, text="Register", bg="blue", font=("Times New Roman", 10),
                     command=lambda: [reg_info(), reg.destroy()])
    button1.pack()


def reg_info():
    text6 = Label(text="Registration Successfully Completed...", fg="green", font=("Times New Roman", 12))
    text6.pack()


root = Tk()
root.title("LOGIN PAGE")
root.geometry("300x400+120+120")
text1 = Label(text="LOGIN PAGE", bg="white", width=300, height=1, font=("Times New Roman", 22))
text1.pack()
Label().pack()
Label(root, text="Username", font=("Times New Roman", 10)).pack()
text2 = Entry(textvariable="Username")
text2.pack()
Label().pack()
Label(root, text="Password").pack()
text3 = Entry(show="*")
text3.pack()
button = Button(root, text="Register", bg="blue", font=("Times New Roman", 10), command=register)
Label().pack()
b = Button(root, text="Login", bg="blue", font=("Times New Roman", 10))
b.pack()
Label().pack()
button.pack()
root.mainloop()
