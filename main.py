from tkinter import * 
import os
#defining more n more functions
def delete2():
	window3.destroy()
def delete3():
	window4.destroy()
def delete4():
	window5.destroy()

def login_success():
	global window3
	window3 = Toplevel(window)
	window3.title("Success")
	window3.geometry("150x100")
	Label(window3, text="Login Success").pack()
	Button(window3, text="OK", command=delete2).pack()
def password_not_recognised():
	global window4
	window4 = Toplevel(window)
	window4.title("Error")
	window4.geometry("150x100")
	Label(window4, text="PasswordNotRecognised").pack()
	Button(window4, text="OK", command=delete3).pack()
def user_not_found():
	global window5
	window5 = Toplevel(window)
	window5.title("Error")
	window5.geometry("150x100")
	Label(window5, text="UserNotFound").pack()
	Button(window5, text="OK", command=delete4).pack()

#defining more classes
def register_user():
	username_info = username.get()
	password_info = password.get()

	file=open(username_info, "w")
	file.write(username_info+"\n")
	file.write(password_info)
	file.close()

	username_entry.delete(0, END)
	password_entry.delete(0, END)

	Label(window1, text = "Registration Successful", fg="green").pack()

def login_verify():

	username1 = username_verify.get()
	password1 = password_verify.get()
	username_entry1.delete(0, END)
	password_entry1.delete(0, END)

	list_of_files = os.listdir()
	if username1 in list_of_files:
		file1 = open(username1, "r")
		verify = file1.read().splitlines()
		if password1 in verify:
			login_success()
		else:
			password_not_recognised()
	else:
		user_not_found()



#defining functions 
def register():
	global window1
	window1 = Toplevel(window)
	window1.title("Register")
	window1.geometry("300x250")

	global username
	global password
	global username_entry
	global password_entry

	username = StringVar()
	password = StringVar()

	Label(window1, text = "Please enter details below").pack()
	Label(window1, text = "").pack()

	Label(window1, text = "Username*").pack()
	username_entry = Entry(window1, textvariable = username)
	username_entry.pack()
	Label(window1, text = "Password*").pack()
	password_entry = Entry(window1, textvariable = password)
	password_entry.pack()
	Label(window1, text = "").pack()
	Button(window1, text="Register", width = 10, height =1, command=register_user).pack()


def login():
	global window2
	window2 = Toplevel(window)
	window2.title("Login")
	window2.geometry("300x250")
	Label(window2, text="Enter details").pack()
	Label(window2, text="").pack()

	global username_verify
	global password_verify

	username_verify = StringVar()
	password_verify = StringVar()

	global username_entry1
	global password_entry1

	Label(window2, text="Username*").pack()
	username_entry1 = Entry(window2, textvariable=username_verify)
	username_entry1.pack()
	Label(window2, text="").pack()
	Label(window2, text="Password*").pack()
	password_entry1 = Entry(window2, textvariable=password_verify)
	password_entry1.pack()
	Label(window2, text="").pack()
	Button(window2, text="Login", width = 10, height =1, command=login_verify).pack()



#creating the main screen
def main_window():
	global window
	window = Tk()
	window.geometry("300x250")
	window.title("Data")
	Label(text="Data", bg="white", width="300", height="2").pack()
	Label(text="").pack()
	Button(text="Login", width="30", height="2", command=login).pack()
	Label(text="").pack()
	Button(text="Register", width="30", height="2", command=register).pack()

	window.mainloop()

main_window()