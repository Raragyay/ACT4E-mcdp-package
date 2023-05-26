all:

.PHONY: build

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

docs:
	mkdocs build

docs-serve:
	mkdocs serve

pack:
	zuper-cli pack -d assets/test-data/downloaded --include '*yaml' -o src/act4e_mcdp/autogen_packed_test_data.py
