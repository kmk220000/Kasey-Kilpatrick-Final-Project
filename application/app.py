import tkinter as tk
import datetime
import PIL
import os

# def welcome_text():
    # tk.label.config()

# print(os.listdir("themes"))

def welcome_screen():
    welcome = tk.Tk()
    welcome.geometry("300x200")
    welcome.title("Welcome!")
    welcome_message = tk.Label(welcome, text="Choose a Theme!",
                                      font=("Arial", 18))
    welcome_message.pack()

    themes = os.listdir("themes")
    clicked = tk.StringVar()
    clicked.set(" ")
    choose = tk.OptionMenu(welcome, clicked, themes)
    choose.pack()
    choose.config(text=clicked.get())

    def launch():
        welcome.destroy()
        schedule_screen()

    start = tk.Button(welcome, text="Start", command=launch)
    start.pack()
    
    welcome.mainloop()

def schedule_screen():
    schedule = tk.Tk()
    schedule.geometry("1920x1080")
    schedule.title("Schedule Builder")
    schedule.configure(bg="black")
    schedule.mainloop()

def main():
    

    welcome_screen()

    

if __name__ == "__main__":
    main()