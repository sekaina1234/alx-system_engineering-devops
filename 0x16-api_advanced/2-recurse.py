#!/usr/bin/python3
"""
    Uses Reddit API to get all hot posts
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Get all hot posts"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyBot/1.0 (by YourUsername)"}
    params = {"limit": 100, "after": after}

    try:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        if response.status_code == 200:
            posts = data["data"]["children"]
            if posts:
                hot_list.extend([post["data"]["title"] for post in posts])
                next_page = data["data"]["after"]
                if next_page:
                    return recurse(subreddit, hot_list, next_page)
            return hot_list
        else:
            return None
    except:
        return None

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        result = recurse(subreddit)
        if result is not None:
            print(len(result))
        else:
            print("None")
