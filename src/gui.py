import customtkinter as ct
import os
import sys
from os import name
from tkinterdnd2 import DND_FILES, TkinterDnD


__version__ = "v0.1"

class MyFrame(ct.CTkScrollableFrame):
    """
    Allows CTkScrollableFrame to be executed in CTkTextbox
    """

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

    def widgets(self, decrypted_data):
        label = ct.CTkLabel(self, text=decrypted_data)
        label.grid(row=0, column=0, padx=20)

class App(ct.CTk, TkinterDnD.DnDWrapper):
    def __init__(self, queue):
        super().__init__()
        self.TkdndVersion = TkinterDnD._require(self)

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width - 500) // 2
        y = (screen_height - 340) // 2

        self.geometry(f"500x340+{x}+{y}")
        ct.set_appearance_mode("dark")
        self.title(f"TTS TwitchChat")

        if name == "nt":
            ico_path = os.path.join(os.path.dirname(__file__), "icon.ico")
            self.iconbitmap(ico_path)
        self.resizable(False, False)

        self.queue = queue

        self.chat_box = ct.CTkTextbox(
            master=self,
            width=300,
            height=300,
            fg_color="#181818",
            text_color="green",
            wrap="word",
            state="disabled"
        )
        self.chat_box.place(x=10, y=10)

        self.btn_json = ct.CTkButton(
            master=self,
            text="Open Json CFG",
            command=lambda: self.open_json(),
            corner_radius=10,
            hover_color="#2a2c2c",
            width=170,
            height=95,
            fg_color="#1d1e1e",
            text_color="#696969",
        )
        self.btn_json.place(x=320, y=10)

        self.btn_models = ct.CTkButton(
            master=self,
            text="Open folder models",
            command=lambda: self.open_models(),
            corner_radius=10,
            hover_color="#2a2c2c",
            width=170,
            height=95,
            fg_color="#1d1e1e",
            text_color="#696969",
        )
        self.btn_models.place(x=320, y=110)

        self.btn_reboot_app = ct.CTkButton(
            master=self,
            text="Reboot APP",
            command=lambda: self.reboot_app(),
            corner_radius=10,
            hover_color="#2a2c2c",
            width=170,
            height=47,
            fg_color="#1d1e1e",
            text_color="#696969",
        )
        self.btn_reboot_app.place(x=320, y=210)

        self.btn_start = ct.CTkButton(
            master=self,
            text="Start",
            command=lambda: self.check_queue_loop(),
            corner_radius=10,
            hover_color="#2a2c2c",
            width=170,
            height=47,
            fg_color="#1d1e1e",
            text_color="#696969",
        )
        self.btn_start.place(x=320, y=263)

        self.canvas = ct.CTkCanvas(self, height=2, width=500, bg=self.cget("bg"), highlightthickness=0)
        self.canvas.create_line(0, 1, 500, 1, fill="grey")
        self.canvas.place(x=0, y=320)

        self.info_time = ct.CTkLabel(
            master=self,
            text=f"{__version__} (by busjr)",
            height=5,
            text_color="#696969",
        )
        self.info_time.place(x=0, y=325)

    def open_json(self):
        os.system("notepad config.json")

    def open_models(self):
        os.system("explorer models")

    def reboot_app(self):
        src = sys.argv[0]
        full_path = os.path.abspath(src)  # full path sourse file
        os.execv(sys.executable, [sys.executable, full_path])

    def check_queue_loop(self):
        self.check_queue()
        self.after(100, self.check_queue_loop)

    def check_queue(self):
        while not self.queue.empty():
            message = self.queue.get()
            if type(message) == str:
                self.paste_chat(message)
            elif type(message) == float:
                self.paste_info(message)

    def paste_chat(self, text):
        self.chat_box.configure(state="normal")
        self.chat_box.insert("end", text + "\n")
        self.chat_box.yview("moveto", 1.0)
        self.chat_box.configure(state="disabled")

    def paste_info(self, text):
        self.info(text)