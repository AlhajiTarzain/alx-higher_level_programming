#!/usr/bin/python3
"""
displays value of x request in header when given a url
"""
if __name__ == '__main__':
    import requests
    from sys import argv
    url = argv[1]
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))

