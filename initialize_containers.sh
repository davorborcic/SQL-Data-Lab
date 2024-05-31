#!/bin/zsh

docker  -v 2> /dev/null
if test  $? -ne 0; then
  echo "Docker not installed. Please install Docker before proceeding"
  exit 1
else
  echo "Verified: Docker Installed"
fi
read -s "mysqlpass?Provide the mysql root password\n"
read "local_path?Enter the full path to the MySQL local *root folder* for volumes and the config files"

if [[ -d "$local_path/volumes" && -f "$local_path/cfg/my.cnf" ]]; then
  echo "Volumes verified"
else
  echo "No proper volumes. Please create proper local volumes"
  exit 1
fi

docker pull mysql:latest
docker  run -d --name sqllab \
-e MYSQL_ROOT_PASSWORD=$mysqlpass \
-p 3306:3306 \
-v $local_path/volumes:/var/lib/mysql \
-v $local_path/cfg/my.cnf:/etc/mysql/my.cnf \
-v $local_path/dataload:/var/lib/mysql-files \
mysql:latest