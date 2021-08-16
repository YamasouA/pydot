import tkinter
from PIL import Image, ImageDraw, ImageTk
from search_flag import search_img


class Application(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title('tkinter')
        self.pack()
        self.create_widgets()
        self.setup()
        #self.paint_color = "black"


    def create_widgets(self):
        self.vr = tkinter.IntVar()
        self.vr.set(1)
        # ボタンと動作の紐づけ
        self.write_radio = tkinter.Radiobutton(self, text='write', variable=self.vr, value=1, command=self.change_radio)
        self.write_radio.grid(row=0, column=0)
        self.erase_radio = tkinter.Radiobutton(self, text='erase', variable=self.vr, value=2, command=self.change_radio)
        self.erase_radio.grid(row=0, column=1)

        self.clear_button = tkinter.Button(self, text='clear all', command=self.clear_canvas)
        self.clear_button.grid(row=0, column=2)

        self.save_button = tkinter.Button(self, text='save', command=self.save_canvas)
        self.save_button.grid(row=0, column=3)

        self.line_color_red = tkinter.Button(self, bg="red", command=lambda: self.change_color("red"))
        self.line_color_red.grid(row=1, column=0)
        self.line_color_blue = tkinter.Button(self, bg="blue", command=lambda:self.change_color("blue"))
        self.line_color_blue.grid(row=1, column=1)
        self.line_color_green = tkinter.Button(self, bg="green", command=lambda:self.change_color("green"))
        self.line_color_green.grid(row=1, column=2)
        self.line_color_black = tkinter.Button(self, bg="black", command=lambda:self.change_color("black"))
        self.line_color_black.grid(row=1, column=3)
        self.line_color_cyan = tkinter.Button(self, bg="cyan", command=lambda:self.change_color("cyan"))
        self.line_color_cyan.grid(row=1, column=4)

        self.test_canvas = tkinter.Canvas(self, bg='white', width=600, height=300)
        self.test_canvas.grid(row=2, column=0, columnspan=4)
        self.test_canvas.bind('<B1-Motion>', self.paint)
        self.test_canvas.bind('<ButtonRelease-1>', self.reset)

        self.flag_img = tkinter.PhotoImage(file="")
        self.flag_canvas = tkinter.Canvas(self, bg='white', width=600, height=300)
        self.flag_canvas.grid(row=3, column=0, columnspan=4)

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.paint_color = 'black'
        self.eraser_on = False
        self.im = Image.new('RGB', (600, 300), 'white')
        self.draw = ImageDraw.Draw(self.im)

    def change_color(self, color):
        self.paint_color = color

    def change_radio(self):
        if self.vr.get() == 1:
            self.eraser_on = False
        else:
            self.eraser_on = True

    def clear_canvas(self):
        print("clear")
        self.test_canvas.delete(tkinter.ALL)
    
    def save_canvas(self):
        #self.test_canvas.postscript(file='out.jpg', colormode='color')
        self.im.save('test.jpg', 'jpeg')

    def paint(self, event):
        if self.eraser_on:
            self.paint_color = 'white'
        if self.old_x and self.old_y:
            self.test_canvas.create_line(self.old_x, self.old_y, event.x, event.y, width = 5.0, fill=self.paint_color,
                                        capstyle=tkinter.ROUND, smooth=tkinter.TRUE, splinesteps=36)
            self.draw.line((self.old_x, self.old_y, event.x, event.y), fill=self.paint_color, width=5)
            self.im.save('test.jpg', 'jpeg')
        self.old_x = event.x
        self.old_y = event.y
        path = search_img('test.jpg')
        path = './hata/' + path + ".gif"
        img = Image.open(path)
        img = img.convert('RGB')
        self.flag_canvas.photo = ImageTk.PhotoImage(img)
        img_show = self.flag_canvas.create_image(0, 0, anchor='nw', image=self.flag_canvas.photo)
        

        

    def reset(self, event):
        self.old_x, self.old_y = None, None
    
if __name__ == "__main__":
    root = tkinter.Tk()
    app = Application(master=root)
    app.mainloop()