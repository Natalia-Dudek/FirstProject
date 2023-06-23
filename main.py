from tkinter import *
from pytube import YouTube
from tkinter import messagebox
from tkinter import filedialog

def Widgets():
    title_label = Label(window, text="YouTube Video Downloader",
                        padx=15,
                        pady=15,
                        font=("Arial", 14),
                        bg="black",
                        fg="red")
    title_label.grid(row=1,
                     column=1,
                     pady=10,
                     padx=5,
                     columnspan=3)

    link_label = Label(window,
                       text="YouTube link :",
                       bg="black",
                       fg="red",
                       pady=5,
                       padx=5)
    link_label.grid(row=2,
                    column=0,
                    pady=5,
                    padx=5)

    window.linkText = Entry(window,
                            width=35,
                            textvariable=video_Link,
                            font="Arial 14",
                            bd=5)
    window.linkText.grid(row=2,
                         column=1,
                         pady=5,
                         padx=5,
                         columnspan=2)

    location_label = Label(window,
                           text="Location :",
                           bg="black",
                           fg="red",
                           pady=5,
                           padx=9)
    location_label.grid(row=3,
                        column=0,
                        pady=5,
                        padx=5)

    window.destinationText = Entry(window,
                                   width=27,
                                   textvariable=download_Path,
                                   font="Arial 14",
                                   bd=5)
    window.destinationText.grid(row=3,
                                column=1,
                                pady=5,
                                padx=5)

    browse_button = Button(window,
                           text="Browse",
                           command=Browse,
                           width=10,
                           bg="white",
                           fg="black",
                           relief=GROOVE,
                           bd=5)
    browse_button.grid(row=3,
                       column=2,
                       pady=1,
                       padx=1)

    download_button = Button(window,
                             text="Download Video",
                             command=Download,
                             width=20,
                             bg="white",
                             fg="black",
                             bd=5,
                             relief=GROOVE,
                             font="Georgia, 13")
    download_button.grid(row=4,
                         column=1,
                         pady=20,
                         padx=20)


def Browse():
    download_Directory = filedialog.askdirectory(
        initialdir="YOUR DIRECTORY PATH", title="Save Video")

    download_Path.set(download_Directory)


def Download():
    Youtube_link = video_Link.get()

    download_Folder = download_Path.get()

    getVideo = YouTube(Youtube_link)

    videoStream = getVideo.streams.first()

    videoStream.download(download_Folder)

    messagebox.showinfo("SUCCESSFULLY",
                        "DOWNLOADED AND SAVED IN\n"
                        + download_Folder)



window = Tk()

# center the window when it appears (kinda)
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_height()

x = int((screen_width/2) - (window_width/1))
y = int((screen_height/1) - (window_height/7))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.geometry("520x280")
window.resizable(False, False)
window.title("YouTube Video Downloader")
window.config(background="black")

video_Link = StringVar()
download_Path = StringVar()

Widgets()

window.mainloop()
