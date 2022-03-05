help: ## This help
	@echo "Makefile for managing project:\n"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

requirements:
	pip-compile --output-file=requirements.txt requirements.in

install:
	pip install -r requirements.txt

simple-solution:
	FLASK_APP=a_simple_solution flask run
