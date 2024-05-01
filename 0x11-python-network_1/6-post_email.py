#!/usr/bin/python3
"""
displays response after taking in parameteres
"""
if __name__ == '__main__':
    import requests
    from sys import argv
    url = argv[1]
    email = argv[2]
    payload = {'email': email}
    response = requests.post(url, data=payload)
    print(response.text)

