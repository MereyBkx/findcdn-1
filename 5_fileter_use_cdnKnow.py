import redis
import json
import urllib
import re

f=open('cdnKnown')
patterns=[]
for line in f:
	s=line.strip()
	pattern = re.compile('.*(\.|)'+s)
	patterns.append(pattern)



r = redis.StrictRedis(host='localhost', port=6379, db=0)
names=r.smembers('candidateHasCDN')

for name in names:
	flag=0
	for pattern in patterns:
		if pattern.match(name):
			flag=1
			#print 'Match:',name
			break
	if flag==0:
		print '\n\n',name
		locations=r.smembers(name)
		for location in locations:
			location=eval(location)
			print location['country']+'  '+ location['area']+ '  '+location['region']+ '  '+location['county']+ '  '+location['isp'] 
