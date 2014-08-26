import redis
import json
import urllib

r = redis.StrictRedis(host='localhost', port=6379, db=0)
names=r.keys('ipinfo@*')
for name in names:
	allIpInfo=r.smembers(name)
	#print type(allNamesIpSetList)
	#print allNamesIpSetList
	print name
	for ipInfo in allIpInfo:
		jsondata = json.loads(ipInfo)
		if jsondata[u'code'] == 0:
	        	#print 'Country :' + jsondata[u'data'][u'country'].encode('utf-8')
	        	#print 'Area    :' + jsondata[u'data'][u'area'].encode('utf-8')
	        	#print 'Province:' + jsondata[u'data'][u'region'].encode('utf-8')
	        	#print 'City    :' + jsondata[u'data'][u'city'].encode('utf-8')
	        	#print 'ISP     :' + jsondata[u'data'][u'isp'].encode('utf-8')
			#infoextract=dict()
			#infoextract['Country :']=jsondata[u'data'][u'country']
			locationInfo=jsondata[u'data']
			
			s='{'
			s=s+'"country_id":"'+locationInfo["country_id"]+'",'
			s=s+'"country":"'+locationInfo["country"]+'",'
			s=s+'"area_id":"'+locationInfo["area_id"]+'",'
			s=s+'"area":"'+locationInfo["area"]+'",'
			s=s+'"region_id":"'+locationInfo["region_id"]+'",'
			s=s+'"region":"'+locationInfo["region"]+'",'
			s=s+'"city_id":"'+locationInfo["city_id"]+'",'
			s=s+'"city":"'+locationInfo["city"]+'",'
			s=s+'"county_id":"'+locationInfo["county_id"]+'",'
			s=s+'"county":"'+locationInfo["county"]+'",'
			s=s+'"isp_id":"'+locationInfo["isp_id"]+'",'
			s=s+'"isp":"'+locationInfo["isp"]+'"'
			s=s+'}'
			r.sadd('locationInfor@'+name,s)
