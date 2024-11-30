import tkinter as tk
import datetime
import PIL
import os

import PIL.Image
import PIL.ImageTk
import tkinter.filedialog

# def welcome_text():
    # tk.label.config()

# print(os.listdir("themes"))

def welcome_screen():
    # Screen to choose theme and start the schedule builder
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
    # Main screen with background image and days coded in
    schedule = tk.Tk()
    schedule.attributes("-fullscreen", True)
    schedule.title("VTuber Schedule Builder")
    schedule.configure(bg="black")
    # print(theme)
    canvas = tk.Canvas(schedule, width=1920, height=1080)
    canvas.pack()
    with PIL.Image.open(f'themes/{theme}/{theme} base.png') as base_open:
        base_img = PIL.ImageTk.PhotoImage(base_open)
    # base = tk.Label(schedule, image=base_img)
    # base.pack()
    canvas.create_image(0,0, anchor=tk.NW, image=base_img)
    
    x = 27
    y = 217
    on_days = []
    for on_day_loop in os.listdir(f'themes/{theme}/days/ON'):
        # print(on_day_open)
        with PIL.Image.open(f'themes/{theme}/days/ON/{on_day_loop}') as on_day_open:
            # on_day_open.show()
            on_day_img = PIL.ImageTk.PhotoImage(on_day_open)
        canvas.create_image(x,y, anchor=tk.NW, image=on_day_img)
        on_days.append(on_day_img)
        print(on_day_img)
        y += 112

    schedule.mainloop()
    




def main():
    

    welcome_screen()

    

if __name__ == "__main__":
    main()