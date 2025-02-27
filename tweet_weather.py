import requests
import tweepy
import os
import logging

# Configure logging
logging.basicConfig(filename='weather_tweet.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def get_paris_temperature():
    api_key = os.getenv("API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?q=Paris,FR&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        logging.info(f"Successfully retrieved temperature: {temperature}°C")
        tweet_temperature(temperature)
    else:
        logging.error(f"Failed to retrieve data: {response.status_code} {response.text}")

def tweet_temperature(temperature):
    try:
        # Retrieve Twitter API credentials from environment variables
        consumer_key = os.getenv("TWITTER_CONSUMER_KEY")
        consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET")
        access_token = os.getenv("TWITTER_ACCESS_TOKEN")
        access_token_secret = os.getenv("TWITTER_ACCESS_SECRET")

        # Authenticate with Twitter
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)

        # Create the tweet
        tweet = f"Current temperature in Paris: {temperature}°C #WeatherUpdate"
        
        # Post the tweet
        client = tweepy.Client(consumer_key=consumer_key,consumer_secret=consumer_secret,access_token=access_token,access_token_secret=access_token_secret)
        client.create_tweet(text=tweet)
    except Exception as e:
        logging.error(f"Error tweeting: {e}")

tweet_temperature("30")



