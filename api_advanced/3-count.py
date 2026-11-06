#!/usr/bin/python3
"""Module for counting keyword occurrences in a subreddit's hot post titles."""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Print a sorted count of keyword occurrences in hot post titles.

    Case-insensitive, whole-word matching. Prints nothing if the
    subreddit is invalid or no keywords match.
    """
    if counts is None:
        counts = {}

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mathiang-ALU-api-advanced/1.0"}
    params = {"limit": 100}
    if after:
        params["after"] = after

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code != 200:
        return

    try:
        data = response.json()["data"]
    except (ValueError, KeyError):
        return

    for post in data["children"]:
        for word in post["data"]["title"].lower().split():
            counts[word] = counts.get(word, 0) + 1

    if data["after"] is not None:
        return count_words(subreddit, word_list, data["after"], counts)

    totals = {}
    for keyword in word_list:
        key = keyword.lower()
        totals[key] = totals.get(key, 0) + counts.get(key, 0)

    sorted_totals = sorted(
        totals.items(), key=lambda item: (-item[1], item[0])
    )
    for word, total in sorted_totals:
        if total > 0:
            print("{}: {}".format(word, total))
