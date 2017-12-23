'''
    NOTE:
        => you should install Python: https://www.python.org/downloads/
        => install the following packages using "pip" or "pip3" command: matplotlib, numpy, scipy,
            ipython, jupyter, pandas, sympy, nose, pillow (Example: pip3 install matplotlib)
'''
import matplotlib.style as style
style.use("dark_background")

import matplotlib as mpl
mpl.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
import os
import tkinter.font as tfont
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import threading
import urllib
import urllib.request as url_req
import json
import datetime as dt
import numpy as np
from PIL import Image, ImageTk
# defining our Data variables (structure) + variables + functions
chart_info_type = "market_price"
chart_info_time = "30days"
chart_info_all = {
        "market_price": "https://api.blockchain.info/charts/market-price?timespan={0}&format=json",
        "bitcoin_in_circulation": "https://api.blockchain.info/charts/total-bitcoins?timespan={0}&format=json",
        "market_capitalization": "https://api.blockchain.info/charts/market-cap?timespan={0}&format=json",
        "number_of_transactions_per_day": "https://api.blockchain.info/charts/n-transactions?timespan={0}&format=json",
        "total_number_of_transactions": "https://api.blockchain.info/charts/n-transactions-total?timespan={0}&format=json"
    }
exit_without_saving = True
new_draw = True
ALL_FONT = ("Verdana", 15)

fig = Figure((10, 5.5))
subplot = fig.add_subplot(111)

def exit_app(c_obj):
    if exit_without_saving:
        os._exit(0)

    def exit_option():
        tk_exit = tk.Tk()

        def save_and_exit():
            c_obj.save_chart()
            os._exit(0)

        lab = tk.Label(tk_exit, text="Do You Want To Save The Chart Before Exiting Or Not?", font=ALL_FONT)
        lab.grid(row=0, column=0, columnspan=2)
        yes_b = ttk.Button(tk_exit, text="Yes", command=save_and_exit)
        noo_b = ttk.Button(tk_exit, text="No", command=lambda: os._exit(0))
        yes_b.grid(row=1, column=0)
        noo_b.grid(row=1, column=1)

        tk_exit.wm_title("Exit Options")
        tk_exit.resizable(False, False)
        tk_exit.mainloop()

    exit_option()
def exit_red():
    tk_exit = tk.Tk()

    lab = tk.Label(tk_exit, text="Do You Want Really To Exit?", font=ALL_FONT)
    lab.grid(row=0, column=0, columnspan=2)
    yes_b = ttk.Button(tk_exit, text="Yes", command=lambda: os._exit(0))
    noo_b = ttk.Button(tk_exit, text="No", command=tk_exit.destroy)
    yes_b.grid(row=1, column=0)
    noo_b.grid(row=1, column=1)

    tk_exit.wm_title("Exit Red Options")
    tk_exit.resizable(False, False)
    tk_exit.mainloop()
def change_chart_info_type(new_info):
    if new_info in chart_info_all:
        global chart_info_type
        global new_draw
        
        new_draw = True
        chart_info_type = new_info
    else:
        msg = msgbox.showerror("ERROR MESSAGE", "{0} isn't supported".format(new_info))
def change_chart_info_time(new_info):
    if new_info in ["2days", "15days", "30days", "60days", "180days", "1year", "2years", "all"]:
        global chart_info_time
        global new_draw
        
        new_draw = True
        chart_info_time = new_info
        
    else:
        msg = msgbox.showerror("ERROR MESSAGE", "{0} isn't supported".format(new_info))
def about_us():
    tk_ab_us = tk.Tk()

    msg = tk.Message(tk_ab_us, text='''
Since you searched for us that means that you like my program.
I'm a programmer, I like creating programs/application and study new thing.
for contacting me: => https://github.com/othLah <=
''', font=ALL_FONT)
    ab_us_butt = ttk.Button(tk_ab_us, text="Exit", command=tk_ab_us.destroy)
    msg.pack()
    ab_us_butt.pack()

    tk_ab_us.wm_title("About Us")
    tk_ab_us.resizable(False, False)
    tk_ab_us.mainloop()
def tutorial():
    tk_01 = tk.Tk()
    
    def tutorial2():
        tk_01.destroy()
        tk_02 = tk.Tk()

        def tutorial3():
            tk_02.destroy()
            tk_03 = tk.Tk()

            def tutorial4():
                tk_03.destroy()
                tk_04 = tk.Tk()

                img = ImageTk.PhotoImage(Image.open("tuto_images\\img04.png"), master=tk_04)
                lab04 = tk.Label(tk_04, image=img)
                lab04.image = img
                lab04.pack()
                butt04 = ttk.Button(tk_04, text="Finish", command=tk_04.destroy)
                butt04.pack()

                tk_04.wm_title("Tutorial -Help & Toolbar-")
                tk_04.geometry("{0}x{1}+0+0".format(tk_04.winfo_screenwidth(), tk_04.winfo_screenheight()))
                tk_04.mainloop()

            img = ImageTk.PhotoImage(Image.open("tuto_images\\img03.png"), master=tk_03)
            lab03 = tk.Label(tk_03, image=img)
            lab03.image = img
            lab03.pack()
            butt03 = ttk.Button(tk_03, text="Next", command=tutorial4)
            butt03.pack()
            
            tk_03.wm_title("Tutorial -Edit-")
            tk_03.geometry("{0}x{1}+0+0".format(tk_03.winfo_screenwidth(), tk_03.winfo_screenheight()))
            tk_03.mainloop()

        img = ImageTk.PhotoImage(Image.open("tuto_images\\img02.png"), master=tk_02)
        lab02 = tk.Label(tk_02, image=img)
        lab02.image = img
        lab02.pack()
        butt02 = ttk.Button(tk_02, text="Next", command=tutorial3)
        butt02.pack()

        tk_02.wm_title("Tutorial -Graph-")
        tk_02.geometry("{0}x{1}+0+0".format(tk_02.winfo_screenwidth(), tk_02.winfo_screenheight()))
        tk_02.mainloop()

    img = ImageTk.PhotoImage(Image.open("tuto_images\\img01.png"), master=tk_01)
    lab01 = tk.Label(tk_01, image=img)
    lab01.image = img
    lab01.pack()
    butt01 = ttk.Button(tk_01, text="Next", command=tutorial2)
    butt01.pack()

    tk_01.wm_title("Tutorial -Introduction & File-")
    tk_01.geometry("{0}x{1}+0+0".format(tk_01.winfo_screenwidth(), tk_01.winfo_screenheight()))
    tk_01.mainloop()
def animate(i):
    try:
        global new_draw
        if new_draw:
            new_draw = False
            if not exit_without_saving:
                msgbox.showinfo("Waiting...", "Wait a Moment Please!!! It's About Your Connexion speed ;)")
        
            bit_data = url_req.urlopen(chart_info_all[chart_info_type].format(chart_info_time)).read().decode("utf-8")
            bit_data = json.loads(bit_data)["values"]

            x_axis, y_axis = [], []
            for xy in bit_data:
                x_axis.append(xy["x"])
                y_axis.append(xy["y"])
        
            date_convert_fct = np.vectorize(dt.datetime.fromtimestamp)
            x_axis = date_convert_fct(x_axis)
    
            subplot.clear()
            subplot.grid(True)
            if chart_info_type=="market_price" or chart_info_type=="market_capitalization":
                subplot.set_title(chart_info_type.replace("_", " ").title() + " (USD)")
            else:
                subplot.set_title(chart_info_type.replace("_", " ").title())
            subplot.plot_date(x_axis, y_axis, "r-")
    except urllib.error.HTTPError:
        msg = msgbox.showerror("ERROR MESAGE", "Check Out Your Network Connection.")
    except:
        msg = msgbox.showerror("ERROR MESAGE", "An Error Has Been Occurred.")
    

class BitcoinClass(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        # a tk.Frame container
        main_frame = tk.Frame(self)
        main_frame.pack()
        
        wel_come = WelcomeFrame(main_frame, self)
        wel_come.grid(row=0, column=0)
        con_tent = ContentFrame(main_frame)
        con_tent.grid(row=0, column=0)
        self.all_frames = {
            WelcomeFrame: wel_come,
            ContentFrame: con_tent
        }
        self.all_frames[WelcomeFrame].tkraise()

        main_menu = tk.Menu(self)
        # adding the File cascade menu
        file_menu = tk.Menu(main_menu, tearoff=False)
        file_menu.add_command(label="Continue", command=self.add_content_frame)
        file_menu.add_command(label="Save", state=tk.DISABLED)
        file_menu.add_command(label="Exit", command=lambda: exit_app(None))
        main_menu.add_cascade(label="File", menu=file_menu)
        # adding the Edit cascade menu
        edit_menu = tk.Menu(main_menu)
        edit_menu.add_command(label="Market Price", command=lambda: change_chart_info_type("market_price"))
        edit_menu.add_command(label="Bitcoin In Circulation", command=lambda: change_chart_info_type("bitcoin_in_circulation"))
        edit_menu.add_command(label="Market Capitalization", command=lambda: change_chart_info_type("market_capitalization"))
        edit_menu.add_command(label="Number Of Transactions Per Day", command=lambda: change_chart_info_type("number_of_transactions_per_day"))
        edit_menu.add_command(label="Total Number Of Transactions", command=lambda: change_chart_info_type("total_number_of_transactions"))
        main_menu.add_cascade(label="Edit", menu=edit_menu)
        # adding the Help cascade menu
        help_menu = tk.Menu(main_menu, tearoff=False)
        help_menu.add_command(label="About Us", command=about_us)
        help_menu.add_command(label="Tutorial", command=tutorial)
        main_menu.add_cascade(label="Help", menu=help_menu)
        # adding all the 3 cascade menus into a dictionary
        self.all_menus = {
                "File": file_menu,  "Edit": edit_menu,  "Help": help_menu
            }
        self.config(menu=main_menu)
        # some configurations
        self.wm_title("Bitcoin Charts App v1.0")
        self.iconbitmap(default=r"bitcoin_icon.ico")
        self.protocol("WM_DELETE_WINDOW", exit_red)
        self.resizable(False, False)
    def add_content_frame(self):
        global exit_without_saving
        exit_without_saving = False

        self.all_frames[ContentFrame].tkraise()
        self.all_frames[WelcomeFrame].destroy()
        
        f_menu = self.all_menus["File"]
        f_menu.delete(0, 2)
        f_menu.insert_command(0, label="Continue", state=tk.DISABLED)
        f_menu.insert_command(1, label="Save", command=self.all_frames[ContentFrame].save_chart)
        f_menu.insert_command(2, label="Exit", command=lambda: exit_app(self.all_frames[ContentFrame]))

        
        self.protocol("WM_DELETE_WINDOW", lambda: exit_app(self.all_frames[ContentFrame]))

class WelcomeFrame(tk.Frame):
    def __init__(self, frame, tkObj):
        tk.Frame.__init__(self, frame)

        message = tk.Message(self, text='''
Welcome to Bitcoin App :) ;)

This app presents the actual statistics concerning Bitcoin

The source code is available on "https://github.com/othLah/Bitcoin_Charts_App_v1.0"
Use it and Change it as you want but with your risks

Leave a star ;)
                                        ''', font=tfont.Font(family="Bitcoin Font", size=15, weight="bold", slant="italic"))
        message.grid(row=0, column=0, columnspan=2)
        
        continue_butt = ttk.Button(self, text="Continue", command=tkObj.add_content_frame)
        exit_butt = ttk.Button(self, text="Exit", command=lambda: os._exit(0))
        continue_butt.grid(row=1, column=0)
        exit_butt.grid(row=1, column=1)

class ContentFrame(tk.Frame):
    def __init__(self, frame):
        tk.Frame.__init__(self, frame)

        # adding the graph to the tkinter window
        g_frame = tk.Frame(frame)
        
        canvas = FigureCanvasTkAgg(fig, g_frame)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        self.toolbar = NavigationToolbar2TkAgg(canvas, g_frame)
        self.toolbar.update()
        
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        g_frame.grid(row=0, column=0)
        
        subplot.grid(True)
        self.add_time_buttons(frame)
        #th_drawing = Charts_Thread()
        #th_drawing.start()
    def save_chart(self):
        self.toolbar.save_figure()
    # adding time option buttons
    def add_time_buttons(self, frame):
        b_frame = tk.Frame(frame)
        
        b1 = ttk.Button(b_frame, text="2 Days", command=lambda: change_chart_info_time("2days"))
        b2 = ttk.Button(b_frame, text="15 Days", command=lambda: change_chart_info_time("15days"))
        b3 = ttk.Button(b_frame, text="30 Days", command=lambda: change_chart_info_time("30days"))
        b4 = ttk.Button(b_frame, text="60 Days", command=lambda: change_chart_info_time("60days"))
        b5 = ttk.Button(b_frame, text="180 Days", command=lambda: change_chart_info_time("180days"))
        b6 = ttk.Button(b_frame, text="1 Year", command=lambda: change_chart_info_time("1year"))
        b7 = ttk.Button(b_frame, text="2 Years", command=lambda: change_chart_info_time("2years"))
        b8 = ttk.Button(b_frame, text="All Time", command=lambda: change_chart_info_time("all"))

        b1.grid(row=0, column=0)
        b2.grid(row=0, column=1)
        b3.grid(row=0, column=2)
        b4.grid(row=0, column=3)
        b5.grid(row=0, column=4)
        b6.grid(row=0, column=5)
        b7.grid(row=0, column=6)
        b8.grid(row=0, column=7)

        b_frame.grid(row=1, column=0)


bit_app = BitcoinClass()
ani = animation.FuncAnimation(fig, animate, interval=2000)
bit_app.mainloop()
