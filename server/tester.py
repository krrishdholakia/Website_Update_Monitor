from aiohttp import web
import socketio
import server
import requests

# Import BeautifulSoup (to parse what we download)
from bs4 import BeautifulSoup

from datetime import datetime, timedelta

# creates a new Async Socket IO Server
sio = socketio.AsyncServer()
# Creates a new Aiohttp Web Application
app = web.Application()
# Binds our Socket.IO server to our Web App
# instance
sio.attach(app)


# we can define aiohttp endpoints just as we normally
# would with no change
async def index(request):
    with open('testhtml.html') as f:
        return web.Response(text=f.read(), content_type='text/html')

# If we wanted to create a new websocket endpoint,
# use this decorator, passing in the name of the
# event we wish to listen out for
url = "https://www.reddit.com/user/muppetiers/comments/"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        # download the homepage
def tempfunc(): 

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "lxml")
    reddit_comment = soup.find('div', {"class": "_a5_x7qimk18YbGSwE8Fy"}).getText()
    print ("reddit_Comment: ", reddit_comment)
    return reddit_comment

@sio.on('message')
async def print_message(sid, message):
    print("Socket ID: " , sid)
    print(message)
    # await a successful emit of our reversed message
    # back to the client
    old_comment = tempfunc()
    endtime = datetime.now() + timedelta(minutes=1)
    while datetime.now() < endtime: 
        # print ("start ************************")
        # print ("reddit_comment_pre_insert: ", reddit_comment_insert)
        # await server.main(reddit_comment_insert)
        # print("hello hello ************************")
        # print ("reddit_comment_post_insert: ", reddit_comment_insert)
        new_comment = tempfunc()
        returnStr = ""
        print("old_comment: {}".format(old_comment))
        if old_comment == new_comment :
            returnStr = "nothing has changed"
        else: 
            returnStr = new_comment
            old_comment = new_comment
        await sio.emit('message', returnStr)
        # time.sleep(1)
    print("we done now ***************")

# We bind our aiohttp endpoint to our app
# router
app.router.add_get('/', index)

# We kick off our server
if __name__ == '__main__':
    web.run_app(app)

