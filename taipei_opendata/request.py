# -*- coding: utf-8 -*-

import urllib3
import gzip
import json
import StringIO

class torequest(object):

    @staticmethod
    def send_request(url, compress = False):
	    urllib3.disable_warnings()
	    http = urllib3.PoolManager()
	    r = http.request('GET', url, preload_content=False)
	    if compress:
	        data = torequest.decompressGzip(r.read())
	    else: 
	        data = r.read()

	    r.release_conn()
	    return data

    @staticmethod
    def decompressGzip(compressStr):
        compressedStram = StringIO.StringIO()
        compressedStram.write(compressStr)
        compressedStram.seek(0)
        decompressedStream = gzip.GzipFile(fileobj=compressedStram, mode='rb')
        result = decompressedStream.read()
        return result

        """docstring for TORequest"""
        def __init__(self):
            super(TORequest, self).__init__()