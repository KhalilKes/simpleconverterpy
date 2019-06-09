from tkinter import *
from tkinter import messagebox, filedialog

import tkinter as tk
import moviepy.editor as audcon

#creating a widget with tkinter
def CreatWidgets():
    sourceLabel = Label(root, text = "VIDEO PATH : ", bg = "gray", font=('Helvetica', 10, 'bold'))
    sourceLabel.grid(row=1, column=1, padx=5, pady=20)

    root.sourceEntry = Entry(root, width=35, textvariable=source)
    root.sourceEntry.grid(row=1, column=2, padx=5, pady=20)

    destinationLabel = Label(root, text="AUDIO PATH: ", bg = "gray", font=('Helvetica', 10, 'bold'))
    destinationLabel.grid(row=3, column=1, padx=5, pady=20)

    root.destinationEntry = Entry(root, width=35, textvariable=destination)
    root.destinationEntry.grid(row=3, column=2, padx=5, pady=20)

    SRCBrowseBTN = Button(root, text="BROWSE", command=SBrowse, width=10)
    SRCBrowseBTN.grid(row=1, column=3, padx=5, pady=20)

    DESTBrowseBTN = Button(root, text="BROWSE", command=DBrowse, width=10)
    DESTBrowseBTN.grid(row=3, column=3, padx=5, pady=20)

    convertBTN = Button(root, text="CONVERT VIDEO", command=Convert, width=20)
    convertBTN.grid(row=2, column=1, columnspan=3, padx=5, pady=5)

# making of Sbrowse et DBrowse !!

def SBrowse():
    videoName = filedialog.askopenfilename(initialdir="C:",
                                            filetypes=(("MP4(*.mp4)", "*.mp4"),("AVI (*.avi)" , "*.avi"), ("ALL files")))

    root.sourceEntry.insert(0, videoName)



def DBrowse():
    audioName = filedialog.asksaveasfilename(initialdir="C:",
                                            defaultextension=".mp3",
                                            filetypes=(("MP3(*.mp3)", "*.mp3"),("WAV (*.wav)" , "*.wav"), ("ALL files")))
    root.destinationEntry.insert(0, audioName)


# making of CONVERT function !

def Convert():
    sourceFile = source.get()
    destinationFile = destination.get()

    sourceVideo = audcon.VideoFileClip(sourceFile)

    sourceVideo.audio.write_audiofile(destinationFile)

    messagebox.showinfo("Success", "Video converted baby, boooyah!")


#creating some objects

root = tk.Tk()

root.title("homemadeconverter")
root.config(bg="gray")
root.geometry("600x300")
root.resizable(True, True)

source = StringVar()
destination = StringVar()

CreatWidgets()

root.mainloop()
