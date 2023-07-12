import tkinter
from tkinter import *
import speech_recognition as sr
from datetime import datetime
r=sr.Recognizer()
tk=Tk()



def get_voice():
    with sr.Microphone() as src:
        audio=r.listen(src)
        texts=r.recognize_google(audio)
        texts=(texts.lower())
        txt.config(text=texts)

def show_data_time():
    dates=datetime.now()
    show_datee.config(text=dates)
    
tk.title("convertor speech to text")
tk.geometry("500x600")
tk.resizable(width=False, height=False)
talk=Label(tk, text="Please Talk", bg="orange", fg="black", font=14, width=60)
talk.place(x=0, y=1)
start=Button(tk, text="Start", bg="red", bd=2, padx=14, pady=14, command=get_voice)
start.place(x=200, y=40)
txt=Label(tk,text="")
txt.place(x=200, y=120)
show_date=Button(tk, text="show_data", command=show_data_time)
show_date.place(x=250, y=120)
show_datee=Label(tk,text="")
show_datee.place(x=100, y=120)















tk.mainloop()
