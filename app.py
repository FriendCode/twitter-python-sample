import os
from flask import Flask

from tweepy import (API, OAuthHandler, Friendship, Cursor,
                    MemoryCache, FileCache)

app = Flask(__name__)
app.run(debug=True)

###### Define your Twitter application settings here #######
oauth_consumer_key = None
oauth_consumer_secret = None
oauth_token = None
oauth_token_secret = None
######

if (oauth_consumer_key is None
or oauth_consumer_secret is None
or oauth_token_secret is None
or oauth_token is None):
    raise Exception("Define your application settings in app.py")


auth = OAuthHandler(oauth_consumer_key, oauth_consumer_secret)
auth.set_access_token(oauth_token, oauth_token_secret)

api = API(auth)


@app.route('/')
def timeline(user="FriendCodeIDE"):
    timeline = api.user_timeline(user)
    content = "Timeline of <b>"+user+"</b><br/>\n<br/>\n"
    for status in timeline:
        content = content + status.text + "\n<br/><br/>\n" 
    return content

@app.route('/user/<user_id>')
def show_user(user_id):
    return timeline(user_id)

@app.route('/tweet/<tweet_id>')
def show_tweet(tweet_id):
    status = api.get_status(id=tweet_id)
    return status.text

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)