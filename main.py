import os
import praw


reddit = praw.Reddit(
    client_id=os.getenv('CLIENT_ID'),
    client_secret=os.getenv('CLIENT_SECRET'),
    username=os.getenv('BOT_USERNAME'),
    password=os.getenv('BOT_PASSWORD'),
    user_agent=os.getenv('BOT_USER_AGENT'),
)       

for submission in reddit.subreddit('SiteSummarizerBot').stream.submissions(skip_existing=True):
    text = submission.selftext.strip()