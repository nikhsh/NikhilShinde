import requests
import json
from tkinter import *
from tkinter.messagebox import showinfo, showerror




def sendsms(number, message):
	url = "https://www.fast2sms.com/dev/bulk"
	params = {
		'authorization' : 'FLNT34Y1DWDHXOWE5087NE0LDJ9GZKKQ',
		'sender_id' : 'SMSIND',
		'message' : message,
		'language' : 'english',
		'route' : 'p',
		'numbers' :number
		}

	response = requests.get(url, params=params)
	dic = response.json()
	print(dic)
	return dic.get('return')


def button():
	num = textNumber.get()
	msg = textMsg.get("1.0",END)
	r = sendsms(num,msg)

	if r:
		showinfo("send Sucessfully")
	else:
		showerror("Error", "something is wrong")



root = Tk()
root.title("W@y T0 $end")
root.geometry("350x300")
font = ("vardana", 16, "bold")
textNumber = Entry(root, font=font)
textNumber.pack(fill=X, pady=20)
textMsg = Text(root)
textMsg.pack(fill=X)

send = Button(root, text="Send SMS",font="Times 15", command=button)
send.pack()


root.mainloop()

