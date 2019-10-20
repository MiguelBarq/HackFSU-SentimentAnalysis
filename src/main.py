import numpy as np
import youtube
import ui
import vidinput
# import sentAnalysis

query_dict = {
    'rock' : 1,
    'instrumental' : 1,
    'pop' : 1,
    'jazz' : 1,
    'edm' : 1,
    'alternative' : 1
}

# General Logic Path:
#   1. Open UI and generate elements
#   2. Start sentiment analysis and analyze the webcam
#   3. Pull a song from Youtube and play it based on user mood
#   4. When song ends, analyze effectiveness of song and adjust probability table
#   5. Fetch new song for user to neutralize mood
#   6. Repeat.

# General Logic Path, but BETTER:
#   1. Open UI and generate elements
#   2. Run sentiment analysis, record it.
#   3. Play song depending on analysis
#   4. Throughout the song, occasionally run sentiment analysis, constructing a list of emotions 
#   5. At the end of the song, determine if mood improved overall over the course of the song
#       a) Determine which emotions are "bad", put them in a list
#       b) Determine if, towards end of sentiment analysis list, if mood improved
#           i) If it got WORSE, maybe set the dict value to one less, or 0 if at 0 (so no negatives)?
#   6. If it improved, add one to the dict value. If it didn't, do nothing
#   7. Go back to 3

def main():
    # Sentiment Analysis
    mood = 'happy'# <TODO: sentAnalysis call (note: needs to return a string)    

    # Create UI
    ui.createUI(mood + ' ' + np.random.choice(list(query_dict.keys()), 1, p = [x/sum(query_dict.values()) for x in query_dict.values()])[0])

main()