import tkinter as tk
from tkinter import filedialog
import time

class SpeedReaderApp:
  def __init__(self, root):
    self.root = root
    self.root.title("Speed Reader")

    self.label = tk.Label(root, text="", font=("Helvetica", 48), wraplength=800)
    self.label.pack(pady=20)

    self.start_button = tk.Button(root, text="Start", command=self.start)
    self.start_button.pack(pady=5)

    self.stop_button = tk.Button(root, text="Stop", command=self.stop)
    self.stop_button.pack(pady=5)

    self.open_button = tk.Button(root, text="Open Text File", command=self.open_file)