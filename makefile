init:
	pip3 install -r requirements.txt

start: source/start.py source/.env
	python3 source/start.py
