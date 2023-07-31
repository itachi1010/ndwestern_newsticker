import tkinter as tk


class Marquee(tk.Canvas):
    def __init__(self, parent, text, margin=2, speed=2, refresh_rate=100):
        tk.Canvas.__init__(self, parent, height=30)  # you can change the height to match your txt height
        self.margin = margin
        self.speed = speed
        self.refresh_rate = refresh_rate
        self._text = text
        self.configure(bg="black")  # you can change the background color here
        self.text = self.create_text(0, 0, anchor='w', tags=("text",), text=self._text, fill="white")  # create a text item
        self.bind("<Configure>", self.on_configure)
        self.after(self.refresh_rate, self.tick)


    def on_configure(self, event):
        bbox = self.bbox("all")
        if bbox is not None:
            self.configure(scrollregion=(-5, -5, bbox[2] + 10, bbox[3] + 10))
            self.itemconfigure("text", text=self._text)

    def tick(self):
        bbox = self.bbox("all")
        if bbox is not None:
            if bbox[2] < 0:  # if it completely scrolled to the left, reset it to start from the right side
                canvas_width = self.winfo_width()
                self.move("all", canvas_width + 2 * self.margin, 0)
            else:
                self.move("all", -self.speed, 0)  # move text with speed
        self.after(self.refresh_rate, self.tick)  # re-run the tick every refresh_rate ms


def fetch_text():
    with open('news.txt', 'r') as file:  # replace 'news.txt' with your file name
        data = file.read().replace('\n', '')
    return data


root = tk.Tk()
root.configure(bg="black")  # set background color of the root window

marquee = Marquee(root, text=fetch_text(), margin=10, speed=2, refresh_rate=50)
marquee.pack(fill="both", expand=True)

root.mainloop()
