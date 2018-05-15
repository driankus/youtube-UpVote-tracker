from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import urllib
import datetime as dt
#import pandas as pd

# All teams in a dic
teamsDic = {
    "TelEOS": {"url": "https://www.youtube.com/watch?v=TSo13vorP8g"},
    "YouRoot.io": {"url": "https://www.youtube.com/watch?v=fJJneJJgzwo"},
    "Team Decentralize": {"url": "https://www.youtube.com/watch?v=-Mtxx3IEZLc"},
    "CADChain": {"url": "https://www.youtube.com/watch?v=_aizBkuaXLM"},
    "Way": {"url": "https://www.youtube.com/watch?v=65X7dlDjB3s"},
    "Armada": {"url": "https://www.youtube.com/watch?v=enTh04mX5FQ"},
    "CollectiveHealth": {"url": "https://www.youtube.com/watch?v=itZ4blsBIDU"},
    "DAO Axis": {"url": "https://www.youtube.com/watch?v=-Mtxx3IEZLc"},
    "This Coin Rocks": {"url": "https://www.youtube.com/watch?v=ZR1DdBL8QDE"},
    "EOS-AGE-Project-DNA": {"url": "https://www.youtube.com/watch?v=ZFouTSVoeAQ"},
    "FinCrowds": {"url": "https://youtu.be/IVIGjQkl0NQ"},
    "VIM": {"url": "https://www.youtube.com/watch?v=enTh04mX5FQ"},
    "Undra.io": {"url": "https://www.youtube.com/watch?v=cyL6khy7ipI"},
    "codum": {"url": "https://www.youtube.com/watch?v=sdtqOXH5svg"},
    "iRespo.com": {"url": "https://www.youtube.com/watch?v=NcZZgCa809U"},
    "FairAccess": {"url": "https://www.youtube.com/watch?v=1M_JPKkHhK4"},
    "Delegator": {"url": "https://www.youtube.com/watch?v=cyL6khy7ipI"},
    "DelegationOne": {"url": "https://www.youtube.com/watch?v=8tXweZ9Y1qI"},
    "Magni": {"url": "https://www.youtube.com/watch?v=HcjWpD2Eteg"},
    "Query:": {"url": "https://www.youtube.com/watch?v=HcjWpD2Eteg"},
    "Binary": {"url": "https://www.youtube.com/watch?v=itZ4blsBIDU"},
    "SE5 Focus": {"url": "https://www.youtube.com/watch?v=nAqBqpMRK7E"},
    "Ownit": {"url": "https://www.youtube.com/watch?v=ir6VlVnG8SI"},
    "LoRaChain": {"url": "https://www.youtube.com/watch?v=p0QRzNIKgBs"},
    "Screen Time": {"url": "https://www.youtube.com/watch?v=ZUEhi2LsFCs"},
    "EOSomnia": {"url": "https://www.youtube.com/watch?v=8tXweZ9Y1qI"},
    "Streamer.IO": {"url": "https://www.youtube.com/watch?v=nmZZzxQsIwU"},
    #"AnyChain": {"url": "youku"},
    "payment.one": {"url": "https://www.youtube.com/watch?v=2KG78PGE1yk"}
}


#Define functions:
def getLikes(url):
    # gets a single youtube-url, returns N of likes
    try:
        # load website & parse with bs4
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')
    except URLError as e:
        print(e)

        # get likes (unclicked)
    try:
        likes = soup.find_all('button', class_='like-button-renderer-like-button-unclicked')
        return likes[0].text  # TODO: transform to int (int(likes[0].text) )
    except HTTPError as e:
        print(e)
        return '0'

def keepTally(teams):
    output = {}
    for tm in teams:
        # getLikes for team (tm) and add result to new key "likes"
        output[tm] = getLikes(teams[tm]['url'])
        print(tm, output[tm])
    return output


# Run Tally
timeRun = dt.datetime.now().strftime("%Hhr%M")
output = keepTally(teamsDic)


# Save results to text
outputFileName = 'Run_'+timeRun+'.txt'  #filename
with open(outputFileName, "w") as text_file:
    text_file.write(str(output))

#TODO: convert to df and save as csv
# tally.to_csv(outputFileName, sep='\t', encoding='utf-8'))