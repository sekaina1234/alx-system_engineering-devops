#!/usr/bin/python3
"""
    Uses Reddit API to print the number of subscribers of a subreddit
"""
import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "MyBot/1.0 (by YourUsername)"}

    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        
        if response.status_code == 200:
            return data["data"]["subscribers"]
        else:
            return 0
    except:
        return 0

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        subscribers = number_of_subscribers(subreddit)
        print(subscribers)
