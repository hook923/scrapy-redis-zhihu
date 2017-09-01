#!user/bin/env python3
# -*- coding: utf-8 -*-

## Define here the models for your scraped items
##
## See documentation in:
## http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field
from scrapy.loader import ItemLoader 
from scrapy.loader.processors import MapCompose,TakeFirst,Join

'''
class zhuanlanSpiderLoader(ItemLoader):
	default_item_class=UserItem
	default_input_processor=MapCompose(lambda s:s.strip())
	default_output_processor=TakeFirst()
	description_out = Join()
'''
class ArticleItem(Item):
	url_token = Field()
	title = Field()
	id = Field()
	content = Field()
	excerpt = Field()
	excerpt_title =  Field()
	image_url = Field()
	type = Field()
	url = Field()
	cretated_time = Field()
	updated_time = Field()
	voteup_count = Field()
	comment_count = Field()
class AnswerItem(Item):
	url_token= Field()##
	id = Field()##
	question_id = Field()
	comment_count = Field()
	voteup_count = Field()
	content = Field()
	created_time = Field()
	updated_time = Field()
	url = Field()
class QuestionItem(Item):
	url_token = Field()
	created = Field()
	id = Field()
	question_type = Field()
	title = Field()	
	type = Field()
	updated_time = Field()
	url = Field()
class UserItem(Item):	
	##locations,employments,gender,educations,business,voteup_count,thanked_Count,follower_count,following_count,cover_url,following_topic_count,following_question_count,following_favlists_count,following_columns_count,answer_count,articles_count,pins_count,question_count,commercial_question_count,favorite_count,favorited_count,logs_count,marked_answers_count,marked_answers_text,message_thread_token,account_status,is_active,is_force_renamed,is_bind_sina,sina_weibo_url,sina_weibo_name,show_sina_weibo,is_blocking,is_blocked,is_following,is_followed,mutual_followees_count,vote_to_count,vote_from_count,thank_to_count,thank_from_count,thanked_count,description,hosted_live_count,participated_live_count,allow_message,industry_category,org_name,org_homepage,badge[?(type=best_answerer)].topics
	#accountStatus=Field()
	locations = Field()#所在地
	educations = Field()#教育背景
	employments = Field()#工作信息
	badge = Field()
	business = Field()
	
	id = Field()
	name = Field()#用户昵称
	avatar_url = Field()
	headline = Field()
	description = Field()#个人描述
	#url = Field()
	url_token = Field()#知乎给予的每个人用户主页唯一的ID
	gender = Field()
	#cover_url = Field()
	type = Field()
	is_active=Field()
	is_advertiser=Field() ##是否是广告用户
	is_org=Field()  ##是否是组织
	
	answer_count = Field()#回答数量
	articles_count = Field()#写过的文章数
	commercial_question_count = Field()
	favorite_count = Field()#收藏数量
	favorited_count = Field()#被收藏次数
	follower_count = Field()#粉丝数量
	following_columns_count = Field()#关注的专栏
	following_count = Field()#关注了多少人
	following_favlists_count = Field()#关注的收藏数量
	following_question_count = Field()#关注问题数量
	following_topic_count = Field()#关注话题数量
	hosted_live_count = Field()#举办live数
	logs_count = Field()#参与公共编辑
	marked_answers_count = Field()##知乎收录
	participated_live_count = Field()     
	pins_count = Field()#分享总数
	question_count = Field()#提问数量
	thank_from_count = Field()
	thank_to_count = Field()
	thanked_count = Field()#获得的感谢数
	vote_from_count = Field()
	vote_to_count = Field()
	voteup_count = Field()#获得的赞数 
	#mutual_followees_count = Field()##我关注的人中 人关注了他

'''
    account_status:[]
    allow_message:true
    answer_count:3045  回答3045
    articles_count:725  文章725
    avatar_url:"https://pic2.zhimg.com/424c70919_is.jpg"
    avatar_url_template:"https://pic2.zhimg.com/424c70919_{size}.jpg"
    commercial_question_count:0   商用问题
    badge:[]
    cover_url:"https://pic3.zhimg.com/v2-7b83d3b9bde245f3bd151aab695725d6_b.jpg"
    description:""
    educations:[]
    employments:[]
    favorite_count:0 收藏
    favorited_count:1167709 获得收藏
    follower_count:1404570  关注者
    following_columns_count:1  关注的专栏
    following_count:84   关注了
    following_favlists_count:0    关注的收藏夹
    following_question_count:2723 关注的问题
    following_topic_count:0  关注的话题
    gender:1 
    headline:"公众号：张佳玮写字的地方"
    hosted_live_count:12  举办的Live
    id:"f9de84865e3e8455a09af78bfe4d1da5"
    is_active:1
    is_advertiser:false  广告用户
    is_bind_sina:false
    is_blocked:false
    is_blocking:false
    is_followed:false
    is_following:false
    is_force_renamed:false
    is_org:false  组织
    locations:[]
    logs_count:11  参与了 次公共编辑
    marked_answers_count:135  知乎收录
    marked_answers_text:"知乎周刊、知乎圆桌和编辑推荐"
    message_thread_token:"1346424000"
    mutual_followees_count:10  我关注的人中 人关注了他
    name:"张佳玮"
    participated_live_count:3  参加的live
    pins_count:40  分享40
    question_count:0 
    show_sina_weibo:false
    thank_from_count:0
    thank_to_count:0
    thanked_count:579005  获得 次感谢
    type:"people"
    url:"http://www.zhihu.com/api/v4/people/f9de84865e3e8455a09af78bfe4d1da5"
    url_token:"zhang-jia-wei"
    user_type:"people"
    vote_from_count:0
    vote_to_count:1
    voteup_count:3774724  获得 次赞同
'''