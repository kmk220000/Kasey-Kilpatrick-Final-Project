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
    
    add_art(canvas)
    exit_button(schedule)

    schedule.mainloop()
    
def add_art(canvas: tk.Canvas):
    # Button to add art behind canvas to the right side of the screen
    art = tk.Button(canvas, text="Add Art", command=lambda: choose_art(canvas))
    art.place(x=1800, y=500)

def choose_art(canvas):
    # Button to choose and place the art on the right
    upload_art = tkinter.filedialog.askopenfilename()
    print(upload_art)
    with PIL.Image.open(upload_art) as uploaded_art:
        canvas.art_img = PIL.ImageTk.PhotoImage(uploaded_art)
        canvas.uploaded_art = uploaded_art
        art_width, art_height = uploaded_art.size
        art_ratio = float(art_width) / art_height

    canvas.create_image(1920,0, anchor=tk.NE, image=canvas.art_img, tag="Art")
    canvas.tag_lower("Art")
    fit_art(canvas, art_ratio, art_height)

def fit_art(canvas: tk.Canvas, art_ratio, art_height):
    # sliders to fit art to space
    rs_var = tk.IntVar()
    x_var = tk.IntVar()
    y_var = tk.IntVar()
    rs_window = tk.Tk()
    rs_window.geometry("300x500")
    def art_resizer():
        rs_newheight = art_height + (5 * rs_var.get())
        rs_newwidth = rs_newheight * art_ratio
        print(rs_newwidth, rs_newheight)
        rs_uploaded_art = canvas.uploaded_art.resize((int(rs_newwidth), rs_newheight))
        with PIL.Image.open(rs_uploaded_art):
            canvas.rs_art_img = PIL.ImageTk.PhotoImage(rs_uploaded_art)

            canvas.create_image(1920,0, anchor=tk.NE, image=canvas.rs_art_img, tag="Art")
        return rs_uploaded_art
        # canvas.tag_lower("Art")
    def art_mover(rs_uploaded_art):
        x_og = 1920
        y_og = 0
        x_new = x_og - x_var.get()
        y_new = y_og + y_var.get()
        with PIL.Image.open(rs_uploaded_art):
            canvas.rs_art_img = PIL.ImageTk.PhotoImage(rs_uploaded_art)

            canvas.create_image(x_new,y_new, anchor=tk.NE, image=canvas.rs_art_img, tag="Art")
    def art_done():
        rs_window.destroy()
    rs_scale = tk.Scale(rs_window, variable=rs_var, from_=-500, to=500,
                            orient="horizontal")
    x_scale = tk.Scale(rs_window, variable=x_var, from_=0, to=1000, orient="horizontal")
    y_scale = tk.Scale(rs_window, variable=y_var, from_=0, to=1000, orient="vertical")
    rs_button = tk.Button(rs_window, text="Resize", command=art_resizer)
    xy_button = tk.Button(rs_window, text="Adjust", command=art_mover)
    artdone_button = tk.Button(rs_window, text="Done", command=art_done)
    rs_label = tk.Label(rs_window, text="Resize/Reposition Art")
    rs_label.pack()
    rs_scale.pack()
    rs_button.pack()
    x_scale.pack()
    y_scale.pack()
    xy_button.pack()
    artdone_button.pack()

        

def exit_button(schedule: tk.Tk):
    # TEMP EXIT BUTTON - ADD SAVE BUTTON
    exit = tk.Button(schedule, text="Exit", command=schedule.destroy)
    exit.place(x=1880, y=1000)


def main():
    

    welcome_screen()

    

if __name__ == "__main__":
    main()