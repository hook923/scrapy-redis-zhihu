import time
import re
from scrapy.dupefilters import BaseDupeFilter

from . import connection
from .bloomfilterOnRedis import BloomFilter
from scrapy.utils.request import request_fingerprint


class RFPDupeFilter(BaseDupeFilter):
    """Redis-based request duplication filter"""

    def __init__(self, server, key):
        """Initialize duplication filter

        Parameters
        ----------
        server : Redis instance
        key : str
            Where to store fingerprints
        """
        self.server = server
        self.key = key
        self.bf = BloomFilter(server,  key=key, blockNum=1)

    @classmethod
    def from_settings(cls, settings):
        server = connection.from_settings_filter(settings)
        key = "dupefilter:%s" % int(time.time())
        return cls(server, key)

    @classmethod
    def from_crawler(cls, crawler):
        return cls.from_settings(crawler.settings)

    def request_seen(self, request):        
        #url=request.url
        fp = request_fingerprint(request)
        if self.bf.isContains(fp):
            print("RFPDupeFilter-->request_seen:true")
            return True
        else:
            self.bf.insert(fp)
            return False            
        '''
        uid = re.findall('members/(.*?)/', request.url)
        if uid:
            uid = uid[0]            
            isExist = self.server.sismember("userid", uid)
            if isExist == 1:
                print("exist:%d" % isExist)
                return True
            else:
                self.server.sadd("userid", uid)
                return False
        '''

    def close(self, reason):
        """Delete data on close. Called by scrapy's scheduler"""
        self.clear()

    def clear(self):
        """Clears fingerprints data"""
        self.server.delete(self.key)
