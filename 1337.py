import tweepy
import time
from plyer import notification

API_KEY = 'LGlGh3ORzXADKBrI02MsKC6Tz'
API_SECRET_KEY = 'GgsVmaRVyBoAlaZGWaKosLZbmRGFDunXdHxxsfUlqIVjHYsPqa'
ACCESS_TOKEN = '1874529763806543872-BDYehAjLumQd68bzxeZtVXCRbDIBkG'
ACCESS_TOKEN_SECRET = 'HHpx37aoTDf2jbL9Wp9GhM51S3BzQ2LoRTuC244XRKLOX'

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

TWITTER_USERNAME = '1337FIL'
KEYWORDS = ['check-in', 'Check-In', 'Check-IN', 'CHECK-IN']

def check_for_tweets():
    try:
        tweets = api.user_timeline(screen_name=TWITTER_USERNAME, count=5, tweet_mode='extended')
        for tweet in tweets:
            if any(keyword.lower() in tweet.full_text.lower() for keyword in KEYWORDS):
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

try:
    while True:
        check_for_tweets()
        time.sleep(300) 
except KeyboardInterrupt:
    print("Exiting script.")
