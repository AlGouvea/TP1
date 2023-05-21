
build: clean
	docker build -t tdd-trab:latest --force-rm .

run_test: clean-container
	docker run -v $(PWD):/src --name tec-prog-trab1 tdd-trab:latest python3 -m pytest test_main.py 

run: clean-container 
	docker run -v $(PWD):/src --name tec-prog-trab1 tdd-trab:latest python3 main.py 

clean: clean-container
	-docker image rm tdd-trab:latest

clean-container:
	-docker rm tec-prog-trab1
