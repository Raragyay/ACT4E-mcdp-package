all:

build:
	rm -f dist/*
	poetry build

publish: build
	twine upload dist/*whl


bump:
	./bumpversion.sh patch

bump-minor:
	./bumpversion.sh minor

bump-major:
	./bumpversion.sh major
