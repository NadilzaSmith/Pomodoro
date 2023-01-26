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
reps = 0
timer = None
#---------------------------- TIMER RESET ------------------------------- #

def reset ():
    screen.after_cancel(timer)
    text_timer.config(text="Timer")
    check_marck.config(text="")
    canvas.itemconfig(count_timer, text ="00:00")
    global reps
    reps = 0




# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break)
        text_timer.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break)
        text_timer.config(text="Short Break", fg=PINK )
    else:
        count_down(work_sec)
        text_timer.config(text="Work",fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = math.floor(count /60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(count_timer, text= f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = screen.after(1000 , count_down, count - 1)
    else:
        start_timer()
        check = ""
        for w in range(math.floor(reps/2)):
            check += "✓"
            check_marck.config(text=check)
# ---------------------------- UI SETUP ------------------------------- #

screen = Tk()
screen.title(" Studing Timer")
screen.config(padx=100,pady=50,bg=YELLOW)


canvas = Canvas(width=200, height=224, bg= YELLOW, highlightthickness=0)
image_tomato = PhotoImage(file="tomato.png")
canvas.create_image(100,113, image=image_tomato)
count_timer = canvas.create_text(100,130, text= "00:00",fill="white",font=(FONT_NAME, 35,"bold"))
canvas.grid(column=1,row=1)



text_timer = Label(text="Timer",fg=GREEN,bg=YELLOW, font= (FONT_NAME,35,"bold"))
text_timer.grid(column=1,row=0)


botao_start = Button(text="Start",command=start_timer)
botao_start.grid(column=0, row=2)

botao_reset = Button(text="Reset",command= reset)
botao_reset.grid(column=3, row=2)

check_marck = Label(text="",fg=GREEN,bg=YELLOW)
check_marck.grid(column=1,row=4)

screen.mainloop()
