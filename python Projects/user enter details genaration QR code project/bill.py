from tkinter import *
import qrcode



def prints():
	try:
		qr = qrcode.QRCode(
				version=1,
				box_size=15,
				)
		data = e1.get(),e2.get(),e3.get(),e4.get()
		qr.add_data(data)
		qr.make(fit=True)
		img = qr.make_image(fill="black",black_color='white')
		img.save('billcode.png')

	except Exception as msg:
		print("Exception as on :", msg)
	return



window = Tk()
l1 = Label(window,text="firstname",font="Times25")
l2 = Label(window,text="Last name",font="Times25")
l3 = Label(window,text="Address",font= "Times25")
l4 = Label(window,text="Pin code",font="Times25")


e1 = Entry(window,font="Times25")
e2 = Entry(window,font="Times25")
e3 = Entry(window,font="Times25")
e4 = Entry(window,font="Times25")


b1 = Button(window,text="Genrate_code", font="Times25", command=prints)
b2 = Button(window,text="Cancel", font="Times25",command=quit)




l1.grid(row=0,column=0)
e1.grid(row=0,column=1)

l2.grid(row=1, column=0)
e2.grid(row=1, column=1)

l3.grid(row=2,column=0)
e3.grid(row=2, column=1)

l4.grid(row=3,column=0)
e4.grid(row=3,column=1)

b1.grid(row=4,column=0)
b2.grid(row=4,column=1)



window.mainloop()
