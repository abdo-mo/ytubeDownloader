import tkinter as tk
import os
from pytube import YouTube
from pytube.cli import on_progress

root = tk.Tk()

def download_the_file():
    path = entry.get()
    yt = YouTube(path, on_progress_callback=on_progress)
    print(f'Video Title: {yt.title}')
    print(f'Number of Views: {yt.views}')
    print()
    save_path = 'C:\\Users\\Abdo\\Downloads'

    video = yt.streams.get_highest_resolution()
    video.download(output_path=save_path)

    print('> Video Successfully Downloaded!!')

canvas = tk.Canvas(root, height=600, width=500, bg='#263042')
canvas.pack()

frame = tk.Frame(root, bg='white')
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

entry = tk.Entry(frame, bd=4)
entry.pack()


download = tk.Button(frame, text="Download the Video", padx=10,
pady=5, fg="white", bg='#263042', command=download_the_file)
download.pack()

root.mainloop()