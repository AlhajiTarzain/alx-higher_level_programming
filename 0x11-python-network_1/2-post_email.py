#!/usr/bin/python3
"""
Display response of POST request 
"""
if __name__ == "__main__":
    import urllib.parse as parse
    import urllib.request as request
    from sys import argv
    
    url = argv[1]
    email = argv[2]
    
    params = {'email': email}
    encoded_data = parse.urlencode(params).encode('utf-8')
    
    post_request = request.Request(url, encoded_data)
    
    with request.urlopen(post_request) as response:
        response_body = response.read().decode('utf-8')
        print(response_body)

