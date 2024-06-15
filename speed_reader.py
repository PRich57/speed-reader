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
    self.open_button.pack(pady=5)

    self.speed_scale = tk.Scale(root, from_=100, to=1000, label="Speed (ms per word)", orient="horizontal")
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

if __name__ == "__main__":
  root = tk.Tk()
  app = SpeedReaderApp(root)
  root.mainloop()