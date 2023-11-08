#!/usr/bin/python3
"""Module Done"""

import requests


def count_words(subreddit, word_list, after=None, counts={}):
    """Queries Reddit API for the subreddit"""

    if not word_list:
        sorted_counts = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
        for word, count in sorted_counts:
            print(f"{word}: {count}")
        return

    word = word_list[0].lower()
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyBot/1.0 (by YourUsername)"}
    params = {"limit": 100, "after": after}

    try:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        if response.status_code == 200:
            posts = data["data"]["children"]
            for post in posts:
                title = post["data"]["title"].lower()
                if word in title:
                    counts[word] = counts.get(word, 0) + title.count(word)

            next_page = data["data"]["after"]
            return count_words(subreddit, word_list, next_page, counts)
        else:
            return
    except:
        return

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        word_list = [x.lower() for x in sys.argv[2].split()]
        count_words(subreddit, word_list)
