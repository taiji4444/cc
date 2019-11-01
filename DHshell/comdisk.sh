#!/bin/bash
aa=$(readlink -f $0)
cd $(dirname $aa)
cp id_rsa* /root/.ssh/
cat id_rsa.pub >>/root/.ssh/authorized_keys
chmod 600 /root/.ssh/id_rsa 
echo "overlay" > /etc/modules-load.d/overlay.conf
echo "macvlan" > /etc/modules-load.d/macvlan.conf
modprobe overlay
lsmod | grep overlay 
if [ $? -eq 0 ];then
	echo "overlay is ok"
else
	echo "overlay is failed"
fi
modprobe macvlan
lsmod | grep macvlan
if [ $? -eq 0 ];then
        echo "macvlan is ok"
else
        echo "maclan is failed"
fi

list=(
"/data1"
"/data2"
"/data3"
"/images"
"/dockerdata"
)
let i=0
for disk in `cat disk.list`
do 
	echo "$disk ${list[i]}"
#	mkfs_mount.sh $disk ${list[i]}
	i=$i+1
done
