import cv2
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os
from PIL import Image, ImageTk

window = Tk()
window.geometry('310x460+500+100')
window.title('Qr-scanner')
im = Image.open('profile.png')
photo = ImageTk.PhotoImage(im)
window.wm_iconphoto(True, photo)



def open():
    file = filedialog.askopenfile(mode='r',filetypes=[('Files','*.jpg')])
    if file:
        filepath =os.path.abspath(file.name)
        Ent1.insert(0,str(filepath))

def scan():
    d = Ent1.get()
    res = cv2.QRCodeDetector()
    val , points , s_qr = res.detectAndDecode(cv2.imread(d))
    messagebox.showinfo('Qr-Scan',val)



photo = PhotoImage(file='qr.png')
imo = Label(window, image=photo)

imo.place(x=24,y=50,width=260,height=220)



Ent1 = Entry(window,font=('Arial',12),width=31)
Ent1.place(x=15,y=290)

btn = Button(window, text='Select Image',fg='white',bg='black',width=34,font=('Arial',10),command=open)
btn.place(x=15,y=340)

btn1 = Button(window, text='Read QR-code',fg='white',bg='black',width=34,font=('Arial',10),command=scan)
btn1.place(x=15,y=383)

exitButton=Button(window,text="Exit program",fg="white",background="black",width=34,font=("Arial",10),command=window.destroy)
exitButton.place(x=15,y=420) 




window.mainloop()
