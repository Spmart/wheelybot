from twython import Twython
from auth import (
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ACCESS_TOKEN,
    ACCESS_TOKEN_SECRET
)
import schedule
import time


emoji = {
    "O": u'\U0000267F',
    "o": u'\U0000267F',
    "О": u'\U0000267F',
    "о": u'\U0000267F',
    "J": u'\U0001F3D1',
    "j": u'\U0001F3D1'
}


def get_tweet():
    with open("tweets.txt", "r") as file:
        tweets = file.readlines()
    tweet = tweets.pop()
    with open("tweets.txt", "w") as file:
        file.writelines(tweets)
    return tweet


def insert_emoji(tweet):
    for key in emoji:
        if key in tweet:
            tweet = tweet.replace(key, emoji.get(key))
    return tweet


def send_tweet(tweet):
    twitter.update_status(status=tweet)


def job():
    send_tweet(insert_emoji(get_tweet()))  # oh, shi~


if __name__ == "__main__":
    twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    schedule.every(300).minutes.do(job)

    while 1:
        schedule.run_pending()
        time.sleep(30)
