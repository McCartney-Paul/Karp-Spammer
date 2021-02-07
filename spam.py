#imports
import pyautogui, time, os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox

#GUI config
root = Tk()
root.geometry("350x250")
frame = Frame(root)
bottomFrame = Frame(root)
frame.pack()
bottomFrame.pack(side=BOTTOM)

#execute spam
def Spammer(index):
    response = messagebox.askokcancel("Are you sure?" , "are you sure that you want to spam the file")
    if(response):
        name = files[index]
        Script = open(name, 'r') 
        time.sleep(5)
        for word in Script:
            pyautogui.typewrite(word)
            pyautogui.press("enter")
    else:
        messagebox.showinfo("no spamming today", "Well i guess theres is no spamming today. Have a nice day :)")

#execute ERROR spam
def err_spammer(num):
    for x in range(num):
        messagebox.showerror("ERROR", "ERROR")

#ERROR spammer num
def err_spammer_popup():
    top = Toplevel()
    err_spam_guide = ttk.Label(top, text="enter the number of error messages")   
    err_spam_num = ttk.Entry(top, width=10)
    err_spam_start = ttk.Button(top, text="submit", command= lambda: err_spammer(int(err_spam_num.get())))
    err_spam_guide.pack()
    err_spam_num.pack()
    err_spam_start.pack()

#custom file finder
def customFileFinder():
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
    files.append(root.filename)
    Spammer(len(files)-1)


#get file names
files = os.listdir()
files.remove('Logo.bmp')
files.remove('spam.py')
files.remove('spam.exe')

#GUI
root.title("Karp Spammer")
root.iconbitmap("Logo.bmp")
heading = ttk.Label(frame, text="Welcome to Karp spammer")
heading.pack()
instructions = ttk.Label(frame, text='choose a file, hit "start spam" and it will spam in 5 seconds. ')
instructions.pack()
var = IntVar()
for file in files:
    ttk.Radiobutton(frame, text=file, variable=var, value=files.index(file)).pack()
errspam = ttk.Button(bottomFrame, text="ERROR spam", command=err_spammer_popup)
start = ttk.Button(bottomFrame, text="Start Spam", command= lambda: Spammer(var.get()))
customText = ttk.Button(bottomFrame, text="open a custom file", command=customFileFinder)
errspam.pack(side = LEFT)
start.pack(side = LEFT)
customText.pack(side = LEFT)

#The End
root.mainloop()