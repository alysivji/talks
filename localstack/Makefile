.PHONY: help

help: ## help
	@echo "Makefile for localstack talk:\n"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

###################
# Local Development
###################
up:  ## bring up local development environment
	docker-compose up -d

down:  ## take down local development environment
	docker-compose down

shell:  ## start ipython shell
	ipython -i scripts/development_shell.py

logs:  ## see localstack logs
	docker-compose logs $(args) localstack

logs-f:  ## see localstack logs and follow tail
	docker-compose logs -f localstack

##############
# Dependencies
##############
install:  ## install dev requirements into venv
	pip install -r requirements_dev.txt

requirements:  ## make project requirements file
	pip-compile --output-file=requirements.txt requirements.in
