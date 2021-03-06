from tkinter import *
from tkinter.filedialog import askopenfilenames
from tkinter.filedialog import askopenfilename
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
        self.button = Button(self, text = "Start", command = self.resize)
        self.button.grid(row=2, column=1)

        #close button
        self.button = Button(self, text = "Close", command = root.destroy)
        self.button.grid(row=6, column=2)

        #Label to tell you this is the alpha you are setting
        self.label = Label(self, text = "Watermark Alpha (0-255)")
        self.label.grid(row=3, column=1, sticky=W)

        #the text entry field with browse for the image files
        self.alpha = Entry(self)
        self.alpha.grid(row=3, column=2, sticky=W)
        self.alpha.insert(0,"155")

        #browse button
        self.browse = Button(self, text = "Browse...", command = self.browse_watermark)
        self.browse.grid(row=3, column=3)

        #images to watermark filedialog
        self.instruction = Label(self, text = "Images to watermark")
        self. instruction.grid(row=4, column=0, columnspan=2, sticky=W)

        #browse button
        self.browse = Button(self, text = "Browse...", command = self.browse_images_watermark)
        self.browse.grid(row=4, column=3)

        #the text entry field with browse for the image files
        self.files = Entry(self)
        self.files.grid(row=4, column=2, sticky=W)

        #the button to make it happen!
        self.button = Button(self, text = "Watermark!", command = self.watermark)
        self.button.grid(row=5, column=1)


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

    def resize(self):
        global fname
        """the actual code being executed"""
        #start the actual image resizing
        from PIL import Image

        i = 0
        j = len(fname)

        while i<j:

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
            resized_image_file = image_file.replace(".jpg","_thumb.jpg")

            resized_image.save(resized_image_file)

    def browse_watermark(self):
        global watermark

        #This returns a list and each element is a filename we have selected
        watermark = askopenfilename(filetypes=(("All files", "*.*"), ("Image files", "*.jpg;*.jpeg;*.png") ))

        if watermark:
            try:
                # Terminal output
                print("""here it comes: self.files["template"].set(%s)""" % watermark)
            except:                     # <- naked except is a bad idea
                    showerror("Open Source File", "Failed to read file\n'%s'" % watermark)
            return watermark

    def browse_images_watermark(self):
        global fname_watermark
        #This returns a list and each element is a filename we have selected
        fname_watermark = askopenfilenames(filetypes=(("All files", "*.*"), ("Image files", "*.jpg;*.jpeg;*.png") ))
        
        if fname_watermark:
            try:
                # Terminal output
                print("""here it comes: self.files["template"].set(%s)""" % fname_watermark)
            except:                     # <- naked except is a bad idea
                    showerror("Open Source File", "Failed to read file\n'%s'" % fname_watermark)
            return fname_watermark

    def watermark(self):
        global fname_watermark
        global watermark

        from PIL import Image

        i=0

        j=len(fname_watermark)

        while i<j:
            image_file = fname_watermark[i]

            image_file = str(image_file)

            i+=1

            alpha = int(self.alpha.get())

            img = Image.open(image_file)

            #we open the watermark image
            wmark = Image.open(watermark)

            wmark.putalpha(alpha)

            #we get the width and heigt of the image
            img_width, img_height = img.size

            pos_width = int(img_width/2)

            pos_height = int(img_height/2)

            #here we set the position to where we want our watermark to appear
            wmark_x_pos = pos_width-wmark.size[0]

            wmark_y_pos = pos_height-wmark.size[1]

            #code to combine both images 
            img.paste(wmark,(wmark_x_pos,wmark_y_pos),wmark)

            #img.show()

            watermarked_image_path = image_file.replace(".jpg","_watermarked.jpg")

            img.save(watermarked_image_path)






root = Tk()
root.title("Image resizer CMProperties")
root.geometry("425x300")

app = Application(root)

root.mainloop()
