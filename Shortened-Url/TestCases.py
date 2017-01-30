import platform

__author__ = 'ansbilal'

import requests
import json


class TestCase:
    def __init__(self):
        self.api_url = "http://127.0.0.1:8000/api/"
        self.headers = {'content-type': 'application/json', 'Accept-Language': 'en-us'}

    def create(self):

        """
        Test method for creating short url

        :return:
            will return newly created url
        """
        var = raw_input("Please enter long url: ")
        r = requests.post(str(self.api_url), data=json.dumps({'long_url':var}), headers=self.headers)
        print r.content

    def list(self):

        """
        Test method for listing a urls

        :return:
        """
        print '----------------------------------------------'
        print '           List of all Short URLs             '
        print '----------------------------------------------'
        r = requests.get(str(self.api_url), headers=self.headers)
        results = eval(r.content)
        for url in results["Results"]:
            print url

        print '--------------------------------------------------------------------'
        print '           Click/Browse any URL from below list to redirect to original URL             '
        print '--------------------------------------------------------------------'

        for url in results["Results"]:
            print url["url"]


if __name__ == '__main__':
    print '----------------------------------------------'
    print 'Current Operating System: ', platform.system()
    print '----------------------------------------------'
    test = TestCase()
    test.create()
    test.list()
