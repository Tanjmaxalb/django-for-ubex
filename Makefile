image_name := django_demo
port := 8080

mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
data_folder := $(dir $(mkfile_path))data

super_user_name := super_user

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
	docker run --rm \
	    -v $(data_folder):/project/data \
	    $(image_name) migrate

create-super-user:
	docker run --rm -it \
	    -v $(data_folder):/project/data \
	    $(image_name) createsuperuser \
		--username $(super_user_name) \
		--email $(super_user_name)@mail.com

print_token:
	@echo $$( \
	    docker run --rm \
		-v $(data_folder):/project/data \
		$(image_name) drf_create_token $(super_user_name) \
	) | cut -d ' ' -f3

clean:
	sudo rm -rf $(data_folder)
