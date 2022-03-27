help: ## This help
	@echo "Makefile for managing project:\n"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

requirements: ## pin dependencies
	pip-compile --output-file=requirements.txt requirements.in

install: ## install dependencies
	pip install -r requirements.txt

ngrok: ## expose port=5000 via ngrok
	ngrok http 5000

mvp: ## start flask application for mvp solution
	FLASK_APP=a_mvp flask run

dispatch: ## start flask application for dictionary dispatch
	FLASK_APP=b_dictionary_dispatch flask run

emitter: ## start flask application for event emitter
	FLASK_APP=c_eventemitter flask run
