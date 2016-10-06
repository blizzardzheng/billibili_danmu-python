VIRTUALENV = $(shell which virtualenv)

send: 
	python send.py
receive: 
	python receive.py