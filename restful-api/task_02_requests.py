#!/usr/bin/python3
"""
Module for consuming and processing data from an API.
"""
import requests
import csv


def fetch_and_print_posts():
    """Fetches all posts and prints titles."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print("Status Code: {}".format(response.status_code))
    if response.status_code == 200:
        for post in response.json():
            print(post.get("title"))


def fetch_and_save_posts():
    """Fetches posts and saves them into a CSV file."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()
        data = [{"id": p["id"], "title": p["title"], "body": p["body"]} for p in posts]
        with open("posts.csv", "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(data)
