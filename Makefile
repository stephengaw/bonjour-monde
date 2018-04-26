# Set important Paths
PROJECT := bonjour_monde

.PHONY: clean help test

# HELP
# This will output the help for each task
# thanks to https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html

help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help

clean:  ## Clean the project directory
	find . -name "*.pyc" -print0 | xargs -0 rm -rf
	rm -rf build
	rm -rf dist
	rm -rf $(PROJECT).egg-info

test:  ## Run unit tests
	nosetests --where=$(PROJECT)/tests
