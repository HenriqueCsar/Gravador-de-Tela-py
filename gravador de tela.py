import pyautogui, os
from tkinter import *
from tkinter import filedialog, messagebox
from time import sleep

class my_grav:
	def __init__(self):
		super().__init__()

		self.app = Tk()
		#self.app.geometry("500x500")
		self.app.title("Gravador de Tela".center(113))
		self.app.resizable(height=0, width=0)
		self.app.iconbitmap('icone.ico')
		self.app.geometry("20x20+1200+650")

		#botões 
		self.play = Button(self.app, text="Play", fg="gray", bg="Black", command=self.plays)
		self.play.grid(row=1, column=1)
		self.pause = Button(self.app, text="Pause", fg="gray", bg="Black")
		self.pause.grid(row=1, column=2)
		self.stop = Button(self.app, text="Stop", fg="gray", bg="Black")
		self.stop.grid(row=1, column=3)
		#run
		self.app.mainloop()

	def plays(self):
		for i in range(0,120):
			self.record = pyautogui.screenshot()
			self.record.save(f"record{i}.png")
		import cv2
		import numpy as np
		import glob

		img_array = []
		for filename in glob.glob('record*.png'):
			   img = cv2.imread(filename)
			   height, width, layers = img.shape
			   size = (width,height)
			   img_array.append(img)

		self.name = filedialog.asksaveasfilename(defaultextension='.avi', title='Salve sua Record', filetypes=[("Avi files", "*.avi")])
		out = cv2.VideoWriter(self.name,cv2.VideoWriter_fourcc(*'DIVX'), 1, size)
			 
		for i in range(len(img_array)):
			out.write(img_array[i])
		out.release()
		sleep(3)
		for i in glob.glob('record*.png'):
			os.remove(i)

	def stop(self):
			pass


	def pause(self):
			pass

my_grav()
