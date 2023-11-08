#!/usr/bin/python3
"""
    Uses reddit API to get 10 hot posts
"""
import requests


def top_ten(subreddit):
    """Get 10 hot posts"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyBot/1.0 (by YourUsername)"}
    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        if response.status_code == 200:
            for post in data["data"]["children"]:
                print(post["data"]["title"])
        else:
            print(None)
    except:
        print(None)

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        top_ten(subreddit)
