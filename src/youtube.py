from youtube_api import YouTubeDataAPI
import json
import random

# def search(searchQuery: str) -> list:
#     api_key = json.load(open("../data/api.json"))["apiKey"]
#     yt = YouTubeDataAPI(api_key)
#
#     searches = yt.search(q=searchQuery)
#     return searches


# Function to retrieve video_id and generate a URL with it to return
def getURL(searchQuery: str, searchResults:int = 1) -> str:
    api_key = json.load(open("../data/api.json"))["apiKey"]
    yt = YouTubeDataAPI(api_key)

    searches = yt.search(q=searchQuery, max_results=searchResults, video_duration="short")
    rNum = random.randint(0,searchResults-1)
    # returns [url to video, video title, url to thumbnail]
    return ["https://www.youtube.com/watch?v=" + searches[rNum]["video_id"],
    searches[rNum]["video_title"], searches[rNum]["video_thumbnail"]]
