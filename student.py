from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk

class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Facial Attendance System")

        # Background image
        img = Image.open("./image_file/background_image.jpeg")
        img = img.resize((1530, 790), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, width=1530, height=790)

        title_lbl = Label(bg_img, text="Student Management System", font=("times new roman", 35, "bold"),
                          bg="blue", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=50)

        #main frame
        main_frame = Frame(bg_img,bd=2,bg= "white")
        main_frame.place(x=20,y=100,width=1400,height=640)

        #Left Label Frame

        left_frame = LabelFrame(main_frame, bd=2,bg="white", relief=RIDGE,text="Student Details",font=("times new roman",15, "bold"))
        left_frame.place(x=10,y=10,width=680, height=600)

        img_left= Image.open("./image_file/Student_image2.jpeg")
        img_left = img_left.resize((720, 125), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(left_frame, image=self.photoimg_left)
        f_lbl.place(x=0, y=0, width=720, height=125)

        #Current Courses

        course_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Courses",
                                font=("times new roman", 15, "bold"))
        course_frame.place(x=10, y=125, width=660, height=140)


        #Department Label

        department_label = Label(course_frame,text="Department:",font=("times new roman",15, "bold"))
        department_label.grid(row=0,column=0, padx=15,pady= 12)

        department_combo = ttk.Combobox(course_frame,font=("times new roman",15, "bold"),width=20,state="readonly")
        department_combo["values"] = ("Select Department", "Engineering", "IT")
        department_combo.current(0)
        department_combo.grid(row=0, column=1, padx=10,pady=12)

        # Course Label

        course_label = Label(course_frame, text="Course:", font=("times new roman", 15, "bold"))
        course_label.grid(row=0, column=2,padx=15,pady=12)

        course_combo = ttk.Combobox(course_frame, font=("times new roman", 15, "bold"), width=20, state="readonly")
        course_combo["values"] = ("Select course", "Civil", "CSIT", "BCA", "Mechanical")
        course_combo.current(0)
        course_combo.grid(row=0, column=3,padx=10,pady=12)

        # Year Label

        year_label = Label(course_frame, text="Year:", font=("times new roman", 15, "bold"))
        year_label.grid(row=1, column=0,padx=15,pady=15)

        year_combo = ttk.Combobox(course_frame, font=("times new roman", 15, "bold"), width=20, state="readonly")
        year_combo["values"] = ("Select Year", "2018", "2019", "2020", "2021","2022","2023")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=10,pady=15)

        # Semester Label

        semester_label = Label(course_frame, text="Semester:", font=("times new roman", 15, "bold"))
        semester_label.grid(row=1, column=2,padx=15,pady=15)

        semester_combo = ttk.Combobox(course_frame, font=("times new roman", 15, "bold"), width=20, state="readonly")
        semester_combo["values"] = ("Select Semester", "First", "Second", "Third", "Fourth","Fifth","Sixth","Seventh","Eighth")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3,padx=10,pady=15)


        #Class Student Information
        student_info_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Student Information", font=("times new roman", 15, "bold"))
        student_info_frame.place(x=10, y=265, width=660, height=305)

        #Student_ID
        student_ID_label = Label(student_info_frame, text="StudentID:", font=("times new roman", 15, "bold"))
        student_ID_label.grid(row=0, column=0,pady=10)

        student_ID_entry = ttk.Entry(student_info_frame, width=20,font=("times new roman", 15, "bold"))
        student_ID_entry.grid(row=0, column=1,pady=10)

        # Student Name
        student_name_label = Label(student_info_frame, text="StudentName:", font=("times new roman", 15, "bold"))
        student_name_label.grid(row=0, column=2, pady=10)

        student_name_entry = ttk.Entry(student_info_frame, width=20, font=("times new roman", 15, "bold"))
        student_name_entry.grid(row=0, column=3, pady=10)

        # Student roll no
        student_roll_label = Label(student_info_frame, text="Roll no:", font=("times new roman", 15, "bold"))
        student_roll_label.grid(row=1, column=0, pady=10)

        student_roll_entry = ttk.Entry(student_info_frame, width=20, font=("times new roman", 15, "bold"))
        student_roll_entry.grid(row=1, column=1, pady=10)

        # Student gender
        student_gender_label = Label(student_info_frame, text="Gender:", font=("times new roman", 15, "bold"))
        student_gender_label.grid(row=1, column=2, pady=10)

        student_gender_entry = ttk.Entry(student_info_frame, width=20, font=("times new roman", 15, "bold"))
        student_gender_entry.grid(row=1, column=3, pady=10)

        # Student DOB
        student_DOB_label = Label(student_info_frame, text="DOB:", font=("times new roman", 15, "bold"))
        student_DOB_label.grid(row=2, column=0, pady=10)

        student_DOB_entry = ttk.Entry(student_info_frame, width=20, font=("times new roman", 15, "bold"))
        student_DOB_entry.grid(row=2, column=1, pady=10)

        # Student Email
        student_Email_label = Label(student_info_frame, text="Email:", font=("times new roman", 15, "bold"))
        student_Email_label.grid(row=2, column=2, pady=10)

        student_Email_entry = ttk.Entry(student_info_frame, width=20, font=("times new roman", 15, "bold"))
        student_Email_entry.grid(row=2, column=3, pady=10)

        # Student Phone
        student_phone_label = Label(student_info_frame, text="Phone:", font=("times new roman", 15, "bold"))
        student_phone_label.grid(row=3, column=0, pady=10)

        student_phone_entry = ttk.Entry(student_info_frame, width=20, font=("times new roman", 15, "bold"))
        student_phone_entry.grid(row=3, column=1, pady=10)

        # Student Address
        student_address_label = Label(student_info_frame, text="Address:", font=("times new roman", 15, "bold"))
        student_address_label.grid(row=3, column=2, pady=10)

        student_address_entry = ttk.Entry(student_info_frame, width=20, font=("times new roman", 15, "bold"))
        student_address_entry.grid(row=3, column=3, pady=10)

        #Radio Buttons
        radiobutton1 = ttk.Radiobutton(student_info_frame,text="Take Photo Sample", value="Yes")
        radiobutton1.grid(row=5,column=0,padx=10)

        radiobutton2 = ttk.Radiobutton(student_info_frame, text="No Photo Sample", value="Yes")
        radiobutton2.grid(row=5, column=1,padx=10)

        #Operation Frame
        operation_frame = LabelFrame(student_info_frame, bd=2, bg="white", relief=RIDGE,)
        operation_frame.place(x=0, y=220, width=655, height=60)

        #Save button
        save_btn = Button(operation_frame,text="Save",width=27, font=("times new roman", 15, "bold"),fg="blue")
        save_btn.grid(row=0, column=0)

        # Update button
        update_btn = Button(operation_frame, text="Update", width=27, font=("times new roman", 15, "bold"), fg="blue")
        update_btn.grid(row=0, column=1)

        # Delete button
        delete_btn = Button(operation_frame, text="Delete", width=26, font=("times new roman", 15, "bold"), fg="blue")
        delete_btn.grid(row=0, column=2)

        # Reset button
        reset_btn = Button(operation_frame, text="Reset", width=27, font=("times new roman", 15, "bold"), fg="blue")
        reset_btn.grid(row=1, column=0)

        # Take photo sample button
        take_photo_btn = Button(operation_frame, text="Take Photo", width=27, font=("times new roman", 15, "bold"), fg="blue")
        take_photo_btn.grid(row=1, column=1)

        # Update Photo button
        update_photo_btn = Button(operation_frame, text="Update Photo", width=26, font=("times new roman", 15, "bold"),fg ="blue")
        update_photo_btn.grid(row=1, column=2)





        # Right Label Frame

        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details",
                                font=("times new roman", 15, "bold"))
        right_frame.place(x=700, y=10, width=680, height=600)

        # search system
        search_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE, text="Search system",
                                 font=("times new roman", 15, "bold"))
        search_frame.place(x=10, y=5, width=660, height=100)

        #Search label
        search_label = Label(search_frame, text="Search By:", font=("times new roman", 15, "bold"))
        search_label.grid(row=0, column=0,padx=10)

        search_combo = ttk.Combobox(search_frame, font=("times new roman", 15, "bold"), width=20, state="readonly")
        search_combo["values"] = ("Select", "StudentID", "Phone")
        search_combo.current(0)
        search_combo.grid(row=0, column=1)

        #Search Entry
        student_address_entry = ttk.Entry(search_frame, width=20, font=("times new roman", 15, "bold"))
        student_address_entry.grid(row=0, column=2 )

        #Search Button
        search_btn = Button(search_frame, text="Search", width=20, font=("times new roman", 15, "bold"),
                                  fg="blue")
        search_btn.grid(row=0, column=3)

        #Table frame
        table_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=10, y=110, width=660, height=460)

        #Scroll Bar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame,columns=("Dep","Course","Year","Semester","ID","Name","Roll no"
                                                              ,"Gender","DOB","Email","Phone","Address","Photo"),
                                          xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Dep",text="Department")
        self.student_table.heading("Course", text="Course")
        self.student_table.heading("Year", text="Year")
        self.student_table.heading("Semester", text="Semester")
        self.student_table.heading("ID", text="ID")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("Roll no", text="Roll no")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("DOB", text="DOB")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("Phone", text="Phone")
        self.student_table.heading("Address", text="Address")
        self.student_table.heading("Photo", text="Photo")
        self.student_table["show"]="headings"

        self.student_table.column("Dep",width=100)
        self.student_table.column("Course", width=100)
        self.student_table.column("Year", width=100)
        self.student_table.column("Semester", width=100)
        self.student_table.column("ID", width=100)
        self.student_table.column("Name", width=100)
        self.student_table.column("Roll no", width=100)
        self.student_table.column("Gender", width=100)
        self.student_table.column("DOB", width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Phone", width=100)
        self.student_table.column("Address", width=100)
        self.student_table.column("Photo", width=100)



        self.student_table.pack(fill=BOTH,expand=1)












if __name__=="__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()