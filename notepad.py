import tkinter
from tkinter import * 
from tkinter import filedialog

########### WINDOW ###################
win = Tk()
win.title("Notepad PY@Mal4D")
win.geometry('1030x830')
win.configure(bg='white')


################ CLASS ##############

class Window ():
    def __init__(self, win):
        self.win=win

########## INPUT SPACE ##############
        self.tinput=Text(self.win,borderwidth=5, background='lightgray')
        self.tinput.grid(row=2,column=2, ipady=180,ipadx=120)

########## BUTTONS ##########
        Button(self.win, text="Open", command=self.ofile).grid(row=0,column=0)   
        Button(self.win, text="Save", command=self.sfile).grid(row=0,column=1)   


    def sfile(self):
        swin=Tk()
        swin.geometry('400x300')
        swin.title('Save File as ')
        swin.configure(background='white')
        fcontents=self.tinput.get(0.0,END)

        def wfile():
            with open(fname.get()+'.txt','w+') as file:
                file.write(fcontents)
                file.close()
                swin.destroy()


        Label(swin, text='File name  : ',background='white' ).grid(row=0,column=1)
        fname=Entry(swin, width=43)
        fname.grid(row=1,column=1)
        Button(swin, text="Save", command=wfile).grid(row=3,column=1)   

    def ofile(self):
        owin=Tk()
        owin.geometry('400x300')
        owin.title('Open File ')
        owin.configure(background='white')

        def rfile():
            try:

                with open (fname1.get(), "r") as file:
                    self.tinput.delete(0.0,END)
                    self.tinput.insert(0.0,file.read())
                    file.close()
                    owin.destroy()
            except FileNotFoundError:
                fname1.delete(0,END)
                fname1.insert(0,"FILE NOT FOUND.")

        Label(owin, text='File name  : ',background='white' ).grid(row=0,column=1)
        fname1=Entry(owin, width=43)
        fname1.grid(row=1,column=1)
        Button(owin, text="Open", command=rfile).grid(row=3,column=1)   




Window(win)













win.mainloop()