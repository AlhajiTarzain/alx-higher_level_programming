#!/usr/bin/python3
"""
variable q holds parameter for request to be sent to
"""

import requests
from sys import argv

def search_user(url, query):
    try:
        response = requests.post(url, data={'q': query})
        response.raise_for_status()  # Raise an exception for HTTP errors (status code >= 400)
        json_data = response.json()
        if not json_data:
            print("No result")
        else:
            print("[{}] {}".format(json_data.get("id"), json_data.get("name")))
    except requests.exceptions.RequestException as e:
        print("Error:", e)

if __name__ == '__main__':
    url = "http://0.0.0.0:5000/search_user"
    query = argv[1][0] if len(argv) > 1 else ""
    search_user(url, query)

