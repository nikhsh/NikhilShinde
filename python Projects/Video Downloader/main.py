from threading import Thread
from tkinter.messagebox  import *
from tkinter.filedialog import *
from pytube import *
from tkinter import *

file_size=0


def progress(strem=None,chunk=None,file_handle=None,remaining=None):
	file_downloaded = (file_size-remaining)
	per=(file_downloaded/file_size)*100
	dbtn.config(text="{00.0f}%startdownload".format(per))

def startdownload():
	global filesize


	try:
		url = urlfield.get()
		dbtn.config(text="plase waiting...")
		dbtn.config(state=DISABLED)
		path_to_save_video="askdirectory()"


		if path_to_save_video is None:
			return

		ob=YouTube(url,on_progress_callback=progress)
#		ob=YouTube(url)
		strm=ob.streams.first()
		file_size=strm.filesize

		strm.download(path_to_save_video)
		print("Done.....")

		dbtn.config(text="startdownload")
		dbtn.config(state=NORMAL)
		showinfo("Download finish","Downlad suceessfully...")
		urlfield.delete(0,END)


	except Exception as e:
		print(e)
#		print("error")


def startdownloadthread():
	thread=Thread(target=startdownload)
	thread.start()


main=Tk()
main.title("MyDownloader")


#photo = PhotoImage(file="index.ico")
#main.iconphoto("index.ico")


main.geometry("400x550")


file = PhotoImage(file="im.png") 
headingIcon = Label(main,image=file)
headingIcon.pack(side=TOP)

urlfield = Entry(main,font=("verdana",18),justify=CENTER)
urlfield.pack(side=TOP,fill=X,padx=10)

#button Downlaods

dbtn=Button(main,text="Start Download", font=("verdana",18),relief='ridge',command=startdownloadthread)
dbtn.pack(side=TOP,pady=10)




main.mainloop()


