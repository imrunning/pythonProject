import urllib2, time


url = 'http://dj.qjmotor.com/wxCore/my/zzbAjax?state=votezwwz&id=1207&openid=oyi-HuFOLkMQejwKH2AyTl-'
index = 00040
totalPage = ""
while index < 10000:
    url2 = url +  str(index)
    request = urllib2.Request(url2)
    request.add_header('Referer', 'http://dj.qjmotor.com/wxCore/my/zwActionWJJ?code=0414V4Ct1wEzRa0pUYFt1ZOuCt14V4CO&state=zwbs_1207')
    response = urllib2.urlopen(request)
    result = response.read()
    index = index + 1
    print "vote count:"+result
    time.sleep(60)
