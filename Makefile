install:
	@echo "Run syncing..."
	@uv sync
	@echo "Done"
	@echo "Creating venv..."
	@uv venv
	@echo "Done"

lock:
	@echo "Run locking..."
	@uv lock
	@echo "Done"

update:
	@echo "Run updating..."
	@uv lock --upgrade
	@echo "Done"

format:
	@echo "Run formatting..."
	@find src/ tests/ -type f -name "*.py" -print0 | xargs -0 uvx autopep8 -i -a -a
	@echo "Done"
	@echo "Run imports sorting..."
	@uvx isort src/ tests/
	@echo "Done"

lint:
	@echo "Run flake8 linting..."
	@uvx flake8 src/ tests/
	@echo "Done"
	@echo "Run ty checking..."
	@uvx ty check src/
	@echo "Done"

run:
	@echo "Run app on port :8000..."
	@uvicorn src.main:app --reload --port 8000

test:
	@echo "Run testing..."
	@pytest -v -s --tb=short --strict-markers tests/
	@echo "Done"

stress:
	@echo "Run locust stress-testing..."
	@locust -f stress.py
