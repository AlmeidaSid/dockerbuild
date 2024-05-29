.PHONY: build test deploy

build:
    docker-compose build

test:
    docker-compose run --rm test

deploy:
    docker-compose up -d
