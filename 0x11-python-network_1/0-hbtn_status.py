#!/usr/bin/python3
"""
obtain feedback/response from https://alx-intranet.hbtn.io/status
"""
if __name__ == "__main__":
    import urllib.request as request
    
    """start connection to URL"""
    with request.urlopen('https://alx-intranet.hbtn.io/status') as fresponse:
        # Read the response body
        response_body = fresponse.read()
        
        # Display information about the response
        print('Body response:')
        print("\t- type: {}".format(type(response_body)))
        print("\t- content: {}".format(response_body))
        print("\t- content (UTF-8): {}".format(response_body.decode('utf-8')))

