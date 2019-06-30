# Import requests (to download the page)
import requests

# Import BeautifulSoup (to parse what we download)
from bs4 import BeautifulSoup

# Import Time (to add a delay between the times the scape runs)
import time

import pdb 

async def main(reddit_comment_insert): 
    url = "https://www.reddit.com/user/muppetiers/comments/"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        # download the homepage
    response = requests.get(url, headers=headers)
        # parse the downloaded homepage and grab all text, then,

    soup = BeautifulSoup(response.text, "lxml")

    reddit_comment = soup.find('div', {"class": "s1p8ey0o-0 WffKZ"}).getText()
    print (reddit_comment)

    while True:
        # set the url as VentureBeat,
        url = "https://www.reddit.com/user/muppetiers/comments/"
        # set the headers like we are a browser,
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        # download the homepage
        response = requests.get(url, headers=headers)
        # parse the downloaded homepage and grab all text, then,
        soup = BeautifulSoup(response.text, "lxml")
        
        new_reddit_comment = soup.find('div', {"class": "s1p8ey0o-0 WffKZ"}).getText()
        # if the number of times the word "Google" occurs on the page is less than 1,
        reddit_comment_insert = new_reddit_comment
        print ("reddit_comment: ", reddit_comment)
        print ("reddit_comment_insert2: ", reddit_comment_insert)
        # breakpoint()
        # await sio.emit('message', reddit_comment)
        print ("new_reddit_comment: ", new_reddit_comment)
        if reddit_comment == new_reddit_comment:
            # wait 60 seconds,
            # time.sleep(100)
            # continue with the script,
            break
            
        # but if the word "Google" occurs any other number of times,
        else:
            print ("new_reddit_comment: ", new_reddit_comment)
            
            continue