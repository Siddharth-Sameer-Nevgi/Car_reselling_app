import csv
import customtkinter as ctk
import random
import smtplib
from sys import exit
from PIL import Image
from tkinter import filedialog
import tkinter.messagebox as tkmb


# To store login credentials
def addcsv(nameofdealer, user_detail2, user_entry, user_pass):
    noo = nameofdealer.get()
    folder = user_detail2.get()
    with open("details__.csv", "a", newline="") as f:
        w = csv.writer(f)
        l = [user_entry.get(), user_pass.get(), noo, folder]
        w.writerow(l)
        func(new_window, new_window1)


colour1 = "#0066b2"
colour2 = "#B9D9EB"


# For switching the windows
def func(a, b):
    a.withdraw()
    b.deiconify()


# For OTP generation
def generate_otp():
    return str(random.randint(100000, 999999))


def send_otp_email(user_mail):
    email = user_mail.get()
    smtp_server = "smtp.office365.com"
    smtp_port = 587
    smtp_username = "sidnevgi@outlook.com"
    smtp_password = "Teachnext@123"
    sender_email = smtp_username
    receiver_email = email
    subject = "OTP Verification"
    otp = generate_otp()
    with open("otp.txt", "w") as f:
        f.write(str(otp))
    message = f"Your OTP is: {otp}"

    email_message = f"Subject: {subject}\n\n{message}\n\nIssued by Sidnevgi"

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(sender_email, receiver_email, email_message)
            button1.configure(state="disabled")
    except Exception:
        tkmb.showwarning(
            title="Your account is not created!!",
            message="Please confirm your password and click signup",
        )


def generate_send(email):
    send_otp_email(email)


# Login function
def login():
    with open("details__.csv", "r") as f:
        try:
            r = csv.reader(f)
            for i in r:
                if user_entry.get() == i[0]:
                    if user_pass.get() == i[1]:
                        tkmb.showinfo(
                            title="Login Successful",
                            message="You have logged in Successfully",
                        )
                        func(app1, new_window1)
                    else:
                        tkmb.showwarning(
                            title="Wrong password", message="Please check your password"
                        )
                else:
                    tkmb.showwarning(
                        title="Wrong username", message="Please check your username"
                    )
        except EOFError:
            tkmb.showwarning(
                title="Your account isnt created!!",
                message="Please confirm your password and click signup",
            )


# Sign up function
def sign_up():
    userp = user_pass.get()
    userc = pass_confirm.get()
    with open("otp.txt", "r") as f:
        s = f.read()
    if (
        userp == userc
        and user_entry.get() != ""
        and userp != ""
        and otp_entry.get() == s
    ):
        tkmb.showinfo(
            title="Sucessfully Signed Up", message=f"Welcome {user_entry.get()}"
        )
        func(app1, new_window)
    else:
        tkmb.showerror(
            title="Error 404", message="Passwords do not match or no username entered"
        )


# Close Button
def close(windowname):
    close_button = ctk.CTkButton(
        windowname, text="X", command=exit, width=50, height=50, hover_color="red"
    )
    close_button.place(
        x=windowname.winfo_screenwidth() - 50 - close_button.winfo_width(), y=0
    )


# Back Button
def back(windowname, d):
    def switch_windows():
        windowname.withdraw()
        d.deiconify()

    back_button = ctk.CTkButton(
        windowname,
        text="Back",
        command=switch_windows,
        width=50,
        height=50,
        hover_color="yellow",
    )
    back_button.place(x=0 - back_button.winfo_width(), y=0)


# To select folder
def select_folder(entry):
    global folder
    file_path = filedialog.askdirectory()
    entry.insert(ctk.END, file_path)
    folder = entry.get()


# To select file
def select_file(entry):
    file_path = filedialog.askopenfilename()
    if file_path:
        entry.delete(0, ctk.END)
        entry.insert(ctk.END, file_path)


def filer():
    global file
    try:
        with open("details__.csv", "r") as f1:
            r = csv.reader(f1)
            for i in r:
                if i[0] == user_entry.get() and i[1] == user_pass.get():
                    folder = i[3]
    except:
        tkmb.showwarning(
            title="Error",
            message="You have deleted Or changed the location of the file",
        )
    file = folder + "/carsnew.csv"


# Login/Signup page
def start1(app):
    global app1
    global user_pass
    global user_entry
    global pass_confirm
    global user_mail
    global otp_entry
    global button1
    app1 = ctk.CTkToplevel(app, fg_color=colour1)
    app1.attributes("-fullscreen", True)
    close(app1)
    label = ctk.CTkLabel(
        app1,
        text="WELCOME TO CARS64 INDIA'S NO 1. CAR RESELLING APP",
        height=20,
        font=("Georgia", 40, "bold"),
        text_color="#CCCCFF",
    )
    label.pack(pady=20)
    frame = ctk.CTkScrollableFrame(app1, fg_color=colour2)
    frame.pack(pady=20, padx=40, fill="both", expand=True)
    label = ctk.CTkLabel(
        frame, text="SIGN UP/LOGIN PAGE", font=("Roboto", 40, "bold"), text_color="blue"
    )
    label.pack(pady=12, padx=12)
    user_mail = ctk.CTkEntry(
        frame, placeholder_text="Email", width=220, height=50, font=("Arial", 15)
    )
    user_mail.pack(pady=12, padx=10)
    user_entry = ctk.CTkEntry(
        frame, placeholder_text="Username", width=220, height=50, font=("Arial", 15)
    )
    user_entry.pack(pady=12, padx=10)
    user_pass = ctk.CTkEntry(
        frame,
        placeholder_text="Password",
        show="*",
        width=220,
        height=50,
        font=("Arial", 15),
    )
    user_pass.pack(pady=12, padx=10)
    pass_confirm = ctk.CTkEntry(
        frame,
        placeholder_text="Confirm password",
        show="*",
        width=220,
        height=50,
        font=("Arial", 15),
    )
    pass_confirm.pack(pady=12, padx=10)
    otp_entry = ctk.CTkEntry(
        frame,
        placeholder_text="Enter the otp",
        width=220,
        height=50,
        font=("Arial", 15),
    )
    otp_entry.pack(pady=12, padx=10)
    button1 = ctk.CTkButton(
        frame,
        text="Send OTP",
        command=lambda: generate_send(user_mail),
        width=190,
        height=40,
        text_color="black",
        font=("Arial", 20),
        fg_color="#FEBE10",
    )
    button1.pack(pady=12, padx=10)
    button = ctk.CTkButton(
        frame,
        text="Login",
        width=190,
        height=40,
        command=lambda: login(),
        text_color="black",
        font=("Arial", 20),
        fg_color="#FEBE10",
    )
    button.pack(pady=12, padx=10)
    sign_upb = ctk.CTkButton(
        frame,
        text="Sign Up",
        width=190,
        height=40,
        command=lambda: sign_up(),
        text_color="black",
        font=("Arial", 20),
        fg_color="#FEBE10",
    )
    sign_upb.pack(pady=12, padx=10)
    app1.withdraw()


# MAIN APP
def main(app):
    global new_window1
    new_window1 = ctk.CTkToplevel(app, fg_color=colour1)
    new_window1.attributes("-fullscreen", True)
    back(new_window1, app1)
    close(new_window1)
    labelmain = ctk.CTkLabel(
        new_window1,
        text=f"WELCOME USER",
        height=20,
        font=("Georgia", 50, "bold"),
        text_color="white",
    )
    labelmain.pack(pady=20)
    frame_main = ctk.CTkFrame(new_window1, fg_color=colour2)
    frame_main.pack(pady=20, padx=40, fill="both", expand=True)
    mainb1 = ctk.CTkButton(
        frame_main,
        text="Add Car",
        font=("Arial", 20, "bold"),
        fg_color="#FEBE10",
        text_color="black",
        width=470,
        height=70,
        command=lambda: func(new_window1, new_window2),
    )
    mainb1.pack(pady=12, padx=16)
    display_button = ctk.CTkButton(
        frame_main,
        text="Display Cars",
        font=("Arial", 20, "bold"),
        fg_color="#FEBE10",
        text_color="black",
        width=470,
        height=70,
        command=lambda: display(app),
    )
    display_button.pack(pady=12, padx=16)
    modify_button = ctk.CTkButton(
        frame_main,
        text="Modify Car Details",
        fg_color="#FEBE10",
        text_color="black",
        font=("Arial", 20, "bold"),
        width=470,
        height=70,
        command=lambda: (func(new_window1, new_window3)),
    )
    modify_button.pack(pady=12, padx=16)
    mainb4 = ctk.CTkButton(
        frame_main,
        text="Search for particular car",
        font=("Arial", 20, "bold"),
        fg_color="#FEBE10",
        text_color="black",
        width=470,
        height=70,
        command=lambda: func(new_window1, new_windows),
    )
    mainb4.pack(pady=12, padx=16)
    mainb5 = ctk.CTkButton(
        frame_main,
        text="Sell Car",
        font=("Arial", 20, "bold"),
        fg_color="#FEBE10",
        text_color="black",
        width=470,
        height=70,
        command=lambda: func(new_window1, new_windowdel),
    )
    mainb5.pack(pady=12, padx=16)
    new_window1.withdraw()


# Custom window
def custom(app):
    global user_detail2
    global new_window
    global nameofdealer
    new_window = ctk.CTkToplevel(app, fg_color=colour1)
    new_window.attributes("-fullscreen", True)
    back(new_window, app1)
    close(new_window)
    label = ctk.CTkLabel(
        new_window,
        text="WELCOME USER",
        font=("Georgia", 50, "bold"),
        text_color="white",
    )
    label.pack(pady=20)
    frame_ = ctk.CTkFrame(master=new_window, fg_color=colour2)
    frame_.pack(pady=20, padx=40, fill="both", expand=True)
    label1 = ctk.CTkLabel(master=frame_, text="Add Your details", font=("Arial", 30))
    label1.pack(pady=12, padx=10)
    nameofdealer = ctk.CTkEntry(
        master=frame_,
        placeholder_text="Name of organisation",
        width=220,
        height=50,
        font=("Arial", 15),
    )
    nameofdealer.pack(pady=12, padx=10)
    user_detail2 = ctk.CTkEntry(
        master=frame_,
        placeholder_text="Select the folder to store data",
        width=220,
        height=50,
        font=("Arial", 15),
    )
    user_detail2.pack(pady=12, padx=10)
    userb = ctk.CTkButton(
        master=frame_,
        text="Select folder",
        command=lambda: select_folder(user_detail2),
        width=190,
        height=40,
        text_color="black",
        font=("Arial", 20),
        fg_color="#FEBE10",
    )
    userb.pack(pady=12, padx=10)
    sub_b = ctk.CTkButton(
        master=frame_,
        text="Submit",
        width=190,
        height=40,
        text_color="black",
        fg_color="#FEBE10",
        font=("Arial", 20),
        command=lambda: addcsv(nameofdealer, user_detail2, user_entry, user_pass),
    )
    sub_b.pack(pady=12, padx=10)
    new_window.withdraw()


def start(app):
    app.title("carbecho")
    label = ctk.CTkLabel(
        app,
        text="WELCOME TO CARS64",
        height=20,
        font=("Georgia", 50, "bold"),
        text_color="white",
    )
    label.pack(pady=20)
    frame = ctk.CTkFrame(app, fg_color=colour2)
    frame.pack(pady=20, padx=40, fill="both", expand=True)
    button = ctk.CTkButton(
        frame,
        text="Login/Sign up",
        font=("Arial", 50),
        width=500,
        height=300,
        command=lambda: func(app, app1),
    )
    button.pack(pady=12, padx=10)


# Add Cars
def addcars(app):
    global new_window2
    global car_name
    global car_model
    global car_price
    global car_image_path
    global cus_name
    global car_term
    new_window2 = ctk.CTkToplevel(app, fg_color=colour1)
    new_window2.attributes("-fullscreen", True)
    back(new_window2, new_window1)
    close(new_window2)
    labeladd = ctk.CTkLabel(
        new_window2,
        text="Add New Cars",
        height=20,
        font=("Georgia", 50),
        text_color="white",
    )
    labeladd.pack(pady=20)
    frame = ctk.CTkFrame(master=new_window2, fg_color=colour2)
    frame.pack(pady=20, padx=40, fill="both", expand=True)
    cus_name = ctk.CTkEntry(
        master=frame,
        placeholder_text="Customer name",
        width=220,
        height=50,
        font=("Arial", 15),
    )
    cus_name.pack(pady=12, padx=10)
    car_name = ctk.CTkEntry(
        master=frame,
        placeholder_text="Car name",
        width=220,
        height=50,
        font=("Arial", 15),
    )
    car_name.pack(pady=12, padx=10)
    car_model = ctk.CTkEntry(
        master=frame,
        placeholder_text="Model no",
        width=220,
        height=50,
        font=("Arial", 15),
    )
    car_model.pack(pady=12, padx=10)
    car_term = ctk.CTkEntry(
        master=frame,
        placeholder_text="Year of purchase",
        width=220,
        height=50,
        font=("Arial", 15),
    )
    car_term.pack(pady=12, padx=10)
    car_price = ctk.CTkEntry(
        master=frame, placeholder_text="Price", width=220, height=50, font=("Arial", 15)
    )
    car_price.pack(pady=12, padx=10)
    car_image_path = ctk.CTkEntry(
        master=frame,
        placeholder_text="Select the car image",
        width=220,
        height=50,
        font=("Arial", 15),
    )
    car_image_path.pack(pady=12, padx=10)
    userb = ctk.CTkButton(
        master=frame,
        text="Select file",
        command=lambda: select_file(car_image_path),
        width=190,
        height=40,
        text_color="black",
        font=("Arial", 20),
        fg_color="#FEBE10",
    )
    userb.pack(pady=12, padx=10)
    save_button = ctk.CTkButton(
        master=frame,
        text="Save Details",
        command=lambda: save_car_details(),
        width=190,
        height=40,
        text_color="black",
        font=("Arial", 20),
        fg_color="#FEBE10",
    )
    save_button.pack(pady=12, padx=10)
    new_window2.withdraw()


def save_car_details():
    cusname = cus_name.get()
    name = car_name.get()
    model = car_model.get()
    year = car_term.get()
    price = car_price.get()
    image_path = car_image_path.get()
    filer()
    with open(file, "a", newline="") as f:
        f.seek(0)
        if (
            cusname != ""
            and name != ""
            and model != ""
            and year != ""
            and price != ""
            and image_path != ""
        ):
            w = csv.writer(f)
            l = [cusname, name, model, year, price, image_path]
            w.writerow(l)
            car_name.delete(0, ctk.END)
            cus_name.delete(0, ctk.END)
            car_term.delete(0, ctk.END)
            car_model.delete(0, ctk.END)
            car_price.delete(0, ctk.END)
            car_image_path.delete(0, ctk.END)
        else:
            tkmb.showerror(title="empty fields", message="Missing fields")


# Modify
def modify(app):
    global new_window3
    global custname
    global car_name1
    global frame
    global carmod
    global car_term1
    global car_price1
    global car_image_path1
    global new_window3
    new_window3 = ctk.CTkToplevel(app, fg_color=colour1)
    new_window3.attributes("-fullscreen", True)
    back(new_window3, new_window1)
    close(new_window3)
    labeladd = ctk.CTkLabel(
        new_window3,
        text="Modify Car details",
        height=20,
        font=("Georgia", 50),
        text_color="white",
    )
    labeladd.pack(pady=20)
    frame = ctk.CTkFrame(master=new_window3, fg_color=colour2)
    frame.pack(pady=20, padx=40, fill="both", expand=True)
    custname = ctk.CTkEntry(
        master=frame,
        placeholder_text="Enter the customer no ",
        width=220,
        height=50,
        font=("Arial", 15),
    )
    custname.pack(pady=12, padx=10)
    carmod = ctk.CTkEntry(
        master=frame,
        placeholder_text="Enter the car model",
        width=220,
        height=50,
        font=("Arial", 15),
    )
    carmod.pack(pady=12, padx=10)
    car_name1 = ctk.CTkEntry(
        master=frame,
        placeholder_text="Car name",
        width=220,
        height=50,
        font=("Arial", 15),
    )
    car_name1.pack(pady=12, padx=10)
    car_term1 = ctk.CTkEntry(
        master=frame,
        placeholder_text="Year of purchase",
        width=220,
        height=50,
        font=("Arial", 15),
    )
    car_term1.pack(pady=12, padx=10)
    car_price1 = ctk.CTkEntry(
        master=frame, placeholder_text="Price", width=220, height=50, font=("Arial", 15)
    )
    car_price1.pack(pady=12, padx=10)
    car_image_path1 = ctk.CTkEntry(
        master=frame,
        placeholder_text="Select the car image",
        width=220,
        height=50,
        font=("Arial", 15),
    )
    car_image_path1.pack(pady=12, padx=10)
    userb = ctk.CTkButton(
        master=frame,
        text="Select file",
        command=lambda: select_file(car_image_path1),
        width=190,
        height=40,
        text_color="black",
        font=("Arial", 20),
        fg_color="#FEBE10",
    )
    userb.pack(pady=12, padx=10)
    save_button = ctk.CTkButton(
        master=frame,
        text="Modify Details",
        command=lambda: mod(),
        width=190,
        height=40,
        text_color="black",
        font=("Arial", 20),
        fg_color="#FEBE10",
    )
    save_button.pack(pady=14, padx=10)
    new_window3.withdraw()


def mod():
    a = custname.get()
    b = car_name1.get()
    c = carmod.get()
    d = car_term1.get()
    e = car_price1.get()
    h = car_image_path1.get()
    filer()
    modified_data = []
    c1 = 0
    try:
        with open(file, "r") as f:
            reader = list(csv.reader(f))
            for row in reader:
                if row[0] == a:
                    c1 += 1
                    l = [a, b, c, d, e, h]
                    modified_data.append(l)
                else:
                    modified_data.append(row)
    except:
        tkmb.showwarning(
            title="Error", message="You have deleted the file or changed its location"
        )
    if c1 == 0:
        tkmb.showerror(title="Error 404", message="No such record")
    else:
        with open(file, "w", newline="") as f1:
            writer = csv.writer(f1)
            writer.writerows(modified_data)
            car_name1.delete(0, ctk.END)
            custname.delete(0, ctk.END)
            car_term1.delete(0, ctk.END)
            carmod.delete(0, ctk.END)
            car_price1.delete(0, ctk.END)
            car_image_path1.delete(0, ctk.END)
            tkmb.showinfo(
                title="Data modified",
                message=f"""Customer name:{l[0]}\nCar Name:{l[1]}\nModel No:{l[2]}\nCar Year:{l[3]}\nCar Price:{l[4]}""",
            )


# Display cars
def display(app):
    global new_windowd
    new_windowd = ctk.CTkToplevel(app, fg_color=colour1)
    new_windowd.attributes("-fullscreen", True)
    back(new_windowd, new_window1)
    close(new_windowd)
    labeladd = ctk.CTkLabel(
        new_windowd,
        text="CARS ON SALE",
        height=20,
        font=("Georgia", 50),
        text_color="white",
    )
    labeladd.pack(pady=20)
    frame = ctk.CTkScrollableFrame(
        master=new_windowd, height=600, width=1300, fg_color="#CCCCFF", corner_radius=10
    )
    frame.pack(anchor="center")
    filer()
    try:
        with open(file) as f1:
            data = list(csv.reader(f1))
            r = co = 0
            for i in data:
                co += 1
                img = ctk.CTkImage(light_image=Image.open(i[5]), size=(300, 300))
                f1 = ctk.CTkLabel(master=frame, image=img, text="", fg_color="#98FB98")
                f1.grid(row=r, column=co, padx=10, pady=10)
                co += 1
                frame1 = ctk.CTkFrame(master=frame, height=100, width=300)
                label1 = ctk.CTkLabel(
                    frame1, text="Customer Name: " + i[0], font=("Arial", 25)
                )
                label1.pack(anchor="w")
                label2 = ctk.CTkLabel(
                    frame1, text="Car Name: " + i[1], font=("Arial", 25)
                )
                label2.pack(anchor="w")
                label3 = ctk.CTkLabel(
                    frame1, text="Car model: " + i[2], font=("Arial", 25)
                )
                label3.pack(anchor="w")
                label4 = ctk.CTkLabel(
                    frame1, text="Car year:" + i[3], font=("Arial", 25)
                )
                label4.pack(anchor="w")
                label5 = ctk.CTkLabel(
                    frame1, text="Car price:" + i[4], font=("Arial", 25)
                )
                label5.pack(anchor="w")
                frame1.grid(row=r, column=co, padx=10, pady=10)
                if co == 4:
                    co = 0
                    r += 1
                    continue
    except:
        tkmb.showerror(title="Error 404", message="No cars available")
    new_window1.withdraw()


# Search Cars
def search(app):
    global new_windows
    global cusno
    global frames
    new_windows = ctk.CTkToplevel(app, fg_color=colour1)
    new_windows.attributes("-fullscreen", True)
    back(new_windows, new_window1)
    close(new_windows)
    labeladd = ctk.CTkLabel(
        new_windows,
        text="Search for Cars",
        height=20,
        font=("Georgia", 50),
        text_color="white",
    )
    labeladd.pack(pady=20)
    frames = ctk.CTkFrame(master=new_windows, fg_color=colour2)
    frames.pack(pady=20, padx=40, fill="both", expand=True)
    cusno = ctk.CTkEntry(
        master=frames,
        placeholder_text="Enter the Customer name",
        width=220,
        height=50,
        font=("Arial", 15),
    )
    cusno.pack(pady=12, padx=10)
    save_button = ctk.CTkButton(
        master=frames,
        text="Search",
        command=lambda: sea(),
        width=190,
        height=40,
        text_color="black",
        font=("Arial", 20),
        fg_color="#FEBE10",
    )
    save_button.pack(pady=14, padx=10)
    new_windows.withdraw()


def sea():
    global labeladd1
    a = cusno.get()
    filer()
    c = 0
    try:
        with open(file, "r", newline="") as f:
            reader = csv.reader(f)
            for i in reader:
                if i[0] == a:
                    c += 1
                    l = i
    except FileNotFoundError:
        tkmb.showerror(title="Error 404", message="No such record")

    if c == 0:
        tkmb.showerror(title="Error 404", message="No such record")
        clear_button = ctk.CTkButton(
            master=frames,
            text="Clear",
            command=lambda: clear1(cusno, clear_button),
            width=190,
            height=40,
            text_color="black",
            font=("Arial", 20),
            fg_color="#FEBE10",
        )
        clear_button.pack(pady=14, padx=10)
    else:
        clear_button = ctk.CTkButton(
            master=frames,
            text="Clear",
            command=lambda: clear(labeladd1, cusno, clear_button),
            width=190,
            height=40,
            text_color="black",
            font=("Arial", 20),
            fg_color="#FEBE10",
        )
        clear_button.pack(pady=14, padx=10)
        labeladd1 = ctk.CTkLabel(frames, width=1000, height=500, font=("Arial", 20))
        labeladd1.pack(pady=12, padx=20)
        img = ctk.CTkImage(light_image=Image.open(l[5]), size=(300, 300))
        f1 = ctk.CTkLabel(master=labeladd1, image=img, text="", fg_color="lightblue")
        f1.grid(row=0, column=0, padx=10, pady=10)
        tkmb.showinfo(
            title="Data found",
            message=f"Customer name:{l[0]}\nCar Name:{l[1]}\nModel No:{l[2]}\nCar Year:{l[3]}\nCar Price:{l[4]}",
        )


# Sell Car
def delete(app):
    global new_windowdel
    global cusno1
    global framedel
    new_windowdel = ctk.CTkToplevel(app, fg_color=colour1)
    new_windowdel.attributes("-fullscreen", True)
    back(new_windowdel, new_window1)
    close(new_windowdel)
    labeladd = ctk.CTkLabel(
        new_windowdel,
        text="Sell Car",
        height=20,
        font=("Georgia", 50),
        text_color="white",
    )
    labeladd.pack(pady=20)
    framedel = ctk.CTkFrame(master=new_windowdel, fg_color=colour2)
    framedel.pack(pady=20, padx=40, fill="both", expand=True)
    cusno1 = ctk.CTkEntry(
        master=framedel,
        placeholder_text="Enter the Customer name",
        width=220,
        height=50,
    )
    cusno1.pack(pady=12, padx=10)
    save_button = ctk.CTkButton(
        master=framedel,
        text="Sell",
        command=lambda: delc(),
        width=190,
        height=40,
        text_color="black",
        font=("Arial", 20),
        fg_color="#FEBE10",
    )
    save_button.pack(pady=12, padx=10)
    new_windowdel.withdraw()


def clear(label, textbox, button):
    label.destroy()
    textbox.delete(0, ctk.END)
    button.destroy()


def clear1(textbox, button):
    textbox.delete(0, ctk.END)
    button.destroy()


def delc():
    global labeladdd
    a = cusno1.get()
    filer()
    modified_data = []
    c = 0
    try:
        with open(file, "r", newline="") as f:
            reader = list(csv.reader(f))
            for i in reader:
                if i[0] != a:
                    modified_data.append(i)
                else:
                    c += 1
                    clear_button = ctk.CTkButton(
                        master=framedel,
                        text="Clear",
                        width=190,
                        height=40,
                        text_color="black",
                        fg_color="#FEBE10",
                        command=lambda: clear(labeladdd, cusno1, clear_button),
                        font=("Arial", 20),
                    )
                    clear_button.pack(pady=14, padx=10)
                    labeladdd = ctk.CTkLabel(
                        framedel, width=1000, height=500, font=("Arial", 20)
                    )
                    labeladdd.pack(pady=12, padx=20)
                    img = ctk.CTkImage(light_image=Image.open(i[5]), size=(300, 300))
                    f1 = ctk.CTkLabel(
                        master=labeladdd, image=img, text="", fg_color="lightblue"
                    )
                    f1.grid(row=0, column=0, padx=10, pady=10)
                    tkmb.showinfo(
                        title="Car sold",
                        message=f"Customer name:{i[0]}\nCar Name:{i[1]}\nModel No:{i[2]}\nCar Year:{i[3]}\nCar Price:{i[4]}",
                    )
    except FileNotFoundError:
        tkmb.showwarning(title="Warning", message="The file has been deleted or moved")
    if c == 0:
        tkmb.showerror(title="Error 404", message="No such record")
        clear_button = ctk.CTkButton(
            master=framedel,
            text="Clear",
            command=lambda: clear1(cusno1, clear_button),
            width=190,
            height=40,
            text_color="black",
            font=("Arial", 20, "bold"),
            fg_color="#FEBE10",
        )
        clear_button.pack(pady=14, padx=10)
    else:
        with open(file, "w", newline="") as f1:
            writer = csv.writer(f1)
            writer.writerows(modified_data)


# Calling all the functions
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("dark-blue")
app = ctk.CTk(fg_color=colour1)
start1(app)
custom(app)
main(app)
search(app)
delete(app)
modify(app)
custom(app)
addcars(app)
start(app)
app.mainloop()
