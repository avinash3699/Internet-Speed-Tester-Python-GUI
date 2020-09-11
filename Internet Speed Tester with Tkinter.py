# Program to find Internet Speed with GUI using 'speedtest' package

# importing 'tkinter' module for GUI
# importing 'speedtest' module for calculating Internet Speed
from tkinter import *
from speedtest import Speedtest
from tkinter import messagebox

# creating and setting the title of the GUI window
window = Tk()
window.title("Internet Speed Tester")

# setting the dimensions of the GUI window
window.geometry("450x225")

# restricting the user to change the dimension of the GUI window
window.resizable(False,False)

# creating widgets for the GUI window
headline_text = Label(window, text= "Internet Speed Tester", font = ("Arial Bold",11,'underline'))
upload = Button(window ,text = "Get Upload Speed", width=18, command = lambda : Upload())
download = Button(window, text = "Get Download Speed", width=18, command = lambda : Download())
ping = Button(window, text = "Get Ping Speed", width = 18, command = lambda: Ping())
empty = Label(window, text="\n\n\n\n\n\n", bd=0)
note_text = Label(window, text = "Note:", font = ("Arial Bold",9))
instructions1 = Label(window, text = "1. Please check 'Ping Speed' after checking 'Download' and 'Upload' Speed.")
instructions2 = Label(window, text = "2. This process may take 10-12 seconds, So be Patient..!")

# checking whether the user's internet connection is turned on,
# if not displaying a error message and disabling the Buttons using 'state' property
try:
	st = Speedtest()
except:
	messagebox.showerror("Error", "Please Connect to Internet")
	download['state'] = DISABLED
	upload['state'] = DISABLED
	ping['state'] = DISABLED

# function that executes when user want the 'Upload' speed
def Upload():
    label = Label(window, text = "Current Upload Speed is %s mbps"%(str(st.upload()/1000000))).grid(row=4,column=1)

# function that executes when user want the 'Download' speed
def Download():
    label = Label(window, text = "Current Download Speed is %s mbps"%(str(st.download()/1000000))).grid(row=3,column=1)

# function that executes when user want the 'Ping' speed
def Ping():
	servernames = []
	st.get_servers(servernames)
	label = Label(window, text = "Current Ping Speed is %s bps"%(str(st.results.ping))).grid(row=5,column=1)


# displaying the widgets onto the tkinter window
headline_text.place(x=135,y=5)
empty.grid(row=1, column=0)
note_text.place(x=10,y=30)
instructions1.place(x=10, y=55)
instructions2.place(x=10,y=80)
download.grid(row=3,column=0, padx=10,pady=5)
upload.grid(row=4,column=0, padx=10,pady=5)
ping.grid(row=5,column=0, padx=10,pady=5)

# to start the GUI window, 'mainloop' method is used
window.mainloop()