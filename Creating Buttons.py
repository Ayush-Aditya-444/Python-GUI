from faulthandler import disable
from tkinter import*
root=Tk()
def MyClick():
    MyLabel=Label(root, text="I Have Cilcked This Button")
    MyLabel.pack()
MyButton1=Button(root, text="Button 1")
MyButton1.pack()
MyButton2=Button(root, text="Button 2", state=DISABLED)
MyButton2.pack()
MyButton3=Button(root, text="Button 3", padx=50, pady=50)
MyButton3.pack()
MyButton1=Button(root, text="Button 4", command=MyClick)
MyButton1.pack()
MyButton5=Button(root, text="Button 5", fg="red")
MyButton5.pack()
MyButton6=Button(root, text="Button 6", bg="blue")
MyButton6.pack()
root.mainloop()