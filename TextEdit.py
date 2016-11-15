import Tkinter
from Tkinter import *
from ScrolledText import *
import ttk
import tkFileDialog
import tkMessageBox

root = Tkinter.Tk(className="TextNext")
textPad = ScrolledText(root, width=100, height=80,undo=True)

def openFile(event):
		file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Select a file')
		if file != None:
			contents = file.read()
			textPad.insert('1.0',contents)
			file.close()

def saveFile(event):
	file = tkFileDialog.asksaveasfile(mode = 'w' , defaultextension = ".txt")
	if file !=  None:
		data = str(textPad.get('1.0', END))
		file.write(data)
		file.close()

def exitPls(event):
	if tkMessageBox.askokcancel("Quit", "Do you really want to quit?"):
		root.destroy()

def openFileMenu():
		file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Select a file')
		if file != None:
			contents = file.read()
			textPad.insert('1.0',contents)
			file.close()

def saveFileMenu():
	file = tkFileDialog.asksaveasfile(mode = 'w' , defaultextension = ".txt")
	if file !=  None:
		data = str(textPad.get('1.0', END))
		file.write(data)
		file.close()

def exitPlsMenu():
	if tkMessageBox.askokcancel("Quit", "Do you really want to quit?"):
		root.destroy()


def aboutUs():
	label = tkMessageBox.showinfo("About", "TextNext-OS Mini-Project\nDeveloped By Rajat and Rushabh")

def sample():
	label=tkMessageBox.showinfo("Edit","This feature will be implemented later")

def selectAll(event):
	textPad.tag_add(SEL,'1.0',END)
	return 'break'

def changeTheme(event):
		ttk.Style().theme_use('alt')
		label=tkMessageBox.showinfo("","Done")

def copy(self):
	self.clipboard_clear()
	text=self.get(SEL_FIRST,SEL_LAST)
	#text = self.get("sel.first", "sel.last")
	self.clipboard_append(text)
	
def cut(self):
	self.copy()
	self.delete(SEL_FIRST, SEL_LAST)

def paste(self):
	text = self.selection_get(selection='CLIPBOARD')
	self.insert('insert', text)

def undo(self):
    self.edit_undo()
	
menu = Menu(root)
root.config(menu=menu)

#File menu created
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Open", command=openFileMenu,accelerator='Ctrl+O')
filemenu.add_command(label="Save", command=saveFileMenu,accelerator='Ctrl+S')
filemenu.add_command(label="Exit", command=exitPlsMenu,accelerator='Ctrl+Q')

#Binding shortcut keys
root.bind_all('<Control-Key-o>',openFile)
root.bind_all('<Control-Key-s>',saveFile)
root.bind_all('<Control-Key-q>',exitPls)
root.bind_all('<Control-Key-a>',selectAll)

#Help menu created
helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=aboutUs)

#Edit menu created
editmenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Dark Theme",command=changeTheme,accelerator='Ctrl+D')
editmenu.add_command(label="Undo",command=undo,accelerator='Ctrl+Z')
editmenu.add_command(label="Cut",command=cut,accelerator='Ctrl+X')
editmenu.add_command(label="Copy",command=copy,accelerator='Ctrl+C')
editmenu.add_command(label="Paste",command=paste,accelerator='Ctrl+V')
editmenu.add_command(label="Select All",command=selectAll,accelerator='Ctrl+A')

#root.bind_all('<Control-Key-d>',changeTheme)

textPad.pack()
root.mainloop()
