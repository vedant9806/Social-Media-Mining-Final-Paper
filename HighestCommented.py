import praw
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

reddit = praw.Reddit(client_id='Juut6aJm8KHXuRjTvCFkhA',
                     client_secret='U3W4hykasRFRA7kvWRk-Y5rnRjrRkQ',
                     username='prez98',
                     password='Vedant98',
                     user_agent='prawpaper2')
def myfunc(e):
    return len(e)

# 4. Connect to a subreddit
subreddit = reddit.subreddit('democrats')
# 5. Getting submissions
submissions = subreddit.search('mask mandate')

submissions.comment_sort = "most"

for submission in submissions:
    print(submission)





