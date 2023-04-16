init:
	pip3 install -r requirements.txt

start: source/entry.py source/.env init
	python3 source/entry.py
