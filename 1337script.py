import tweepy
import time
import webbrowser
from plyer import notification

# Twitter API credentials
API_KEY = ''
API_SECRET_KEY = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Twitter username to monitor
twitter_username = '1337FIL'
keywords_to_search = ['check-in', 'Check-In', 'Check-IN', 'CHECK-IN']

# URL of the check-in page
CHECKIN_URL = "https://admission.1337.ma/candidature/check-in"


def check_for_tweets():
    """Check for recent tweets mentioning check-in."""
    try:
        tweets = api.user_timeline(screen_name=twitter_username, count=5, tweet_mode='extended')

        for tweet in tweets:
            if any(keyword.lower() in tweet.full_text.lower() for keyword in keywords_to_search):
                print(f"🔔 Found tweet: {tweet.full_text}")
                send_notification(tweet.full_text)

                # Open the check-in website automatically
                print("Opening check-in page...")
                webbrowser.open(CHECKIN_URL)

                return  # Stop checking after finding the tweet

        print("No new check-in tweets found.")

    except Exception as error:
        print(f"❌ Error: {error}")


def send_notification(message):
    """Send a desktop notification."""
    print("📢 Sending notification...")
    notification.notify(
        title="1337 Check-In Alert",
        message=message,
        timeout=10
    )


try:
    print("🚀 Script started! Press Ctrl+C to stop.")
    while True:
        check_for_tweets()
        time.sleep(300)  # Check every 5 minutes
except KeyboardInterrupt:
    print("❌ Script stopped by the user.")
