#!/usr/bin/python3
"""
Module that prints all commits by: `<sha>: <author name>` (one by line)
* The first argument will be the repository name
* The second argument will be the owner name
API INFO -> GET /repos/:owner/:repo/commits
"""
import requests
from sys import argv

if __name__ == '__main__':
    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])
    response = requests.get(url)
    json = response.json()
    for count, el in enumerate(json):
        if count < 10:
            print("{}: {}".format(el.get('sha'),
                                  el.get('commit').get('author').get('name')))
