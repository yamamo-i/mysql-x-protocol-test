# MySQL X Protocol test

## 概要

* MySQLのX Protocolの動作確認をするレポジトリ  
https://dev.mysql.com/doc/refman/8.0/en/document-store.html

## 環境

* Docker Image
    * mysql:8.0.13  
    https://hub.docker.com/_/mysql/
* python: 3.7.1
    * python-connector  
    https://pypi.org/project/mysql-connector-python/

## MySQL環境の用意

* docker imageの用意
```sh
$ docker build -t mysql:8.0.13-x .
or
$ docker pull yamamoi/mysql:8.0.13-x
https://hub.docker.com/r/yamamoi/mysql/
```
* 起動
```sh
$ docker run --name mysql --rm -d -p 3306:3306 -p33060:33060 --env MYSQL_ROOT_PASSWORD='root' mysql:8.0.13-x 
```

## 


