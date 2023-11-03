from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3
import cv2
import os
import uuid

def main():
    main_win()

def center(window, w, h):
    window.resizable(False, False)
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (w/2))
    y_cordinate = int((screen_height/2) - (h/2))
    window.geometry("{}x{}+{}+{}".format(w, h, x_cordinate, y_cordinate))

def main_win():
    global main_window
    main_window = tk.Tk()
    main_window.resizable(False, False)
    center(main_window, 500, 500)
    main_window.title("員工註冊系統")

    frame = tk.Frame(main_window)
    frame.pack()
    # screen
    register_btn = tk.Button(frame, font= "微軟正黑體", text= "註冊", height=2, width= 7, bg= "#FFD306", command=register_win)
    update_btn = tk.Button(frame, font= "微軟正黑體", text= "更新", height=2, width= 7, bg= "#ADADAD", command=update_win)
    delete_btn = tk.Button(frame, font= "微軟正黑體", text= "刪除", height=2, width= 7, bg= "#F75000", command=delete_win)
    register_btn.grid(row= 0, column= 1, padx= 15, pady=220)
    update_btn.grid(row= 0, column= 2, padx= 15, pady= 220)
    delete_btn.grid(row= 0, column= 3, padx= 15, pady= 220)

    main_window.mainloop()

def delete_win():
    main_window.destroy()
    global delete_window
    delete_window = tk.Tk()
    frame = tk.Frame(delete_window)
    frame.pack()
    center(delete_window, 350, 250)
    delete_window.title("刪除資料")

    global delete_userId_en
    # label
    delete_userId_lb = tk.Label(frame, font= "微軟正黑體", text= "員工編號: ")
    delete_userId_lb.grid(row= 0, column= 0, pady= 20)
    # entry
    delete_userId_en = tk.Entry(frame, font= "微軟正黑體")
    delete_userId_en.grid(row= 0, column=1, pady= 20)
    # button
    delete_btn = tk.Button(frame, font="微軟正黑體", text= "刪除", command=delete)
    back_btn = tk.Button(frame, font= "微軟正黑體", text= "返回", command= lambda:[delete_window.destroy(), main_win()])
    delete_btn.grid(row= 4, column= 0, columnspan=1)
    back_btn.grid(row= 4, column= 1, columnspan=1)
    
    delete_window.mainloop()

def update_win():
    main_window.destroy()
    update_window = tk.Tk()
    frame = tk.Frame(update_window)
    frame.pack()
    update_window.title("更新資料")
    center(update_window, 400, 300)

    update_userId_lb = tk.Label(frame, font= "微軟正黑體", text= "員工編號: ")
    update_name_lb = tk.Label(frame, font= "微軟正黑體", text= "員工姓名: ")
    update_company_lb = tk.Label(frame, font= "微軟正黑體", text= "所屬公司: ")
    update_number_lb = tk.Label(frame, font= "微軟正黑體", text= "聯絡方式: ")
    update_userId_lb.grid(row= 0, column= 0, pady= 20)
    update_name_lb.grid(row= 1, column= 0, pady= 20)
    update_company_lb.grid(row= 2, column= 0, pady= 20)
    update_number_lb.grid(row= 3, column= 0, pady= 20)
    # entry
    global update_userId_en,update_name_en,update_company_en,update_number_en
    update_userId_en = tk.Entry(frame, font= "微軟正黑體")
    update_name_en = tk.Entry(frame, font= "微軟正黑體")
    update_company_en = tk.Entry(frame, font= "微軟正黑體")
    update_number_en = tk.Entry(frame, font= "微軟正黑體")
    update_userId_en.grid(row= 0, column=1)
    update_name_en.grid(row= 1, column= 1)
    update_company_en.grid(row= 2, column= 1)
    update_number_en.grid(row= 3, column= 1)
    # button
    update_btn = tk.Button(frame, font= "微軟正黑體", text= "更新", command=update)
    back_btn = tk.Button(frame, font= "微軟正黑體", text= "返回", command= lambda:[update_window.destroy(), main_win()])
    update_btn.grid(row= 4, column= 0)
    back_btn.grid(row= 4, column= 1)

    update_window.mainloop()

def register_win():
    main_window.destroy()
    global register_window
    register_window = tk.Tk()
    # screen
    register_window.title("員工註冊系統")
    center(register_window, 600, 500)
    leftframe = tk.Frame(register_window)
    leftframe.pack(side=tk.LEFT, padx=20)
    rightframe = tk.Frame(register_window)
    rightframe.pack(side=tk.RIGHT, padx=20)
    # rightframe label
    userId_lb = tk.Label(rightframe, font= "微軟正黑體", text= "員工編號: ")
    name_lb = tk.Label(rightframe, font= "微軟正黑體", text= "員工姓名: ")
    company_lb = tk.Label(rightframe, font= "微軟正黑體", text= "所屬公司: ")
    number_lb = tk.Label(rightframe, font= "微軟正黑體", text= "聯絡方式: ")
    userId_lb.grid(row= 0, column= 0, pady= 20)
    name_lb.grid(row= 1, column= 0, pady= 20)
    company_lb.grid(row= 2, column= 0, pady= 20)
    number_lb.grid(row= 3, column= 0, pady= 20)
    # leftframe label
    canvas = tk.Canvas(leftframe, width=224, height=224, highlightthickness=2, highlightbackground="black")
    canvas.pack()
    canvas.create_rectangle(0, 0, 226, 226, fill="white")
    # entry
    global userId_en,name_en,company_en,number_en
    userId_en = tk.Entry(rightframe, font= "微軟正黑體")
    name_en = tk.Entry(rightframe, font= "微軟正黑體")
    company_en = tk.Entry(rightframe, font= "微軟正黑體")
    number_en = tk.Entry(rightframe, font= "微軟正黑體")
    userId_en.grid(row= 0, column=1)
    name_en.grid(row= 1, column= 1)
    company_en.grid(row= 2, column= 1)
    number_en.grid(row= 3, column= 1)
    # button
    save_btn = tk.Button(rightframe, font= "微軟正黑體", text= "註冊", command= lambda: save(canvas))
    back_btn = tk.Button(rightframe, font= "微軟正黑體", text= "返回", command= lambda:[register_window.destroy(), main_win()])
    save_btn.grid(row= 4, column= 0)
    back_btn.grid(row= 4, column= 1)

    register_window.mainloop()

def save(canvas):
    conn = sqlite3.connect('Account.db')
    mycursor = conn.cursor()

    global userId
    if (userId_en.get() == "" or name_en.get() == "" or company_en.get() == "" or number_en.get() == ""):
        messagebox.showerror("註冊失敗", "資料未填寫完整")
    else:
        userId = userId_en.get()
        name = name_en.get()
        company = company_en.get()
        number = number_en.get()
        mycursor.execute("SELECT * FROM Account WHERE userId = (?) ", (userId,))
        exist = mycursor.fetchone()
        if exist:
            messagebox.showwarning("重複", "重複使用者!")
        else:
            mycursor.execute("INSERT INTO Account VALUES(?,?,?,?)", (userId, name, company, number))
            messagebox.showinfo("", "註冊成功,請看鏡頭")
            conn.commit()
            # 蒐集照片
            datacollect(canvas, userId)

        conn.close()

def update():
    conn = sqlite3.connect('Account.db')
    mycursor = conn.cursor()

    if (update_userId_en.get() == "" or update_name_en.get() == "" or update_company_en.get() == "" or update_number_en.get() == ""):
        messagebox.showerror("更新失敗", "更新資料未填寫完整")
    else:
        update_userId = update_userId_en.get()
        update_name = update_name_en.get()
        update_company = update_company_en.get()
        update_number = update_number_en.get()
        mycursor.execute("SELECT * FROM Account WHERE userId = (?) ", (update_userId,))
        exist = mycursor.fetchone()
        if not exist:
            messagebox.showwarning("錯誤", "查無使用者")
        else:
            mycursor.execute("UPDATE Account SET name = (?), company = (?), number = (?) WHERE userId = (?)", (update_name, update_company, update_number, update_userId))
            messagebox.showinfo("更新", "更新成功！")
            conn.commit()
        conn.close()

def delete():
    conn = sqlite3.connect('Account.db')
    mycursor = conn.cursor()
    if delete_userId_en.get() == "":
        messagebox.showerror("錯誤", "請輸入使用者")
    else:
        delete_userId = delete_userId_en.get()
        path = f'./images/train/{delete_userId}'
        mycursor.execute("SELECT * FROM Account WHERE userId = (?) ", (delete_userId,))
        exist = mycursor.fetchone()
        if not exist:
            messagebox.showerror("錯誤", "使用者不存在")
        else:    
            mycursor.execute("DELETE FROM Account WHERE userId = (?)", (delete_userId,))
            messagebox.showinfo("成功", "成功刪除使用者")
            if os.path.exists(path):
                try:
                    os.remove(path)
                except OSError:
                    messagebox.showwarning("異常", "文件路徑異常")
            conn.commit()
    conn.close()

def datacollect(canvas, userId):
    cap = cv2.VideoCapture(0)
    path = f'./images/train/{userId}'
    os.makedirs(path, exist_ok=True)
    count = 0

    def show_frame():
        nonlocal count
        ret, frame = cap.read()
        frame = frame[120:120+224, 200:200+224, :]

        if ret:
            uid = uuid.uuid4()
            image_path = f'{path}/{uid}.jpg'
            cv2.imwrite(image_path, frame)
            count += 1
            print(f"Captured image: {count}")

            # Display the current frame in the Toplevel window
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            photo = ImageTk.PhotoImage(image=img)
            canvas.create_image(0, 0, anchor=tk.NW, image=photo)
            canvas.image = photo 
        if count < 300:
            canvas.configure(highlightthickness=2, highlightbackground="red")
            register_window.after(20, show_frame)
        else:
            cap.release()
            canvas.create_rectangle(0, 0, 226, 226, fill="white")
            canvas.configure(highlightthickness=2, highlightbackground="black")

    show_frame()


main()