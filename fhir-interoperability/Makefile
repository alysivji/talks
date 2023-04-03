#########
# General
#########
help: ## this help
	@echo "Makefile for managing application:\n"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

#########
# General
#########
up: ## start fhir server
	docker-compose up -d

down: ## stop fhir server
	docker-compose down

requirements: ## compile requirements
	pip-compile --output-file requirements.txt requirements.in

requirements-dev: ## compile requirements-dev
	pip-compile --output-file requirements-dev.txt requirements-dev.in

install: ## install requirements
	pip install -r requirements.txt -r requirements-dev.txt
