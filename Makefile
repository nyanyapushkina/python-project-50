install:
	poetry install

lint:
	poetry run flake8 brain_games

generate-diff:
	poetry run generate-diff

build: 
	poetry build

publish: 
	poetry publish --dry-run

package-install: 
	python3 -m pip install --user dist/*.whl