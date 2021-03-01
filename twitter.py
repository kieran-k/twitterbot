import tweepy
import time
import re
# import auth code files 
import authcode

# create seperate python file to hold authenitcation (example authcode.py) 

# authcode.py contains codes for authentication :

## auth.set_access_token( ** Codes go here **)

## api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

## id = *Twitter account code here*

# end authcode.py 

file = open("twitcount.txt", "r")
prev_count_str = (file.read())



user = api.get_user(id)

prev_fav_count = (int(prev_count_str))
file.close

fav = api.favorites(user) 

fav_count = user.favourites_count

calc = fav_count - prev_fav_count
print(calc)

for tweet in tweepy.Cursor(api.favorites, id=872727322138365953).items(calc): 
    try: 
        tweet.retweet()
        print("retweeted")
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break



prev_fav_count = fav_count

file = open("twitcount.txt", "r")
fav_count = (str(fav_count))
file = open("twitcount.txt", "w")
file.write(fav_count)
file = open("twitcount.txt", "r")
prev_count_str = (file.read())
prev_fav_count = (int(prev_count_str))


