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
                self.browse.grid(row=1, column=3)

                #the button to make it happen!
                self.button = Button(self, text = "Start", command = self.code)
                self.button.grid(row=2, column=1)

                #close button
                self.button = Button(self, text = "Close", command = root.destroy)
                self.button.grid(row=2, column=3)



        def browse(self):
                global fname
                #This returns a list and each element is a filename we have selected
                fname = askopenfilenames(filetypes=(("All files", "*.*"), ("Image files", "*.jpg;*.jpeg;*.png") ))
                
                if fname:
                        try:
                                # Terminal output
                                print("""here it comes: self.files["template"].set(%s)""" % fname)
                        except:                     # <- naked except is a bad idea
                                showerror("Open Source File", "Failed to read file\n'%s'" % fname)
                        return fname

        def code(self):
                global fname
                """the actual code being executed"""
                #start the actual image resizing
                from PIL import Image

                i = 0
                j = len(fname)

                while i<=j:

                        image_file = fname[i]

                        #We convert the element into a string to be able to manipulate it
                        image_file = str(image_file)

                        i+=1
                        
                        #We open the image with the path specified
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
                        
                        #We strip the extention from the filename
                        image_file = image_file.replace(".jpg","")
                        
                        #We add the suffix
                        resized_image_file = image_file + "_thumb.jpg"
                        resized_image.save(resized_image_file)


root = Tk()
root.title("Image resizer CMProperties")
root.geometry("350x200")

app = Application(root)

root.mainloop()
