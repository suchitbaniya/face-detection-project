from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student

class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Facial Attendance System")

        #Background image
        img = Image.open("./image_file/background_image.jpeg")
        img = img.resize((1530,790),Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, width=1530, height=790)

        title_lbl =Label(bg_img,text="Face Recognition Attendance System",font=("times new roman",35, "bold"),bg= "blue"
                         ,fg="white")
        title_lbl.place(x=0,y=0,width=1530,height= 50)

        #Student Button
        img1 = Image.open("./image_file/button_image.jpeg")
        img1 = img1.resize((250, 250), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        b1 = Button(bg_img,image=self.photoimg1,command=self.student_details,cursor="hand2")
        b1.place(x= 200,y=100,width= 250,height=250)

        b1_1 = Button(bg_img, text="Students Details",command=self.student_details, cursor="hand2",font=("times new roman",20, "bold"),bg="blue",fg="white")
        b1_1.place(x=200, y=350, width=250, height=40)

        # Detect face Button
        img2 = Image.open("./image_file/face_detector_image.jpeg")
        img2 = img2.resize((250, 250), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        b2 = Button(bg_img, image=self.photoimg2, cursor="hand2")
        b2.place(x=600, y=100, width=250, height=250)

        b2_1 = Button(bg_img, text="Face Detector", cursor="hand2", font=("times new roman", 20, "bold"),bg="blue",fg="white")
        b2_1.place(x=600, y=350, width=250, height=40)

        # Attendance Button
        img3 = Image.open("./image_file/Attendance_image.jpeg")
        img3 = img3.resize((250, 250), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b3 = Button(bg_img, image=self.photoimg3, cursor="hand2")
        b3.place(x=1000, y=100, width=250, height=250)

        b3_1 = Button(bg_img, text="Attendance", cursor="hand2", font=("times new roman", 20, "bold"),bg="blue",fg="white")
        b3_1.place(x=1000, y=350, width=250, height=40)

        # Train dataset Button
        img4 = Image.open("./image_file/train_dataset_image.jpeg")
        img4 = img4.resize((250, 250), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b4 = Button(bg_img, image=self.photoimg4, cursor="hand2")
        b4.place(x=200, y=450, width=250, height=250)

        b4_1 = Button(bg_img, text="Train Data", cursor="hand2", font=("times new roman", 20, "bold"),bg="blue",fg="white")
        b4_1.place(x=200, y=700, width=250, height=40)

        # Developers Button
        img5 = Image.open("./image_file/Developers_image.jpeg")
        img5 = img5.resize((250, 250), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b5 = Button(bg_img, image=self.photoimg5, cursor="hand2")
        b5.place(x=600, y=450, width=250, height=250)

        b5_1 = Button(bg_img, text="Developers", cursor="hand2", font=("times new roman", 20, "bold"),bg="blue",fg="white")
        b5_1.place(x=600, y=700, width=250, height=40)

        # Exit Button
        img6 = Image.open("./image_file/Exit_image.jpeg")
        img6 = img6.resize((250, 250), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b6 = Button(bg_img, image=self.photoimg6, cursor="hand2")
        b6.place(x=1000, y=450, width=250, height=250)

        b6_1 = Button(bg_img, text="Exit", cursor="hand2", font=("times new roman", 20, "bold"),bg="blue",fg="white")
        b6_1.place(x=1000, y=700, width=250, height=40)


    #=========Functions button==========
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)









if __name__=="__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
