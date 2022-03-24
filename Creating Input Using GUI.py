from tkinter import*
root=Tk()

e=Entry(root, bg="red", fg="white", width=50, borderwidth=5)
e.pack()
e.insert(0, "Enter Your Name:-")

def MyClick():
    MyLabel=Label(root, text="Your Name :- " + e.get())
    MyLabel.pack()

MyButton1=Button(root, text="Enter Your Name", command=MyClick)
MyButton1.pack()

root.mainloop()