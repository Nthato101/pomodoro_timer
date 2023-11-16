from tkinter import *
import math



# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
time = 0
mark = ""

# ---------------------------- TIMER RESET ------------------------------- #

def reset_func():

    global reps, time, mark
    window.after_cancel(str(time))
    tomato.itemconfig(tomato_timer, text="00:00")
    timer.config(text="Timer")
    tick.config(text="")
    mark = ""
    reps = 1

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():

    global reps
    global time

    work_seconds = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60

    if reps > 9:
        reset_func()
        return None
    elif reps % 8 == 0:
        timer.config(text="Long Break", fg=RED)
        time = long_break_secs
        reps += 1
    elif reps <= 1 or (reps % 2) != 0:
        timer.config(text=" Working ", fg=PINK)
        time = work_seconds
        reps += 1
    elif reps % 2 == 0:
        timer.config(text="Short Break", fg=RED)
        time = short_break_secs
        reps += 1
    count_down(time)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global time, mark
    count_minute = math.floor(count/60)
    count_second = count % 60
    if count_minute < 10:
        count_minute = f"0{count_minute}"
    if count_second < 10:
        count_second = f"0{count_second}"
    tomato.itemconfig(tomato_timer, text=f"{count_minute}:{count_second}")

    if count > 0:
        time = window.after(1000, count_down, count - 1)
    else:
        start_timer()

        if reps >= 2 and (reps % 2) != 0:
            mark += "✔"
            tick.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro APP")
window.config(padx=100, pady=50, bg=YELLOW)


tomato = Canvas()
tomato.config(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
tomato.create_image(100, 110, image=image)
tomato_timer = tomato.create_text(104, 130, text="00:00", fill="White", font=(FONT_NAME, 35, "bold"))
tomato.grid(row=1, column=1)


# Timer Label

timer = Label(text="Timer", fg=RED, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
timer.grid(row=0, column=1)

# Start Button

start = Button(text="Start", bg=YELLOW, fg=RED, font=(FONT_NAME, 15, "bold"), highlightthickness=0, command=start_timer)
start.grid(row=2, column=0)

# Reset Button

reset = Button(text="Reset", bg=YELLOW, fg=RED, font=(FONT_NAME, 15, "bold"), highlightthickness=0, command=reset_func)
reset.grid(row=2, column=2)

# tick

tick = Label()
tick.grid(row=3, column=1)


window.mainloop()
