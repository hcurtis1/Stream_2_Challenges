import json
import re
import pandas
import matplotlib.pyplot as plt

tweets_data_path = 'tweet_mining.json'

def read_json(file_path):
    results = []
    tweets_file = open(file_path, "r")
    for tweet_line in tweets_file:
        try:
            status = json.loads(tweet_line)
            results.append(status)
        except:
            continue
    return results

def is_token_in_tweet_text(token, tweet_text):
    token = token.lower()
    tweet_text = tweet_text.lower()
    match = re.search(token, tweet_text)
    if match:
        return True
    return False

results = read_json(tweets_data_path)

# create a dataframe
statuses = pandas.DataFrame()

# store the text values
statuses['text'] = map(lambda status: status['text'], results)
# store the language values
statuses['lang'] = map(lambda status: status ['lang'], results)
# sometimes there may not be a 'place' listed in the tweet, so set to 'N/A; if not present
statuses['country'] = map(lambda status: status['place']['country'] if status['place'] else "N/A", results)

#  new DataFrame columns
statuses['python'] = statuses['text'].apply(lambda status: is_token_in_tweet_text('python', status))
statuses['java']   = statuses['text'].apply(lambda status: is_token_in_tweet_text('java', status))
statuses['c#']     = statuses['text'].apply(lambda status: is_token_in_tweet_text('c#', status))
statuses['ruby']   = statuses['text'].apply(lambda status: is_token_in_tweet_text('ruby', status))

python_val = statuses['python'].value_counts()[True]
java_val = statuses['java'].value_counts()[True]
c_sharp_val = statuses['c#'].value_counts()[True]
ruby_val = statuses['ruby'].value_counts()[True]

slices = [int(python_val), int(java_val), int(c_sharp_val), int(ruby_val)]
languages = ['Python', 'Java', 'C#', 'Ruby']
cols = ['g', 'r', 'b', 'y']

plt.pie(slices,
        labels=languages,
        colors=cols,
        startangle=90,
        shadow=True,
        explode=(0.1, 0, 0, 0),
        autopct='%1.1f%%')
plt.show()