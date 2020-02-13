# %%
from TwitterClient import TwitterClient
import os


def main():
    api = TwitterClient()
    tweets = api.get_tweets(query='Donald Trump', count=2000)

    positive_tweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']

    print(f'Postive tweets percentage: {len(positive_tweets) * 100 / len(tweets)}')

    negative_tweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']

    print(f'Negative tweets percentage: {len(negative_tweets) * 100 / len(tweets)}')

    for tweet in positive_tweets:
        print(os.linesep)
        print(tweet)


if __name__ == '__main__':
    main()
