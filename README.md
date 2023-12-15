
Hello Farmers and Citizens

Follow terminal command

```
$ sudo sh -c 'echo "0.0.0.0 api.cityfarm.com cityfarm.com" >> /etc/hosts'
$ docker-compose up
```

access: 

http://api.cityfarm.com

http://api.cityfarm.com/admin

http://cityfarm.com


useful commands:

```shell
$ docker-compose run --rm backend-django python manage.py collectstatic --noinput
$ docker-compose run --rm backend-django python manage.py migrate
```