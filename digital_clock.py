from tkinter import Tk,Label
from datetime import datetime

window = Tk()
window.title("Digital Clock")
window.geometry("1000x300")
window.configure(bg="steelblue")

label = Label(window, text= "Good to see you!", font= ("Arial Black", 70, "bold"), bg = "steelblue",fg="white")
label.pack(pady=100)

def clock():
    time =datetime.now().strftime("%H:%M:%S")
    label.configure(text=time)
    label.after(500, clock)
    
clock()
window.mainloop()
