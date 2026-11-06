#!/usr/bin/python3
"""Module for recursively collecting all hot post titles of a subreddit."""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """Return a list of titles of all hot posts for a subreddit.

    Returns None if the subreddit is invalid or has no hot posts.
    """
    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mathiang-ALU-api-advanced/1.0"}
    params = {"limit": 100}
    if after:
        params["after"] = after

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code != 200:
        return None

    try:
        data = response.json()["data"]
    except (ValueError, KeyError):
        return None

    for post in data["children"]:
        hot_list.append(post["data"]["title"])

    if data["after"] is None:
        return hot_list if hot_list else None

    return recurse(subreddit, hot_list, data["after"])
