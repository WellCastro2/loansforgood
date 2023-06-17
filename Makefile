build
	docker-compose build
	docker-compose up &
	sleep 3
	docker-compose run web python manage.py initadmin

run
	docker-compose up &
