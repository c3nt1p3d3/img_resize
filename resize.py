from tkinter import *
from tkinter.filedialog import askopenfilenames
from tkinter.messagebox import showerror
import sys
import string
import re

class Application(Frame):
	"""GUI for the image resize"""

	def __init__(self, master):
		"""initialize the frame"""
		Frame.__init__(self,master)
		self.grid()
		self.create_widgets()

	def create_widgets(self):
		"""Create the various widgets"""
		#the instruction telling you what to do
		self.instruction = Label(self, text = "Files")
		self. instruction.grid(row=1, column=0, columnspan=2, sticky=W)

		#the text entry field with browse for the image files
		self.files = Entry(self)
		self.files.grid(row=1, column=2, sticky=W)

		#browse button
		self.browse = Button(self, text = "Browse...", command = self.browse)
		self.browse.grid(row=1, column=4)

		#the button to make it happen!
		self.button = Button(self, text = "Start", command = self.code)
		self.button.grid(row=3, column=1)

		#close button
		#self.button = Button(self, text = "Close", command = self.close)
		#self.button.grid(row=3, column=3)



	def browse(self):
		global fname
		fname = askopenfilenames(filetypes=(("All files", "*.*"), ("Image files", "*.jpg;*.jpeg;*.png") ))
		if fname:
			try:
				print("""here it comes: self.files["template"].set(%s)""" % fname)
			except:                     # <- naked except is a bad idea
				showerror("Open Source File", "Failed to read file\n'%s'" % fname)
			return fname

	def code(self):
		global fname
		"""the actual code being executed"""
		#start the actual image resizing
		from PIL import Image

		fname_list = fname.split(',')

		i = 0
		j = len(fname_list)

		while i<=j:

			image_file = fname_list[i]
			# image_file = '/home/belf/Documents/IT/Programming/Python/somepic.jpg'

			image_file = image_file.lstrip('{')

			image_file = image_file.rstrip('}')

			i+=1
		
			img = Image.open(image_file)

			# get the image's width and height in pixels
			width, height = img.size

			# resize the image using the largest side as dimension
			factor = 0.3

			new_width = int(width*factor)

			new_height = int(height*factor)

			resized_image = img.resize((new_width, new_height), Image.ANTIALIAS)

			# save the resized image to a file
			# and view it with your favorite image viewer
			# image_file = re.sub('*.jpg', '', image_file)
			image_file = image_file.replace(".jpg","")
			resized_image_file = image_file + "_thumb.jpg"
			resized_image.save(resized_image_file)


root = Tk()
root.title("Image resizer CMProperties")
root.geometry("250x100")

app = Application(root)

root.mainloop()
