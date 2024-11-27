import tkinter as tk
import datetime
import PIL
import os

import PIL.Image
import PIL.ImageTk

# def welcome_text():
    # tk.label.config()

# print(os.listdir("themes"))

def welcome_screen():
    welcome = tk.Tk()
    welcome.geometry("300x200")
    welcome.title("Welcome!")
    welcome_message = tk.Label(welcome, text="VTuber Schedule Builder",
                                      font=("Arial", 18))
    welcome_message.pack()

    themes = os.listdir("themes")
    clicked = tk.StringVar(welcome)
    clicked.set("Choose a Theme")
    choose = tk.OptionMenu(welcome, clicked, *themes)
    choose.pack()
    # choose.config(text=clicked.get())

    def launch():
        theme = clicked.get()
        welcome.destroy()
        schedule_screen(theme)
        return theme

    start = tk.Button(welcome, text="Start", command=launch)
    start.pack()
    
    welcome.mainloop()

def schedule_screen(theme):
    schedule = tk.Tk()
    schedule.geometry("1920x1080")
    schedule.title("VTuber Schedule Builder")
    schedule.configure(bg="black")
    # print(theme)
    with PIL.Image.open(f'themes/{theme}/{theme} base.png') as base_open:
        base_img = PIL.ImageTk.PhotoImage(base_open)
    base = tk.Label(schedule, image=base_img)
    base.pack()

    schedule.mainloop()

def main():
    

    welcome_screen()

    

if __name__ == "__main__":
    main()