import tweepy
import time
from plyer import notification

API_KEY = 'your_api_key'
API_SECRET_KEY = 'your_api_secret_key'
ACCESS_TOKEN = 'your_access_token'
ACCESS_TOKEN_SECRET = 'your_access_token_secret'

auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

TWITTER_USERNAME = '1337_username'
KEYWORD = 'check-in'

def check_for_tweets():
    try:
        tweets = api.user_timeline(screen_name=TWITTER_USERNAME, count=5, tweet_mode='extended')
        for tweet in tweets:
            if KEYWORD.lower() in tweet.full_text.lower():
                print(f"Found tweet: {tweet.full_text}")
                notify_user(tweet.full_text)
                return
        print("No new check-in tweets found.")
    except Exception as e:
        print(f"Error: {e}")

def notify_user(message):
    print("Sending notification...")
    notification.notify(
        title="1337 Check-In Alert",
        message=message,
        timeout=10
    )

while True:
    check_for_tweets()
    time.sleep(300)
