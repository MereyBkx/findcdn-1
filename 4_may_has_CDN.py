import redis
import json
import urllib

r = redis.StrictRedis(host='localhost', port=6379, db=0)
names=r.keys('locationInfor@*')
count=1
for name in names:
	number=r.scard(name)
	#print type(allNamesIpSetList)
	#print allNamesIpSetList
	if number > 1:
		print name
		count=count+1

		locations=r.smembers(name)
		for location in locations:
			#print location
			location=eval(location)
			#print location
	        	s='Country :' + location['country']+'\n'
	        	s=s+'Area    :' + location['area']+'\n'
	        	s=s+'Province:' + location['region']+'\n'
	        	s=s+'City    :' + location['city']+'\n'
	        	s=s+'ISP     :' + location['isp']+'\n'
			r.sadd('decodeLocationInfor@'+name,s)
			r.sadd('candidateHasCDN',name);
			
