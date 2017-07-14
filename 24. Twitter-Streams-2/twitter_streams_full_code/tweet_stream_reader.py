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

# get each tweet language and the  count of its appearance (not to be confused with programming languages)
tweets_by_lang = statuses['lang'].value_counts()
# get each tweet country of origin and the count of its appearance
tweets_by_country = statuses['country'].value_counts()

# create our drawing space (figure)
fig = plt.figure()

# prepare to plot two charts on the same figure
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)

# style the axes
ax1.tick_params(axis='x', labelsize=15)
ax1.tick_params(axis='y', labelsize=10)
ax1.set_xlabel('Tweet Languages', fontsize=15)
ax1.set_ylabel('Number of tweets', fontsize=15)
ax1.xaxis.label.set_color('#666666')
ax1.yaxis.label.set_color('#666666')
ax1.tick_params(axis='x', colors='#666666')
ax1.tick_params(axis='y', colors='#666666')
# style the title
ax1.set_title('Top 10 languages', fontsize=15, color='#666666')

# plot the top 10 tweet languages and appearance count using a bar chart
tweets_by_lang[:10].plot(ax=ax1, kind='bar', color='#FF7A00')

# color the spines (borders)
for spine in ax1.spines.values():
    spine.set_edgecolor('#666666')

# Second subplot
ax2.tick_params(axis='x', labelsize=15)
ax2.tick_params(axis='y', labelsize=10)
ax2.set_xlabel('Countries', fontsize=15)
ax2.set_ylabel('Number of tweets', fontsize=15)
ax2.xaxis.label.set_color('#666666')
ax2.yaxis.label.set_color('#666666')
ax2.tick_params(axis='x', colors='#666666')
ax2.tick_params(axis='y', colors='#666666')
# style the title
ax2.set_title('Top 10 Countries', fontsize=15, color='#666666')

# plot the top 10 tweet languages and appearance count using a bar chart
tweets_by_country[:10].plot(ax=ax2, kind='bar', color='#FF7A00')

# color the spines (borders)
for spine in ax2.spines.values():
    spine.set_edgecolor('#666666')

# render the two graphs at once
plt.show()
