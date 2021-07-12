//Create a browse option with a specific folder which has all the JPEG Files & create a Convert button to convert the image from JPEG to PNG – Basic Image converter App

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
root = tk.Tk()
canvas1 = tk.Canvas(root, width=570, height=570, bg='red', relief='raised')
canvas1.pack()
label1 = tk.Label(root, text='Convert From JPEG To PNG')
label1.config(font=('Arial', 22))
canvas1.create_window(250,40, window=label1)
def getJPEG():
    global img1
    import_file_path = filedialog.askopenfilename()
    img1 = Image.open(import_file_path)
browseButton_JPG = tk.Button(text="       JPEG File     ", command=getJPEG, bg='green', fg='red',font=('Arial', 16, 'bold'))
canvas1.create_window(250, 200, window=browseButton_JPG)
def convToPNG():
    global img1
    export_file_path = filedialog.asksaveasfilename(defaultextension='.png')
    img1.save(export_file_path)
saveAsButton_PNG = tk.Button(text='Convert JPG to PNG', command=convToPNG, bg='green', fg='red',font=('Arial', 16, 'bold'))
canvas1.create_window(250, 280, window=saveAsButton_PNG)
root.mainloop()

/Create two browse button and place the .pdf file for the buttons and create a merge pdf option -  Watermark Merger App



from tkinter import *
from tkinter import filedialog as fd
from PyPDF2 import PdfFileReader,PdfFileWriter,PdfFileMerger,PageRange


root = Tk()

# naming the GUI interface to image_conversion_APP
root.title("PDF APP ")

def merger():
	global pdf1,pdf2
	import1=fd.askopenfilename()
	pdf1=PdfFileReader(import1)
	import2=fd.askopenfilename()
	pdf2=PdfFileReader(import2)

	obj=PdfFileMerger()
	obj.append(pdf1,'rb')
	obj.append(pdf2,'rb')
	obj.write('mergedpdf.PDF')
  
 button1=Button(root,text="pdf merger",width=8,height=2,bg='white',fg='red',font=('helvetica',8,'bold'),command=merger)
button1.grid(column=1,row=6)

root.geometry("550x550+450+250")
root.mainloop()
