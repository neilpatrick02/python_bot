import tweepy
import requests
import json

url = 'https://hooks.slack.com/services/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'

consumer_key = 'Zk8So9v4o4nFLaB6mvi4E8SXK'
consumer_secret = 'zW0MeLcCshDEG4iHld6wRciZPD4nyZRRK7tv6H5zmTRMMnJg1K'
access_token = 	'aaaa-nnnnnnnnnnn-AaaaAAaAnanAAAaaAAAaanAa'
access_token_secret = 'vQvu6x8QhTtDdkbXIALlkbqvU9FKRqnoPFARQCR9xCv6V'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
trends1 = api.trends_place(1199477) #MANILA
data = trends1[0] 
trends = data['trends']
names = [trend['name'] for trend in trends]

hashtags = ""
for i in names[:10]:
	hashtags += i + "\n" 
	
payload = {'text' : hashtags}

r = requests.post(url, data=json.dumps(payload))
r.text
r.status_code
