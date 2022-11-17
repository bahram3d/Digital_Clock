from tkinter import Tk,Label

window = Tk()
window.title("Digital Clock")
window.geometry("1000x300")
window.configure(bg="steelblue")

label = Label(window, text= "Good to see you!", font= ("Arial Black", 70, "bold"), bg = "steelblue",fg="white")
label.pack(pady=100)
window.mainloop()
