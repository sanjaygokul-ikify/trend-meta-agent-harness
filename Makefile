build:	poetry build
run:	poetry run meta-agent-harness serve
test:	pytest --cov
lint:	typo3
clean: 	rm -rf dist/ build/ .mypy_cache/ .pytest_cache/
deploy:	poetry publish --build
format:	isort .	black .