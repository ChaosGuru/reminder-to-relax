from tkinter import *
from PIL import Image, ImageTk
import time

def timer():
    tmr = 10 - int(time.perf_counter())

    if tmr < 0:
        app.destroy()

    label.config(text='Please relax your eyes\n%s' % tmr)
    label.after(1000, timer)

# window
app = Tk()
app.configure(bg='white')
app.overrideredirect(True)
app.wm_attributes("-transparentcolor", "black")
# app.wm_attributes("-transparentcolor", "#eeeeee")
app.wm_attributes("-topmost", True)
app.wm_attributes("-disabled", True)

# centered

# label
label = Label(app, font=('Segoe','100'), fg='#eeeeee', bg='black')
label.pack()
timer()

# test with image
# It is possible to make photo with transperent background
# just make sure pixels you want to be transperent have the same rgb or hex what you set
# if there are annoying leftovers - recheck their rgb or hex
# 
# render1 = ImageTk.PhotoImage(Image.open('test1.png'))
# lebel_img1 = Label(app, image=render1, borderwidth=0)
# lebel_img1.image = render1
# lebel_img1.pack()

app.mainloop()

# room for modefication
# 1) add setting from json, for example displayed text
# 2) differnt mods - annoying and not so much