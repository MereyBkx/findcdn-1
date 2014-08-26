import redis
import urllib

r = redis.StrictRedis(host='localhost', port=6379, db=0)
allNamesIpSetList=r.keys('iplist@*')
#print type(allNamesIpSetList)
#print allNamesIpSetList
for name in allNamesIpSetList:
	ipSet=r.smembers(name)
	#print type(ipSet)
	for ip in ipSet:
		print ip
		page=urllib.urlopen('http://ip.taobao.com/service/getIpInfo.php?ip='+ip)
		ipInformation=page.read();
		#print ipInformation
		r.sadd("ipinfo@"+name,ipInformation)
	#print ''
	print name
	#print ipSet



