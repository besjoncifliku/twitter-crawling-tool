# Twitter Crawling Tool

Twitter Crawling is a tool that utilizes Twitter API to get tweets based on keywords searches

----

You need to set some environemntal variable from twitter API developer portal. Note that as Twitter is migrated to 'X' the API might not work as expected.

```
    consumer_key = os.environ.get('TWITTER_CONSUMER_KEY')
    consumer_secret = os.environ.get('TWITTER_SECRET_KEY')
    access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
    access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')
```

Specify number of tweets and the date you want to collect in the method properties:

`collect_twitter_data(key_words, date_since="2022-1-16", limit=1000):`

At the moment we collect tweets that are considered hate speech based on keyword mathcing for 3 main topics LGBTQ+, Donald Trum and Covid-19. If you need to extend these topics add more keywords to the configurations. You can also specify your own keywords in the configs.

Run the main script using python.


## Hydration Process:

The `/hydrate` scripts maps twitter with specific user IDs. This creates some kind of anonymization safely handling only Tweets content. If needed for the purpose of user mapping you can use the hydration script in the respective directory. 

This script will walk through the tweet id file and hydrate with twarc. The line oriented JSON files will be placed right next to the tweet id file.

Note: you will need to install twarc, tqdm, and run twarc configure from the command line to tell it your Twitter API keys.


## Further Notes: 

For more details please check:

- Reference: Developer Account Twitter: https://developer.twitter.com/en
- Documentation Twitter API v2: https://developer.twitter.com/en/docs
- Documentation Tweepy: https://www.tweepy.org/
- Reference Hydration: https://github.com/sjgiorgi/blm_twitter_corpus/blob/master/hydrate.py

## Sample Result:

You can find some samples in `/collected-tweets`

Here are a few (marked with * due to unappropriate language):

```
index,tweets,username,location
0,my classmates (? idk what the f**k to call the ppl i major w) are so weird because theyre antiva*x but theyre also anti capitalist? but hom*ph*bic?,y*nibinnie,🇭🇺 🏳️‍🌈 ✡️ 18 white
1,@ecoengr @LilyYily It also gives antivax people the ability to order a bunch and do dumb sh**t like making TikToks of them burning their tests or some other dumb sh*t.,BongHead_420,FRISCO
```
