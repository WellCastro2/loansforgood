build:
	docker-compose build
	docker-compose up image_db_api_data &
	sleep 10
	docker-compose up &
	sleep 15
	docker-compose run web python manage.py initadmin

run:
	docker-compose up &
