#!/bin/bash
pingTest()
{
#cat /home/check_tools/allIp.txt  | while read all_dn_ip
cat $1  | while read dn_ip
do
    /bin/ping -c 10 -w 10 $dn_ip > /tmp/$dn_ip &
    wait
#判断ping结果
    net_ok=1
    loss_packet=`/bin/grep loss /tmp/$dn_ip | awk 'BEGIN{FS=","}{for (i=1;i<=NF;i+=1){if ($i ~ /loss$/) {print $i;break}}}'|awk '{print $1}'`
    avg_time=`/bin/grep avg /tmp/$dn_ip | awk -F "/" '{print $5}'`
    if [[ "$loss_packet" > "0%" ]] || [[ "$avg_time" >  "2.0" ]]
    then
	echo -e "\e[1;41m [network]Ping$dn_ip丢包率:$loss_packet,平均延迟:$avg_time ms!\e[0m"
	net_ok=0
    fi
    if [ $net_ok -eq 1 ]
    then
	    echo "[network]Ping$dn_ip节点网络正常,没有丢包且延迟小于2.0ms!"
    fi
done
}
diskUse()
{
	for ip in `cat $1`
	do
		echo "[disk]$ip"
		ssh $ip "df  -h / /data1 /data2 /data3 /dockerdata /images" | awk '{if(int(substr($5,0,2))>=80) printf "\033[1;31m" $0 "\033[0m" "\n" ;else print $0 }' 
	done
}
dockerStatus()
{
	for ip in `cat $1`
	do
		status=`ssh $ip "systemctl status docker | grep Active" |awk '{print \$2}'`
		if [ $status == "active" ];then

			echo "[docker]$ip:$status"
		else
			echo -e "\e[1;41m [docker] $ip:$status \e[0m"
		fi
	done
}
kubletSttaus()
{
	for ip in `cat $1`
	do
		status=`ssh $ip "systemctl status kubelet | grep Active"  |awk '{print $2}'`
		if [ $status == "active" ];then
			echo "[kubelt]$ip:$status"
		else
			echo  -e "\e[1;41m [kubelt] $ip:$status \e[0m"
	done
}
podNetstatus()
{
	cat $1 | while read nip
	do
		name=`echo $nip | cut -f 1 -d ' '`
		ip=`echo $nip | cut -f 2 -d ' '`
		/bin/ping -c 10 -w 10 $ip > /tmp/$ip &
		wait
		#判断ping结果
		net_ok=1
		
		loss_packet=`/bin/grep loss /tmp/$ip | awk 'BEGIN{FS=","}{for (i=1;i<=NF;i+=1){if ($i ~ /loss$/) {print $i;break}}}'|awk '{print $1}'`
		avg_time=`/bin/grep avg /tmp/$ip | awk -F "/" '{print $5}'`
		if [[ "$loss_packet" > "0%" ]] || [[ "$avg_time" >  "2.0" ]]
		then
			echo -e "\e[1;41m[network] Ping $name :$ip丢包率:$loss_packet,平均延迟:$avg_time ms!\e[0m"
			net_ok=0
		fi
		if [ $net_ok -eq 1 ]
		then
			echo "[network]Ping 容器$name:$ip节点网络正常,没有丢包且延迟小于2.0ms!"
		fi
	done

}
pthost=$1
#获取宿主机节点ip地址 node.ip
mysql -h$pthost -P 13306 -uroot -p123456  --database=dahua_minicloud -N -e "select ip from node"  >node.ip
#获取容器ip pod.nameip
mysql -h$pthost -P13306 -uroot -p123456  --database=dahua_minicloud -N -e "select name ,ip  from pod "  >pod.nameip
#测试宿主机网络
pingTest node.ip
#宿主机硬盘使用情况
diskUse node.ip
#docker 运行状态
dockerStatus node.ip
#容器网络
podNetstatus pod.nameip
#kublet 网络
kubletSttaus node.ip
