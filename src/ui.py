import tkinter as tk
import webbrowser
# import youtube
import pafy
import vlc
import time
import sentAnalysis

player = []

def createUI(searchQuery:str):
    ui = tk.Tk()
    ui.geometry("300x120")
    ui.wm_title("HackFSU - Music Player")

    elements = createElements(ui, searchQuery)

    ui.mainloop()

def createElements(ui, searchQuery:str) -> list:
    outList = []

    title = tk.Label(ui, text="Title, bruvh")
    title.pack(side="top")
    outList.append(title)
    
    stop = tk.Button(text="stop", command=lambda: stopButton(player))
    stop.pack(side="bottom", fill="x")
    outList.append(stop)

    pause = tk.Button(text="pause", command=lambda: pauseButton(player))
    pause.pack(side="bottom", fill="x")
    outList.append(pause)

    button = tk.Button(text="play the video", command=lambda: playButton(player, searchQuery))
    button.pack(side="bottom", fill="x")
    outList.append(button)

    return outList

def setSong(searchQuery:str):
    print("setSong attempting to search for: " + searchQuery)

    # bulding player to stream music on pc
    try:
        # url = youtube.getURL(searchQuery)
        # print(url)
        video = pafy.new("https://www.youtube.com/watch?v=BAGkYLoVFLM")
        aStream = video.getbestaudio()
        playurl = aStream.url
        player = vlc.MediaPlayer(playurl)
        loopyboi(player)
    except:
        print("[WARNING] We were not able to retrieve a viable audio stream at this time from Youtube.")

def playButton(player, searchQuery:str):
    setSong(searchQuery)
    player.play()

def pauseButton(player):
    player.pause()

def stopButton(player):
    player.stop()

# For you to place where needed
def loopyboi(player):
    # Holds the sentiment analysis for throughout the song
    song_sent = []
    # Tells when near end of song. TODO
    end_of_song = False

    # This loop will call sentiment analysis at 3fps once every 2 seconds
    start_time = time.time()
    song_start_time = time.time()
    song_sent.append(sentAnalysis.sentAnalysis(3))
    while True:
        if end_of_song:
            break
        
        # Updating time
        curr_time = time.time()

        # Checks if song is over
        if(float(curr_time - song_start_time) >= player.get_length()):
            end_of_song = True

        # If two seconds have elapsed
        if (float(curr_time - start_time) >= 2):
            # Getting another sentiment analysis
            song_sent.append(sentAnalysis.sentAnalysis(3))
            # Updating start_time
            start_time = time.time()

    return song_sent


    