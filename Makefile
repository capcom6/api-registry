# Variables
PYTHON=python3
PIP=pip
PROJECT_NAME=api-registry
APP_NAME=app
MODULE=api
ENV_PATH=venv
ALEMBIC_CONFIG=alembic.ini

# Commands
.PHONY: install
install:
	$(PIP) install -r requirements.txt

.PHONY: run
run:
	$(PYTHON) -m $(APP_NAME) $(MODULE)

.PHONY: test
test:
	pytest

.PHONY: format
format:
	black $(APP_NAME) tests

.PHONY: lint
lint:
	flake8 $(APP_NAME) tests

.PHONY: clean
clean:
	rm -rf $(ENV_PATH)
	find . -name "*.pyc" -type f -delete
	find . -name "__pycache__" -type d -delete

.PHONY: setup
setup:
	$(PYTHON) -m venv $(ENV_PATH)
	source $(ENV_PATH)/bin/activate && $(PIP) install --upgrade pip
	source $(ENV_PATH)/bin/activate && $(PIP) install -r requirements.txt
	source $(ENV_PATH)/bin/activate && $(PIP) install -r requirements-dev.txt

.PHONY: build
docker-build:
	docker build -f ./package/Dockerfile -t $(PROJECT_NAME) .

.PHONY: docker-run
docker-run:
	docker run --name $(PROJECT_NAME) --rm -v $(PWD)/configs:/configs:ro -e CONFIG_FILE=/configs/config.yml -p 8000:8000 $(PROJECT_NAME)

# Start Docker Compose stack
docker-up:
	docker-compose -p $(PROJECT_NAME) -f deployments/docker-compose.yml up --build -d

# Stop Docker Compose stack
docker-down:
	docker-compose -p $(PROJECT_NAME) -f deployments/docker-compose.yml down

# View Docker Compose logs
docker-logs:
	docker-compose -p $(PROJECT_NAME) -f deployments/docker-compose.yml logs -f

.PHONY: alembic-upgrade
alembic-upgrade:
	alembic upgrade head

.PHONY: alembic-downgrade
alembic-downgrade:
	alembic downgrade -1