import tkinter as tk
import youtube
import pafy
import vlc
import time
from keras.models import load_model
from collections import Counter
import sentAnalysis
import numpy as np

model = load_model("../data/simple_CNN.985-0.66.hdf5")
query_dict = {
    'rock' : 1,
    'instrumental' : 1,
    'pop' : 1,
    'jazz' : 1,
    'edm' : 1,
    'country': 1
}
uiElements = []

def createUI(searchQuery:str):
    ui = tk.Tk()
    ui.geometry("300x120")
    ui.wm_title("HackFSU - Music Player")

    global uiElements
    uiElements = createElements(ui, searchQuery)

    ui.mainloop()

def createElements(ui, searchQuery:str) -> list:
    outList = []

    # bulding player to stream music on pc
    try:
        player = setSong(searchQuery)
    except:
        print("[WARNING] We were not able to retrieve a viable audio stream at this time from Youtube.")

    title = tk.Label(ui, text="HackFSU - Music Player")
    title.pack(side="top")
    outList.append(title)

    stop = tk.Button(text="stop", command=lambda: stopButton(player))
    stop.pack(side="bottom", fill="x")
    outList.append(stop)

    # pause = tk.Button(text="pause", command=lambda: pauseButton(player))
    # pause.pack(side="bottom", fill="x")
    # outList.append(pause)

    button = tk.Button(text="play the video", command=lambda: playButton(player))
    button.pack(side="bottom", fill="x")
    outList.append(button)

    return outList

def setSong(searchQuery:str):
    print("setSong attempting to search for: " + searchQuery)

    # bulding player to stream music on pc
    try:
        dataList = youtube.getURL(searchQuery, 10)
        url = dataList[0]
        title = dataList[1]
        thumbnail = dataList[2]

        print(url)
        print(title)
        print(thumbnail)

        global uiElements
        uiElements[0].config(text=title)

        video = pafy.new(url)
        aStream = video.getbestaudio()
        playurl = aStream.url
        player = vlc.MediaPlayer(playurl)
        print(player.get_length())

        return player
    except:
        print("[WARNING] We were not able to retrieve a viable audio stream at this time from Youtube.")

def playButton(player):
    start_mood = sentAnalysis.sentAnalysis(5, model)
    random_genre = np.random.choice(list(query_dict.keys()), 1, p = [x/sum(query_dict.values()) for x in query_dict.values()])[0]
    player = setSong(opposite_mood(start_mood) + ' ' + random_genre + " music")
    player.play()
    loopyboi(player, start_mood, random_genre)

def pauseButton(player):
    player.pause()

def stopButton(player):
    quit()

# For you to place where needed
def loopyboi(player, start_mood, last_genre):
    time.sleep(1)
    print("\n\n\n\nLoopy Boi Print:", player.get_length()/2000 - 1)
    time.sleep(player.get_length()/2000 - 1)

    # Holds the sentiment analysis for throughout the song
    song_sent = []
    # Tells when near end of song.
    end_of_song = False

    # This loop will call sentiment analysis at 3fps once every 2 seconds
    start_time = time.time()
    song_start_time = time.time()
    song_sent.append(sentAnalysis.sentAnalysis(5, model))
    while True:
        print(time.time() + player.get_length()/2000 - song_start_time ," : " , player.get_length()/1000)

        if end_of_song:
            player.stop()
            break

        # Updating time
        curr_time = time.time()

        # Checks if song is over
        if(float(curr_time + player.get_length()/2000 - song_start_time) >= player.get_length()/1000.0):
            end_of_song = True

        # If two seconds have elapsed
        if (float(curr_time - start_time) >= 2):
            # Getting another sentiment analysis
            song_sent.append(sentAnalysis.sentAnalysis(5, model))
            # Updating start_time
            start_time = time.time()

        time.sleep(1)
    # To make transition less abrupt
    time.sleep(1)

    # Interpreting song_sent -> success or failure
    c = Counter(song_sent)
    temp = c.most_common(1)[0][0]
    if(temp != 'Angry' or 'Disgust' or 'Fear' or 'Sad'):
        query_dict[last_genre] += 1

    new_mood = temp
    new_genre = np.random.choice(list(query_dict.keys()), 1, p = [x/sum(query_dict.values()) for x in query_dict.values()])[0]
    player = setSong(new_mood + ' ' + new_genre + " music")
    player.play()
    loopyboi(player, new_mood, new_genre)

def opposite_mood(mood:str) -> str:
    if mood == 'Angry':
        return 'Calm'
    elif mood == 'Happy':
        return 'Sad'
    elif mood == 'Sad':
        return 'Happy'
    elif mood == 'Disgust':
        return 'Romantic'
    elif mood == 'Surprise':
        return 'Slow'
    elif mood == 'Fear':
        return 'Happy'
    elif mood == 'Neutral':
        return ''

start_mood = sentAnalysis.sentAnalysis(5, model)
random_genre = np.random.choice(list(query_dict.keys()), 1, p = [x/sum(query_dict.values()) for x in query_dict.values()])[0]
createUI(opposite_mood(start_mood) + ' ' + random_genre + " music")
