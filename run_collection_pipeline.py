from TwitterAPI import collect_twitter_data
from data_preprocessing import clean_text
from config_keywords import configs

print('\n>>   Welcome to the Twitter Collection Pipeline  <<')
print('____________________________________________________\n')

topic_select = ['lgbt', 'covid', 'trump']
select_message = '>> \tPlease, select one of the following topics. Press 1, 2 or 3: \n'
for i, select in enumerate(topic_select):
    select_message += '\t\t' + str(i+1) + '. ' + select + '\n'
select_message += '>>\t Select: '
input_selected = input(select_message)
try:
    selected = int(input_selected)
    if selected < 1 or selected > 3:
        print('>>\tYour selection is out of range. '
              '[ERROR]Please make sure your input is 1, 2, or 3. corresponding to the desired topic.')
        exit(-1)
except Exception as e:
    print('>>\t[ERROR]Unknown value entered. '
          'Please make sure your input is 1, 2, or 3 corresponding to the desired topic.')
    print('Try again!')
    exit(-1)

# Define the keywords
selected_topic = topic_select[selected-1]
topic = configs[selected_topic]
topic_keywords = topic['topic_keywords']
hate_keywords = topic['hate_keywords']
# Join the keyword sets together
search_keywords = ' '.join([topic_keywords, hate_keywords])

# Collect data from Twitter API
tweets_data = collect_twitter_data(search_keywords)

# Preprocess tweets (Cleaning, removing emojis, divide words, split hash tags etc...)
print('>>   Cleaning data...    <<')
clean_tweet_df = tweets_data.apply(lambda tweet: clean_text(tweet['tweets']), axis=1)
clean_tweet_df.to_csv('clean_tweets.csv')
print('\n>>   Process Finished Successfully!    <<')

