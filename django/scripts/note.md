The follows might be useful.
1. django-dashing       https://github.com/talpor/django-dashing.git
2. django-analytical    https://github.com/jcassee/django-analytical.git
3. Django SQL Explorer  https://github.com/groveco/django-sql-explorer.git

docker rmi `docker images | awk '$1=="<none>" || NR==0 {printf "%-1s ",$3}'`
docker-compose stop;docker-compose rm -f;docker-compose build; docker-compose up;

#run mysql at first
#wait 10 seconds to make sure that mysql service has been started-up
#create djangodb database using the below command.
docker exec -it mysql1 mysql -uroot -ppassword -e 'CREATE DATABASE djangodb CHARACTER SET utf8;'
#start django.

docker exec -it mysql1 mysql -uroot -ppassword -e 'show databases;use djangodb;show tables;'