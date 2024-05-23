#!/usr/bin/python3
"""
Shows the value of x request
Made by taking in a url
"""

if __name__ == "__main__":
    import urllib.request as request
    from sys import argv
    url = argv[1]
    req = request.Request(url)
    with request.urlopen(req) as response:
        x_request_id = response.headers.get('X-Request-Id')
        print(x_request_id)

