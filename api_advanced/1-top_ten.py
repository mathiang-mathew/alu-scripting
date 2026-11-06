#!/usr/bin/python3
"""Module for printing the titles of a subreddit's top ten hot posts."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a subreddit.

    Prints None if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mathiang-ALU-api-advanced/1.0"}
    params = {"limit": 10}

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code != 200:
        print(None)
        return

    try:
        posts = response.json()["data"]["children"]
    except (ValueError, KeyError):
        print(None)
        return

    for post in posts:
        print(post["data"]["title"])
