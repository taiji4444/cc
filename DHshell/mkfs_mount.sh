#!/bin/bash
disk=/dev/$1
datadir=$2
if [ $# -ne 2 ];then
	echo "argment error"
	echo "exmple:sh $0 sdb /data"
	exit 1 
fi
if [ ! -d $datadir ];then
	mkdir -p $datadir
fi
flag=`fdisk -l | grep $disk| wc -l`
if [ $flag -eq 1 ];then
	mkfs.xfs $disk
else
	echo "$disk not exits "
	exit 1	
fi
if [ $? -ne 0 ];then
	echo "format disk failed: $disk"
fi
uuid=`blkid $disk`
if [ "${datadir:0:1}" ==  '/' ];then
	sed  "$datadir/d" /etc/fstab
else
	sed  "/$datadir/d" /etc/fstab
fi
echo "UUID=$uuid $datadir  xfs defaults 0 0" >> /etc/fstab
