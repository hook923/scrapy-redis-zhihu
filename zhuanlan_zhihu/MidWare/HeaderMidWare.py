#!user/bin/env python3
#encoding:utf-8
from scrapy.utils.project import get_project_settings
from scrapy.downloadermiddlewares.retry import RetryMiddleware
import random

settings = get_project_settings()

class ProcessHeaderMidware():
    """process request add request info"""
    
    def process_request(self,request,spider):
        """
        随机从列表中获得header， 并传给user_agent进行使用
        """
        spider.logger.info("add request head: authorization")
        request.headers['authorization']='Bearer Mi4xa2RBVUFBQUFBQUFBVUFKdzNVOHlEQmNBQUFCaEFsVk5tQ3pJV1FEMUJvTFBWdzRReVFKZ2xWSzBpVUM5Z2FXTjNR|1503698840|a9115293037d65485cf9438b6151cde23d9e8164'       
        
        userAgent=random.choice(settings.get('USER_AGENT_LIST'))
        #spider.logger.info(msg="now entring download midware")
        if userAgent:
            request.headers['User-Agent']=userAgent
            # Add desired logging message here.
            spider.logger.info(u'request headers is {}\n{}'.format(request.headers,request))
        pass
class ProxyMiddleware(RetryMiddleware):
    def __init__(self, settings):
        pass
class CookiesMiddleware(RetryMiddleware):
    def __init__(self, settings):
        pass    