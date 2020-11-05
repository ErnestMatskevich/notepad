import tkinter
from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter.messagebox import showerror
from tkinter import messagebox

FILE_NAME = tkinter.NONE

#comment
def new_file():
	global FILE_NAME
	FILE_NAME = "Untitled"
	text.delete('1.0', tkinter.END)


def save_file():
	data = text.get('1.0', tkinter.END)
	out = open(FILE_NAME, 'w')
	out.write(data)
	out.close()


def save_as():
	out = asksaveasfile(mode='w', defaultextension='txt')
	data = text.get('1.0', tkinter.END)
	try:
		out.write(data.rstrip())
	except Exception:
		showerror(title="Error", message="Saving file error")


def open_file():
	global FILE_NAME
	inp = askopenfile(mode="r")
	if inp is None:
		return
	FILE_NAME = inp.name
	data = inp.read()
	text.delete('1.0', tkinter.END)
	text.insert('1.0', data)


def info():
	messagebox.showinfo("Information", "Notepad by Ernest Matskevich ")


def replace():
	def getting():
		g_old_word = old_word.get()
		g_new_word = new_word.get()

		data = text.get('1.0', tkinter.END)
		data = data.replace(g_old_word, g_new_word)

		text.delete('1.0', tkinter.END)
		text.insert('1.0', data)
		support.destroy()

	support = Toplevel()
	support.title("Replace")
	support.resizable(False, False)
	Label(support, text="Old word").grid(row=0, column=0)
	Label(support, text="New word").grid(row=1, column=0)

	old_word = Entry(support, width=30)
	old_word.grid(row=0, column=1, sticky=W)

	new_word = Entry(support, width=30)
	new_word.grid(row=1, column=1, sticky=W)

	Button(support, text="Replace", command=getting).grid(row=2, columnspan=4)

	support.geometry('300x70')
	support.mainloop()


root = Tk()
root.title("Simple Notepad")

root.minsize(width=500, height=500)
root.maxsize(width=500, height=500)

text = tkinter.Text(root, width=400, height=400, wrap="word")

scrollb = Scrollbar(root, orient=VERTICAL, command=text.yview)
scrollb.pack(side="right", fill="y")

text.configure(yscrollcommand=scrollb.set)

text.pack()

menuBar = tkinter.Menu(root)
fileMenu = tkinter.Menu(menuBar)
instrumentsMenu = tkinter.Menu(menuBar)

fileMenu.add_command(label="New", command=new_file)
fileMenu.add_command(label="Open", command=open_file)
fileMenu.add_command(label="Save", command=save_file)
fileMenu.add_command(label="Save as", command=save_as)

instrumentsMenu.add_command(label="Replace", command=replace)

menuBar.add_cascade(label="File", menu=fileMenu)
menuBar.add_cascade(label="Insruments", menu=instrumentsMenu)
menuBar.add_cascade(label="Info", command=info)
menuBar.add_cascade(label="Exit", command=root.quit)


root.config(menu=menuBar)

root.mainloop()