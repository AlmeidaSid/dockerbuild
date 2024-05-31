.PHONY: build test deploy

build:
    docker-compose build    

test:
    docker-compose run --rm test

deploy:
    docker-compose up -d


#Arquivo de Automatizacao dos 3 passos ate o Deploy