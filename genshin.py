import subprocess
import random
from PIL import Image, ImageDraw, ImageFont
import tkinter as tk
from PIL import ImageTk

video_file1 = "原神.mp4"
font_file = "AaLongYanTi-2.ttf"
min_num = 1
max_num = 51
font_size = 500
font = ImageFont.truetype(font_file, font_size)

command1 = ["ffplay", "-autoexit", video_file1]
subprocess.run(command1)

last_frame = Image.open("genshin.png")
draw = ImageDraw.Draw(last_frame)
random_number = str(random.randint(min_num, max_num))
draw.text((500,300), random_number + '号', font=font, fill=(0, 0, 0))

root = tk.Tk()
img = ImageTk.PhotoImage(last_frame)
panel = tk.Label(root, image=img)
panel.pack(side="bottom", fill="both", expand="yes")
root.mainloop()
