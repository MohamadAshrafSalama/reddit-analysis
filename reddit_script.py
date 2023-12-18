import requests
import pandas as pd
from datetime import datetime
import time

# Function to read secrets from the file
def read_secrets():
    with open("secrets.txt", "r") as file:
        secrets = {}
        for line in file:
            key, value = line.strip().split("=")
            secrets[key] = value
    return secrets

# Function to convert responses to dataframes
def df_from_response(res):
    df = pd.DataFrame()
    for post in res.json()['data']['children']:
        df = df.append({
            'id': post['data']['id'],
            'ups': post['data']['ups'],
            'upvote_ratio': post['data']['upvote_ratio'],
            'num_comments': post['data']['num_comments'],
            'score': post['data']['score'],
            'post_length_chars': len(post['data']['selftext']),
            'post_length_words': len(post['data']['selftext'].split()),
            'created_utc': datetime.fromtimestamp(post['data']['created_utc']).strftime('%Y-%m-%dT%H:%M:%SZ'),
            'selftext': post['data']['selftext'],
            'kind': post['kind']
        }, ignore_index=True)
    return df

# Function to authenticate API using secrets
def authenticate():
    secrets = read_secrets()
    client_auth = requests.auth.HTTPBasicAuth(secrets['client_id'], secrets['client_secret'])
    data = {
        'grant_type': 'password',
        'username': secrets['reddit_username'],
        'password': secrets['reddit_password']
    }
    headers = {'User-Agent': 'myBot/0.0.1'}
    res = requests.post('https://www.reddit.com/api/v1/access_token', auth=client_auth, data=data, headers=headers)
    TOKEN = f"bearer {res.json()['access_token']}"
    headers = {**headers, **{'Authorization': TOKEN}}
    return headers

# Function to get data within the specified date range
def get_filtered_data(headers, start_date, end_date, subreddit):
    data = pd.DataFrame()
    params = {'limit': 50}

    for i in range(19):
        res = requests.get(f"https://oauth.reddit.com/r/{subreddit}/new", headers=headers, params=params)
        new_df = df_from_response(res)

        last_post_date = datetime.strptime(new_df.iloc[len(new_df) - 1]['created_utc'], '%Y-%m-%dT%H:%M:%SZ')
        if last_post_date < start_date:
            break

        row = new_df.iloc[len(new_df) - 1]
        fullname = row['kind'] + '_' + row['id']
        params['after'] = fullname

        data = data.append(new_df, ignore_index=True)

    filtered_data = data[data['created_utc'].apply(lambda x: start_date <= datetime.strptime(x, '%Y-%m-%dT%H:%M:%SZ') <= end_date)]
    return filtered_data

# Function to prompt user for input
def get_user_input():
    start_date_str = input("Enter the start date (YYYY-MM-DD): ")
    end_date_str = input("Enter the end date (YYYY-MM-DD): ")
    subreddit = input("Enter the subreddit: ")
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
    return start_date, end_date, subreddit

# Main script
secrets = read_secrets()
headers = authenticate()
start_date, end_date, subreddit = get_user_input()
filtered_data = get_filtered_data(headers, start_date, end_date, subreddit)
filtered_data.to_csv(f'{subreddit}.csv', index=False)
print(f"Filtered data saved to {subreddit}.csv")
