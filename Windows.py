import tkinter

window = tkinter.Tk()
window.title('переводчик')
window.geometry('600x400+300+300')
message =input('qweqwe')
input_entry = tkinter.Entry(textvariable=message)
input_entry.place(relx=.5, rely=.1, anchor="c")
window.mainloop()