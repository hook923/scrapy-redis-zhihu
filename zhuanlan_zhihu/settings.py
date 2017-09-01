# -*- coding: utf-8 -*-

# Scrapy settings for zhuanlan_zhihu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Zhuanlan'

SPIDER_MODULES = ['zhuanlan_zhihu.spiders']
NEWSPIDER_MODULE = 'zhuanlan_zhihu.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zhuanlan_zhihu (+http://www.yourdomain.com)'
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
USER_AGENT_LIST = ['zspider/0.9-dev http://feedback.redkolibri.com/',
                    'Xaldon_WebSpider/2.0.b1',
                    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) Speedy Spider (http://www.entireweb.com/about/search_tech/speedy_spider/)',
                    'Mozilla/5.0 (compatible; Speedy Spider; http://www.entireweb.com/about/search_tech/speedy_spider/)',
                    'Speedy Spider (Entireweb; Beta/1.3; http://www.entireweb.com/about/search_tech/speedyspider/)',
                    'Speedy Spider (Entireweb; Beta/1.2; http://www.entireweb.com/about/search_tech/speedyspider/)',
                    'Speedy Spider (Entireweb; Beta/1.1; http://www.entireweb.com/about/search_tech/speedyspider/)',
                    'Speedy Spider (Entireweb; Beta/1.0; http://www.entireweb.com/about/search_tech/speedyspider/)',
                    'Speedy Spider (Beta/1.0; www.entireweb.com)',
                    'Speedy Spider (http://www.entireweb.com/about/search_tech/speedy_spider/)',
                    'Speedy Spider (http://www.entireweb.com/about/search_tech/speedyspider/)',
                    'Speedy Spider (http://www.entireweb.com)',
                    'Sosospider+(+http://help.soso.com/webspider.htm)',
                    'sogou spider',
                    'Nusearch Spider (www.nusearch.com)',
                    'nuSearch Spider (compatible; MSIE 4.01; Windows NT)',
                    'lmspider (lmspider@scansoft.com)',
                    'lmspider lmspider@scansoft.com',
                    'ldspider (http://code.google.com/p/ldspider/wiki/Robots)',
                    'iaskspider/2.0(+http://iask.com/help/help_index.html)',
                    'iaskspider',
                    'hl_ftien_spider_v1.1',
                    'hl_ftien_spider',
                    'FyberSpider (+http://www.fybersearch.com/fyberspider.php)',
                    'FyberSpider',
                    'everyfeed-spider/2.0 (http://www.everyfeed.com)',
                    'envolk[ITS]spider/1.6 (+http://www.envolk.com/envolkspider.html)',
                    'envolk[ITS]spider/1.6 ( http://www.envolk.com/envolkspider.html)',
                    'Baiduspider+(+http://www.baidu.com/search/spider_jp.html)',
                    'Baiduspider+(+http://www.baidu.com/search/spider.htm)',
                    'BaiDuSpider',
                    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0) AddSugarSpiderBot www.idealobserver.com',
			"Mozilla/5.0 (Linux; U; Android 2.3.6; en-us; Nexus S Build/GRK39F) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
			"Avant Browser/1.2.789rel1 (http://www.avantbrowser.com)",
			"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5",
			"Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9",
			"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
			"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14",
			"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14",
			"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
			"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
			"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
			"Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre",
			"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10",
			"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)",
			"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5",
			"Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)",
			"Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
			"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
			"Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
			"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2",
			"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1",
			"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre",
			"Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0 )",
			"Mozilla/4.0 (compatible; MSIE 5.5; Windows 98; Win 9x 4.90)",
			"Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a",
			"Mozilla/2.02E (Win95; U)",
			"Mozilla/3.01Gold (Win95; I)",
			"Mozilla/4.8 [en] (Windows NT 5.1; U)",
			"Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)",
			"HTC_Dream Mozilla/5.0 (Linux; U; Android 1.5; en-ca; Build/CUPCAKE) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
			"Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.2; U; de-DE) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/234.40.1 Safari/534.6 TouchPad/1.0",
			"Mozilla/5.0 (Linux; U; Android 1.5; en-us; sdk Build/CUPCAKE) AppleWebkit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
			"Mozilla/5.0 (Linux; U; Android 2.1; en-us; Nexus One Build/ERD62) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
			"Mozilla/5.0 (Linux; U; Android 2.2; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
			"Mozilla/5.0 (Linux; U; Android 1.5; en-us; htc_bahamas Build/CRB17) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
			"Mozilla/5.0 (Linux; U; Android 2.1-update1; de-de; HTC Desire 1.19.161.5 Build/ERE27) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
			"Mozilla/5.0 (Linux; U; Android 2.2; en-us; Sprint APA9292KT Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
			"Mozilla/5.0 (Linux; U; Android 1.5; de-ch; HTC Hero Build/CUPCAKE) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
			"Mozilla/5.0 (Linux; U; Android 2.2; en-us; ADR6300 Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
			"Mozilla/5.0 (Linux; U; Android 2.1; en-us; HTC Legend Build/cupcake) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
			"Mozilla/5.0 (Linux; U; Android 1.5; de-de; HTC Magic Build/PLAT-RC33) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1 FirePHP/0.3",
			"Mozilla/5.0 (Linux; U; Android 1.6; en-us; HTC_TATTOO_A3288 Build/DRC79) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
			"Mozilla/5.0 (Linux; U; Android 1.0; en-us; dream) AppleWebKit/525.10  (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2",
			"Mozilla/5.0 (Linux; U; Android 1.5; en-us; T-Mobile G1 Build/CRB43) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari 525.20.1",
			"Mozilla/5.0 (Linux; U; Android 1.5; en-gb; T-Mobile_G2_Touch Build/CUPCAKE) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
			"Mozilla/5.0 (Linux; U; Android 2.0; en-us; Droid Build/ESD20) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
			"Mozilla/5.0 (Linux; U; Android 2.2; en-us; Droid Build/FRG22D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
			"Mozilla/5.0 (Linux; U; Android 2.0; en-us; Milestone Build/ SHOLS_U2_01.03.1) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
			"Mozilla/5.0 (Linux; U; Android 2.0.1; de-de; Milestone Build/SHOLS_U2_01.14.0) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
			"Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/525.10  (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2",
			"Mozilla/5.0 (Linux; U; Android 0.5; en-us) AppleWebKit/522  (KHTML, like Gecko) Safari/419.3",
			"Mozilla/5.0 (Linux; U; Android 1.1; en-gb; dream) AppleWebKit/525.10  (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2",
			"Mozilla/5.0 (Linux; U; Android 2.0; en-us; Droid Build/ESD20) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
			"Mozilla/5.0 (Linux; U; Android 2.1; en-us; Nexus One Build/ERD62) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
			"Mozilla/5.0 (Linux; U; Android 2.2; en-us; Sprint APA9292KT Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
			"Mozilla/5.0 (Linux; U; Android 2.2; en-us; ADR6300 Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
			"Mozilla/5.0 (Linux; U; Android 2.2; en-ca; GT-P1000M Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
			"Mozilla/5.0 (Linux; U; Android 3.0.1; fr-fr; A500 Build/HRI66) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
			"Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/525.10  (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2",
			"Mozilla/5.0 (Linux; U; Android 1.6; es-es; SonyEricssonX10i Build/R1FA016) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
			"Mozilla/5.0 (Linux; U; Android 1.6; en-us; SonyEricssonX10i Build/R1AA056) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1"
                   ]

AUTHORIZATION_List=['Bearer Mi4xa2RBVUFBQUFBQUFBVUFKdzNVOHlEQmNBQUFCaEFsVk5IV19PV1FERVBhelRlc3ZBRnhfd2VIa0FGdkRoa2xKU0hR|1504109085|6473f8c39e3f63c8d2d730cd6a481ca1f44fd188',
                    'Bearer Mi4xVFg5aEFBQUFBQUFBVUFKdzNVOHlEQmNBQUFCaEFsVk51QlhOV1FEYk1jakhGUWx6b2lrQlp0c3FRWHotLWZLRDNB|1504020665|8dcd1a54e020a9cf16a3335bea3316f5f251cfb5',
                    'Bearer Mi4xaUg3MEFRQUFBQUFBVUFKdzNVOHlEQmNBQUFCaEFsVk5zaGpOV1FDcjlfeHFobmFFNUd2Y19qY21hNW5IVHo2SGd3|1504021426|917e64cc47163d50742c93d507c39a76e9de9a0a',
                    'Bearer Mi4xdUNnakJRQUFBQUFBVUFKdzNVOHlEQmNBQUFCaEFsVk5TUnpOV1FDWTFxcFZKQUdyeEVhRkFqUmRNUTZkZ2ZWX3Rn|1504022346|54b9ceedd278a99d87112b9c3359649a417fe055',
                    'Bearer Mi4xVi1xR0FnQUFBQUFBVUFKdzNVOHlEQmNBQUFCaEFsVk5IaDdOV1FCeGpDNWV3REVfMU1KVm1LMmRtQXdic0ZqbHpB|1504022814|725b3fa38801e6179d4dc7bbeeb4af5f15005ed1',
                    'Bearer Mi4xVFdGdkFBQUFBQUFBVUFKdzNVOHlEQmNBQUFCaEFsVk5DUl9OV1FBc3hQSzhMLXlWSVFoVzBEcGFDVkJraHlUdFVB|1504023049|b91772b09c4e911bea873cd8090e48dbe3f976c9',
                    'Bearer Mi4xYWtIQ0JBQUFBQUFBVUFKdzNVOHlEQmNBQUFCaEFsVk5GaUhOV1FESlBtTDZGWFhNWjU4RTROUWxlOUdSVG9laFNB|1504023574|0316c26d6b3d73ceb3a5358d2c723e0a39ffbfa7',
                    'Bearer Mi4xRDczTEJRQUFBQUFBVUFKdzNVOHlEQmNBQUFCaEFsVk5MQ1ROV1FCTmxzajNOOUJKcU9TSncwamJ3UE9PTExxckRR|1504024364|ebc07588d7eeac744984b4758390549eb615dd04',
                    'Bearer Mi4xeFFIc0F3QUFBQUFBVUFKdzNVOHlEQmNBQUFCaEFsVk5iaVhOV1FBMkx5OVhfVUpuLUJlbjRBOXJzcHUwQ3g2ejhR|1504024686|315b4582ca8b05e324034cc66c83df547af97e02',
                    'Bearer Mi4xVzhUTEJRQUFBQUFBVUFKdzNVOHlEQmNBQUFCaEFsVk5LQ2JOV1FEdXVfVGlFU1VvXzRtejV3bWlCSm5tLTNEZktB|1504024872|d088951f266e0204944900e8b7183576cbc7cbcf',
                    'Bearer Mi4xZk1oZkFBQUFBQUFBVUFKdzNVOHlEQmNBQUFCaEFsVk4yakhOV1FBSGhjbVNwQ2lYWDZqWkhDLThTZUZTWHphY1p3|1504027866|86461ed7571944bdcc39807aa56cf0f9ecc4a26a',
                    'Bearer Mi4xcDlLUEJRQUFBQUFBVUFKdzNVOHlEQmNBQUFCaEFsVk5fVFBOV1FBcHJ2bW44UVluNEJPTjRKa255QVl2WEw2Ty13|1504028413|5f2628c60f7da9997aee498d53a55cbb0114916f'
                    ]

# Obey robots.txt rules
#ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#Scrapy downloader 并发请求(concurrent requests)的最大值
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY:下载器在下载同一个网站下一个页面前需要等待的时间。该选项可以用来限制爬取速度， 减轻服务器压力。同时也支持小数:
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
'''
DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'authorization': 'oauth c3cef7c66a1843f8b3a9e6a1e3160e20',
}
'''
# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'zhuanlan_zhihu.MidWare.HeaderMidWare.ProcessHeaderMidware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html

DOWNLOADER_MIDDLEWARES = {
    'zhuanlan_zhihu.MidWare.HeaderMidWare.ProcessHeaderMidware': 543,
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#保存项目中启用的pipeline及其顺序的字典。该字典默认为空，值(value)任意。 不过值(value)习惯设置在0-1000范围内。
ITEM_PIPELINES = {
    'zhuanlan_zhihu.pipelines.MongoPipeline': 300,
	#'scrapy_redis.pipelines.RedisPipeline': 400,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

#分布式功能 官方文档：https://github.com/rmax/scrapy-redis
SCHEDULER = "zhuanlan_zhihu.scrapy_redis.scheduler.Scheduler"  #启用Redis调度存储请求队列
SCHEDULER_PERSIST = True    #不清除Redis队列、这样可以暂停/恢复 爬取
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"  #确保所有的爬虫通过Redis去重
SCHEDULER_QUEUE_CLASS = 'zhuanlan_zhihu.scrapy_redis.queue.SpiderSimpleQueue'## 指定排序爬取地址时使用的队列，默认是按照优先级排序
# 可选的先进先出排序
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderQueue'
# 可选的后进先出排序
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderStack'
# 只在使用SpiderQueue或者SpiderStack是有效的参数,，指定爬虫关闭的最大空闲时间
SCHEDULER_IDLE_BEFORE_CLOSE = 10
REDIS_HOST = '127.0.0.1'  # 也可以根据情况改成 localhost
REDIS_PORT = 6379
REDIS_URL = None #用多台主机部署分布式爬虫时，在REDIS_URL中填入连接redis的主机URL，我这里只在一台主机上使用，写None或去掉这句话都可以。
#REDIS_PARAMS  = {}
#REDIS_URL = 'redis://user:pass@hostname:9001'
#REDIS_PARAMS['password'] = 'itcast.cn'

# 去重队列的信息
FILTER_URL = None
FILTER_HOST = 'localhost'
FILTER_PORT = 6379
FILTER_DB = 0

MONGO_HOST = "127.0.0.1"  # 主机IP
MONGO_PORT = 27017  # 端口号
MONGO_DATABASE = "zhihu"  # 库名
MONGO_COLL = "user"  # collection名
# MONGO_USER = "username"
# MONGO_PSW = "password"
#DOWNLOAD_TIMEOUT = 10 #下载超时时间
DOWNLOAD_DELAY = 0.001  # 间隔时间
CONCURRENT_REQUESTS = 64  # 默认为16
REDIRECT_ENABLED = False
RETRY_TIMES = 1

LOG_LEVEL='DEBUG' ##设置log级别['CRITICAL','ERROR','WARNING','INFO','DEBUG'],即[严重错误，一般错误，警告信息，一般信息，调试信息]
#LOG_FILE='zhihu.log'
