# encoding=utf8  

import sys  

reload(sys)  

sys.setdefaultencoding('utf8')   
 
import urllib
import urllib2
import re
 

#爬取老番茄视屏信息
class Spider:
 
    def __init__(self):
        self.siteURL = 'http://space.bilibili.com/ajax/channel/getChannel?mid=546195&guest=1'
 
    def getPage(self,pageIndex):
        url = self.siteURL 
        
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        return response.read().decode('utf-8')
 
    def getContents(self,pageIndex):
        page = self.getPage(pageIndex)
        return page
      
spider = Spider()
res=spider.getContents(1)
