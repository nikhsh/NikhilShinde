import sounddevice
from scipy.io.wavfile import write
from tkinter import *
import os

def recorder():
#	path = "/root/Music/"
	try:
		fs = 44100
		second = 10

		print("recording start......")

		record_voice = sounddevice.rec(int(second * fs),samplerate=fs,channels=2)
		sounddevice.wait()
		write("outss.wav",fs,record_voice)
	#	os.mkdir(path)
	#	print("path created")
	except Exception as e:
		print(e)



main=Tk()
main.title("audio recorder")
main.geometry("350x300")


button = Button(main,text="Start Recording", font=("verdana,18"),padx=14,pady=14,relief="ridge",command=recorder)
button.pack(side=TOP,pady=18)

button1 = Button(main,text="Stop", font=("verdana, 18"),padx=18,pady=18,relief="ridge",command=quit)
button1.pack(side=TOP,pady=18)
main.mainloop()
