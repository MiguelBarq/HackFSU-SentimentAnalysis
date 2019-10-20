import tkinter as tk
import webbrowser
import youtube
import pafy
import vlc

def createUI():
    ui = tk.Tk()
    ui.geometry("500x500")
    ui.wm_title("HackFSU - Music Player")

    createElements(ui)

    ui.mainloop()

def createElements(ui):
    label = tk.Label(text="test text")
    label.pack()

    label2 = tk.Label(text="more test text")
    label2.pack()

    url = youtube.getURL("happy music")
    print(url)
    button = tk.Button(text="play the video", command=lambda: onClick(url))
    button.pack()

def onClick(url):
    video = pafy.new("https://www.youtube.com/watch?v=BAGkYLoVFLM")
    aStream = video.getbestaudio()
    playurl = aStream.url
    player = vlc.MediaPlayer(playurl)
    player.play()

createUI()