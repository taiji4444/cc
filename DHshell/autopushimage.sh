#!/bin/bash
aa=$(readlink -f $0)
cd $(dirname $aa)
for i in `ls *.tar`
do 
docker load -i $i >> load.log
done
sleep 10
while read line
do
docker push  "${line:14}">>push.log
done<load.log
