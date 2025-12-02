import logging
import webbrowser
import json
import os
import sys
import tkinter as tk

from tkinter import ttk, messagebox

logging.basicConfig(
    format="[%(levelname)s] %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def is_ip_valid(ip):
    fields = ip.split(".")
    if len(fields) != 4:
        return False

    for field in fields:
        if not field.isdigit():
            return False

        if int(field) < 0 or int(field) > 255:
            return False

    return True

class Connect:
    def __init__(self, root):
        self.root = root
        self.root.title("remote desktop connector")
        self.root.geometry("1280x720")
        #self.root.resizable(False, False)
        
        self.config = "config.json"
        
        self.create_widgets()
        self.load_config()
    
    def create_widgets(self):
        padx, pady = 20, 10

        frame = ttk.Frame(self.root, padding="100")
        frame.grid(row=0, column=0, sticky="nsew")
        
        self.root.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)

        ttk.Label(frame, text="IP Address").grid(row=0, column=0, sticky=tk.W, pady=pady)
        self.ip = ttk.Entry(frame, width=64)
        self.ip.grid(row=0, column=1, sticky="ew", padx=padx, pady=pady)
        
        ttk.Label(frame, text="Username").grid(row=1, column=0, sticky=tk.W, pady=pady)
        self.username = ttk.Entry(frame, width=64)
        self.username.grid(row=1, column=1, sticky="ew", padx=padx, pady=pady)
        
        ttk.Label(frame, text="Password").grid(row=2, column=0, sticky=tk.W, pady=10)
        self.password = ttk.Entry(frame, width=64, show="*")
        self.password.grid(row=2, column=1, sticky="ew", padx=padx, pady=pady)
        
        self.connect_button = ttk.Button(frame, text="Connect", command=self.connect)
        self.connect_button.grid(row=3, column=0, columnspan=2, pady=pady)
        
        self.ip.bind("<KeyRelease>", lambda event: self.save_config())
        self.username.bind("<KeyRelease>", lambda event: self.save_config())
        self.password.bind("<KeyRelease>", lambda event: self.save_config())
    
    def load_config(self):
        if os.path.exists(self.config):
            try:
                with open(self.config, "r") as file:
                    config = json.load(file)
                    self.ip.insert(0, config.get("ip", ""))
                    self.username.insert(0, config.get("username", ""))
                    self.password.insert(0, config.get("password", ""))
            except Exception as e:
                logger.error(f"failed to load config: {e}")
    
    def save_config(self):
        try:
            config = {
                "ip": self.ip.get(),
                "username": self.username.get(),
                "password": self.password.get()
            }
            with open(self.config, "w") as file:
                json.dump(config, file, indent=2)
        except Exception as e:
            logger.error(f"failed to save config: {e}")
    
    def connect(self):
        ip = self.ip.get().strip()
        username = self.username.get().strip()
        password = self.password.get().strip()
        
        if not ip or not username or not password:
            messagebox.showerror("Error", "all fields are required!")
            return

        if not is_ip_valid(ip):
            messagebox.showerror("Error", "invalid ip address!")
            return

        
        url = f"{ip}/s/?mmk&u={username}&p={password}"
        
        try:
            webbrowser.open(url)
            self.save_config()
        except Exception as e:
            messagebox.showerror("Error", f"failed to open browser: {e}")


