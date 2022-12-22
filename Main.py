#karmaGainer 1.0 by amirparsab90-maker

#made for MISSION TRP-RAID

#you can use it fot yourself but sharing it without

#giving credits to me is ELIGAL

#pip install praw

import praw

import time

#https://reddit.com/prefs/apps/

#make sure its a script app

redditAccount = praw.Reddit(

                             client_id="",

                             client_secret="",

                             password="",

                             user_agent="qwert 0.0 by u/null",

                             username="")

karmaForKarmaSubs = ["karmaforkarma", "freeKarma4You", "karma4free", "getkarma_here", "karmafarming4pros", "EarnFreeKarma"]

MODE = 0

#0 : once

#1 : repeat

#repeat mode options

repeatPost = 30

breakSeconds = 120

#post options

postTitle = "I Need Karma So Badly"

postBody = "Please Upvote My post\n\n(1.0)"

isNSFW = False

isSpoiler = False

if MODE == 1:

    print("MODE 1")

    for i in range(repeatPost):

        for i in karmaForKarmaSubs:

            print("posting in r/" + i)

            try:

                redditAccount.subreddit(i).subscribe()

            except:

                continue

            redditAccount.subreddit(i).submit(postTitle, selftext=postBody,nsfw=isNSFW,spoiler=isSpoiler)

        print("round done. taking break")

        time.sleep(breakSeconds)

if MODE == 0:

    print("MODE 0")

    for i in karmaForKarmaSubs:

        print("posting in r/" + i)

        try:

            redditAccount.subreddit(i).subscribe()

        except:

            continue

        redditAccount.subreddit(i).submit(postTitle, selftext=postBody,nsfw=isNSFW,spoiler=isSpoiler)

print("done!")         
