from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Facial Attendance System")

        title_lbl =Label(text="Face Recognition Attendance System")
        title_lbl.place(x=0,y=0,width=10,height= 1245)






if __name__=="__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
