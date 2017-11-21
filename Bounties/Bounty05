#Bounty05-Tkinter Button Maker
from tkinter import *
import webbrowser

root = Tk()
frame = Frame(root, width=400, height=200)
theLabel = Label(root, text='main frame window')
theLabel.pack()
frame.pack()

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

#def printit():
#    nameit= input("what is your name?")
#    print ("hello",nameit)
#    return nameit


button1 = Button(topFrame, text="Button 001", fg='red', command=webbrowser.open('http://www.github.com'))
button2 = Button(topFrame, text="Button 002", fg='yellow')
button3 = Button(topFrame, text="Button 003", fg='green')
button4 = Button(topFrame, text="Button 004", fg='blue')

button1.pack(side=TOP)
button2.pack(side=BOTTOM)
button3.pack(side=LEFT)
button4.pack(side=RIGHT)

root.mainloop()
