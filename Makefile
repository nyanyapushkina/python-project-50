install:
	poetry install

lint:
	poetry run flake8 gendiff

generate-diff:
	poetry run generate-diff

build: 
	poetry build

publish: 
	poetry publish --dry-run

package-install: 
	python3 -m pip install --user dist/*.whl