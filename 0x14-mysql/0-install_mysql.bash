#!/usr/bin/env bash
# Install and configure MySQL

# Install MySQL
sudo apt-key add './mysql-5.7_signing.key'
sudo /bin/bash -c 'echo "deb http://repo.mysql.com/apt/ubuntu/ trusty mysql-5.7" > /etc/apt/sources.list.d/mysql.list'
sudo apt-get update
sudo apt-get install -y mysql-server mysql-client libmysqlclient-dev
