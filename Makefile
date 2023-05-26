all:

build:
	rm -f dist/*
	poetry build -f wheel

publish: build
	twine upload dist/*whl


bump:
	./bump-version.sh patch

bump-minor:
	./bump-version.sh minor

bump-major:
	./bump-version.sh major
