from tkinter import *
from tkinter import messagebox
class Application(Frame):
	def __init__(self,master):
		Frame.__init__(self,master)
		self.grid()
		self.create_widgets()

	def create_widgets(self):
		Label(self,text="Movie Selection").grid(row=0,column=1,columnspan=2,sticky=W)
		self.language = StringVar()
		Label(self,text="Choose a Language").grid(row=1,column=0,columnspan=2,sticky=W)
		Radiobutton(self,value="English",variable=self.language,command = self.movies,text="English").grid(row=2,column=0,sticky=W)
		Radiobutton(self,value="Kannada",variable=self.language,command = self.movies,text="Kannada").grid(row=2,column=1,sticky=W)
		Radiobutton(self,value="Hindi",variable=self.language,command = self.movies,text="Hindi").grid(row=2,column=2,sticky=W)
		self.movieselect1 = BooleanVar()
		self.movieselect2 = BooleanVar()
		self.movieselect3 = BooleanVar()
		Label(self,text="Choose Movies:").grid(row=3,column=0,columnspan=2,sticky=W)
		self.chk1 = Checkbutton(self,variable=self.movieselect1,text=" ")
		self.chk1.grid(row=4,column=0,sticky=W)
		self.chk2 = Checkbutton(self,variable=self.movieselect2,text=" ")
		self.chk2.grid(row=4,column=1,sticky=W)
		self.chk3 = Checkbutton(self,variable=self.movieselect3,text=" ")
		self.chk3.grid(row=4,column=2,sticky=W)
		Label(self,text="Select the Number of Tickets:").grid(row=5,column=0,columnspan=2,sticky=W)
		self.tickets = StringVar()
		choices=['1','2','3','4','5']
		self.tickets.set('1')
		self.popupMenu = OptionMenu(self, self.tickets, *choices)
		self.popupMenu.grid(row = 6, column =0,sticky=W)
		self.btn = Button(self,text="Submit",command=self.check)
		self.btn.grid(row=10,column=1,sticky=W)


	def check(self):
		if self.language.get() == "":
			messagebox.showerror("Error","Please choose a Language")
		elif not self.movieselect1.get() and not self.movieselect2.get() and not self.movieselect3.get():
			messagebox.showerror("Error","Please choose a Movie")
		else:
			msg = "  "
			if(self.movieselect1.get()):
				msg = msg+"\n  "+self.chk1['text']
			if(self.movieselect2.get()):
				msg = msg+"\n  "+self.chk2['text']
			if(self.movieselect3.get()):
				msg = msg+"\n  "+self.chk3['text']
			messagebox.showinfo("Booking Successful","Movies selected are "+msg)
	
	def movies(self):
		lang = self.language.get()
		if(lang == "Kannada"):
			self.chk1['text'] = "KGF"
			self.chk2['text'] = "Kirik party"
			self.chk3['text'] = "Mugulnage"
		elif(lang == "English"):
			self.chk1['text'] = "Avengers"
			self.chk2['text'] = "Spider Man"
			self.chk3['text'] = "Joker"
		elif(lang == "Hindi"):
			self.chk1['text'] = "War"
			self.chk2['text'] = "Zefrom tkinter import *
from tkinter import messagebox
class Application(Frame):
	def __init__(self,master):
		Frame.__init__(self,master)
		self.grid()
		self.create_widgets()

	def create_widgets(self):
		Label(self,text="Movie Selection").grid(row=0,column=1,columnspan=2,sticky=W)
		self.language = StringVar()
		Label(self,text="Choose a Language").grid(row=1,column=0,columnspan=2,sticky=W)
		Radiobutton(self,value="English",variable=self.language,command = self.movies,text="English").grid(row=2,column=0,sticky=W)
		Radiobutton(self,value="Kannada",variable=self.language,command = self.movies,text="Kannada").grid(row=2,column=1,sticky=W)
		Radiobutton(self,value="Hindi",variable=self.language,command = self.movies,text="Hindi").grid(row=2,column=2,sticky=W)
		self.movieselect1 = BooleanVar()
		self.movieselect2 = BooleanVar()
		self.movieselect3 = BooleanVar()
		Label(self,text="Choose Movies:").grid(row=3,column=0,columnspan=2,sticky=W)
		self.chk1 = Checkbutton(self,variable=self.movieselect1,text=" ")
		self.chk1.grid(row=4,column=0,sticky=W)
		self.chk2 = Checkbutton(self,variable=self.movieselect2,text=" ")
		self.chk2.grid(row=4,column=1,sticky=W)
		self.chk3 = Checkbutton(self,variable=self.movieselect3,text=" ")
		self.chk3.grid(row=4,column=2,sticky=W)
		Label(self,text="Select the Number of Tickets:").grid(row=5,column=0,columnspan=2,sticky=W)
		self.tickets = StringVar()
		choices=['1','2','3','4','5']
		self.tickets.set('1')
		self.popupMenu = OptionMenu(self, self.tickets, *choices)
		self.popupMenu.grid(row = 6, column =0,sticky=W)
		self.btn = Button(self,text="Submit",command=self.check)
		self.btn.grid(row=10,column=1,sticky=W)


	def check(self):
		if self.language.get() == "":
			messagebox.showerror("Error","Please choose a Language")
		elif not self.movieselect1.get() and not self.movieselect2.get() and not self.movieselect3.get():
			messagebox.showerror("Error","Please choose a Movie")
		else:
			msg = "  "
			if(self.movieselect1.get()):
				msg = msg+"\n  "+self.chk1['text']
			if(self.movieselect2.get()):
				msg = msg+"\n  "+self.chk2['text']
			if(self.movieselect3.get()):
				msg = msg+"\n  "+self.chk3['text']
			messagebox.showinfo("Booking Successful","Movies selected are "+msg)
	
	def movies(self):
		lang = self.language.get()
		if(lang == "Kannada"):
			self.chk1['text'] = "KGF"
			self.chk2['text'] = "Kirik party"
			self.chk3['text'] = "Mugulnage"
		elif(lang == "English"):
			self.chk1['text'] = "Avengers"
			self.chk2['text'] = "Spider Man"
			self.chk3['text'] = "Joker"
		elif(lang == "Hindi"):
			self.chk1['text'] = "War"
			self.chk2['text'] = "Zero"
			self.chk3['text'] = "Bala"
	

root = Tk()
root.title("Movie ticket booking")
root.geometry("300x300")
app =Application(root)
root.mainloop()		ro"
			self.chk3['text'] = "Bala"
	

root = Tk()
root.title("Movie ticket booking")
root.geometry("300x300")
app =Application(root)
root.mainloop()		
