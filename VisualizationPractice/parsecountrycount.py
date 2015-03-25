import json,csv
from collections import defaultdict
    
    
tweets_data_path = 'fourtweets20min.log'
tweets_data = []
tweets_file = open(tweets_data_path, "r")
Hashtags = ['vote5sos','votealall','vote1duk','votedebbyryan']
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue
print len(tweets_data)

with open('CountryCodes.csv', mode='r') as infile:
    reader = csv.reader(infile)
    mydict = dict((rows[1],rows[2]) for rows in reader)


country = defaultdict(lambda: dict(zip(Hashtags,[0]*len(Hashtags))))
for tweet in tweets_data:
    if 'place' in tweet and tweet['place'] != None:
        place = tweet['place']
        if 'country_code' in place and place['country_code'] != None:
            key = mydict[place['country_code']]
            print tweet
            for hashtag in Hashtags:
                if hashtag in str(tweet):
                    country[key][hashtag] += 1
print country
#with open('country_result.json','w') as out:
#    json.dump(country,out)
with open('country_test.csv','w') as outfile:
    out = csv.writer(outfile)
    out.writerow(['Country Code']+country.values()[0].keys())
    rows = map(lambda (key, value):[key]+value.values() ,country.items())
    out.writerows(rows)

