from tkinter import *

#main

#text stuffs

text_file = (open("output.txt", "a"))
emailFile = open("emails.txt", "a")
#opens text file


window = Tk()
window.title("Computing club recruitment")


#button callback function

def callback():
    nameInputted = name.get()
    emailInputted = email.get()
    qrtInputted = qrt.get()
    print(nameInputted)
    print(emailInputted)
    print(qrtInputted)
    text_file.write(nameInputted +"\n")
    text_file.write(emailInputted +"\n")
    text_file.write(qrtInputted + "\n")
    emailFile.write(emailInputted +"\n")
    name.delete(0, END)
    email.delete(0, END)
    qrt.delete(0,END)
#photo

photo1= PhotoImage(file = "FcHacks.png")
Label(window, image = photo1, bg = "white").grid(row = 0, column = 0, sticky = W )

#create label
Label(window, text= "Join Computing Club!", font = "none 12 bold") .grid(row = 1, column = 0, sticky = W)
# name label

nameLabel = Label(window, text= "Name:", font = "none 12 bold").grid(row = 2,column = 0, sticky = W)


#Name Text input
name = Entry(window, width = 20, bg = "white")

name.grid(row = 3, column = 0, sticky = W)

#end name text input

emailLabel = Label(window, text = "E-Mail: ", font = "none 12 bold").grid(row = 4, column = 0, sticky = W)

#email text input

email = Entry(window, width = 20, bg = "white")
email.grid(row = 5, column = 0, sticky = W)

#Qrt Label
qrtLabel = Label(window, text = "Qrt:", font = "none 12 bold").grid(row = 6, column = 0, sticky = W)

#Qrt text input

qrt = Entry(window, width = 20, bg = "white")
qrt.grid(row = 7, column = 0, sticky = W)
#Create Button
submitbutton = Button(window, text = "Submit", bg = "white", command = callback).grid(row = 8, column = 0, sticky = W)
#submitbutton.pack

# main loop
window.mainloop()
