#!/usr/bin/python3
"""
shows body of the response when url is sent a request
"""
if __name__ == "__main__":
    import urllib.error as url_error
    import urllib.request as url_request
    from sys import argv
    
    url = argv[1]
    request_obj = url_request.Request(url)
    
    try:
        with url_request.urlopen(request_obj) as response:
            print(response.read().decode('utf-8'))
    except url_error.HTTPError as e:
        print("Error code: {}".format(e.code))


