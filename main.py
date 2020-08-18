import time

from tkinter import *
from PIL import Image, ImageTk


def timer():
    tmr = 60 - int(time.perf_counter())

    if tmr < 0:
        app.destroy()

    label.config(text='RELAX, let your eyes rest\n%s' % tmr)
    label.after(1000, timer)


# Create window and make it transparent.
app = Tk()
app.configure(bg='black')
app.overrideredirect(True)
app.wm_attributes("-transparentcolor", "black")
app.wm_attributes("-topmost", True)
app.wm_attributes("-disabled", True)
app.state('zoomed')

# Add label and change it every second in function 'timer'.
label = Label(app, font=('Segoe UI','100', 'bold'), fg='#74B62E', bg='black')
label.pack()
timer()


app.mainloop()

# It is possible to make photo with transperent background
# just make sure pixels you want to be transperent have the same rgb or hex what you set
# if there are annoying leftovers - recheck their rgb or hex
# 
# render1 = ImageTk.PhotoImage(Image.open('test1.png'))
# lebel_img1 = Label(app, image=render1, borderwidth=0)
# lebel_img1.image = render1
# lebel_img1.pack()