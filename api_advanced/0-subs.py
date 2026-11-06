#!/usr/bin/python3
"""Query the Reddit API for a subreddit's subscriber count.
"""
import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers for a given subreddit.

    If the subreddit is invalid, return 0.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "alu-practice/0.1 by mathy-cruz211"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0

    try:
        data = response.json()
    except ValueError:
        return 0

    return data.get("data", {}).get("subscribers", 0)
