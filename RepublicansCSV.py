import praw
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from empath import Empath
import pandas as pd
import datetime

reddit = praw.Reddit(client_id='Juut6aJm8KHXuRjTvCFkhA',
                     client_secret='U3W4hykasRFRA7kvWRk-Y5rnRjrRkQ',
                     username='prez98',
                     password='Vedant98',
                     user_agent='prawpaper2')

# Body Acceptance Code
#
# submission = reddit.submission(id='lwef9p')
# print("ID: ", submission.id)
# print("Name: ", submission.name)
# print("Title: ", submission.title)
# print("Upvote Ratio: ", submission.upvote_ratio)
# print("Num of Comments: ", submission.num_comments)
#
# lexicon = Empath()
# analyser = SentimentIntensityAnalyzer()
# submission.comments.replace_more(limit=30)
# comments = submission.comments
# limit = 500
# index = 0
# df = pd.DataFrame([], columns=['ParentID', 'CommentID', 'Comment Body', 'Upvotes', 'Comment Char Length',
#                                'Comment Time', 'Empath Positive', 'Empath Negative'])
#
# for comment in comments:
#     sentiment_dict = analyser.polarity_scores(comment.body)
#     empath_pos =  lexicon.analyze(comment.body, categories=["positive_emotion"], normalize=True)
#     empath_neg = lexicon.analyze(comment.body, categories=["negative_emotion"], normalize=True)
#     comment_time = datetime.datetime.fromtimestamp(comment.created_utc)
#     df = df.append({
#             'ParentID': comment.parent(),
#             'CommentID': comment.id,
#             'Comment Body': comment.body.encode("utf-8"),
#             'Upvotes': comment.ups,
#             'Comment Char Length' : len(comment.body.encode("utf-8")),
#             'Comment Time': comment_time,
#             'VADER Pos': sentiment_dict['pos'],
#             'VADER Neg' :  sentiment_dict['neg'],
#             'VADER Neutral' : sentiment_dict['neu'],
#             'VADER Comp': sentiment_dict['compound'],
#             'Empath Positive' : empath_pos['positive_emotion'],
#             'Empath Negative' : empath_neg['negative_emotion']
#         }, ignore_index=True)
#     df.to_excel("output50.xlsx")
#
# submission = reddit.submission(id='k1ekxn')
# print("ID: ", submission.id)
# print("Name: ", submission.name)
# print("Title: ", submission.title)
# print("Upvote Ratio: ", submission.upvote_ratio)
# print("Num of Comments: ", submission.num_comments)
#
# lexicon = Empath()
# analyser = SentimentIntensityAnalyzer()
# submission.comments.replace_more(limit=30)
# comments = submission.comments.list()
# limit = 100
# index = 0
# df = pd.DataFrame([], columns=['ParentID', 'CommentID', 'Comment Body', 'Upvotes', 'Comment Char Length',
#                                'Comment Time', 'Empath Positive', 'Empath Negative'])
#
# for comment in comments:
#     sentiment_dict = analyser.polarity_scores(comment.body)
#     empath_pos = lexicon.analyze(comment.body, categories=["positive_emotion"], normalize=True)
#     empath_neg = lexicon.analyze(comment.body, categories=["negative_emotion"], normalize=True)
#     comment_time = datetime.datetime.fromtimestamp(comment.created_utc)
#     df = df.append({
#         'ParentID': comment.parent(),
#         'CommentID': comment.id,
#         'Comment Body': comment.body.encode("utf-8"),
#         'Upvotes': comment.ups,
#         'Comment Char Length': len(comment.body.encode("utf-8")),
#         'Comment Time': comment_time,
#         'VADER Pos': sentiment_dict['pos'],
#         'VADER Neg': sentiment_dict['neg'],
#         'VADER Neutral': sentiment_dict['neu'],
#         'VADER Comp': sentiment_dict['compound'],
#         'Empath Positive': empath_pos['positive_emotion'],
#         'Empath Negative': empath_neg['negative_emotion']
#     }, ignore_index=True)
#     df.to_excel("output51.xlsx")
#
# submission = reddit.submission(id='lwe928')
# print("ID: ", submission.id)
# print("Name: ", submission.name)
# print("Title: ", submission.title)
# print("Upvote Ratio: ", submission.upvote_ratio)
# print("Num of Comments: ", submission.num_comments)
#
# lexicon = Empath()
# analyser = SentimentIntensityAnalyzer()
# submission.comments.replace_more(limit=30)
# comments = submission.comments.list()
# limit = 100
# index = 0
# df = pd.DataFrame([], columns=['ParentID', 'CommentID', 'Comment Body', 'Upvotes', 'Comment Char Length',
#                                'Comment Time', 'Empath Positive', 'Empath Negative'])
#
# for comment in comments:
#     sentiment_dict = analyser.polarity_scores(comment.body)
#     empath_pos = lexicon.analyze(comment.body, categories=["positive_emotion"], normalize=True)
#     empath_neg = lexicon.analyze(comment.body, categories=["negative_emotion"], normalize=True)
#     comment_time = datetime.datetime.fromtimestamp(comment.created_utc)
#     df = df.append({
#         'ParentID': comment.parent(),
#         'CommentID': comment.id,
#         'Comment Body': comment.body.encode("utf-8"),
#         'Upvotes': comment.ups,
#         'Comment Char Length': len(comment.body.encode("utf-8")),
#         'Comment Time': comment_time,
#         'VADER Pos': sentiment_dict['pos'],
#         'VADER Neg': sentiment_dict['neg'],
#         'VADER Neutral': sentiment_dict['neu'],
#         'VADER Comp': sentiment_dict['compound'],
#         'Empath Positive': empath_pos['positive_emotion'],
#         'Empath Negative': empath_neg['negative_emotion']
#     }, ignore_index=True)
#     df.to_excel("output52.xlsx")
#
# submission = reddit.submission(id='msv775')
# print("ID: ", submission.id)
# print("Name: ", submission.name)
# print("Title: ", submission.title)
# print("Upvote Ratio: ", submission.upvote_ratio)
# print("Num of Comments: ", submission.num_comments)
#
# lexicon = Empath()
# analyser = SentimentIntensityAnalyzer()
# submission.comments.replace_more(limit=30)
# comments = submission.comments.list()
# limit = 100
# index = 0
# df = pd.DataFrame([], columns=['ParentID', 'CommentID', 'Comment Body', 'Upvotes', 'Comment Char Length',
#                                'Comment Time', 'Empath Positive', 'Empath Negative'])
#
#
# for comment in comments:
#     sentiment_dict = analyser.polarity_scores(comment.body)
#     empath_pos = lexicon.analyze(comment.body, categories=["positive_emotion"], normalize=True)
#     empath_neg = lexicon.analyze(comment.body, categories=["negative_emotion"], normalize=True)
#     comment_time = datetime.datetime.fromtimestamp(comment.created_utc)
#     df = df.append({
#         'ParentID': comment.parent(),
#         'CommentID': comment.id,
#         'Comment Body': comment.body.encode("utf-8"),
#         'Upvotes': comment.ups,
#         'Comment Char Length': len(comment.body.encode("utf-8")),
#         'Comment Time': comment_time,
#         'VADER Pos': sentiment_dict['pos'],
#         'VADER Neg': sentiment_dict['neg'],
#         'VADER Neutral': sentiment_dict['neu'],
#         'VADER Comp': sentiment_dict['compound'],
#         'Empath Positive': empath_pos['positive_emotion'],
#         'Empath Negative': empath_neg['negative_emotion']
#     }, ignore_index=True)
#     df.to_excel("output53.xlsx")
#
# submission = reddit.submission(id='p477ej')
# print("ID: ", submission.id)
# print("Name: ", submission.name)
# print("Title: ", submission.title)
# print("Upvote Ratio: ", submission.upvote_ratio)
# print("Num of Comments: ", submission.num_comments)
#
# lexicon = Empath()
# analyser = SentimentIntensityAnalyzer()
# submission.comments.replace_more(limit=30)
# comments = submission.comments.list()
# limit = 100
# index = 0
# df = pd.DataFrame([], columns=['ParentID', 'CommentID', 'Comment Body', 'Upvotes', 'Comment Char Length',
#                                'Comment Time', 'Empath Positive', 'Empath Negative'])
# for comment in comments:
#     sentiment_dict = analyser.polarity_scores(comment.body)
#     empath_pos = lexicon.analyze(comment.body, categories=["positive_emotion"], normalize=True)
#     empath_neg = lexicon.analyze(comment.body, categories=["negative_emotion"], normalize=True)
#     comment_time = datetime.datetime.fromtimestamp(comment.created_utc)
#     df = df.append({
#         'ParentID': comment.parent(),
#         'CommentID': comment.id,
#         'Comment Body': comment.body.encode("utf-8"),
#         'Upvotes': comment.ups,
#         'Comment Char Length': len(comment.body.encode("utf-8")),
#         'Comment Time': comment_time,
#         'VADER Pos': sentiment_dict['pos'],
#         'VADER Neg': sentiment_dict['neg'],
#         'VADER Neutral': sentiment_dict['neu'],
#         'VADER Comp': sentiment_dict['compound'],
#         'Empath Positive': empath_pos['positive_emotion'],
#         'Empath Negative': empath_neg['negative_emotion']
#     }, ignore_index=True)
#     df.to_excel("output55.xlsx")
#
submission = reddit.submission(id='lwctlu')
print("ID: ", submission.id)
print("Name: ", submission.name)
print("Title: ", submission.title)
print("Upvote Ratio: ", submission.upvote_ratio)
print("Num of Comments: ", submission.num_comments)

lexicon = Empath()
analyser = SentimentIntensityAnalyzer()
submission.comments.replace_more(limit=30)
comments = submission.comments.list()
limit = 100
index = 0
df = pd.DataFrame([], columns=['ParentID', 'CommentID', 'Comment Body', 'Upvotes', 'Comment Char Length',
                               'Comment Time', 'Empath Positive', 'Empath Negative'])

for comment in comments:
    sentiment_dict = analyser.polarity_scores(comment.body)
    empath_pos = lexicon.analyze(comment.body, categories=["positive_emotion"], normalize=True)
    empath_neg = lexicon.analyze(comment.body, categories=["negative_emotion"], normalize=True)
    comment_time = datetime.datetime.fromtimestamp(comment.created_utc)
    df = df.append({
        'ParentID': comment.parent(),
        'CommentID': comment.id,
        'Comment Body': comment.body.encode("utf-8"),
        'Upvotes': comment.ups,
        'Comment Char Length': len(comment.body.encode("utf-8")),
        'Comment Time': comment_time,
        'VADER Pos': sentiment_dict['pos'],
        'VADER Neg': sentiment_dict['neg'],
        'VADER Neutral': sentiment_dict['neu'],
        'VADER Comp': sentiment_dict['compound'],
        'Empath Positive': empath_pos['positive_emotion'],
        'Empath Negative': empath_neg['negative_emotion']
    }, ignore_index=True)
    df.to_excel("outputNewR1.xlsx")

submission = reddit.submission(id='lkbdql')
print("ID: ", submission.id)
print("Name: ", submission.name)
print("Title: ", submission.title)
print("Upvote Ratio: ", submission.upvote_ratio)
print("Num of Comments: ", submission.num_comments)

lexicon = Empath()
analyser = SentimentIntensityAnalyzer()
submission.comments.replace_more(limit=30)
comments = submission.comments.list()
limit = 100
index = 0
df = pd.DataFrame([], columns=['ParentID', 'CommentID', 'Comment Body', 'Upvotes', 'Comment Char Length',
                               'Comment Time', 'Empath Positive', 'Empath Negative'])

for comment in comments:
    sentiment_dict = analyser.polarity_scores(comment.body)
    empath_pos = lexicon.analyze(comment.body, categories=["positive_emotion"], normalize=True)
    empath_neg = lexicon.analyze(comment.body, categories=["negative_emotion"], normalize=True)
    comment_time = datetime.datetime.fromtimestamp(comment.created_utc)
    df = df.append({
        'ParentID': comment.parent(),
        'CommentID': comment.id,
        'Comment Body': comment.body.encode("utf-8"),
        'Upvotes': comment.ups,
        'Comment Char Length': len(comment.body.encode("utf-8")),
        'Comment Time': comment_time,
        'VADER Pos': sentiment_dict['pos'],
        'VADER Neg': sentiment_dict['neg'],
        'VADER Neutral': sentiment_dict['neu'],
        'VADER Comp': sentiment_dict['compound'],
        'Empath Positive': empath_pos['positive_emotion'],
        'Empath Negative': empath_neg['negative_emotion']
    }, ignore_index=True)
    df.to_excel("outputNewR2.xlsx")
