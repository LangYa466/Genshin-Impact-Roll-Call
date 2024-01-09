import random
from io import BytesIO
from tkinter import Tk, Label
from PIL import Image, ImageDraw, ImageFont , ImageTk

video_file1 = "原神.mp4"
font_file = "AaLongYanTi-2.ttf"
min_num = 1
max_num = 51
font_size = 500
text_position = (500, 300)
text_color = (0, 0, 0)

# 打开图片
with open("genshin.png", "rb") as f:
    image_data = f.read()
last_frame = Image.open(BytesIO(image_data))

# 在图片上绘制文本
draw = ImageDraw.Draw(last_frame)
font = ImageFont.truetype(font_file, font_size)
random_number = str(random.randint(min_num, max_num))
draw.text(text_position, random_number + '号', font=font, fill=text_color)

# 显示图像
root = Tk()

# 将图像转换为Tkinter可用的格式
image_tk = ImageTk.PhotoImage(last_frame)

# 创建标签并显示图像
panel = Label(root, image=image_tk)
panel.image = image_tk
panel.pack(side="bottom", fill="both", expand="yes")

# 运行Tkinter事件循环
root.mainloop()
