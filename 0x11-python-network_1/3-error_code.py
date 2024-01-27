#!/usr/bin/python3
"""URL as input, sends a request to the given URL, 
then outputs the response body's decoded UTF-8 content. responds to HTTP problems 
by displaying the relevant error code when it occurs.
"""

import sys
from urllib import request, error

if __name__ == "__main__":
    url = sys.argv[1]

    own_request = request.Request(url)
    try:
        with request.urlopen(own_request) as response:
            print(response.read().decode("ascii"))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
