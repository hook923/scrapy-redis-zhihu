#!user/bin/env python3
# -*- coding: utf-8 -*-
#import sys
from scrapy.spider import Spider
from scrapy_redis.spiders import RedisSpider
from scrapy.http import Request
from zhuanlan_zhihu.items import UserItem,QuestionItem,AnswerItem,ArticleItem

import json
import re
import math
#reload(sys)
#sys.setdefaultencoding('utf8')

class ZhuanlanSpider(RedisSpider): 
    '''
    fieldNumList=["followingCount","voteFromCount","pinsCount","favoriteCount","voteupCount","commercialQuestionCount","followingColumnsCount","participatedLiveCount","followingFavlistsCount",
                      "favoritedCount","followerCount","followingTopicCount","columnsCount","hostedLiveCount","isActive","thankToCount","mutualFolloweesCount","markedAnswersCount","thankFromCount",
               "voteToCount","answerCount","articlesCount","questionCount","logsCount","followingQuestionCount","thankedCount"]
    fieldBoolList=["isFollowed","showSinaWeibo","isFollowing","isPrivacyProtected","isForceRenamed","isBlocking","isAdvertiser","isBindSina","isOrg","isBlocked","allowMessage"]
    fieldStrList=["userType","markedAnswersText","id","headline","type","avatarHue","avatarUrlTemplate","description","avatarUrl","coverUrl","name","url","messageThreadToken"]
    '''    
    name = "Zhuanlan"  ##定义spider名字的字符串。
    pageMaxCount=20
    allowed_domains = ["www.zhihu.com"] ##可选。包含了spider允许爬取的域名(domain)列表(list)
    user_url = 'https://www.zhihu.com/api/v4/members/{user}?include={include}'
    follows_url = 'https://www.zhihu.com/api/v4/members/{user}/followees?include={include}&offset={offset}&limit={limit}'
    followers_url = 'https://www.zhihu.com/api/v4/members/{user}/followers?include={include}&offset={offset}&limit={limit}'
    answers_url='https://www.zhihu.com/api/v4/members/{user}/answers?include={include}&offset={offset}&limit={limit}'
    question_url='https://www.zhihu.com/api/v4/members/{user}/questions?offset={offset}&limit={limit}'
    article_url='https://www.zhihu.com/api/v4/members/{user}/articles?include={include}&offset={offset}&limit={limit}'
    start_user = 'zhang-jia-wei'
    user_query = 'locations,employments,gender,educations,business,voteup_count,thanked_Count,follower_count,following_count,cover_url,following_topic_count,following_question_count,following_favlists_count,following_columns_count,answer_count,articles_count,pins_count,question_count,commercial_question_count,favorite_count,favorited_count,logs_count,marked_answers_count,marked_answers_text,message_thread_token,account_status,is_active,is_force_renamed,is_bind_sina,sina_weibo_url,sina_weibo_name,show_sina_weibo,is_blocking,is_blocked,is_following,is_followed,mutual_followees_count,vote_to_count,vote_from_count,thank_to_count,thank_from_count,thanked_count,description,hosted_live_count,participated_live_count,allow_message,industry_category,org_name,org_homepage,badge[?(type=best_answerer)].topics'
    follows_query = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'
    followers_query = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'
    answers_query="data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cupvoted_followees%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics"
    article_query='data[*].comment_count,content,voteup_count,created,updated'
    '''
    start_urls = [  
        "https://www.zhihu.com/people/zhang-jia-wei/followers"，
        "https://www.zhihu.com/people/jiayangqing/followers"
    ]  
    '''
    start_urls =[] ##初始URL列表。当没有制定特定的URL时，spider将从该列表中开始进行爬取。    
    redis_key='ZhuanlanSpider:start_urls'
    
    def start_requests(self):##当spider启动爬取并且未指定start_urls时，该方法被调用
        user=self.start_user
        url=self.user_url.format(user=user, include=self.user_query)
        self.logger.info("start_request:%s" % url)        
        yield Request(url, self.parse_user)
        yield Request(self.follows_url.format(user=user, include=self.follows_query, limit=20, offset=0),
                          self.parse_follows)
        yield Request(self.followers_url.format(user=user, include=self.followers_query, limit=20, offset=0),
                          self.parse_followers)
        yield Request(self.answers_url.format(user=user,include=self.answers_query,limit=20,offset=0),self.parse_answers,meta={'url_token':user})
        yield Request(self.question_url.format(user=user,offset=0,limit=20),callback=self.parse_question,meta={"url_token":user})
        yield Request(self.article_url.format(user=user,include=self.article_query,limit=20,offset=0,callback=self.parse_article,meta={"url_token":user}))
        
    #def parse(self, response):  ##当请求url返回网页没有指定回调函数时，默认下载回调方法。
    #def log(message[, level, component]):##使用 scrapy.log.msg() 方法记录(log)message。 更多数据请参见 Logging
    @staticmethod
    def DealResult(result):        
        newEducations=[]
        for school in result["educations"]:
            sch={}
            try:
                try:
                    name=school["major"]["name"]
                except Exception:
                    #self.logger.info("educations error-->major-->name")
                    name=""
                sch[school["school"]["name"]]=name
            except Exception:
                #self.logger.info("educations error:%s" % result["educations"])
                pass
            if len(sch)>0:
                newEducations.append(sch)
        result["educations"]=newEducations
        
        newEmployments=[]
        for job in result["employments"]:
            company={}
            try :
                company[job["company"]["name"]]=job["job"]["name"]
            except Exception:
                #self.logger.info("employments error" % result["employments"])
                pass
            if len(company)>0:
                newEmployments.append(company)
        result["employments"]=newEmployments
        
        try:
            if "business" in result.keys():
                result["business"]=result["business"]["name"]
        except Excepution:
            #self.logger.info("business error" )
            pass
        
        
        newlocations=[]
        for l in result["locations"]:
            try:
                newlocations.append(l["name"])
            except Exception:
                #self.logger.info("locations error:cannot get name")            
                pass
        result["locations"]=newlocations
        
        newbadge=[]
        for badge in result["badge"]:
            topics={}
            try:
                tList=[]
                for t in badge["topics"]:
                    tList.append(t["name"])
                topics[t["type"]]=','.join(tList)
            except Exception:
                #self.logger.info("badge error:")
                pass
            if len(topics)>0:
                newbadge.append(topics)
        result["badge"]=newbadge
            
    def parse_user(self,response):
        self.logger.info("start parse_user...")
        item=UserItem()
        try:
            try:
                result = json.loads(response.text)
            except Exception:
                result={}
                self.logger.info("json load error")
            
            self.logger.info("start Deal educations,employments,business,locations,badge")
            try:
                self.DealResult(result)
            except Exception:
                self.logger.info("DealResult error")
            
            for field in item.fields:
                if field in result.keys():
                    item[field] = result.get(field)
            if dict(item)=={}:
                self.logger.info("\nparse_user: empty Item\n")
                return
            yield item
            
            yield Request(
                self.follows_url.format(user=result.get('url_token'), include=self.follows_query, limit=20, offset=0),
                self.parse_follows)
    
            yield Request(
                self.followers_url.format(user=result.get('url_token'), include=self.followers_query, limit=20, offset=0),
                self.parse_followers)
            
            user=item['url_token']
            
            yield Request(self.answers_url.format(user=user,include=self.answers_query,limit=20,offset=0),self.parse_answers,meta={'url_token':user})
            yield Request(self.question_url.format(user=user,offset=0,limit=20),callback=self.parse_question,meta={"url_token":user})
            yield Request(self.article_url.format(user=user,include=self.article_query,limit=20,offset=0,callback=self.parse_article,meta={"url_token":user}))            
        except Exception :                    
            pass
        else:
            yield item
        
    def parse_follows(self, response):
        results = json.loads(response.text)

        if 'data' in results.keys():
            for result in results.get('data'):
                ##
                yield Request(self.user_url.format(user=result.get('url_token'), include=self.user_query),self.parse_user)

        if 'paging' in results.keys() and results.get('paging').get('is_end') == False:
            next_page = results.get('paging').get('next')
            yield Request(next_page,self.parse_follows)

    def parse_followers(self, response):
        results = json.loads(response.text)

        if 'data' in results.keys():
            for result in results.get('data'):
                ##
                yield Request(self.user_url.format(user=result.get('url_token'), include=self.user_query),self.parse_user)

        if 'paging' in results.keys() and results.get('paging').get('is_end') == False:
            next_page = results.get('paging').get('next')
            yield Request(next_page,self.parse_followers)
            
    def parse_answers(self,response):
        results = json.loads(response.text)
        try:
            user = response.meta["url_token"]##
        except Exception :
            try:
                user=re.findall("members/(.*?)/",response.url)[0]
            except Exception :
                user=""
            self.logger.info("author empty,can not pass answers response.meta['url_token'],use:%s" % user)  
        
        if 'data' in results.keys():
            for answers in results.get('data'):
                item=AnswerItem()
                item["url_token"]=user
                
                try :
                    item["question_id"] = answers.get("question").get("id")##
                except Exception :
                    pass
                for field in item.fields:
                    if field in answers.keys():
                        item[field] = answers.get(field)
                
                yield item

        if 'paging' in results.keys() and results.get('paging').get('is_end') == False:
            next_page = results.get('paging').get('next')
            yield Request(next_page,self.parse_answers,meta={"url_token":user})
    
    def parse_question(self,response):
        results = json.loads(response.text)
        try:
            user = response.meta["url_token"]##
        except Exception :
            try:
                user=re.findall("members/(.*?)/",response.url)[0]
            except Exception :
                user=""
            self.logger.info("author empty,can not pass question response.meta['url_token'],use:%s" % user) 
        
        if 'data' in results.keys():
            for answers in results.get('data'):
                item=QuestionItem()
                item["url_token"]= user

                for field in item.fields:
                    if field in answers.keys():
                        item[field] = answers.get(field)
                
                yield item

        if 'paging' in results.keys() and results.get('paging').get('is_end') == False:
            next_page = results.get('paging').get('next')
            yield Request(next_page,callback=self.parse_question,meta={"url_token":user})        
    def parse_article(self,response):
        results = json.loads(response.text)
        try:
            user = response.meta["url_token"]##
        except Exception :
            try:
                user=re.findall("members/(.*?)/",response.url)[0]
            except Exception :
                user=""
            self.logger.info("author empty,can not pass question response.meta['url_token'],use:%s" % user) 
        
        if 'data' in results.keys():
            for answers in results.get('data'):
                item=QuestionItem()
                item["url_token"]= user

                for field in item.fields:
                    if field in answers.keys():
                        item[field] = answers.get(field) 
                yield item
        if 'paging' in results.keys() and results.get('paging').get('is_end') == False:
            next_page = results.get('paging').get('next')
            yield Request(next_page,callback=self.parse_article,meta={"url_token":user})             
    def dealFollowers(self, response):
        fieldDic={}
        data=[]
        ##r=response.body
        ##selecters=etree.HTML(r.text.encode(encoding='utf-8'))
        ##iddata=selecters.xpath("//div[@id='data']/@data-state")[0].replace("null,","")
        iddata=response.xpath("//div[@id='data']/@data-state")[0].extract().replace("null,","")
        iddataa=iddata.split(',"questions')[0]+"}}" ##去除,"questions之后的字符，badge等必须去除[]才好提取数据
        ##提取粉丝，加入新的爬取链接
        pattern='"urlToken":(.*?),'
        urltokenList=re.findall(pattern,iddata)##
        fieldDic["urlToken"]=urltokenList[-1]
        addUserUrl(urltokenList[:-1])
        
        pattern='"business":{(.*?)\}'
        businessList=re.findall(pattern,iddata)
        if len(businessList)>0:
            fieldDic["business"]=eval("{"+businessList[-1]+"}")["name"]
        else:
            fieldDic["business"]=""
        
        schList=dealEducations(self,urltokenList[-1],iddata)##教育经历
        jobList=dealEducations(self,urltokenList[-1],iddata)##工作经历
        pattern='"locations":\[(.*?)\]'
        locationsList=re.findall(pattern, iddata)     
        #badge忽略
        
        for f in fieldNumList:
            ##'"followerCount":(.*?),'
            pattern='"%s":(.*?),' % f 
            fieldList=re.findall(pattern,iddata)
            if len(fieldList)>0:
                fieldDic[f]=int(fieldList[-1])
            else:
                fieldDic[f]=-9
        pattern='"gender":(.*?)\}'
        fieldList=re.findall(pattern,iddata)
        if len(fieldList)>0:
            fieldDic["gender"]=int(fieldList[-1])
        else:
            fieldDic["gender"]=-1
        
        followerCount=fieldDic["followerCount"]
        addFollowerUrl(self,urltokenList[-1],followerCount)##每页的粉丝
        
        for f in fieldStrList:
            pattern='"%s":(.*?),' % f 
            fieldList=re.findall(pattern,iddata)
            if len(fieldList)>0:
                fieldDic[f]=fieldList[-1]
            else:
                fieldDic[f]=""
        return data
    def dealIddata(self,iddata):
        num=0  
        newdata=iddata
        for i in range(len(newdata)-1,0,-1):        
            if newdata[i]=="]":
                num+=1
                if num==1:
                    newdata=newdata[:i]+'''"'''+newdata[i+1:]
                else:
                    newdata=newdata[:i]+newdata[i+1:]
                continue
            if newdata[i]=="[":
                num-=1
                if num==0:
                    newdata=newdata[:i]+'''"'''+newdata[i+1:] 
                else:
                    newdata=newdata[:i]+newdata[i+1:]
                continue
            if num>0:
                newdata=newdata[:i]+newdata[i+1:]
        return newdata
    def addUserUrl(self,urltokenList):
        for u in urltokenList:
            url="https://www.zhihu.com/people/%s/followers" % u.replace('"',"")
            start_urls.addpend(url)
    def addFollowerUrl(self,user,followerCount):
        pageCount=math.ceil(followerCount/pageMaxCount)+1
        for page in range(2,pageCount):
            url="https://www.zhihu.com/people/%s/followers?page=%d" %(user,page)
            start_urls.addpend(url)
    def dealEducations(self,user,iddata):
        schList=[]
        pattern='"educations":\[(.*?)\]'
        schoolList=re.findall(pattern,iddata)
        ##['{"school":{"introduction":"一所位于美国加州旧金山东湾伯克利的公立研究型大学。其许多科系位于全球大学排行前十名，是世界上最负盛名的大学之一，常被誉为美国乃至世界最顶尖的公立大学。<a class=\\"\\" href=\\"http://zh.wikipedia.org/zh-cn/%E5%8A%A0%E5%B7%9E%E5%A4%A7%E5%AD%B8%E6%9F%8F%E5%85%8B%E8%90%8A%E5%88%86%E6%A0%A1\\" data-editable=\\"true\\" data-title=\\"维基百科\\">维基百科</a>","avatarUrl":"https://pic2.zhimg.com/ffd86654d_is.jpg","name":"加州大学伯克利分校 (UC Berkeley)","url":"http://www.zhihu.com/api/v4/topics/19563305","type":"topic","excerpt":"一所位于美国加州旧金山东湾伯克利的公立研究型大学。其许多科系位于全球大学排行前十名，是世界上最负盛名的大学之一，常被誉为美国乃至世界最顶尖的公立大学。维基百科 ","id":"19563305"},"major":{"introduction":"<b>计算机科学</b>（Computer Science, CS）是系统性研究信息与计算的理论基础以及它们在计算机系统中如何实现与应用的实用技术的学科。<br> 它通常被形容为对那些创造、描述以及转换信息的算法处理的系统研究。计算机科学包含很多分支领域；其中一些，比如计算机图形学强调特定结果的计算，而另外一些，比如计算复杂性理论是学习计算问题的性质。还有一些领域专注于挑战怎样实现计算。比如程序设计语言理论学习描述计算的方法，而程序设计是应用特定的程序设计语言解决特定的计算问题，人机交互则是专注于挑战怎样使计算机和计算变得有用、可用，以及随时随地为<a href=\\"http://zh.wikipedia.org/wiki/%E4%BA%BA\\" data-editable=\\"true\\" data-title=\\"人\\">人</a>所用。<br><b>现代计算机科学( Computer Science)包含理论计算机科学和应用计算机科学两大分支。</b>","avatarUrl":"https://pic3.zhimg.com/b85ddd8aa_is.jpg","name":"计算机科学","url":"http://www.zhihu.com/api/v4/topics/19580349","type":"topic","excerpt":"计算机科学（Computer Science, CS）是系统性研究信息与计算的理论基础以及它们在计算机系统中如何实现与应用的实用技术的学科。 它通常被形容为对那些创造、描述以及转换信息的算法处理的系统研究。计算机科学包含很多分支领域；其中一些，比如计算机图形学强调特定结果的计算，而另外一些，比如计算复杂性理论是学习计算问题的性质。还有一些领域专注于挑战怎样实现计算。比如程序设计语言理论学习描述计算的方法，而程序设计…","id":"19580349"}},{"school":{"introduction":"清华大学是中国乃至亚洲最著名的高等学府之一。其前身即1911年利用美国退还庚子赔款之退款在北京设立之清华学堂，1912年中华民国成立后改为清华学校，1928年北伐后由国民政府改制为国立清华大学。对日抗战期间西迁昆明，与北京大学、南开大学合组国立西南联合大学。1946年迁返北平复校。<br><br>source：<a href=\\"http://t.cn/RXZMG2M\\" data-editable=\\"true\\" data-title=\\"海外名校留学申请条件\\">海外名校留学申请条件</a>","avatarUrl":"https://pic2.zhimg.com/dfa000c15_is.jpg","name":"清华大学","url":"http://www.zhihu.com/api/v4/topics/19563245","type":"topic","excerpt":"清华大学是中国乃至亚洲最著名的高等学府之一。其前身即1911年利用美国退还庚子赔款之退款在北京设立之清华学堂，1912年中华民国成立后改为清华学校，1928年北伐后由国民政府改制为国立清华大学。对日抗战期间西迁昆明，与北京大学、南开大学合组国立西南联合大学。1946年迁返北平复校。 source：海外名校留学申请条件 ","id":"19563245"}}']
        if len(schoolList)>0:              
            pattern='\{"school":(.*?)\}\}'
            schoolword=re.findall(pattern, schoolList[0])
            for s in schoolword:
                pattern='"name":(.*?),'
                schoolExcerpt=re.findall(pattern, s)
                schList.append(schoolExcerpt)
            ##['{"introduction":"一所位于美国加州旧金山东湾伯克利的公立研究型大学。其许多科系位于全球大学排行前十名，是世界上最负盛名的大学之一，常被誉为美国乃至世界最顶尖的公立大学。<a class=\\"\\" href=\\"http://zh.wikipedia.org/zh-cn/%E5%8A%A0%E5%B7%9E%E5%A4%A7%E5%AD%B8%E6%9F%8F%E5%85%8B%E8%90%8A%E5%88%86%E6%A0%A1\\" data-editable=\\"true\\" data-title=\\"维基百科\\">维基百科</a>","avatarUrl":"https://pic2.zhimg.com/ffd86654d_is.jpg","name":"加州大学伯克利分校 (UC Berkeley)","url":"http://www.zhihu.com/api/v4/topics/19563305","type":"topic","excerpt":"一所位于美国加州旧金山东湾伯克利的公立研究型大学。其许多科系位于全球大学排行前十名，是世界上最负盛名的大学之一，常被誉为美国乃至世界最顶尖的公立大学。维基百科 ","id":"19563305"},
            ###  "major":{"introduction":"<b>计算机科学</b>（Computer Science, CS）是系统性研究信息与计算的理论基础以及它们在计算机系统中如何实现与应用的实用技术的学科。<br> 它通常被形容为对那些创造、描述以及转换信息的算法处理的系统研究。计算机科学包含很多分支领域；其中一些，比如计算机图形学强调特定结果的计算，而另外一些，比如计算复杂性理论是学习计算问题的性质。还有一些领域专注于挑战怎样实现计算。比如程序设计语言理论学习描述计算的方法，而程序设计是应用特定的程序设计语言解决特定的计算问题，人机交互则是专注于挑战怎样使计算机和计算变得有用、可用，以及随时随地为<a href=\\"http://zh.wikipedia.org/wiki/%E4%BA%BA\\" data-editable=\\"true\\" data-title=\\"人\\">人</a>所用。<br><b>现代计算机科学( Computer Science)包含理论计算机科学和应用计算机科学两大分支。</b>","avatarUrl":"https://pic3.zhimg.com/b85ddd8aa_is.jpg","name":"计算机科学","url":"http://www.zhihu.com/api/v4/topics/19580349","type":"topic","excerpt":"计算机科学（Computer Science, CS）是系统性研究信息与计算的理论基础以及它们在计算机系统中如何实现与应用的实用技术的学科。 它通常被形容为对那些创造、描述以及转换信息的算法处理的系统研究。计算机科学包含很多分支领域；其中一些，比如计算机图形学强调特定结果的计算，而另外一些，比如计算复杂性理论是学习计算问题的性质。还有一些领域专注于挑战怎样实现计算。比如程序设计语言理论学习描述计算的方法，而程序设计…","id":"19580349"',
            ###'{"introduction":"清华大学是中国乃至亚洲最著名的高等学府之一。其前身即1911年利用美国退还庚子赔款之退款在北京设立之清华学堂，1912年中华民国成立后改为清华学校，1928年北伐后由国民政府改制为国立清华大学。对日抗战期间西迁昆明，与北京大学、南开大学合组国立西南联合大学。1946年迁返北平复校。<br><br>source：<a href=\\"http://t.cn/RXZMG2M\\" data-editable=\\"true\\" data-title=\\"海外名校留学申请条件\\">海外名校留学申请条件</a>","avatarUrl":"https://pic2.zhimg.com/dfa000c15_is.jpg","name":"清华大学","url":"http://www.zhihu.com/api/v4/topics/19563245","type":"topic","excerpt":"清华大学是中国乃至亚洲最著名的高等学府之一。其前身即1911年利用美国退还庚子赔款之退款在北京设立之清华学堂，1912年中华民国成立后改为清华学校，1928年北伐后由国民政府改制为国立清华大学。对日抗战期间西迁昆明，与北京大学、南开大学合组国立西南联合大学。1946年迁返北平复校。 source：海外名校留学申请条件 ","id":"19563245"']        
        return schList
    def dealEmployments(self,user,iddata):
        jobList=[]
        pattern='"employments":\[(.*?)\]'
        employList=re.findall(pattern, iddata)
        ##['{"job":{"introduction":"","avatarUrl":"https://pic1.zhimg.com/e82bab09c_is.jpg","name":"Research Lead","url":"http://www.zhihu.com/api/v4/topics/","type":"topic","excerpt":"","id":""},
        ###"company":{"introduction":"Facebook 是一个社交网络服务网站，于 2004 年 2 月 4 日上线。从 2006 年 9 月到 2007 年 9 月间，该网站在全美网站中的排名由第 60 名上升至第 7 名。同时 Facebook 是美国排名第一的照片分享站点。<br><br>2012年 2 月 1 日，Facebook向美国证券交易委员会提交集资规模为 50 亿美元的上市申请。","avatarUrl":"https://pic3.zhimg.com/86cb8736a8a7498fafe2f017465bf5b2_is.jpg","name":"Facebook","url":"http://www.zhihu.com/api/v4/topics/19550340","type":"topic","excerpt":"Facebook 是一个社交网络服务网站，于 2004 年 2 月 4 日上线。从 2006 年 9 月到 2007 年 9 月间，该网站在全美网站中的排名由第 60 名上升至第 7 名。同时 Facebook 是美国排名第一的照片分享站点。 2012年 2 月 1 日，Facebook向美国证券交易委员会提交集资规模为 50 亿美元的上市申请。","id":"19550340"}},
        ###{"job":{"introduction":"","avatarUrl":"https://pic1.zhimg.com/e82bab09c_is.jpg","name":"Research scientist","url":"http://www.zhihu.com/api/v4/topics/19702224","type":"topic","excerpt":"","id":"19702224"},
        ###"company":{"introduction":"一家美国的跨国科技企业，致力于互联网搜索、云计算、广告技术等领域，由当时在斯坦福大学攻读理学博士的拉里·佩奇和谢尔盖·布林共同创建。创始之初，Google 官方的公司使命为「整合全球范围的信息，使人人皆可访问并从中受益」。<br><br>Google 开发并提供了大量基于互联网的产品与服务，其主要利润来自于 AdWords 等广告服务。<br><br>2004 年 8 月 19 日， 公司以「GOOG」为代码正式登陆纳斯达克交易所。","avatarUrl":"https://pic3.zhimg.com/v2-275d4f0e9bad3711cd6e6861df899712_is.jpg","name":"谷歌 (Google)","url":"http://www.zhihu.com/api/v4/topics/19565870","type":"topic","excerpt":"一家美国的跨国科技企业，致力于互联网搜索、云计算、广告技术等领域，由当时在斯坦福大学攻读理学博士的拉里·佩奇和谢尔盖·布林共同创建。创始之初，Google 官方的公司使命为「整合全球范围的信息，使人人皆可访问并从中受益」。 Google 开发并提供了大量基于互联网的产品与服务，其主要利润来自于 AdWords 等广告服务。 2004 年 8 月 19 日， 公司以「GOOG」为代码正式登陆纳斯达克交易所。","id":"19565870"}}']
        if len(employList)>0:            
            pattern='\{"job":(.*?)\}\}'
            employJob=re.findall(pattern,employList[0])
            for j in employJob:
                pattern='"name":(.*?),'
                jobList.append(re.findall(pattern,j))    
        return jobList
    

    
    ##爬取粉丝总数可以用以下链接每次智能返回20个
    ##https://www.zhihu.com/api/v4/members/jiayangqing/followers?limit=20&offset=19
def testAuthor():
    author=[]
    f=open("F:\\Database\zhihu\\知乎账户.txt","rb")
    lines=f.readlines()
    f.close()
    import os
    for l in lines:
        if b"Bearer" in l:
            author.append(l.decode().replace(os.linesep,"").replace("authorization:",""))
    print(author)
    user_url = 'https://www.zhihu.com/api/v4/members/{user}?include={include}'
    follows_url = 'https://www.zhihu.com/api/v4/members/{user}/followees?include={include}&offset={offset}&limit={limit}'
    followers_url = 'https://www.zhihu.com/api/v4/members/{user}/followers?include={include}&offset={offset}&limit={limit}'
    answers_url='https://www.zhihu.com/api/v4/members/{user}/answers?include={include}&offset={offset}&limit={limit}'
    question_url='https://www.zhihu.com/api/v4/members/{user}/questions?offset={offset}&limit={limit}'
    article_url='https://www.zhihu.com/api/v4/members/{user}/articles?include={include}&offset={offset}&limit={limit}'
    user = 'zhang-jia-wei'
    user_query = 'locations,employments,gender,educations,business,voteup_count,thanked_Count,follower_count,following_count,cover_url,following_topic_count,following_question_count,following_favlists_count,following_columns_count,answer_count,articles_count,pins_count,question_count,commercial_question_count,favorite_count,favorited_count,logs_count,marked_answers_count,marked_answers_text,message_thread_token,account_status,is_active,is_force_renamed,is_bind_sina,sina_weibo_url,sina_weibo_name,show_sina_weibo,is_blocking,is_blocked,is_following,is_followed,mutual_followees_count,vote_to_count,vote_from_count,thank_to_count,thank_from_count,thanked_count,description,hosted_live_count,participated_live_count,allow_message,industry_category,org_name,org_homepage,badge[?(type=best_answerer)].topics'
    follows_query = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'
    followers_query = 'data[*].answer_count,articles_count,gender,follower_count,is_followed,is_following,badge[?(type=best_answerer)].topics'
    answers_query="data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cupvoted_followees%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics"
    article_query='data[*].comment_count,content,voteup_count,created,updated'
    urlhead=[user_url,follows_url,followers_url,answers_url,article_url,question_url]
    urlquery=[user_query,follows_query,followers_query,answers_query,article_query]
    urlList=[]
    for i,head in enumerate(urlhead):
        if i!=len(urlhead)-1:
            url=head.format(user=user,include=urlquery[i],offset=0,limit=20)
        else:
            url=head.format(user=user,offset=0,limit=20)
        urlList.append(url)        
    headers = {'User-Agent': 'BaiDuSpider','authorization':'',}
    for url in urlList:
        r=requests.get(url,headers=headers)
        try:
            a=re.findall(user+"/(.*?)\?",url)[0]
        except Exception:
            a=''
        print("%s,%d" %(a,r.status_code))
    use_author =[]
    for au in author:
        headers['authorization']=au
        for url in urlList:
            r=requests.get(url,headers=headers)
            try:
                a=re.findall(user+"/(.*?)\?",url)[0]
            except Exception:
                a=''
            if r.status_code==200:
                use_author.append(au)
            print("%s,%d" %(a,r.status_code))        
    print(use_author)
    
    from selenium import webdriver
    from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
    from selenium.webdriver.common.keys import Keys
    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36")    
    browser = webdriver.PhantomJS(executable_path="F:\\DevTools\\phantomjs-2.1.1-windows\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe", desired_capabilities=dcap)
    browser.set_window_size(1920, 1080)
    browser.get("https://www.zhihu.com/#signin")
    #name[0].send_keys(Keys.CONTROL,"a")
    #name[0].send_keys(Keys.DELETE)
    name=browser.find_elements_by_name("account")
    name[0].send_keys("+17692225415")
    p=browser.find_element_by_xpath("//input[@placeholder='密码']")
    
    import requests
    import re
    import json
    import http.cookiejar
    s=requests.session()
    # 建立LWPCookieJar实例，可以存Set-Cookie3类型的文件。
    # 而MozillaCookieJar类是存为'/.txt'格式的文件    
    s.cookies = http.cookiejar.LWPCookieJar("cookie")
    # 若本地有cookie则不用再post数据了
    try:
        s.cookies.load(ignore_discard=True)
    except IOError:
        print('Cookie未加载！')    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 '
               '(KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36',
               "Referer": "https://www.zhihu.com/",}
    
          
       
    #'33626564373335362d633864342d346232382d623262312d356565323964643832336365'
    r=s.get('https://www.zhihu.com', headers=headers)    
    pattern='_xsrf\" value=\"(.*?)\"'
    xsrfList=re.findall(pattern,r.text)
    xsrf=xsrfList[0]
    data={"_xsrf":"e022888799a994545d70524da91f4970","password":"abcd1234","phone_num":"+17692225415"}
    data["_xsrf"]=xsrf
    url="https://zhihu-web-analytics.zhihu.com/api/v1/logs/batch"
    r=s.get(url,headers=headers)
    r=s.post(url="https://www.zhihu.com/login/phone_num",data=data,headers=headers)
    if (json.loads(r.text))["r"] == 1:
        import time
        t = str(int(time.time() * 1000))
        captcha_url = 'http://www.zhihu.com/captcha.gif?r=' + t + "&type=login"
        r=s.get(captcha_url, headers=headers)
        with open('F:\\Database\\zhihu\\cptcha.gif', 'wb') as f:
            f.write(r.content)
        data['captcha']="p6xd"
        r=s.post(url="https://www.zhihu.com/login/phone_num",data=data,headers=headers)
        if (json.loads(r.text))["r"] == 0:
            author=eval(r.cookies["z_c0"])
            headers={'User-Agent': 'BaiDuSpider', 'authorization': 'oauth c3cef7c66a1843f8b3a9e6a1e3160e20'}
            headers["authorization"]="Bearer "+author
            user_url = 'https://www.zhihu.com/api/v4/members/{user}?include={include}'
            user_query = 'locations,employments,gender,educations,business,voteup_count,thanked_Count,follower_count,following_count,cover_url,following_topic_count,following_question_count,following_favlists_count,following_columns_count,answer_count,articles_count,pins_count,question_count,commercial_question_count,favorite_count,favorited_count,logs_count,marked_answers_count,marked_answers_text,message_thread_token,account_status,is_active,is_force_renamed,is_bind_sina,sina_weibo_url,sina_weibo_name,show_sina_weibo,is_blocking,is_blocked,is_following,is_followed,mutual_followees_count,vote_to_count,vote_from_count,thank_to_count,thank_from_count,thanked_count,description,hosted_live_count,participated_live_count,allow_message,industry_category,org_name,org_homepage,badge[?(type=best_answerer)].topics'
            user='zhang-jia-wei'
            url=user_url.format(user=user, include=user_query)
            r=s.get(url,headers=headers)            
    
if __name__ == '__main__':
    user_url = 'https://www.zhihu.com/api/v4/members/{user}?include={include}'
    user_query = 'locations,employments,gender,educations,business,voteup_count,thanked_Count,follower_count,following_count,cover_url,following_topic_count,following_question_count,following_favlists_count,following_columns_count,answer_count,articles_count,pins_count,question_count,commercial_question_count,favorite_count,favorited_count,logs_count,marked_answers_count,marked_answers_text,message_thread_token,account_status,is_active,is_force_renamed,is_bind_sina,sina_weibo_url,sina_weibo_name,show_sina_weibo,is_blocking,is_blocked,is_following,is_followed,mutual_followees_count,vote_to_count,vote_from_count,thank_to_count,thank_from_count,thanked_count,description,hosted_live_count,participated_live_count,allow_message,industry_category,org_name,org_homepage,badge[?(type=best_answerer)].topics'
    user='shuoliu'
    url=user_url.format(user=user, include=user_query)
    headers={'User-Agent': 'BaiDuSpider', 'authorization': 'oauth c3cef7c66a1843f8b3a9e6a1e3160e20'}
    import requests
    import json
    r=requests.get(url,headers=headers)
    result=json.loads(r.text)
    #result={'show_sina_weibo': False, 'following_topic_count': 0, 'name': '张佳玮', 'educations': [], 'is_active': 1, 'gender': 1, 'thank_to_count': 0, 'following_question_count': 2726, 'question_count': 0, 'thank_from_count': 0, 'url': 'http://www.zhihu.com/api/v4/people/f9de84865e3e8455a09af78bfe4d1da5', 'mutual_followees_count': 0, 'is_followed': False, 'avatar_url_template': 'https://pic2.zhimg.com/424c70919_{size}.jpg', 'following_columns_count': 1, 'favorited_count': 1172546, 'is_following': False, 'url_token': 'zhang-jia-wei', 'marked_answers_count': 135, 'is_blocking': False, 'is_advertiser': False, 'following_count': 84, 'voteup_count': 3797538, 'answer_count': 3048, 'is_org': False, 'locations': [], 'articles_count': 727, 'is_blocked': False, 'is_bind_sina': False, 'description': '', 'message_thread_token': '1346424000', 'pins_count': 44, 'account_status': [], 'headline': '公众号：张佳玮写字的地方', 'follower_count': 1408476, 'allow_message': False, 'favorite_count': 0, 'cover_url': 'https://pic3.zhimg.com/v2-7b83d3b9bde245f3bd151aab695725d6_b.jpg', 'following_favlists_count': 0, 'id': 'f9de84865e3e8455a09af78bfe4d1da5', 'vote_to_count': 0, 'type': 'people', 'participated_live_count': 3, 'vote_from_count': 0, 'commercial_question_count': 0, 'logs_count': 11, 'hosted_live_count': 12, 'user_type': 'people', 'is_force_renamed': False, 'avatar_url': 'https://pic2.zhimg.com/424c70919_is.jpg', 'badge': [{'description': '优秀回答者', 'topics': [{'url': 'http://www.zhihu.com/api/v4/topics/19556423', 'introduction': '文学是语言的艺术，包括戏剧、诗歌、小说、散文等，是文化的重要组成部分。', 'name': '文学', 'excerpt': '文学是语言的艺术，包括戏剧、诗歌、小说、散文等，是文化的重要组成部分。', 'avatar_url': 'https://pic3.zhimg.com/cf0156d3a_is.jpg', 'id': '19556423', 'type': 'topic'}], 'type': 'best_answerer'}], 'thanked_count': 581269, 'employments': [], 'marked_answers_text': '知乎周刊、知乎圆桌和编辑推荐'}
    ZhuanlanSpider.DealResult(result)
    print(result)
'''
 Scrapy提供了log功能。您可以通过 logging 模块使用
 Log levels
 Scrapy提供5层logging级别:
    CRITICAL - 严重错误(critical)
    ERROR - 一般错误(regular errors)
    WARNING - 警告信息(warning messages)
    INFO - 一般信息(informational messages)
    DEBUG - 调试信息(debugging messages)
默认情况下python的logging模块将日志打印到了标准输出中，且只显示了大于等于WARNING级别的日志，这说明默认的日志级别设置为WARNING（日志级别等级CRITICAL > ERROR > WARNING > INFO > DEBUG，默认的日志格式为DEBUG级别


    {paging: {is_end: false, totals: 39896,…},…}
data:[{avatar_url_template: "https://pic1.zhimg.com/da8e974dc_{size}.jpg", name: "蘑菇菇家小小孩",…},…]
0:{avatar_url_template: "https://pic1.zhimg.com/da8e974dc_{size}.jpg", name: "蘑菇菇家小小孩",…}
1:{avatar_url_template: "https://pic1.zhimg.com/v2-6b76d76f67cf5f067d3f7d990026bb0c_{size}.jpg",…}
...
{avatar_url_template: "https://pic4.zhimg.com/887b34ac481efeb40b096751e93b655b_{size}.jpg", name: "阿飞",…}
19:{avatar_url_template: "https://pic2.zhimg.com/2a6c6c37a36d25a46a4a574e792eb419_{size}.jpg",…}
avatar_url:"https://pic2.zhimg.com/2a6c6c37a36d25a46a4a574e792eb419_is.jpg"
avatar_url_template:"https://pic2.zhimg.com/2a6c6c37a36d25a46a4a574e792eb419_{size}.jpg"
badge:[]
gender:-1
headline:""
id:"f8e5d7450ba581f4fc860a650b112231"
is_advertiser:false
is_org:false
name:"bao"
type:"people"
url:"http://www.zhihu.com/api/v4/people/f8e5d7450ba581f4fc860a650b112231"
url_token:"bao-51-28"
user_type:"people"
paging:{is_end: false, totals: 39896,…}
is_end:false
is_start:false
next:"http://www.zhihu.com/api/v4/members/jiayangqing/followers?limit=20&offset=39"
previous:"http://www.zhihu.com/api/v4/members/jiayangqing/followers?limit=20&offset=0"
totals:39896

user_url = 'https://www.zhihu.com/api/v4/members/{user}?include={include}'
user_query = 'locations,employments,gender,educations,business,voteup_count,thanked_Count,follower_count,following_count,cover_url,following_topic_count,following_question_count,following_favlists_count,following_columns_count,answer_count,articles_count,pins_count,question_count,commercial_question_count,favorite_count,favorited_count,logs_count,marked_answers_count,marked_answers_text,message_thread_token,account_status,is_active,is_force_renamed,is_bind_sina,sina_weibo_url,sina_weibo_name,show_sina_weibo,is_blocking,is_blocked,is_following,is_followed,mutual_followees_count,vote_to_count,vote_from_count,thank_to_count,thank_from_count,thanked_count,description,hosted_live_count,participated_live_count,allow_message,industry_category,org_name,org_homepage,badge[?(type=best_answerer)].topics'
follows_url = 'https://www.zhihu.com/api/v4/members/{user}/followers?include={include}&offset={offset}&limit={limit}'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
'Upgrade-Insecure-Requests':'1',
'authorization': 'oauth c3cef7c66a1843f8b3a9e6a1e3160e20',}
r=requests.get(url,headers=headers)
dic=json.loads(r.text)
dic['educations'][0]['school']["name"]

    <a class="UserLink-link" target="_blank" href="/people/zhang-lei-99-40">石石石</a>
    '''
    
