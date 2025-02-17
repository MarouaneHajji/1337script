import tweepy 
import time 
from plyer import notification

API_KEY = ''
API_SECRET_KEY = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

authentification = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
authentification.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(authentification)

twitter_username = '1337FIL'
keywords_to_search = ['check-in', 'Check-In', 'Check-IN', 'CHECK-IN']

def check_for_tweets():
    try:
        tweets = api.user_timeline(screen_name=twitter_username, count=5, tweet_mode='extended')
        
        for tweet in tweets:
            if any(keyword.lower() in tweet.full_text.lower() for keyword in keywords_to_search):
                print(f"Found tweet: {tweet.full_text}")
                send_notification(tweet.full_text)
                return

        print("No new check-in tweets found.")
    
    except Exception as error:
        print(f"Error: {error}")

def send_notification(message):
    print("Sending notification _ _ _")
    notification.notify(
        title="1337 Check-In Alert",
        message=message,
        timeout=10
    )

try:
    print("Starting the script. Press Ctrl+C to stop :)")
    while True:
        check_for_tweets() 
        time.sleep(300)   
except KeyboardInterrupt:
    print("Script stopped by the user :(")
