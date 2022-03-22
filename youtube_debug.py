import config
import sys
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

DevKey = config.API_KEY
youtubeAPIServiceName = "youtube"
youtubeAPIVersion = "v3"


def youtubeSearch(queryTerm, max_results, page_token=None):
    youtube = build(youtubeAPIServiceName, youtubeAPIVersion, developerKey=DevKey)

    searchResponce = youtube.search().list(
        q=queryTerm,
        part= "id,snippet",
        maxResults=max_results,
    ).execute()

    return searchResponce

if __name__ == "__main__":
    queryTerm =sys.argv[1]
    max_results = sys.argv[2]
    try:
        response = youtubeSearch(queryTerm, max_results)
        print(response)
    except HttpError as e:
            print("An Http error %d occured: /n%s" % (type(e).__name__, str(e)))


