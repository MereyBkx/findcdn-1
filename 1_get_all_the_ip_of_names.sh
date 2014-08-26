#/bin/bash

dnsservers=( 
           "129.250.35.250" "129.250.35.251" "208.67.222.222" "208.67.220.220"
           "208.67.220.123" "74.82.42.42" "2001:4860:4860::8888" "2001:4860:4860::8844"
           "2620:0:ccc::2" "2620:0:ccd::2" "2001:470:20::2" "202.112.112.100" "101.226.4.6" "114.114.114.110" "114.114.114.114" "8.8.8.8")

temp=` redis-cli zrevrange cache 0 -1  |sed 's/^.//' `
read -a namelist <<< $temp

for name in ${namelist[@]};do
	for server in ${dnsservers[@]}; do
		nslookup $name $server >/root/servernametmp
		temp=`cat /root/servernametmp|grep 'Address:'|grep -v '#'|grep -oP '[\d]+\.[\d]+\.[\d]+\.[\d]+' `
		read -a iplist <<< $temp
		for ip in  ${iplist[@]};do
			redis-cli sadd iplist@$name $ip
		done
		echo $name@$server
		sleep 1
	done
done
