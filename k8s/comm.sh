#!/bin/bash
#节点打标签
kubectl label nodes xxxnode key=value
#停止更新操作
kubectl rollout pause deployment/nginx-deployment
#修改镜像
kubectl set image deploy/nginx-deployment nginx=nginx:1.9.1
#查看历史记录
kubectl rollout history deployment/nginx_deployment
#更新容器资源限制
kubectl set resources deployment nginx_deployment -c=nginx --limit=cpu=200m,memory=512Mi
#恢复
kubectl rollout resume deploy nginx_deployment
#升级命令
kubectl rolling-update redis-master -f resis-controller-new.yaml