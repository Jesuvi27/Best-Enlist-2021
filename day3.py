from tkinter import *
import tkinter.messagebox
root =Tk()
root.title("Employee Registration Form")
root.geometry('700x400')
root.configure(background = "blue")

label1=Label(root ,text= "Employee Registration Form ", font=("bold", 25)).grid(row =0, column=2)
Firstname = Label(root ,text = "First Name").grid(row = 1,column = 1)
LastName = Label(root ,text = "Last Name").grid(row = 2,column = 1)
Address = Label(root,text = "Address").grid(row = 3,column = 1)
District = Label(root ,text = "District").grid(row = 4,column = 1)
State= Label(root,text = "state").grid(row = 5,column = 1)
Country = Label(root ,text = "Country").grid(row = 7,column = 1)
postal = Label(root,text = "Postal /Zip Code").grid(row = 6,column = 1)
list1 = ['India','London','America','Africa','France'];
x=StringVar()
droplist=OptionMenu(root,x, *list1)
droplist.config(width=15)
x.set('select your country')
droplist.grid(row = 7,column = 2)
Mobile = Label(root ,text = "Contact Number").grid(row = 8,column = 1)
Email = Label(root ,text = "Email Id").grid(row = 9,column = 1)
Gender =Label(root ,text = "Gender").grid(row = 10,column = 1)
var = IntVar()
Radiobutton(root, text="Male",padx = 30, variable=var, value=1).grid(row = 10,column = 2)
Radiobutton(root, text="Female",padx = 20, variable=var, value=2).grid(row = 10,column = 3)
Radiobutton(root, text="Others",padx = 10, variable=var, value=2).grid(row = 10,column = 4)
Choose =Label(root ,text = "Date Of Birth",width=20,font=("bold", 10)).grid(row = 11,column = 1)
label_12 = Label(root, text="Position Need",width=20,font=("bold", 10))
label_12.grid(row = 12,column = 1)
var1 = IntVar()
Checkbutton(root, text="Human resource managaer", variable=var1).grid(row = 12,column = 2)
var2 = IntVar()
Checkbutton(root, text="General Manager", variable=var2).grid(row = 12,column = 3)


Firstname1 = Entry(root).grid(row = 1,column = 2)
Lastna = Entry(root).grid(row = 2,column = 2)
Adderss1=Entry(root).grid(row = 3,column = 2)
District1=Entry(root).grid(row = 4,column = 2)
state1=Entry(root).grid(row = 5,column = 2)
postal1=Entry(root).grid(row = 6,column = 2)
Email1 = Entry(root).grid(row = 9,column = 2)
Mobile1 = Entry(root).grid(row = 8,column = 2)
choose1 = Entry(root).grid(row = 11,column = 2)


def onClick():
    tkinter.messagebox.showinfo("Thanks for regestering !")


# Create a Button
Button(root, text="Submit", command=onClick,width=20,bg='brown',fg='white').grid(row = 14,column = 2)


root.mainloop()
