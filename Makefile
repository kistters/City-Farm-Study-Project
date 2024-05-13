COMPOSE_DEV_FILES := -f docker-compose.yml -f docker-compose.dev.yml

start:
	docker-compose $(COMPOSE_DEV_FILES) up --build -d

test:
	docker-compose $(COMPOSE_DEV_FILES) exec -T backend-django python manage.py test

developer:
	docker-compose $(COMPOSE_DEV_FILES) up

production:
	docker-compose -f docker-compose.yml up

