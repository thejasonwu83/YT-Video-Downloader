import tkinter
from tkinter import filedialog
import customtkinter
from pytube import YouTube
from PIL import ImageTk, Image

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

title = customtkinter.CTkLabel(app, text='Insert a YouTube link')
title.pack(padx=10, pady=10)

url = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url)
link.pack()
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()
    

def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        if option == "Highest quality":
            video = ytObject.streams.get_highest_resolution()
        elif option == "Lowest quality":
            video = ytObject.streams.get_lowest_resolution()
        else:
            video = ytObject.streams.get_audio_only()

        title.configure(text="Now downloading: " + ytObject.title + f" ({option_var})")
        finishLabel.configure(text="Download in progress", text_color='white')

        video.download()
        finishLabel.configure(text='Download complete')
        title.configure(text="Insert a YouTube link")
        link.delete(0, 'end')

    except:
        finishLabel.configure(text='YouTube link is invalid', text_color='red')

option_var = customtkinter.StringVar(value="Highest quality")
option = "Highest quality"
def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)
    option = choice

combobox = customtkinter.CTkOptionMenu(master=app,
                                       values=["Highest quality", "Lowest quality", "Audio only"],
                                       command=optionmenu_callback,
                                       variable=option_var)
combobox.pack(padx=20, pady=10)

download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

progPercent = customtkinter.CTkLabel(app, text="0%")
progPercent.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0.0)
progressBar.pack(padx=10, pady=10)

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    percentage = (total_size - bytes_remaining) / total_size
    progressBar.set(percentage)
    per = str(int(percentage * 100))
    progPercent.configure(text=per + '%')
    progPercent.update()


if __name__ == '__main__':
    app.mainloop()
