all:

build:
	rm -f dist/*
	poetry build

publish: build
	twine upload dist/*whl

bumpversion:
	poetry version patch

bumpversion-minor:
	poetry version minor
