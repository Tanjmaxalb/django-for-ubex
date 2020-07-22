image_name := django_demo
port := 8080

mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
data_folder := $(dir $(mkfile_path))data

build:
	docker build -t $(image_name) .

test:
	docker run --rm $(image_name) test

run:
	docker run --rm -it \
	    -p $(port):$(port) \
	    -v $(data_folder):/project/data \
	    $(image_name) runserver 0.0.0.0:$(port)

migrate:
	docker run --rm -it \
	    -v $(data_folder):/project/data \
	    $(image_name) migrate
