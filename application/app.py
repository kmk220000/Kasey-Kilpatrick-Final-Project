import tkinter as tk
import PIL
import os
import time
import pyglet

import PIL.Image
import PIL.ImageGrab
import PIL.ImageTk
import tkinter.filedialog
from tkinter import font

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

    def launch():
        # When start button is clicked, launches schedule
        global theme
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
    canvas = tk.Canvas(schedule, width=1920, height=1080)
    canvas.pack()
    with PIL.Image.open(f'themes/{theme}/{theme} base.png') as base_open:
        base_img = PIL.ImageTk.PhotoImage(base_open)
    canvas.create_image(0,0, anchor=tk.NW, image=base_img)
    
    x = 27
    y = 217
    global on_days
    on_days = []
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", 
            "Thursday", "Friday", "Saturday"]
    index = 0
    for on_day_loop in os.listdir(f'themes/{theme}/days/ON'):
        # Loop to place each day of the week separately
        with PIL.Image.open(f'themes/{theme}/days/ON/{on_day_loop}') as on_day_open:
            on_day_img = PIL.ImageTk.PhotoImage(on_day_open)
        canvas.create_image(x,y, anchor=tk.NW, image=on_day_img, tag=days[index])
        on_days.append(on_day_img)
        index += 1
        y += 112
    
    add_art(canvas)
    add_games(canvas, theme)
    exit_button(schedule, canvas)

    schedule.mainloop()
    
def add_games(canvas: tk.Canvas, theme):
    # Button to add games to each day
    game_button = tk.Button(canvas, text="Edit Games", 
                            command=lambda: choose_games(canvas, theme, game_button))
    game_button.place(x=1250, y=200)

def no_stream(day, canvas: tk.Canvas):
    # When "No" is selected in the games window, change day to "no stream" dark ver
    day_nums = {
    "Sunday": 1,
    "Monday": 2,
    "Tuesday": 3,
    "Wednesday": 4,
    "Thursday": 5,
    "Friday": 6,
    "Saturday": 7
    }
    print(day_nums[day])
    with PIL.Image.open(f'themes/{theme}/days/OFF/{theme} {day_nums[day]} OFF.png') as ns_open:
        ns_img = PIL.ImageTk.PhotoImage(ns_open)

    if not hasattr(canvas, "image_refs"):
        canvas.image_refs = {}
    canvas.image_refs[day] = ns_img
    canvas.itemconfig(day, image=ns_img)

def choose_games(canvas: tk.Canvas, theme, game_button: tk.Button):
    # Fields to enter games and times
    # Variables and fonts needed for this function
    game_button.place_forget()
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", 
            "Thursday", "Friday", "Saturday"]
    on_offs = []
    games = []
    hours = []
    mins = []
    ampms = []
    tzs = []

    gm_window = tk.Tk()
    gm_window.geometry("600x600")
    gm_window.title("Choose Games")

    #pyglet.font.add_file(f'themes/{theme}/{theme} game font.otf')
    #pyglet.font.add_file(f'themes/{theme}/{theme} time font.ttf')
    #pyglet.font.add_file(f'themes/{theme}/{theme} other font.ttf')

    #gm_font = f"{theme} game font"
    #time_font = f"{theme} time font"
    #other_font = f"{theme} other font"

    gm_font_path = os.path.abspath(f'themes/{theme}/{theme} game font.otf')
    time_font_path = os.path.abspath(f'themes/{theme}/{theme} time font.ttf')
    print(gm_font_path, time_font_path)
    gm_font = font.Font(family=gm_font_path, size=42)
    time_font = font.Font(family=time_font_path, size=20)

    # placeholder_font1 = tkinter.font.Font(family="Arial", size=42)
    # placeholder_font2 = tkinter.font.Font(family="Arial", size=20)
    

    def write_games():
        # Displays text/options entered by user in each field for each day
        y_game = 260
        y_time = 300
        for idx, day in enumerate(days):
            if on_offs[idx].get() == "No":
                no_stream(day, canvas)
                print(on_offs[idx].get())
                continue
            game = games[idx].get()
            hour = hours[idx].get()
            minute = mins[idx].get()
            ampm = ampms[idx].get()
            timezone = tzs[idx].get()
            
            canvas.create_text(220,y_game, text=game, fill="#110D40", font=gm_font, anchor="w")
            if ampm != "AM/PM" and timezone != "Timezone":
                canvas.create_text(220,y_time, text=f"{hour}:{minute} {ampm} {timezone}", fill="#9C7130", font=time_font, anchor="w")
            y_game += 112
            y_time += 112
            print(game,hour,minute,ampm,timezone)
        gm_window.destroy()
        
    row = 0
    for idx, day in enumerate(days):
        # Generates all necessary input fields for each day of the week
        # Stream: Yes/No
        on_off_text = tk.Label(gm_window, text=f"Stream on {day}?")
        on_off_text.grid(row=row)
        on_off_entered = tk.StringVar(gm_window)
        on_off_entered.set("Yes")
        on_off_input = tk.OptionMenu(gm_window, on_off_entered, *["No"])
        on_off_input.grid(row=row, column=1)
        row+=1
        # Game Title Input
        day_text = tk.Label(gm_window, text=f"{day}'s Game")
        day_text.grid(row=row)
        gm_input = tk.Entry(gm_window)
        gm_input.grid(row=row, column=1)
        # Stream Time Input, AM/PM, Timezone
        time_text = tk.Label(gm_window, text="Time")
        time_text.grid(row=row, column=2)
        time_input = tk.Entry(gm_window, width=5)
        time_input.grid(row=row, column=3)
        time_text2 = tk.Label(gm_window, text=":")
        time_text2.grid(row=row, column=4)
        time_input2 = tk.Entry(gm_window, width=5)
        time_input2.grid(row=row, column=5)
        am_pm_entered = tk.StringVar(gm_window)
        am_pm_entered.set("AM/PM")
        am_pm = tk.OptionMenu(gm_window, am_pm_entered, 
                            *["AM", "PM"])
        am_pm.grid(row=row, column=6)
        tz_entered = tk.StringVar(gm_window)
        tz_entered.set("Timezone")
        tz = tk.OptionMenu(gm_window, tz_entered, 
                            *["EST", "UTC", "JST"])
        tz.grid(row=row, column=7)
        row+=1
        # Add to lists
        on_offs.append(on_off_entered)
        games.append(gm_input)
        hours.append(time_input)
        mins.append(time_input2)
        ampms.append(am_pm_entered)
        tzs.append(tz_entered)    

    tk.Button(gm_window, text="Add Games", command=write_games).grid()
    
def add_art(canvas: tk.Canvas):
    # Button to add art behind canvas to the right side of the screen
    art = tk.Button(canvas, text="Add Art", command=lambda: choose_art(canvas, art))
    art.place(x=1500, y=500)

def choose_art(canvas, art: tk.Button):
    # Choose and place the art on the right
    art.place_forget()
    upload_art = tkinter.filedialog.askopenfilename()
    print(upload_art)
    canvas.delete("Art")
    with PIL.Image.open(upload_art) as uploaded_art:
        canvas.art_img = PIL.ImageTk.PhotoImage(uploaded_art)
        canvas.uploaded_art = uploaded_art
        art_width, art_height = uploaded_art.size
        art_ratio = float(art_width) / art_height

    canvas.create_image(1920,0, anchor=tk.NE, image=canvas.art_img, tag="Art")
    canvas.tag_lower("Art")
    fit_art(canvas, art_ratio, art)

def fit_art(canvas: tk.Canvas, art_ratio, art):
    # sliders to fit art to space
    rs_window = tk.Toplevel()
    rs_window.geometry("300x500")
    rs_window.title("Resize & Move Art")

    og_img = canvas.uploaded_art
    og_height = og_img.height

    rs_var = tk.IntVar(value=0)
    x_var = tk.IntVar(value=0)
    y_var = tk.IntVar(value=0)

    current_img = canvas.art_img
    x_pos = 1920
    y_pos = 0

    def update_art(value):
        # Changes art in real time as the sliders are moved
        nonlocal current_img, x_pos, y_pos
        rs_factor = rs_var.get()
        x_move = x_var.get()
        y_move = y_var.get()
        rs_newheight = og_height + (5 * rs_factor)
        rs_newwidth = int(rs_newheight * art_ratio)
        rs_img = og_img.resize((rs_newwidth, rs_newheight), PIL.Image.LANCZOS)
        current_img = PIL.ImageTk.PhotoImage(rs_img)
        x_pos = 1920 - x_move
        y_pos = y_move
        canvas.itemconfig("Art", image=current_img)
        canvas.coords("Art", x_pos, y_pos)

    tk.Label(rs_window, text="Resize Art").pack()
    tk.Scale(rs_window, from_=-200, to=200, variable=rs_var, 
            orient="horizontal", command=update_art).pack()
    tk.Label(rs_window, text="Move Art Horizontally").pack()
    tk.Scale(rs_window, from_=0, to=500, variable=x_var,
            orient="horizontal", command=update_art).pack()
    tk.Label(rs_window, text="Move Art Vertically").pack()
    tk.Scale(rs_window, from_=0, to=500, variable=y_var, 
            orient="vertical", command=update_art).pack()
    tk.Button(rs_window, text="Done", command=rs_window.destroy).pack()

    rs_window.mainloop()

def exit_button(schedule: tk.Tk, canvas: tk.Canvas):
    # Saves image to files and exits
    def confirmation():
        # Asks if you are ready to save and quit
        exit.place_forget()
        exit_window = tk.Tk()
        exit_window.geometry("200x200")
        exit_window.title("Confirm")
        tk.Label(exit_window, text="Save and Quit?").pack()
        tk.Button(exit_window, text="Yes", command=lambda: save_button(exit_window)).pack()
    def save_button(exit_window: tk.Tk):
        # Saves screen as image and ends program
        x = canvas.winfo_rootx() + canvas.winfo_x()
        y = canvas.winfo_rooty() + canvas.winfo_y()
        x1 = x + canvas.winfo_width()
        y1 = y + canvas.winfo_height()
        exit_window.destroy()
        time.sleep(1)
        PIL.ImageGrab.grab().crop((x, y, x1, y1)).save("schedule.png")
        schedule.destroy()
    
    exit = tk.Button(schedule, text="Save & Quit", command=confirmation)
    exit.place(x=1800, y=1000)


def main():
    welcome_screen()

    

if __name__ == "__main__":
    main()