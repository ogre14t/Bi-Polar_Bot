<<<<<<< HEAD
import praw
import pandas as pan
import pdb
import re
import os

# Create an instance of reddit and log in
reddit = praw.Reddit('bot')
# Create a list of subreddits
subs = ["politics", "liberal", "republican"]
# Create a counter
hate_count = 0
love_count = 0
trump = 0
aoc = 0
pelosi = 0
for sub in subs:
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=500):
        if ("hate" in submission.title.lower()):
            hate_count += 1
        elif ("love" in submission.title.lower()):
            love_count += 1
        elif("trump" in submission.title.lower()):
            trump += 1
        elif("aoc" in submission.title.lower()):
            aoc += 1
        elif("pelosi" in submission.title.lower()):
            pelosi += 1


print("Hate: ", hate_count)
print("Love: ", love_count)
print("Trump: ", trump)
print("AOC: ", aoc)
print("Pelosi: ", pelosi)
=======
import praw
import pandas as pan
import pdb
import re
import os

# Create an instance of reddit and log in
reddit = praw.Reddit('bot')
# Create a list of subreddits
subs = ["politics", "liberal", "republican"]
# Create a counter
hate_count = 0
love_count = 0
trump = 0
aoc = 0
pelosi = 0
for sub in subs:
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=500):
        if ("hate" in submission.title.lower()):
            hate_count += 1
        elif ("love" in submission.title.lower()):
            love_count += 1
        elif("trump" in submission.title.lower()):
            trump += 1
        elif("aoc" in submission.title.lower()):
            aoc += 1
        elif("pelosi" in submission.title.lower()):
            pelosi += 1


print("Hate: ", hate_count)
print("Love: ", love_count)
print("Trump: ", trump)
print("AOC: ", aoc)
print("Pelosi: ", pelosi)
>>>>>>> 6799b698a486ebd4f0761a4403c4b8071847002a
