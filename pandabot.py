import tweepy
import requests
import json
import datetime

url = 'https://hooks.slack.com/services/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'


consumer_key = 'OKaaZZ8EIo1jme4FCpD2gdh9t'
consumer_secret = 'ksLwFur4MFRDCiZ9jzBGXDs1A4NPqE3iXa1Fi3t1GSG5x5hOOI'
access_token = 	'nnnnnnnnn-AnaAaaAanaAAAAAAaAAAaaaaAaAAAAaAAnaAAanA' #278088267-I0sKpkMq1jOPGGUScJVBhtkoDeTRRAaSI9dEQe2R
access_token_secret = 'vQvu6x8QhTtDdkbXIALlkbqvU9FKRqnoPFARQCR9xCv6V'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
trends1 = api.trends_place(1199477) #MANILA
data = trends1[0]
trends = data['trends']
names = [trend['name'] for trend in trends]

date = datetime.date.today()

hashtags = "Top Trends in Manila: " + str(date.strftime('%b. %d, %Y')) + "\n"
ctr = 1
for i in names[:10]:
	hashtags += str(ctr) + ". " + i + "\n"
	ctr += 1

payload = {'text' : hashtags}

# print hashtags

r = requests.post(url, data=json.dumps(payload))
r.text
r.status_code

