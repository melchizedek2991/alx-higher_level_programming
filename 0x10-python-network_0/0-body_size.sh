#!/bin/bash
#GET request to the specified URL, retrieve the response body,
curl -s "$1" | wc -c
