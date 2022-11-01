#!/usr/bin/python3
"""Queries the Reddit API.

Recursively obtains the count of words in all hot post titles.
"""
from requests import get
after = ""


def count_words(subreddit, word_list):
    """Print the count of words fro, all hot post titles."""
    hot_list = recurse(subreddit)
    word_dict = {}

    if not hot_list:
        return None
    else:
        word_dict = {word.lower(): 0 for word in word_list}

    for title in hot_list:
        title_split = title.split(" ")
        title_words = [word for word in title_split]
        for word in word_dict:
            count = title_words.count(word)
            if count > 0:
                word_dict[word] += count

    word_list = [
        [word, count] for word, count in word_dict.items() if count > 0
    ]
    word_list = sorted(word_list, key=lambda x: x[1], reverse=True)
    for word in word_list:
        print('{}: {}'.format(word[0], word[1]))


def recurse(subreddit, hot_list=[]):
    """Return a list with the titles of all hot articles for subreddit."""
    global after
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'
    headers = {'User-Agent': 'matv:1.0.0'}
    request = get(url.format(subreddit, after),
                  headers=headers,
                  allow_redirects=False)
    if request.status_code != 200:
        return None
    if after is None:
        return hot_list
    data = request.json().get('data').get('children')

    for post in data:
        hot_list.append(post.get('data').get('title').lower())

    after = request.json().get('data').get('after')
    recurse(subreddit, hot_list)
    return(hot_list)