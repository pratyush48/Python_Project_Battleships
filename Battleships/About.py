from Tkinter import *
windowA = Tk()
windowA.title("About")
logo = PhotoImage(file="SeaStar.png")

about = "The BATTLESHIPS game is created by:\n\nSRIHARI VEMURU\n\nPRATYUSH NANDI\n\nRAHUL MURALI SHANKAR\n\n\nENJOY BATTLING!!!"

w = Label(windowA,compound = CENTER,text=about,image=logo, fg = 'red')
w.pack(side="right")
windowA.mainloop()
