from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import time
import datetime as dt

# set firefox driver
browser = webdriver.Firefox(executable_path=r'/home/duko/dev/youtubeScrapper/geckodriver')

# Dictionary of all teams with their respective URL
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
    "FinCrowds": {"url": "https://www.youtube.com/watch?v=nAqBqpMRK7E"},
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
    "AnyChain": {"url": "youku"},
    "payment.one": {"url": "https://www.youtube.com/watch?v=2KG78PGE1yk"}
}

# ------------------------------------------
def videoStats(browser, url):
    browser.get(url)
    # Team title
    # try:
    #     title = browser.find_element_by_tag_name('h1')
    #     print("Title ", title.text)
    # except TimeoutException:
    #     print("Title NOT found")

    # video likes
    try:
        likes = browser.find_element_by_xpath("//a/yt-formatted-string[@id='text']")
        print("likes A: ", likes.text)
    except TimeoutException:
        print("Likes NOT found")

    return [dt.datetime.today(),"team.name.HERE",likes.text]

def vStats2(browser, teamName, url):
    browser.get(url)
    # video likes
    try:
        likes = browser.find_element_by_xpath("//a/yt-formatted-string[@id='text']")
        print("likes A: ", likes.text)
    except TimeoutException:
        print("Likes NOT found")
    #output
    return [dt.datetime.today(),teamName,likes.text]
    browser.quit()


print("OUTPUT test 1 : ")
print(videoStats(browser, "https://www.youtube.com/watch?time_continue=14&v=hEQAMeaYCr8"))

print("OUTPUT test 2 : ")
for i in teamsDic:
    print(vStats2(browser, teamsDic[str(i)], teamsDic[str(i)]['url']))
    browser.quit()
