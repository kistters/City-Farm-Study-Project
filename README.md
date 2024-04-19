Hello Farmers and Citizens

Follow terminal command

```
$ sudo sh -c 'echo "0.0.0.0 api.cityfarm.com cityfarm.com" >> /etc/hosts'
$ docker-compose up
```

access: 

http://cityfarm.com
http://api.cityfarm.com

useful commands:

```shell
$ docker-compose run --rm backend-django python manage.py collectstatic --noinput
$ docker-compose run --rm backend-django python manage.py migrate

$ docker-compose up
```

data folder:

* here we will save logs/data end other good insight output from service
```shell
.data/nginx
.data/postgres
```
# install new libs 
```shell
cd backend-django
pipenv install --dev pytest pytest-asyncio
docker-compose build
```
