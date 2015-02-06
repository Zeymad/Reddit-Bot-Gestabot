#!/usr/bin/python

import time
import praw

user_agent = ("PyYou 0.1")
f = open('workfile.txt', 'w')
r = praw.Reddit(user_agent = user_agent)

r.login('username', 'password')

#the subreddit we search
subreddit = r.get_subreddit("all")
#retrieves the subreddit comments as seen in /test/
subreddit_comments = subreddit.get_comments()
already_done = []
counter=0
SearchWords = ["your a ", "your the ", "your on ", "your at ", "your before ", "your not ", "your an ", "your of ", "your with " ]
##SearchWords = ["your not", "your a", "your the", "your on", "your at", "your before" ]
while True:
    for comment in subreddit_comments:
        for Words in SearchWords:
            if Words in comment.body and comment.id not in already_done:
                comment.reply("Hi, I'm a Bot! It's you're*. FTFY.")
                print(comment)
                lause=str("probleem ise => "+Words+" kommentaar ise =>"+comment.body+"\n")
                print(lause,"123")
                f.write(lause)

            if "your not" in comment.body:
                comment.reply("Hi! I'm a Bot. Not 100% sure but YOUR grammar seems to be wrong. If I'm mistaken downvote this.")
                print(comment)
                lause=str("probleem ise => "+" your not"+" kommentaar ise =>"+comment.body+"\n")
                f.write(lause)
        already_done.append(comment.id)
    time.sleep(10)
    counter=counter+1
    print(counter)
    if counter == 100:
        f.close()
        break
print("done!!!!!222")



##subreddit = r.get_subreddit('dataisbeautiful')
##subreddit_comments = subreddit.get_comments()
####multi_reddits = r.get_subreddit('python+learnpython')
####multi_reddits_comments = multi_reddits.get_comments()
