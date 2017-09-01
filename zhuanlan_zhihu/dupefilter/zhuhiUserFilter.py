#!user/bin/env python3
#encoing:utf-8
from scrapy.dupefilter import RFPDupeFilter
class zhihuUserFilter(RFPDupeFilter):
    """A dupe filter that considers the URL"""
    def __init__(self, path=None):
        self.user = set()
        RFPDupeFilter.__init__(self, path)
    def request_seen(self, request):
        pattern='members/(.*?)/'
        userList=re.findall(pattern,request.url)
        user="" if len(userList)==0 else userList[0]
        if user in self.user:
            return True
        else:
            self.user.add(user)
    