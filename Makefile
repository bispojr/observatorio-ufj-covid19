runserver:
	# sua versao do python 
	python3.8 manage.py runserver

migrate:
	# migracao das tabela de banco de dados	 
	python3.8 manage.py makemigrations
	python3.8 manage.py migrate
	


