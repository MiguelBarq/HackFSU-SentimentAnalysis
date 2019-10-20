import tkinter as tk
import webbrowser
# import youtube
import pafy
import vlc

def createUI():
    ui = tk.Tk()
    ui.geometry("300x120")
    ui.wm_title("HackFSU - Music Player")

    elements = createElements(ui)

    ui.mainloop()

def createElements(ui) -> list:
    outList = []

    # bulding player to stream music on pc
    try:
        # url = youtube.getURL("happy music")
        # print(url)
        video = pafy.new("https://www.youtube.com/watch?v=NvZtkt9973A")
        aStream = video.getbestaudio()
        playurl = aStream.url
        player = vlc.MediaPlayer(playurl)
    except:
        print("[WARNING] We were not able to retrieve a viable audio stream at this time from Youtube.")

    title = tk.Label(ui, text="Title, bruvh")
    title.pack(side="top")
    outList.append(title)
    
    stop = tk.Button(text="stop", command=lambda: stopButton(player))
    stop.pack(side="bottom", fill="x")
    outList.append(stop)

    pause = tk.Button(text="pause", command=lambda: pauseButton(player))
    pause.pack(side="bottom", fill="x")
    outList.append(pause)

    button = tk.Button(text="play the video", command=lambda: playButton(player))
    button.pack(side="bottom", fill="x")
    outList.append(button)

    return outList


def playButton(player):
    player.play()

def pauseButton(player):
    player.pause()

def stopButton(player):
    player.stop()

createUI()