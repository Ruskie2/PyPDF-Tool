import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

print(file_path)
# to convert a python file to an exe: python -m pip install pyinstaller
# then: pyinstaller mypythonfile.py