import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import time

class SpeedReaderApp:
  def __init__(self, root):
    self.root = root
    self.root.title("Speed Reader")
    self.root.configure(bg="#2E2E2E")

    window_width = 800
    window_height = 600

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    center_x = int(screen_width/2 - window_width/2)
    center_y = int(screen_height/2 - window_height/2)

    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    style = ttk.Style()
    style.theme_use('clam')
    style.configure("TButton", background="#3A3A3A", foreground="white", font=("Helvetica", 12), padding=10)
    style.configure("TLabel", background="#2E2E2E", foreground="white", font=("Helvetica", 48))
    style.configure("TScale", background="#2E2E2E")
    style.configure("TFrame", background="#2E2E2E")

    self.frame = ttk.Frame(root, padding=10)
    self.frame.pack(fill="both", expand=True)

    self.label = ttk.Label(self.frame, text="", wraplength=800, anchor="center")
    self.label.pack(pady=20)

    self.start_button = ttk.Button(self.frame, text="Start", command=self.start)
    self.start_button.pack(pady=5)

    self.stop_button = ttk.Button(self.frame, text="Stop", command=self.stop)
    self.stop_button.pack(pady=5)

    self.open_button = ttk.Button(self.frame, text="Open Text File", command=self.open_file)
    self.open_button.pack(pady=5)

    self.speed_label = ttk.Label(self.frame, text="Speed: 300 ms per word", font=("Helvetica", 12))
    self.speed_label.pack(pady=5)

    self.speed_scale = ttk.Scale(self.frame, from_=100, to=1000, orient="horizontal", command=self.update_speed_label)
    self.speed_scale.set(300)
    self.speed_scale.pack(pady=5)

    self.text = ""
    self.running = False

  def start(self):
    self.running = True
    self.display_words()

  def stop(self):
    self.running = False

  def open_file(self):
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
      with open(file_path, 'r') as file:
        self.text = file.read()

  def display_words(self):
    if self.text:
      words = self.text.split()
      speed = self.speed_scale.get()
      for word in words:
        if not self.running:
          break
        self.label.config(text=word)
        self.root.update()
        time.sleep(speed / 1000)
      self.label.config(text="")

  def update_speed_label(self, value):
    self.speed_label.config(text=f"Speed: {int(float(value))} ms per word")

if __name__ == "__main__":
  root = tk.Tk()
  app = SpeedReaderApp(root)
  root.mainloop()