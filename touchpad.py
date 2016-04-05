#!/usr/bin/env python3
import time
from tkinter import *
from blink1.blink1 import blink1
import socket
import pygame

class Application(Frame):
    def __init__(self, master=None):
        self.page = 1
        Frame.__init__(self, master)
        self.draw()
    
    def draw(self, master=None):
        self.grid()
        self.master.title("PyButtons")
        for r in range(3):
            self.master.rowconfigure(r, weight=1)
        for c in range(4):
            self.master.columnconfigure(c, weight=1)

        self.frame0 = Frame(master, bg="red")
        self.frame0.grid(row=0,column=0, rowspan=3, columnspan=2, sticky = W+E+N+S)
        self.frame1 = Frame(master, bg="green")
        self.frame1.grid(row=0,column=2, rowspan=3, columnspan=2, sticky = W+E+N+S)
        self.frame2 = Frame(master, bg="blue")
        self.frame2.grid(row=0,column=4, rowspan=3, columnspan=1, sticky = W+E+N+S)
        self.createWidgets()
 
    def createWidgets(self):
        if self.page == 1:
            self.red = Button(self.frame1, text="BUSY", fg="red", command=lambda: self.set_color('red'), font=("Helvetica, 20")) 
            self.red.pack(fill="both", expand=True)
            self.green = Button(self.frame1, text="FREE", fg="green", command=lambda: self.set_color('green'), font=("Helvetica, 20")) 
            self.green.pack(fill="both", expand=True)
            self.blue = Button(self.frame1, text="Busy", fg="blue", command=lambda: self.set_color('blue'), font=("Helvetica, 20")) 
            self.blue.pack(fill="both", expand=True)

            self.SOUNDS = Button(self.frame2, text="SNDS", command=lambda: self.set_page(2), font=("Helvetica, 20"))
            self.SOUNDS.pack(fill="both", expand=True)

        if self.page == 2:
            self.gun = Button(self.frame0, text="GUN", command=lambda: self.playSound('/home/pi/Desktop/scripts/sounds/gun.wav'), font=("Helvetica, 20"))
            self.gun.pack(fill=BOTH, expand=True)
            self.cricket = Button(self.frame0, text="CRICKET", command=lambda: self.playSound('/home/pi/Desktop/scripts/sounds/cricket.wav'), font=("Helvetica, 20"))
            self.cricket.pack(fill=BOTH, expand=True)
            self.dun = Button(self.frame0, text="DUN", command=lambda: self.playSound('/home/pi/Desktop/scripts/sounds/DUN.wav'), font=("Helvetica, 20"))
            self.dun.pack(fill=BOTH, expand=True)
            self.buzz = Button(self.frame1, text="BUZZ", command=lambda: self.playSound('/home/pi/Desktop/scripts/sounds/buzz.wav'), font=("Helvetica, 20"))
            self.buzz.pack(fill=BOTH, expand=True)
            self.yes = Button(self.frame1, text="YES", command=lambda: self.playSound('/home/pi/Desktop/scripts/sounds/yes.wav'), font=("Helvetica, 20"))
            self.yes.pack(fill=BOTH, expand=True)
            self.moist = Button(self.frame1, text="MOIST", command=lambda: self.playSound('/home/pi/Desktop/scripts/sounds/moist.wav'), font=("Helvetica, 20"))
            self.moist.pack(fill=BOTH, expand=True)

            self.STATUS = Button(self.frame2, text="STATS", command=lambda: self.set_page(1), font=("Helvetica, 20"))
            self.STATUS.pack(fill="both", expand=True)

        self.QUIT = Button(self.frame2, text="QUIT", command=lambda: self.quit(), font=("Helvetica, 20"))
        self.QUIT.pack(fill="both", expand=True)

        self.IP = Button(self.frame2, text="IP", command=lambda: self.get_ip(), font=("Helvetica, 20"))
        self.IP.pack(fill="both", expand=True)

    def set_page(self, page):
        self.page = page
        self.draw()

    def set_color(self, color):
        with blink1(switch_off=False) as b1:
            b1.fade_to_color(1000, color)
            time.sleep(1)

    def playSound(self, filename):
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

    def quit(self):
        with blink1() as b1:
            b1.fade_to_color(1000, 'black')
            time.sleep(1)
        root.destroy()

    def get_ip(self):
        ip = ([l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0])
        messagebox.showinfo("IP", "{0}".format(ip))

pygame.init()
root = Tk()
root.attributes('-fullscreen', True)
app = Application(master=root)
app.mainloop()

