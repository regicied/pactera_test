# Welcome to the WeatherGetter !

![avatar](FilesFolder/imageonline-co-textimage_1.png)


[![standard-readme compliant](https://api.travis-ci.org/spacewander/termdump.svg)](http://100.98.97.86)
[![standard-readme compliant](https://img.shields.io/badge/lincense-sdu_cn_cloud-green)](https://gitlab.rosetta.ericssondevops.com/sdu-cn/sdu-cn-cloud)

It is a platform to get a specify city's weather

# README

A platform for City's Weathter

Our team will keep on going all the time 🚀 ~

## Table of Contents

- [Background](#background)
- [Installation](#Installation)
- [Usage](#usage)
	- [YamlGenerator](#YamlGenerator)
	- [EriCIC](#EriCIC)
- [Related Efforts](#related-efforts)
- [Maintainers](#maintainers)
- [Contributing](#contributing)
- [License](#license)

## Background

Optimus started with the issue originally posed by [@randolph](https://gitlab.rosetta.ericssondevops.com/randolph.zhang) and [@leon](https://gitlab.rosetta.ericssondevops.com/leon.w.liu)
 during the CEE-NEXT's daily maintenance work, about the if the CEE-Next's daily maintenance work can be automated.
 After a lot of discussion, out team decided to develop the platform from the yamlGen function and info dashboard.
With all [team](#contributing)'s effort, Optimus grown step by step and will make it a easier work about CEE-Next's operation and maintenance. 

The goals for the platform are:

>1. Save the time for the preparing of config yaml
>2. Monitor the CEE-Next status
>3. Customize scheduler task for maintenance and operation periodic work 
>4. Check the health of CEE-Next and alarm 
 
 
## Installation

👉 This installation guid is just for the Optimus's backend.

### Installation base on file

#### Prepare environment 

* Hardware dependent

    - Centos 7.0
    - Core 2 +
    - Memory 2GB +
    - Disk 1GB +
 
* Software dependent

    - python 3.8
    - torando 6.1
 
#### Install python package


Download requirement for gitlab repository

    
```sh
wget https://gitlab.rosetta.ericssondevops.com/gaofeng.a.zhang/optimus/-/blob/master/requirement.txt
```
    

Install package with [requirement.txt](https://gitlab.rosetta.ericssondevops.com/gaofeng.a.zhang/optimus/-/blob/master/requirement.txt)

    
```sh
$ sudo pip install -r requirement.txt
```

Start Optimus backend service

```sh
# download the backend file
$ sudo gitclone https://gitlab.rosetta.ericssondevops.com/sdu-cn/sdu-cn-cloud/optimus.git

# go to the project floder
$ cd optimus

# start the service with gunicorn
$ sudo nohup  nohup gunicorn --workers=5  --timeout=10  main:app -b 0.0.0.0:8000 &


docker run -it -d  --rm --name rabbitmq -p 1234:5672 -p 12345:15672 rabbitmq:3-management


root@c079ac07cb22:/# rabbitmqctl add_user root optimus
Adding user "root" ...
root@c079ac07cb22:/#
root@c079ac07cb22:/#
root@c079ac07cb22:/#
root@c079ac07cb22:/# rabbitmqctl add_vhost db_refresh
Adding vhost "db_refresh" ...
root@c079ac07cb22:/#
root@c079ac07cb22:/#
root@c079ac07cb22:/#
root@c079ac07cb22:/#
root@c079ac07cb22:/# rabbitmqctl set_permissions -p db_refresh root ".*" ".*" ".*"
Setting permissions for user "root" in vhost "db_refresh" ...
root@c079ac07cb22:/#
root@c079ac07cb22:/#
root@c079ac07cb22:/#
root@c079ac07cb22:/#
root@c079ac07cb22:/#
root@c079ac07cb22:/#
root@c079ac07cb22:/# rabbitmqctl list_vhosts
Listing vhosts ...
name
db_refresh
/
root@c079ac07cb22:/#
root@c079ac07cb22:/#
root@c079ac07cb22:/#
root@c079ac07cb22:/# rabbitmqctl set_user_tags root administrator
Setting tags for user "root" to [administrator] ...

 
```
    
### Installation base on docker

image 路径：https://ericsson.sharepoint.com/sites/cloud-optimus/Release/Forms/AllItems.aspx

 

    TBD
    
    
    optimus runner
    docker run -d  --name optimus_runner -v /root/gaofzhan/root/gaofzhan:/optimus --privileged=true  --net=host  optimus-exec-container   /bin/bash -c "source optimus_env/bin/activate;cd /optimus; nohup gunicorn --workers=5 --timeout=5  main:app -b 0.0.0.0:8000"
    
    celery worker 
    docker run -d  --name celery_runner -v /root/gaofzhan/root/gaofzhan:/optimus --privileged=true  --net=host  optimus-exec-container   /bin/bash -c "source optimus_env/bin/activate;cd /optimus/celeryFolder; nohup celery -A celery_app.celery_app worker -l info"
    
    mongo
    docker run --privileged=true  -d --net=host --name optimus_mongo -e MONGO_INITDB_ROOT_USERNAME=root -e MONGO_INITDB_ROOT_PASSWORD=optimus -v /root/mongo_data:/data/db mongo
    
    docker run -d  --name optimus_runner -v /root/gaofzhan/root/gaofzhan:/optimus --privileged=true  --net=host  optimus-exec-container   /bin/bash -c "source optimus_env/bin/activate;cd /optimus; nohup gunicorn --workers=5 --timeout=5  main:app -b 0.0.0.0:8000"

    docker run -d  --name redis_runner --privileged=true --net=host redis 
    
    
    RUN mysql -u root -p$MYSQL_ROOT_PASSWORD -e "create database if not exists optimus" && mysql -u root -p$MYSQL_ROOT_PASSWORD 
    
    
    docker run -d --name mysql_runner  --net=host  --privileged=true  -e MYSQL_ROOT_PASSWORD=optimus -v mysql_data:/var/lib/mysql  mysql
    
    
    docker run -d --name mysql_runner  --net=host  --privileged=true  -e MYSQL_ROOT_PASSWORD=optimus -v /home/ecap/etiaguo/Optimus/mysql_data:/var/lib/mysql  mysql
    
    
     docker run -d  --name redis_runner --privileged=true --net=host  -v /home/ecap/etiaguo/Optimus/redis_conf:/etc/redis/ redis
     
     
     docker run  -d --name redis_runner  --privileged=true --net=host -v /home/ecap/etiaguo/Optimus/redis_conf:/etc/redis/  redis redis-server /etc/redis/redis.conf
     
     docker run -v /myredis/conf:/usr/local/etc/redis --name myredis redis redis-server /usr/local/etc/redis/redis.conf
     
     
     docker run -d --name nginx_runner --net=host -v /home/ecap/etiaguo/Optimus/nginx_conf:/etc/nginx/conf.d nginx
     
     /home/ecap/etiaguo/Optimus/webapp
     
     docker run -d  --name celery_runner -v /home/ecap/etiaguo/Optimus/optimus_code:/optimus --privileged=true  --net=host  optimus-exec-container:v1.2   /bin/bash -c "source optimus_env/bin/activate;cd /optimus/celeryFolder; nohup celery -A celery_app.celery_app worker -l info"
     
     docker run -d  --name optimus_runner -v /home/ecap/etiaguo/Optimus/optimus_code:/optimus --privileged=true  --net=host  optimus-exec-container   /bin/bash -c "source optimus_env/bin/activate;cd /optimus; nohup gunicorn --workers=5 --timeout=5  main:app -b 0.0.0.0:8000"
     
    
    单实例部署命令
     
     
    optimus-backend-container
	    docker run -d  --name optimus_runner -v {项目代码绝对路径}:/optimus --privileged=true  --net=host  optimus-exec-container:{tag}   /bin/bash -c "source optimus_env/bin/activate;cd /optimus; nohup gunicorn --workers={后台worker数量} --timeout={request超时时间}  main:app -b 0.0.0.0:{项目监听端口(建议8000)}"
    
    celery-executor-container
        docker run -d  --name celery_runner -v {项目代码绝对路径}:/optimus --privileged=true  --net=host  optimus-exec-container:{tag}   /bin/bash -c "source optimus_env/bin/activate;cd /optimus/celeryFolder; nohup celery -A celery_app.celery_app worker -l info"
        
    mongodb-service-container
        docker run --privileged=true  -d --net=host --name optimus_mongo -e MONGO_INITDB_ROOT_USERNAME=root -e MONGO_INITDB_ROOT_PASSWORD=optimus -v {数据持久化文件夹绝对路径}:/data/db mongo:{tag}
        
    frontend-service-container(base on nginx server)
        docker run -d --name nginx_runner --net=host -v {nginx配置文件绝对路径}:/etc/nginx/conf.d -v {前端代码绝对路径}:/webapp/build nginx
    
    mysql-service-container	
        docker run -d --name mysql_runner  --net=host  --privileged=true  -e MYSQL_ROOT_PASSWORD=optimus -v {数据持久化文件夹绝对路径}:/var/lib/mysql  mysql
        
    redis-service-container	
        docker run  -d --name redis_runner  --privileged=true --net=host -v {redis配置文件绝对路径}:/etc/redis/  redis redis-server /etc/redis/redis.conf
    
    rabbitmq-service-container
        docker run -d  --rm --name rabbitmq -p 1234:5672 -p 12345:15672 rabbitmq:3-management
        docker exec -ti rabbitmq bash
        rabbitmqctl add_user root optimus
        rabbitmqctl add_vhost db_refresh
        rabbitmqctl set_permissions -p db_refresh root ".*" ".*" ".*"
        rabbitmqctl set_user_tags root administrator
     
    
    
## Usage

This is only a documentation package. You can print out [spec.md](spec.md) to your console:

```sh
$ standard-readme-spec
# Prints out the standard-readme spec
```

### YamlGenerator

To use the generator, look at [generator-standard-readme](https://github.com/RichardLitt/generator-standard-readme). There is a global executable to run the generator in that package, aliased as `standard-readme`.

### EriCIC

To use the generator, look at [generator-standard-readme](https://github.com/RichardLitt/generator-standard-readme). There is a global executable to run the generator in that package, aliased as `standard-readme`.

## Related Efforts

- [CICD PIPLINE](https://gitlab.rosetta.ericssondevops.com/jason) - 💌 Supported by Jason Tian.
- [RESOURCE_COORDINATE]() - 🍹 Supported by Claire Jiao.

## Maintainers

[@CMCC_Automation](https://gitlab.rosetta.ericssondevops.com/sdu-cn/sdu-cn-cloud/cmcc_automation).

## Contributing



### Contributors

This project exists thanks to all the people who contribute.  (in no particular order)


## License

